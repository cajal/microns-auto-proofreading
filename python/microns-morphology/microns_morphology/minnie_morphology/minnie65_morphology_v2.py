import numpy as np
import datajoint as dj
import datajoint_plus as djp
import microns_utils.datajoint_utils as dju
from microns_utils.misc_utils import FieldDict
from microns_utils.version_utils import \
    check_package_version_from_distributions as cpvfd

from microns_materialization_api.schemas import minnie65_materialization as m65mat
from microns_morphology_api.schemas import minnie65_morphology_v2 as m65mor2

from ..neurd_interface.volume_data_interface import vdi
vdi.set_parameters_for_directory_modules()

schema = m65mor2.schema
config = m65mor2.config

logger = djp.getLogger(__name__)


class Tag(m65mor2.Tag):
    pass


class Segment(m65mor2.Segment):

    class MatV3Nucleus(m65mor2.Segment.MatV3Nucleus):
        @classmethod
        def fill(cls, ver):
            rel = m65mat.Segment.Nucleus & {'ver': ver} & 'segment_id>0'
            cls.insert(rel, ignore_extra_fields=True, insert_to_master=True)


class Mesh(m65mor2.Mesh):

    class MatV3MeshParty(m65mor2.Mesh.MatV3MeshParty):
        @property
        def key_source(cls):
            return m65mat.Mesh.MeshParty & Segment
        
        def make(self, key):
            self.insert1(key, ignore_extra_fields=True, insert_to_master=True)

        @classmethod
        def fill(cls):
            cls.insert(cls.key_source, ignore_extra_fields=True, insert_to_master=True, skip_duplicates=True, allow_direct_insert=True)


class DecimationMethod(m65mor2.DecimationMethod):
    
    run = classmethod(dju.run_method_from_parts)

    class Decimate(m65mor2.DecimationMethod.Decimate):
        @classmethod
        def update_method(cls, decimation_ratio, package_name):
            cls.insert1({
                'decimation_ratio': decimation_ratio,
                'package_name': package_name,
                'package_version': cpvfd(package_name),
                Tag.attr_name: Tag.version,
            }, ignore_extra_fields=True, insert_to_master=True)

        def run(self, mesh, **kwargs):
            params = self.fetch1()
            self.Log('info', f'Running {self.class_name} with params: {params}')

            # assert method compatibility
            error_msg = '{method_name} method {method_hash} requires {param} to be {value} but it is {current_value}.'
            attrs = [
                'package_version'
            ]
            values = [
                params['package_version']
            ]
            current_values = [
                cpvfd(params['package_name'])
            ]
            for attr, value, current_value in zip(attrs, values, current_values):
                if value != current_value:
                    msg = error_msg.format(
                        method_name=self.class_name,
                        method_hash=params[self.hash_name],
                        param=attr,
                        value=value,
                        current_value=current_value
                    )
                    self.Log('error', msg)
                    raise ValueError(msg)

            # run method
            from mesh_tools import trimesh_utils as tu
            dec_mesh = tu.decimate(mesh, decimation_ratio=params['decimation_ratio'])
            return FieldDict(dec_mesh=dec_mesh, n_vertices=len(dec_mesh.vertices), n_faces=len(dec_mesh.faces))


class DecimatedMesh(m65mor2.DecimatedMesh):

    class Maker(m65mor2.DecimatedMesh.Maker):
        @property
        def key_source(self):
            return DecimationMethod * Mesh
        
        def make(self, key):
            key[self.hash_name] = self.hash1(key)
            key = {**key, **DecimationMethod.r1p(key).run(**Mesh.get1(key))}
            key = self.master.Store.put(key)
            self.master.Store.insert1(key, ignore_extra_fields=True, insert_to_master=True)
            self.insert1(key, ignore_extra_fields=True, skip_hashing=True)

    class Store(m65mor2.DecimatedMesh.Store):
        @classmethod
        def put(cls, key, ext='.npz'):
            fp = cls.get_file_path(key['dec_mesh_id'], ext=ext)
            np.savez_compressed(fp, vertices=key['dec_mesh'].vertices, faces=key['dec_mesh'].faces)
            key['dec_mesh'] = fp
            return key
        

class DecompositionMethod(m65mor2.DecompositionMethod):

    class NEURD(m65mor2.DecompositionMethod.NEURD):
        @classmethod
        def update_method(cls, package_name):
            cls.insert1({
                'package_name': package_name,
                'package_version': cpvfd(package_name),
                Tag.attr_name: Tag.version,
            }, ignore_extra_fields=True, insert_to_master=True)

        def run(self, dec_mesh, segment_id, **kwargs):
            params = self.fetch1()
            self.Log('info', f'Running {self.class_name} with params: {params}')

            # assert method compatibility
            error_msg = '{method_name} method {method_hash} requires {param} to be {value} but it is {current_value}.'
            attrs = [
                'package_version'
            ]
            values = [
                params['package_version']
            ]
            current_values = [
                cpvfd(params['package_name'])
            ]
            for attr, value, current_value in zip(attrs, values, current_values):
                if value != current_value:
                    msg = error_msg.format(
                        method_name=self.class_name,
                        method_hash=params[self.hash_name],
                        param=attr,
                        value=value,
                        current_value=current_value
                    )
                    self.Log('error', msg)
                    raise ValueError(msg)

            # run method
            from neurd import neuron
            neuron_obj = neuron.Neuron(
                mesh=dec_mesh,
                segment_id=segment_id,
                suppress_preprocessing_print=False,
                suppress_output=False,
            )
            _ = neuron_obj.calculate_decomposition_products(
                store_in_obj=True,
            )
            return FieldDict(decomposition=neuron_obj)

class Decomposition(m65mor2.Decomposition):

    class Maker(m65mor2.Decomposition.Maker):
        @property
        def key_source(self):
            return DecompositionMethod * DecimatedMesh
        
        def make(self, key):
            key[self.hash_name] = self.hash1(key)
            key = {**key, **DecompositionMethod.r1p(key).run(**DecimatedMesh.get1(key))}
            key = self.master.Store.put(key)
            self.master.Store.insert1(key, ignore_extra_fields=True, insert_to_master=True)
            self.insert1(key, ignore_extra_fields=True, skip_hashing=True)

    class Store(m65mor2.Decomposition.Store):
        def _get_neuron_obj(self, decomp_data):
            filepath = decomp_data.decomposition
            segment_id = decomp_data.segment_id
            dec_mesh_id = decomp_data.dec_mesh_id
            mesh_decimated = DecimatedMesh.get1({'dec_mesh_id': dec_mesh_id}).dec_mesh
            decomp_data['decomposition_filepath'] = decomp_data['decomposition']
            decomp_data['decomposition'] = vdi.load_neuron_obj(
                    segment_id=segment_id,
                    mesh_decimated=mesh_decimated,
                    filepath=filepath,
                )
            return decomp_data

        def get(self, key):
            decomp_data_list = super().get(key)
            return [self._get_neuron_obj(decomp_data=decomp_data) for decomp_data in decomp_data_list]

        def get1(self, key):
            decomp_data = super().get1(key)
            return self._get_neuron_obj(decomp_data)

        @classmethod
        def put(cls, key, ext='.pbz2'):
            fp = cls.get_file_path(key['decomposition_id'], ext=ext)
            vdi.save_neuron_obj(
                key['decomposition'],
                verbose=True,
                directory=fp.parent,
                filename=fp.stem,
                suffix=fp.suffix
            )
            key['decomposition'] = fp
            return key