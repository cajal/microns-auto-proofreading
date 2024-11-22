from pathlib import Path
import datajoint as dj
import datajoint_plus as djp
import microns_utils.datajoint_utils as dju
from microns_utils.misc_utils import classproperty, unwrap, FieldDict
from microns_materialization_api.schemas import minnie65_materialization as m65mat

from ..config import minnie65_morphology_v2_config as config

config.register_adapters(context=locals())
config.register_externals()

schema = djp.schema(config.schema_name)

@schema
class Tag(dju.VersionLookup):
    package = 'microns-morphology-api'
    attr_name = 'tag'


@schema
class Segment(djp.Lookup):
    definition = """
    segment_id           : bigint unsigned              # id of the segment under the nucleus centroid. Equivalent to Allen 'pt_root_id'.
    """

    get = classmethod(dju.get_from_parts)
    
    @classmethod
    def get1(cls, key=None):
        return cls.r1p(key).get1()

    class MatV3Nucleus(djp.Part):
        definition = """
        -> master
        -> m65mat.Segment.Nucleus
        ---
        ts_inserted          : timestamp                    # the time at which the tuple was inserted into the database
        """

        def _get_restrict(self, key=None):
            return self & key if key is not None else self
                
        def _get_fetch(self, rel):
            print(f'Fetching {len(rel)} row(s) from {self.master.class_name}.')
            return [FieldDict(**r) for r in rel.fetch(as_dict=True)]
        
        def get(self, key=None):
            assert not isinstance(self, dict), 'get must be called on an instance, not a class'
            rel = self._get_restrict(key)
            return self._get_fetch(rel)
        
        def get1(self, key=None):
            assert not isinstance(self, dict), 'get1 must be called on an instance, not a class'
            rel = self._get_restrict(key)
            len_rel = len(rel)
            assert len_rel == 1, f'Expected 1 row, got {len_rel}'
            return unwrap(self._get_fetch(rel))


@schema
class Mesh(djp.Lookup):
    hash_name = 'mesh_id'
    definition = """
    mesh_id              : varchar(18)                  # unique identifier of a mesh
    """

    get = classmethod(dju.get_from_parts)
    
    @classmethod
    def get1(cls, key=None):
        return cls.r1p(key).get1()

    class MatV3MeshParty(djp.Part, dj.Computed):
        hash_name = 'mesh_id'
        definition = """
        -> master
        -> Segment
        -> m65mat.Mesh.MeshParty
        ---
        ts_inserted          : timestamp                    # the time at which the tuple was inserted into the database
        """

        def _get_restrict(self, key=None):
            return (self.proj() & key) * m65mat.Mesh.Object if key is not None else self.proj() * m65mat.Mesh.Object
                
        def _get_fetch(self, rel):
            print(f'Fetching {len(rel)} row(s) from {self.master.class_name}.')
            return [FieldDict(**r) for r in rel.fetch(as_dict=True)]
        
        def get(self, key=None):
            assert not isinstance(self, dict), 'get must be called on an instance, not a class'
            rel = self._get_restrict(key)
            return self._get_fetch(rel)
        
        def get1(self, key=None):
            assert not isinstance(self, dict), 'get1 must be called on an instance, not a class'
            rel = self._get_restrict(key)
            len_rel = len(rel)
            assert len_rel == 1, f'Expected 1 row, got {len_rel}'
            return unwrap(self._get_fetch(rel))
            

@schema
class DecimationMethod(djp.Lookup):
    hash_name = 'decimation_method'
    definition = """
    decimation_method    : varchar(8)                   # hash
    """

    class Decimate(djp.Part):
        enable_hashing = True
        hash_name = 'decimation_method'
        hashed_attrs = 'decimation_ratio', 'package_name', 'package_version', Tag.attr_name
        definition = """
        -> master
        ---
        decimation_ratio     : decimal(3,2)           #
        package_name         : varchar(1000)          # package name of mesh_tools used
        package_version      : varchar(48)            # version of mesh_tools used
        -> Tag
        ts_inserted=CURRENT_TIMESTAMP : timestamp     #
        """


@schema
class DecimatedMesh(djp.Lookup):
    hash_name = 'dec_mesh_id'
    definition = """
    dec_mesh_id              : varchar(18)                  # unique identifier of a decimated mesh
    """
    
    @classmethod
    def get(cls, key=None, store=None):
        store = store if store is not None else cls.Store
        return store().get(key)

    @classmethod
    def get1(cls, key=None, store=None):
        store = store if store is not None else cls.Store
        return store().get1(key)

    class Maker(djp.Part, dj.Computed):
        enable_hashing = True
        hash_name = 'dec_mesh_id'
        hashed_attrs = 'decimation_method', 'mesh_id'
        definition = """
        -> master
        -> DecimationMethod
        -> Mesh
        """

    class Store(djp.Part):
        hash_name = 'dec_mesh_id'
        definition = """
        -> master
        ---
        n_vertices          : int unsigned                  # number of vertices
        n_faces             : int unsigned                  # number of faces
        dec_mesh            : <minnie65_decimated_meshes>   # in-place path to the mesh file
        ts_inserted=CURRENT_TIMESTAMP : timestamp
        """

        @classproperty
        def store_path(cls):
            return Path(config.externals['minnie65_decimated_meshes']['location'])
        
        @classmethod
        def get_file_path(cls, dec_mesh_id, ext='.npz'):
            return cls.store_path / f'{dec_mesh_id}{ext}'
        
        def _get_restrict(self, key=None):
            key_source = self.master.Maker * Mesh.MatV3MeshParty.include_attrs('mesh_id', 'segment_id')
            return self * (key_source & key) if key is not None else self * key_source
                
        def _get_fetch(self, rel):
            print(f'Fetching {len(rel)} row(s) from {self.master.class_name}.')
            return [FieldDict(**r) for r in rel.fetch(as_dict=True)]
        
        def get(self, key=None):
            assert not isinstance(self, dict), 'get must be called on an instance, not a class'
            rel = self._get_restrict(key)
            return self._get_fetch(rel)
        
        def get1(self, key=None):
            assert not isinstance(self, dict), 'get1 must be called on an instance, not a class'
            rel = self._get_restrict(key)
            len_rel = len(rel)
            assert len_rel == 1, f'Expected 1 row, got {len_rel}'
            return unwrap(self._get_fetch(rel))


@schema
class DecompositionMethod(djp.Lookup):
    hash_name = 'decomposition_method'
    definition = f"""
    {hash_name}    : varchar(8)                   # hash
    """

    class NEURD(djp.Part):
        enable_hashing = True
        hash_name = 'decomposition_method'
        hashed_attrs = 'package_version', Tag.attr_name
        definition = """
        -> master
        ---
        package_name         : varchar(1000)          # package name of NEURD used
        package_version      : varchar(48)            # version of package used
        -> Tag
        ts_inserted=CURRENT_TIMESTAMP : timestamp     #
        """


@schema
class Decomposition(djp.Lookup):
    hash_name = 'decomposition_id'
    definition = f"""
    {hash_name}              : varchar(18)                  # unique identifier of a decomposition object
    """
    
    @classmethod
    def get(cls, key=None, store=None):
        store = store if store is not None else cls.Store
        return store().get(key)

    @classmethod
    def get1(cls, key=None, store=None):
        store = store if store is not None else cls.Store
        return store().get1(key)

    class Maker(djp.Part, dj.Computed):
        enable_hashing = True
        hash_name = 'decomposition_id'
        hashed_attrs = 'decomposition_method', 'dec_mesh_id'
        definition = """
        -> master
        -> DecompositionMethod
        -> DecimatedMesh
        """

    class Store(djp.Part):
        hash_name = 'decomposition_id'
        definition = """
        -> master
        ---
        decomposition            : <minnie65_decomposition>      # in-place path to the mesh file
        ts_inserted=CURRENT_TIMESTAMP : timestamp
        """

        @classproperty
        def store_path(cls):
            return Path(config.externals['minnie65_decomposition']['location'])
        
        @classmethod
        def get_file_path(cls, decomposition_id, ext='.pbz2'):
            return cls.store_path / f'{decomposition_id}{ext}'
        
        def _get_restrict(self, key=None):
            key_source = self.master.Maker * \
                DecimatedMesh.Maker.include_attrs('dec_mesh_id', 'mesh_id') * \
                Mesh.MatV3MeshParty.include_attrs('mesh_id', 'segment_id')
            return self * (key_source & key) if key is not None else self * key_source
                
        def _get_fetch(self, rel):
            print(f'Fetching {len(rel)} row(s) from {self.master.class_name}.')
            return [FieldDict(**r) for r in rel.fetch(as_dict=True)]
        
        def get(self, key=None):
            assert not isinstance(self, dict), 'get must be called on an instance, not a class'
            rel = self._get_restrict(key)
            return self._get_fetch(rel)
        
        def get1(self, key=None):
            assert not isinstance(self, dict), 'get1 must be called on an instance, not a class'
            rel = self._get_restrict(key)
            len_rel = len(rel)
            assert len_rel == 1, f'Expected 1 row, got {len_rel}'
            return unwrap(self._get_fetch(rel))



