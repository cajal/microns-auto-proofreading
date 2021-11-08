from pathlib import Path
# TODO: place in microns-utils
def make_store_dict(path):
    return {
        'protocol': 'file',
        'location': str(path),
        'stage': str(path)
    }

'''
minnie_em_external_stack_path = Path() / '/mnt' / 'dj-stor01' / 'microns'/ 'minnie' / 'stacks'
minnie_em = {
    'stacks': make_store_dict(minnie_em_external_stack_path)
    }
    
'''

#h01 morphology
h01_morphology_external_somas_path = Path() / '/mnt' / 'dj-stor01' / 'microns'/ 'h01' / 'somas'
h01_morphology_external_skeletons_path = Path() / '/mnt' / 'dj-stor01' / 'microns'/ 'h01' / 'skeletons'
h01_morphology_external_meshes_path = Path() / '/mnt' / 'dj-stor01' / 'microns'/ 'h01' / 'meshes'
h01_morphology = {
    'h01_somas': make_store_dict(h01_morphology_external_somas_path),
    'h01_skeletons': make_store_dict(h01_morphology_external_skeletons_path),
    'h01_meshes': make_store_dict(h01_morphology_external_meshes_path),
    
    }


#h01_auto_proofreading
h01_auto_proofreading_external_decomposition_path = Path() / '/mnt' / 'dj-stor01' / 'microns'/ 'h01' / 'decomposition'

h01_auto_proofreading_external_faces_path = Path() / '/mnt' / 'dj-stor01' / 'microns'/ 'h01' / 'faces'

h01_auto_proofreading_external_skeletons_path = Path() / '/mnt' / 'dj-stor01' / 'microns'/ 'h01' / 'skeletons'

h01_auto_proofreading_external_meshes_path = Path() / '/mnt' / 'dj-stor01' / 'microns'/ 'h01' / 'meshes'

h01_auto_proofreading = {
    'h01_decomposition': make_store_dict(h01_auto_proofreading_external_decomposition_path),
    'h01_faces': make_store_dict(h01_auto_proofreading_external_faces_path),
    'h01_skeletons': make_store_dict(h01_auto_proofreading_external_skeletons_path),
    'h01_meshes': make_store_dict(h01_auto_proofreading_external_meshes_path),
    
    }



#minnie65_morphology
minnie65_morphology_external_somas_path = Path() / '/mnt' / 'dj-stor01' / 'microns'/ 'minnie' / 'somas'
minnie65_morphology_external_skeletons_path = Path() / '/mnt' / 'dj-stor01' / 'microns'/ 'minnie' / 'skeletons'
minnie65_morphology_external_meshes_path = Path() / '/mnt' / 'dj-stor01' / 'microns'/ 'minnie' / 'meshes'
minnie65_morphology = {
    'minnie65_somas': make_store_dict(minnie65_morphology_external_somas_path),
    'minnie65_skeletons': make_store_dict(minnie65_morphology_external_skeletons_path),
    'minnie65_meshes': make_store_dict(minnie65_morphology_external_meshes_path),
    
    }

#minnie65_auto_proofreading
minnie65_auto_proofreading_external_decomposition_path = Path() / '/mnt' / 'dj-stor01' / 'microns'/ 'minnie' / 'decomposition'

minnie65_auto_proofreading_external_faces_path = Path() / '/mnt' / 'dj-stor01' / 'microns'/ 'minnie' / 'faces'

minnie65_auto_proofreading_external_skeletons_path = Path() / '/mnt' / 'dj-stor01' / 'microns'/ 'minnie' / 'skeletons'

minnie65_auto_proofreading_external_meshes_path = Path() / '/mnt' / 'dj-stor01' / 'microns'/ 'minnie' / 'meshes'

minnie65_auto_proofreading = {
    'minnie65_decomposition': make_store_dict(minnie65_auto_proofreading_external_decomposition_path),
    'minnie65_faces': make_store_dict(minnie65_auto_proofreading_external_faces_path),
    'minnie65_skeletons': make_store_dict(minnie65_auto_proofreading_external_skeletons_path),
    'minnie65_meshes': make_store_dict(minnie65_auto_proofreading_external_meshes_path),
    
    }




