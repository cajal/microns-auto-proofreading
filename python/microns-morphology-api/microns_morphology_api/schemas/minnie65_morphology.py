import datajoint as dj
import datajoint_plus as djp

from ..config import minnie65_morphology_config as config
from ..config import minnie65_auto_proofreading_config as autoconfig

config.register_adapters(context=locals())
config.register_externals()
schema = djp.schema(config.schema_name)

m65auto = djp.create_djp_module(schema_name=autoconfig.schema_name, add_externals=autoconfig.externals, add_objects=autoconfig.adapters)

@schema
class Segment(djp.Lookup):
    definition = """
    segment_id           : bigint unsigned              # id of the segment under the nucleus centroid. Equivalent to Allen 'pt_root_id'.
    """

    class MatV3(djp.Part):
        definition = """
        -> master
        """

    class Validation(djp.Part):
        definition = """
        -> master
        """


@schema
class Mesh(djp.Lookup):
    definition = """
    # mesh pass through from m65mat
    mesh_hash            : varchar(8)                   # hash
    ---
    timestamp=CURRENT_TIMESTAMP : timestamp                    # 
    """


@schema
class MeshSet(djp.Lookup):
    enable_hashing = True
    hash_name = 'mesh_set'
    hashed_attrs = 'segment_id'
    hash_group = True
    definition = """
    mesh_set             : varchar(8)                   # hash
    ---
    name=null            : varchar(24)                  # 
    description=null     : varchar(120)                 # 
    timestamp=CURRENT_TIMESTAMP : timestamp                    # 
    """

    class Member(djp.Part):
        definition = """
        -> master
        -> Segment
        """


@schema
class DecimationMethod(djp.Lookup):
    hash_name = 'decimation_method'
    definition = """
    decimation_method    : varchar(8)                   # hash
    ---
    timestamp=CURRENT_TIMESTAMP : timestamp                    #
    """

    class RatioAlgorithm(djp.Part):
        enable_hashing = True
        hash_name = 'decimation_method'
        hashed_attrs = 'decimation_ratio', 'algorithm'
        definition = """
        # combination of decimation ratio and decimation algorithm
        -> master
        ---
        decimation_ratio     : decimal(3,2)                 # 
        algorithm            : varchar(24)                  # 
        name=null            : varchar(24)                  # 
        description=null     : varchar(120)                 #
        """

    class Standard(djp.Part):
        enable_hashing = True
        hash_name = 'decimation_method'
        hashed_attrs = 'decimation_ratio', 'algorithm'
        definition = """
        # parameters for automatic proofreading
        -> master
        ---
        decimation_ratio=null : float                        # 
        algorithm=null       : varchar(14)                  # 
        name=null            : varchar(24)                  # 
        description=null     : varchar(120)                 # 
        """


@schema
class DecimationMethodMeshSet(djp.Lookup):
    enable_hashing = True
    hash_name = 'decimation_method_mesh_set'
    hashed_attrs = 'decimation_method', 'mesh_set'
    hash_group = True
    definition = """
    decimation_method_mesh_set : varchar(8)                   # hash
    ---
    name=null            : varchar(24)                  # 
    description=null     : varchar(120)                 # 
    timestamp=CURRENT_TIMESTAMP : timestamp                    #
    """

    class Member(djp.Part):
        definition = """
        -> master
        -> DecimationMethod
        -> MeshSet
        """


@schema
class MeshFragmentMethod(djp.Lookup):
    hash_name = 'mesh_fragment_method'
    definition = """
    # decimation method | 
    mesh_fragment_method : varchar(8)                   # hash
    ---
    timestamp=CURRENT_TIMESTAMP : timestamp                    # 
    """

    class Glia(djp.Part):
        enable_hashing = True
        hash_name = 'mesh_fragment_method'
        hashed_attrs = 'glia_volume_threshold_in_um', 'glia_n_faces_threshold', 'glia_n_faces_min'
        definition = """
        # nuclei detection parametersbefore soma detection
        -> master
        ---
        glia_volume_threshold_in_um=null : int unsigned                 # 
        glia_n_faces_threshold=null : int unsigned                 # 
        glia_n_faces_min=null : int unsigned                 # 
        name=null            : varchar(24)                  # 
        description=null     : varchar(120)                 # 
        """

    class Nuclei(djp.Part):
        enable_hashing = True
        hash_name = 'mesh_fragment_method'
        hashed_attrs = 'nuclei_volume_threshold_in_um', 'nuclei_n_faces_threshold', 'nuclei_n_faces_min'
        definition = """
        # nuclei detection parametersbefore soma detection
        -> master
        ---
        nucleus_min=null     : int unsigned                 # 
        nucleus_max=null     : int unsigned                 # 
        name=null            : varchar(24)                  # 
        description=null     : varchar(120)                 #  
        """

    class Soma(djp.Part):
        enable_hashing = True
        hash_name = 'mesh_fragment_method'
        hashed_attrs = 'outer_decimation_ratio', 'large_mesh_threshold', 'large_mesh_threshold_inner', 'inner_decimation_ratio', 'max_fail_loops', 'remove_inside_pieces', 'size_threshold_to_remove', 'pymeshfix_clean', 'check_holes_before_pymeshfix', 'second_poisson', 'soma_width_threshold', 'soma_size_threshold', 'soma_size_threshold_max', 'volume_mulitplier', 'side_length_ratio_threshold', 'perform_pairing', 'backtrack_soma_mesh_to_original', 'backtrack_soma_size_threshold', 'poisson_backtrack_distance_threshold', 'close_holes', 'boundary_vertices_threshold', 'last_size_threshold', 'segmentation_at_end', 'largest_hole_threshold', 'second_pass_size_threshold'
        definition = """
        # nuclei detection parametersbefore soma detection
        -> master
        ---
        outer_decimation_ratio=null : float                        # 
        large_mesh_threshold=null : int unsigned                 # 
        large_mesh_threshold_inner=null : int unsigned                 # 
        inner_decimation_ratio=null : float                        # 
        max_fail_loops=null  : int unsigned                 # 
        remove_inside_pieces=null : tinyint unsigned             # 
        size_threshold_to_remove=null : int unsigned                 # 
        pymeshfix_clean=null : tinyint unsigned             # 
        check_holes_before_pymeshfix=null : tinyint unsigned             # 
        second_poisson=null  : tinyint unsigned             # 
        soma_width_threshold=null : float                        # 
        soma_size_threshold=null : int unsigned                 # 
        soma_size_threshold_max=null : int unsigned                 # 
        volume_mulitplier=null : int unsigned                 # 
        side_length_ratio_threshold=null : int unsigned                 # 
        perform_pairing=null : tinyint unsigned             # 
        backtrack_soma_mesh_to_original=null : tinyint unsigned             # 
        backtrack_soma_size_threshold=null : int unsigned                 # 
        poisson_backtrack_distance_threshold=null : int unsigned                 # 
        close_holes=null     : tinyint unsigned             # 
        boundary_vertices_threshold=null : int unsigned                 # 
        last_size_threshold=null : int unsigned                 # 
        segmentation_at_end=null : tinyint unsigned             # 
        largest_hole_threshold=null : int unsigned                 # 
        second_pass_size_threshold=null : int unsigned                 # 
        name=null            : varchar(24)                  # 
        description=null     : varchar(120)                 # 
        """


@schema
class KeySource(djp.Lookup):
    hash_name = 'entry_hash'
    definition = """
    # keysources for m65mor
    entry_hash           : varchar(8)                   # hash
    ---
    timestamp=CURRENT_TIMESTAMP : timestamp                    #
    """


@schema
class MeshFragmentMethodSet(djp.Lookup):
    enable_hashing = True
    hash_name = 'mesh_fragment_method_set'
    hashed_attrs = 'mesh_fragment_method'
    hash_group = True
    definition = """
    mesh_fragment_method_set : varchar(8)                   # hash
    ---
    name=null            : varchar(24)                  # 
    description=null     : varchar(120)                 # 
    timestamp=CURRENT_TIMESTAMP : timestamp                    #
    """

    class Member(djp.Part):
        definition = """
        -> master
        -> MeshFragmentMethod
        ---
        table_type           : varchar(40)                  #
        """


@schema
class MeshFragmentMethodSetMeshSet(djp.Lookup):
    enable_hashing = True
    hash_name = 'mesh_fragment_method_set_mesh_set'
    hashed_attrs = 'mesh_fragment_method_set', 'mesh_set'
    hash_group = True
    definition = """
    mesh_fragment_method_set_mesh_set : varchar(8)                   # hash
    ---
    name=null            : varchar(24)                  # 
    description=null     : varchar(120)                 # 
    timestamp=CURRENT_TIMESTAMP : timestamp                    #
    """

    class Member(djp.Part):
        definition = """
        -> master
        -> MeshFragmentMethodSet
        -> MeshSet
        """


@schema
class Decimation(djp.Computed):
    definition = """
    -> Segment
    -> DecimationMethod
    ---
    n_vertices           : int unsigned                 # number of vertices
    n_faces              : int unsigned                 # number of faces
    old_database         : tinyint                      # whether the mesh from the old database was used
    """

    class Object(djp.Part):
        definition = """"
        -> master
        ---
        mesh                 : <minnie65_decimated_meshes>  # in-place path to the hdf5 mesh file
        """


@schema
class MeshFragment(djp.Computed):
    definition = """
    -> Segment
    -> DecimationMethod
    -> MeshFragmentMethodSet
    ---
    old_database         : tinyint                      #
    """

    class Glia(djp.Part):
        definition = """
        -> master
        ---
        n_faces              : int unsigned                 # The number of faces that were saved off as belonging to glia
        mesh_fragment_method : varchar(8)                   # hash        
        """

    class GliaObject(djp.Part):
        definition = """
        -> master
        ---
        faces                : <minnie65_faces>             # 
        """

    class Nuclei(djp.Part):
        definition = """
        -> master
        ---
        n_faces              : int unsigned                 # The number of faces that were saved off as belonging to glia
        mesh_fragment_method : varchar(8)                   # hash
        """

    class NucleiObject(djp.Part):
        definition = """
        -> master
        ---
        faces                : <minnie65_faces>             #
        """

    class Soma(djp.Part):
        definition = """
        -> master
        soma_index           : tinyint unsigned             # 
        ---
        centroid_x=null      : int unsigned                 # (EM voxels)
        centroid_y=null      : int unsigned                 # (EM voxels)
        centroid_z=null      : int unsigned                 # (EM voxels)
        centroid_x_nm=null   : double                       # nm x coordinate of soma
        centroid_y_nm=null   : double                       # nm y coordinate of soma
        centroid_z_nm=null   : double                       # nm z coordinate of soma
        n_vertices=null      : bigint                       # number of vertices
        n_faces=null         : bigint                       # number of faces
        multiplicity=null    : tinyint unsigned             # the number of somas found for this base segment
        sdf=null             : double                       # sdf width value for the soma
        volume=null          : double                       # the volume in billions (10*9 nm^3) of the convex hull
        surface_area=null    : double                       # surface area of the
        max_side_ratio=null  : double                       # the maximum of the side length ratios used for check if soma
        bbox_volume_ratio=null : double                       # ratio of bbox (axis aligned) volume to mesh volume to use for check if soma
        max_hole_length=null : double                       # euclidean distance of the maximum hole size
        run_time=null        : double                       # the amount of time to run (seconds)
        mesh_fragment_method : varchar(8)                   # hash
        """

    class SomaObject(djp.Part):
        definition = """"
        -> master
        soma_index           : tinyint unsigned             # 
        ---
        mesh                 : <minnie65_soma_meshes>       # in-place path to the hdf5 mesh file
        """


@schema
class SkeletonDecomposition(djp.Computed):
    definition = """
    -> MeshFragment
    -> m65auto.DecompositionMethod
    ---
    skeletal_length      : int unsigned                 # length of the skeleton
    n_branches           : int unsigned                 # number of branches in the skeleton
    n_limbs              : int unsigned                 # number of limbs in the skeleton
    centroid_x=null      : int unsigned                 # (EM voxels)
    centroid_y=null      : int unsigned                 # (EM voxels)
    centroid_z=null      : int unsigned                 # (EM voxels)
    centroid_x_nm=null   : double                       # nm x coordinate of soma
    centroid_y_nm=null   : double                       # nm y coordinate of soma
    centroid_z_nm=null   : double                       # nm z coordinate of soma
    centroid_volume      : double                       # 
    branch_length_median=null : double                       # 
    branch_length_mean=null : double                       # 
    n_short_branches=null : int unsigned                 # 
    n_long_branches=null : int unsigned                 # 
    n_medium_branches=null : int unsigned                 # 
    bbox_volume=null     : double                       # 
    bbox_x_min=null      : double                       # 
    bbox_y_min=null      : double                       # 
    bbox_z_min=null      : double                       # 
    bbox_x_max=null      : double                       # 
    bbox_y_max=null      : double                       # 
    bbox_z_max=null      : double                       # 
    bbox_x_min_soma_relative=null : double                       # 
    bbox_y_min_soma_relative=null : double                       # 
    bbox_z_min_soma_relative=null : double                       # 
    bbox_x_max_soma_relative=null : double                       # 
    bbox_y_max_soma_relative=null : double                       # 
    bbox_z_max_soma_relative=null : double                       #
    """

    class Object(djp.Part):
        definition = """
        -> master
        ---
        skeleton             : <minnie65_skeletons>         # skeleton
        """

@schema
class SkeletonDecompositionSplit(djp.Computed):
    definition = """
    # 
    -> m65auto.Decomposition
    -> m65auto.DecompositionSplitMethod
    split_index          : tinyint unsigned             # the index of the neuron object that resulted AFTER THE SPLITTING ALGORITHM
    ---
    skeletal_length      : int unsigned                 # length of the skeleton
    n_branches           : int unsigned                 # number of branches in the skeleton
    n_limbs              : int unsigned                 # number of limbs in the skeleton
    centroid_x=null      : int unsigned                 # (EM voxels)
    centroid_y=null      : int unsigned                 # (EM voxels)
    centroid_z=null      : int unsigned                 # (EM voxels)
    centroid_x_nm=null   : double                       # nm x coordinate of soma
    centroid_y_nm=null   : double                       # nm y coordinate of soma
    centroid_z_nm=null   : double                       # nm z coordinate of soma
    centroid_volume      : double                       # 
    branch_length_median=null : double                       # 
    branch_length_mean=null : double                       # 
    n_short_branches=null : int unsigned                 # 
    n_long_branches=null : int unsigned                 # 
    n_medium_branches=null : int unsigned                 # 
    bbox_volume=null     : double                       # 
    bbox_x_min=null      : double                       # 
    bbox_y_min=null      : double                       # 
    bbox_z_min=null      : double                       # 
    bbox_x_max=null      : double                       # 
    bbox_y_max=null      : double                       # 
    bbox_z_max=null      : double                       # 
    bbox_x_min_soma_relative=null : double                       # 
    bbox_y_min_soma_relative=null : double                       # 
    bbox_z_min_soma_relative=null : double                       # 
    bbox_x_max_soma_relative=null : double                       # 
    bbox_y_max_soma_relative=null : double                       # 
    bbox_z_max_soma_relative=null : double                       #
    """

    class Object(djp.Part):
        definition = """
        -> master
        ---
        skeleton             : <minnie65_skeletons>         # skeleton        
        """


@schema
class SkeletonAxonDendrite(djp.Computed):
    definition = """
    -> m65auto.Decomposition
    -> m65auto.DecompositionSplitMethod
    -> m65auto.DecompositionCellTypeMethod
    split_index          : tinyint unsigned             # the index of the neuron object that resulted AFTER THE SPLITTING ALGORITHM
    ---
    axon_skeletal_length : int unsigned                 # length of the skeleton
    axon_n_branches      : int unsigned                 # number of branches in the skeleton
    axon_n_limbs         : int unsigned                 # number of limbs in the skeleton
    axon_branch_length_median=null : double                       # 
    axon_branch_length_mean=null : double                       # 
    axon_n_short_branches=null : int unsigned                 # 
    axon_n_long_branches=null : int unsigned                 # 
    axon_n_medium_branches=null : int unsigned                 # 
    axon_bbox_volume=null : double                       # 
    axon_bbox_x_min=null : double                       # 
    axon_bbox_y_min=null : double                       # 
    axon_bbox_z_min=null : double                       # 
    axon_bbox_x_max=null : double                       # 
    axon_bbox_y_max=null : double                       # 
    axon_bbox_z_max=null : double                       # 
    axon_bbox_x_min_soma_relative=null : double                       # 
    axon_bbox_y_min_soma_relative=null : double                       # 
    axon_bbox_z_min_soma_relative=null : double                       # 
    axon_bbox_x_max_soma_relative=null : double                       # 
    axon_bbox_y_max_soma_relative=null : double                       # 
    axon_bbox_z_max_soma_relative=null : double                       # 
    dendrite_skeletal_length : int unsigned                 # length of the skeleton
    dendrite_n_branches  : int unsigned                 # number of branches in the skeleton
    dendrite_n_limbs     : int unsigned                 # number of limbs in the skeleton
    dendrite_branch_length_median=null : double                       # 
    dendrite_branch_length_mean=null : double                       # 
    dendrite_n_short_branches=null : int unsigned                 # 
    dendrite_n_long_branches=null : int unsigned                 # 
    dendrite_n_medium_branches=null : int unsigned                 # 
    dendrite_bbox_volume=null : double                       # 
    dendrite_bbox_x_min=null : double                       # 
    dendrite_bbox_y_min=null : double                       # 
    dendrite_bbox_z_min=null : double                       # 
    dendrite_bbox_x_max=null : double                       # 
    dendrite_bbox_y_max=null : double                       # 
    dendrite_bbox_z_max=null : double                       # 
    dendrite_bbox_x_min_soma_relative=null : double                       # 
    dendrite_bbox_y_min_soma_relative=null : double                       # 
    dendrite_bbox_z_min_soma_relative=null : double                       # 
    dendrite_bbox_x_max_soma_relative=null : double                       # 
    dendrite_bbox_y_max_soma_relative=null : double                       # 
    dendrite_bbox_z_max_soma_relative=null : double                       # 
    n_syn_axon_bouton_presyn=null : int unsigned                 # 
    n_syn_axon_bouton_postsyn=null : int unsigned                 # 
    n_syn_axon_non_bouton_presyn=null : int unsigned                 # 
    n_syn_axon_non_bouton_postsyn=null : int unsigned                 # 
    n_syn_dendrite_head_postsyn=null : int unsigned                 # 
    n_syn_dendrite_neck_postsyn=null : int unsigned                 # 
    n_syn_dendrite_shaft_postsyn=null : int unsigned                 # 
    n_syn_dendrite_no_head_postsyn=null : int unsigned                 # 
    n_syn_axon_ais_postsyn=null : int unsigned                 # 
    n_syn_soma_postsyn=null : int unsigned                 #
    """

    class Object(djp.Part):
        definition = """ 
        -> master
        ---
        axon_skeleton        : <minnie65_skeletons>         # skeleton
        dendrite_skeleton    : <minnie65_skeletons>         # skeleton
        """


@schema
class MatchedNuclei(djp.Manual):
    definition = """
    nucleus_id           : bigint unsigned              # 
    """