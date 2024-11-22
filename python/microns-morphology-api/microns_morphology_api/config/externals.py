"""
Externals for DataJoint tables.
"""

from pathlib import Path
import datajoint_plus as djp


base_path = Path() / '/mnt' / 'dj-stor01' / 'microns'
base_path2 = Path() / '/mnt' / 'dj-stor02' / 'microns'

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

#minnie65_morphology v2
minnie65_morphology_v2_decimated_meshes_path = base_path2 / 'minnie' / 'morphology'/ 'decimated_meshes'
minnie65_morphology_v2_decomposition_path = base_path2 / 'minnie' / 'morphology' / 'decomposition'
minnie65_morphology_v2 = {
    'minnie65_decimated_meshes': djp.make_store_dict(minnie65_morphology_v2_decimated_meshes_path),
    'minnie65_decomposition': djp.make_store_dict(minnie65_morphology_v2_decomposition_path),
}

#minnie_auto_proofreading v2
minnie65_auto_proofreading_v2_meshes_path = base_path2 / 'minnie' / 'auto_proofreading' / 'meshes'
minnie65_auto_proofreading_v2_skeletons_path = base_path2 / 'minnie' / 'auto_proofreading' / 'skeletons'
minnie65_auto_proofreading_v2_graphs_path = base_path2 / 'minnie' / 'auto_proofreading' / 'graphs'
minnie65_auto_proofreading_v2 = {
    'minnie65_auto_proof_meshes': djp.make_store_dict(minnie65_auto_proofreading_v2_meshes_path),
    'minnie65_auto_proof_skeletons': djp.make_store_dict(minnie65_auto_proofreading_v2_skeletons_path),
    'minnie65_auto_proof_graphs': djp.make_store_dict(minnie65_auto_proofreading_v2_graphs_path),
}