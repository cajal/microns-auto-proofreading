from pathlib import Path
from microns_utils import config_utils

'''
minnie_em_external_stack_path = Path() / '/mnt' / 'dj-stor01' / 'microns'/ 'minnie' / 'stacks'
minnie_em = {
    'stacks': make_store_dict(minnie_em_external_stack_path)
    }
    
'''

base_path = Path() / '/mnt' / 'dj-stor01' / 'microns'

#h01 morphology
h01_morphology_external_somas_path =  base_path / 'h01' / 'somas'
h01_morphology_external_skeletons_path = base_path / 'h01' / 'skeletons'
h01_morphology_external_meshes_path = base_path / 'h01' / 'meshes'
h01_morphology = {
    'h01_somas': config_utils.make_store_dict(h01_morphology_external_somas_path),
    'h01_skeletons': config_utils.make_store_dict(h01_morphology_external_skeletons_path),
    'h01_meshes': config_utils.make_store_dict(h01_morphology_external_meshes_path),
    
    }

#h01_auto_proofreading
h01_auto_proofreading_external_decomposition_path = base_path / 'h01' / 'decomposition'
h01_auto_proofreading_external_faces_path = base_path / 'h01' / 'faces'
h01_auto_proofreading_external_skeletons_path = base_path / 'h01' / 'skeletons'
h01_auto_proofreading_external_meshes_path = base_path / 'h01' / 'meshes'
h01_auto_proofreading = {
    'h01_decomposition': config_utils.make_store_dict(h01_auto_proofreading_external_decomposition_path),
    'h01_faces': config_utils.make_store_dict(h01_auto_proofreading_external_faces_path),
    'h01_skeletons': config_utils.make_store_dict(h01_auto_proofreading_external_skeletons_path),
    'h01_meshes': config_utils.make_store_dict(h01_auto_proofreading_external_meshes_path),
    
    }

#minnie65_morphology
minnie65_morphology_external_somas_path = base_path / 'minnie' / 'somas'
minnie65_morphology_external_skeletons_path = base_path / 'minnie' / 'skeletons'
minnie65_morphology_external_meshes_path = base_path / 'minnie' / 'meshes'
minnie65_morphology = {
    'minnie65_somas': config_utils.make_store_dict(minnie65_morphology_external_somas_path),
    'minnie65_skeletons': config_utils.make_store_dict(minnie65_morphology_external_skeletons_path),
    'minnie65_meshes': config_utils.make_store_dict(minnie65_morphology_external_meshes_path),
    
    }

#minnie65_auto_proofreading
minnie65_auto_proofreading_external_decomposition_path = base_path / 'minnie' / 'decomposition'
minnie65_auto_proofreading_external_faces_path = base_path / 'minnie' / 'faces'
minnie65_auto_proofreading_external_skeletons_path = base_path / 'minnie' / 'skeletons'
minnie65_auto_proofreading_external_meshes_path = base_path / 'minnie' / 'meshes'
minnie65_auto_proofreading = {
    'minnie65_decomposition': config_utils.make_store_dict(minnie65_auto_proofreading_external_decomposition_path),
    'minnie65_faces': config_utils.make_store_dict(minnie65_auto_proofreading_external_faces_path),
    'minnie65_skeletons': config_utils.make_store_dict(minnie65_auto_proofreading_external_skeletons_path),
    'minnie65_meshes': config_utils.make_store_dict(minnie65_auto_proofreading_external_meshes_path),
    
    }
