"""
Externals for DataJoint tables.
"""

from pathlib import Path
import datajoint.datajoint_plus as djp

'''
minnie_em_external_stack_path = Path() / '/mnt' / 'dj-stor01' / 'microns'/ 'minnie' / 'stacks'
minnie_em = {
    'stacks': make_store_dict(minnie_em_external_stack_path)
    }
    
'''

base_path = Path() / '/mnt' / 'dj-stor01' / 'microns'

#h01 morphology
#h01_morphology_external_somas_path =  base_path / 'h01' / 'somas'
h01_morphology_external_skeletons_path = base_path / 'h01' / 'skeletons'
h01_morphology_external_meshes_path = base_path / 'h01' / 'meshes'
h01_morphology_external_decimated_meshes_path = base_path / 'h01' / 'decimated_meshes'
h01_morphology_external_soma_meshes_path = base_path / 'h01' / 'soma_meshes'
h01_morphology_external_faces_path = base_path / 'h01' / 'faces'
h01_morphology = {
    #'h01_somas': djp.make_store_dict(h01_morphology_external_somas_path),
    'h01_skeletons': djp.make_store_dict(h01_morphology_external_skeletons_path),
    'h01_meshes': djp.make_store_dict(h01_morphology_external_meshes_path),
    'h01_faces': djp.make_store_dict(h01_morphology_external_faces_path),
    'h01_decimated_meshes': djp.make_store_dict(h01_morphology_external_decimated_meshes_path),
    'h01_soma_meshes': djp.make_store_dict(h01_morphology_external_soma_meshes_path),
}

#h01_auto_proofreading
h01_auto_proofreading_external_decomposition_path = base_path / 'h01' / 'decomposition'
h01_auto_proofreading_external_faces_path = base_path / 'h01' / 'faces'
h01_auto_proofreading_external_skeletons_path = base_path / 'h01' / 'skeletons'
#h01_auto_proofreading_external_meshes_path = base_path / 'h01' / 'meshes'
h01_auto_proofreading_external_auto_proof_meshes_path = base_path / 'h01' / 'auto_proof_meshes'
h01_auto_proofreading_external_auto_proof_skeletons_path = base_path / 'h01' / 'auto_proof_skeletons'
h01_auto_proofreading_external_graph_path = base_path / 'h01' / 'graph'
h01_auto_proofreading = {
    'h01_decomposition': djp.make_store_dict(h01_auto_proofreading_external_decomposition_path),
    'h01_faces': djp.make_store_dict(h01_auto_proofreading_external_faces_path),
    'h01_skeletons': djp.make_store_dict(h01_auto_proofreading_external_skeletons_path),
    'h01_auto_proof_meshes': djp.make_store_dict(h01_auto_proofreading_external_auto_proof_meshes_path),
    'h01_auto_proof_skeletons': djp.make_store_dict(h01_auto_proofreading_external_auto_proof_skeletons_path),
    'h01_graph': djp.make_store_dict(h01_auto_proofreading_external_graph_path),
}

#minnie65_morphology
#minnie65_morphology_external_somas_path = base_path / 'minnie65' / 'somas' 
minnie65_morphology_external_skeletons_path = base_path / 'minnie65' / 'skeletons'
minnie65_morphology_external_decimated_meshes_path = base_path / 'minnie65' / 'decimated_meshes'
minnie65_morphology_external_soma_meshes_path = base_path / 'minnie65' / 'soma_meshes'
minnie65_morphology_external_faces_path = base_path / 'minnie65' / 'faces'
minnie65_morphology = {
    #'minnie65_somas': djp.make_store_dict(minnie65_morphology_external_somas_path),
    'minnie65_skeletons': djp.make_store_dict(minnie65_morphology_external_skeletons_path),
    'minnie65_faces': djp.make_store_dict(minnie65_morphology_external_faces_path),
    'minnie65_decimated_meshes': djp.make_store_dict(minnie65_morphology_external_decimated_meshes_path),
    'minnie65_soma_meshes': djp.make_store_dict(minnie65_morphology_external_soma_meshes_path),
}

#minnie65_auto_proofreading
minnie65_auto_proofreading_external_decomposition_path = base_path / 'minnie65' / 'decomposition'
minnie65_auto_proofreading_external_faces_path = base_path / 'minnie65' / 'faces'
minnie65_auto_proofreading_external_skeletons_path = base_path / 'minnie65' / 'skeletons'
minnie65_auto_proofreading_external_auto_proof_meshes_path = base_path / 'minnie65' / 'auto_proof_meshes'
minnie65_auto_proofreading_external_auto_proof_skeletons_path = base_path / 'minnie65' / 'auto_proof_skeletons'
minnie65_auto_proofreading_external_graph_path = base_path / 'minnie65' / 'graph'
minnie65_auto_proofreading = {
    'minnie65_decomposition': djp.make_store_dict(minnie65_auto_proofreading_external_decomposition_path),
    'minnie65_faces': djp.make_store_dict(minnie65_auto_proofreading_external_faces_path),
    'minnie65_skeletons': djp.make_store_dict(minnie65_auto_proofreading_external_skeletons_path),
    'minnie65_auto_proof_meshes': djp.make_store_dict(minnie65_auto_proofreading_external_auto_proof_meshes_path),
    'minnie65_auto_proof_skeletons': djp.make_store_dict(minnie65_auto_proofreading_external_auto_proof_skeletons_path),
    'minnie65_graph': djp.make_store_dict(minnie65_auto_proofreading_external_graph_path),
}
