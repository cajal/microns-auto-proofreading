import datajoint_plus as djp

from ..config import minnie65_auto_proofreading_config as config
config.register_adapters(context=locals())
config.register_externals()

schema = djp.schema(config.schema_name)


@schema
class DecompositionMethod(djp.Lookup):
    hash_name = 'decomposition_method'
    definition = """
    # decomposition method
    decomposition_method : varchar(8)                   # hash
    ---
    timestamp=CURRENT_TIMESTAMP : timestamp                    # 
    """
            
    class Standard(djp.Part):
        enable_hashing = True
        hash_name = 'decomposition_method'
        hashed_attrs = (
            "fill_hole_size", "width_threshold_map", "size_threshold_map", "size_threshold_map_stitch", "apply_expansion", 
            "max_stitch_distance", "max_stitch_distance_cgal", "filter_end_node_length", "use_adaptive_invalidation_d", 
            "use_adaptive_invalidation_d_floating", "axon_width_preprocess_limb_max", "limb_remove_mesh_interior_face_threshold", 
            "surface_reconstruction_size", "floating_piece_face_threshold", "invalidation_d", "remove_mesh_interior_face_threshold", 
            "combine_close_skeleton_nodes_threshold_meshparty_axon", "filter_end_node_length_meshparty_axon", 
            "filter_end_node_length_axon", "invalidation_d_axon", "smooth_neighborhood_axon", "meshparty_segment_size_axon", 
            "stitch_floating_axon_pieces", "max_stitch_distance_high_fid_axon", "floating_piece_face_threshold_high_fid_axon", 
            "query", "calculate_spine_volume", "clusters_threshold", "smoothness_threshold", "shaft_threshold", 
            "spine_n_face_threshold", "spine_sk_length_threshold", "filter_by_bounding_box_longest_side_length", 
            "side_length_threshold", "filter_out_border_spines", "skeleton_endpoint_nullification", 
            "skeleton_endpoint_nullification_distance", "soma_vertex_nullification", "border_percentage_threshold", 
            "check_spine_border_perc", "filter_by_volume", "filter_by_volume_threshold", "head_smoothness", 
            "head_ray_trace_min", "head_face_min"
        )
        definition = """
        # decomposition base parameters
        -> master
        ---
        fill_hole_size=null  : int unsigned                 # 
        width_threshold_map=null : int unsigned                 # 
        size_threshold_map=null : int unsigned                 # 
        size_threshold_map_stitch=null : int unsigned                 # 
        apply_expansion=null : tinyint unsigned             # 
        max_stitch_distance=null : int unsigned                 # 
        max_stitch_distance_cgal=null : int unsigned                 # 
        filter_end_node_length=null : int unsigned                 # 
        use_adaptive_invalidation_d=null : tinyint unsigned             # 
        use_adaptive_invalidation_d_floating=null : tinyint unsigned             # 
        axon_width_preprocess_limb_max=null : int unsigned                 # 
        limb_remove_mesh_interior_face_threshold=null : int unsigned                 # 
        surface_reconstruction_size=null : int unsigned                 # 
        floating_piece_face_threshold=null : int unsigned                 # 
        invalidation_d=null  : int unsigned                 # 
        remove_mesh_interior_face_threshold=null : int unsigned                 # 
        combine_close_skeleton_nodes_threshold_meshparty_axon=null : int unsigned                 # 
        filter_end_node_length_meshparty_axon=null : int unsigned                 # 
        filter_end_node_length_axon=null : int unsigned                 # 
        invalidation_d_axon=null : int unsigned                 # 
        smooth_neighborhood_axon=null : int unsigned                 # 
        meshparty_segment_size_axon=null : int unsigned                 # 
        stitch_floating_axon_pieces=null : tinyint unsigned             # 
        max_stitch_distance_high_fid_axon=null : int unsigned                 # 
        floating_piece_face_threshold_high_fid_axon=null : int unsigned                 # 
        query=null           : varchar(57)                  # 
        calculate_spine_volume=null : tinyint unsigned             # 
        clusters_threshold=null : int unsigned                 # 
        smoothness_threshold=null : float                        # 
        shaft_threshold=null : int unsigned                 # 
        spine_n_face_threshold=null : int unsigned                 # 
        spine_sk_length_threshold=null : int unsigned                 # 
        filter_by_bounding_box_longest_side_length=null : tinyint unsigned             # 
        side_length_threshold=null : int unsigned                 # 
        filter_out_border_spines=null : tinyint unsigned             # 
        skeleton_endpoint_nullification=null : tinyint unsigned             # 
        skeleton_endpoint_nullification_distance=null : int unsigned                 # 
        soma_vertex_nullification=null : tinyint unsigned             # 
        border_percentage_threshold=null : float                        # 
        check_spine_border_perc=null : float                        # 
        filter_by_volume=null : tinyint unsigned             # 
        filter_by_volume_threshold=null : int unsigned                 # 
        head_smoothness=null : float                        # 
        head_ray_trace_min=null : int unsigned                 # 
        head_face_min=null   : int unsigned                 # 
        name=null            : varchar(24)                  # 
        description=null     : varchar(120)                 # 
        """


@schema
class DecompositionSplitMethod(djp.Lookup):
    hash_name = 'decomposition_split_method'
    definition = """
    # decomposition split method
    decomposition_split_method : varchar(8)                   # hash
    ---
    timestamp=CURRENT_TIMESTAMP : timestamp                    # 
    """
            
    class Standard(djp.Part):
        enable_hashing = True
        hash_name = "decomposition_split_method"
        hashed_attrs = (
            "remove_segment_threshold", "remove_segment_threshold_round_2", "consider_path_neighbors_for_removal", 
            "offset_high_degree", "comparison_distance_high_degree", "match_threshold_high_degree", 
            "skip_small_soma_connectors", "small_soma_connectors_skeletal_threshold", "double_back_threshold", 
            "offset_double_back", "comparison_distance_double_back", "width_jump_threshold", "simple_path_of_2_cut", 
            "apply_double_back_first", "double_back_threshold_at_first", "min_skeletal_length_limb"
        )
        definition = """
        # decomposition split parameters for separating multi touches and multi-somas
        -> master
        ---
        remove_segment_threshold=null : int unsigned                 # 
        remove_segment_threshold_round_2=null : int unsigned                 # 
        consider_path_neighbors_for_removal=null : tinyint unsigned             # 
        offset_high_degree=null : int unsigned                 # 
        comparison_distance_high_degree=null : int unsigned                 # 
        match_threshold_high_degree=null : int unsigned                 # 
        skip_small_soma_connectors=null : tinyint unsigned             # 
        small_soma_connectors_skeletal_threshold=null : int unsigned                 # 
        double_back_threshold=null : int unsigned                 # 
        offset_double_back=null : int unsigned                 # 
        comparison_distance_double_back=null : int unsigned                 # 
        width_jump_threshold=null : int unsigned                 # 
        simple_path_of_2_cut=null : tinyint unsigned             # 
        apply_double_back_first=null : tinyint unsigned             # 
        double_back_threshold_at_first=null : int unsigned                 # 
        min_skeletal_length_limb=null : int unsigned                 # 
        name=null            : varchar(24)                  # 
        description=null     : varchar(120)                 # 
        """


@schema
class DecompositionCellTypeMethod(djp.Lookup):
    hash_name = 'decomposition_cell_type_method'
    definition = """
    # method for
    decomposition_cell_type_method : varchar(8)                   # hash
    ---
    timestamp=CURRENT_TIMESTAMP : timestamp                    # 
    """
            
    class Standard(djp.Part):
        enable_hashing = True
        hash_name = "decomposition_cell_type_method"
        hashed_attrs = "ax_so_an_th_ex", "ai_ma_di_fr_so_ex", "ax_cl_wi_sy_ex", "ax_cl_wi_sy_if_no_ca", "ai_ma_di_fr_so_in", 
        "ax_so_an_th", "ai_sy_de_ma", "ai_sy_al_ma", "ai_n_sy_pr_ma", "ai_wi_mi", "ai_wi_ma", "ma_se_di", 
        "mi_sk_le", "n_po_ma", "po_di", "ai_wi_fi", "ai_ne_wi_mi", "ai_ne_wi_mi_in", "ai_ne_wi_do_sk_le", 
        "ai_ma_di_fr_so", "n_sy_sp_of_en_up_ma", "at_se_pa", "ai_sy_de_ma_ba", "ai_n_sy_pr_ma_ba", 
        "ma_se_di_ad_ba", "re_be_ca", "be_ca_me", "ma_sk_le_mi", "ma_sk_le_bu", "si_lo_de_mi_sk_le", 
        "lo_de_ra", "do_di_fo_ax_an", "axon_classification_without_synapses_if_no_candidate", "ax_cl_wi_sy", 
        "ai_sy_de_ma_ex", "ai_sy_de_ma_ba_ex", "ca_do_po_de_ma", "mi_di_fr_so_in_de_on", "mi_di_fr_so_ex_de_on", 
        "n_sy_pr_mi_de_on_ax", "sy_po_pe_mi_de_on_ax", "sp_de_mi_de_on_ax", "de_wi_mi_de_on_ax", 
        "de_sk_le_mi_de_on_ax", "co_de_fi", "co_de_ax_wi_mi", "co_de_sy_po_pe_mi", "co_de_n_sy_po_mi", 
        "co_de_n_sp_mi", "co_de_sp_de", "sy_po_pe_do_mi_de_on", "n_sy_pr_do_ma_de_on_", "fi_aw_sp_br_de_on_ax", 
        "n_sy_po_sp_ma_de_on_", "sp_de_ma_de_on_ax", "wi_ma_ax_on_de", "n_sp_ma_ax_on_de", 
        "n_sy_po_sp_ma_ax_on_", "n_sy_pr_mi_ax_on_de", "sy_pr_pe_mi_ax_on_de", "sy_pr_pe_do_mi_ax_on", 
        "ax_sk_le_mi_ax_on_de", "fi_aw_th_br_ax_on_de", "de_wi_mi_ax_on_de", "th_ax_sk_le_mi_ax_on", 
        "th_ax_n_sy_po_do_ma_", "me_ar_mi_ax_on_de", "cl_me_sk_di_ma_ax_on", "fi_aw_my_my", "mi_sk_le_my", 
        "ma_sy_de_my", "ma_sy_de_pa_2_my", "mi_sk_le_pa_2_my", "mi_di_fr_so_pa_2_my", "ma_wi_my", "mi_di_fr_so_my", 
        "sk_le_do_mi_ax_on_de", "n_sy_po_do_ma_my", "co_cl_sk_no_th_me_ax", "fi_en_no_le_me_ax", "fi_en_no_le_ax", 
        "in_d_ax", "sm_ne_ax", "me_se_si_ax", "st_fl_ax_pi", "ma_st_di_hi_fi_ax", "fl_pi_fa_th_hi_fi_ax", 
        "no_ai_wi_ax", "ai_wi_ax", "ma_n_sp_ax", "ma_sp_de_ax", "ma_sk_le_lo_br_cl_de", "mi_n_no_in_cl_lo_br_", 
        "ma_sk_le_lo_br_cl_ax", "min_n_nodes_in_cluster_low_branch_clusters_axon", "sk_di_fr_so_mi_ax"
        definition = """
        -> master
        ---
        ax_so_an_th_ex=null  : int unsigned                 # 
        ai_ma_di_fr_so_ex=null : int unsigned                 # 
        ax_cl_wi_sy_ex=null  : tinyint unsigned             # 
        ax_cl_wi_sy_if_no_ca=null : tinyint unsigned             # 
        ai_ma_di_fr_so_in=null : int unsigned                 # 
        ax_so_an_th=null     : int unsigned                 # 
        ai_sy_de_ma=null     : float                        # 
        ai_sy_al_ma=null     : int unsigned                 # 
        ai_n_sy_pr_ma=null   : int unsigned                 # 
        ai_wi_mi=null        : int unsigned                 # 
        ai_wi_ma=null        : int unsigned                 # 
        ma_se_di=null        : int unsigned                 # 
        mi_sk_le=null        : int unsigned                 # 
        n_po_ma=null         : int unsigned                 # 
        po_di=null           : int unsigned                 # 
        ai_wi_fi=null        : tinyint unsigned             # 
        ai_ne_wi_mi=null     : int unsigned                 # 
        ai_ne_wi_mi_in=null  : int unsigned                 # 
        ai_ne_wi_do_sk_le=null : int unsigned                 # 
        ai_ma_di_fr_so=null  : int unsigned                 # 
        n_sy_sp_of_en_up_ma=null : int unsigned                 # 
        at_se_pa=null        : tinyint unsigned             # 
        ai_sy_de_ma_ba=null  : float                        # 
        ai_n_sy_pr_ma_ba=null : int unsigned                 # 
        ma_se_di_ad_ba=null  : int unsigned                 # 
        re_be_ca=null        : tinyint unsigned             # 
        be_ca_me=null        : varchar(56)                  # 
        ma_sk_le_mi=null     : int unsigned                 # 
        ma_sk_le_bu=null     : int unsigned                 # 
        si_lo_de_mi_sk_le=null : int unsigned                 # 
        lo_de_ra=null        : int unsigned                 # 
        do_di_fo_ax_an=null  : int unsigned                 # 
        axon_classification_without_synapses_if_no_candidate=null : tinyint unsigned             # 
        ax_cl_wi_sy=null     : tinyint unsigned             # 
        ai_sy_de_ma_ex=null  : blob                         # 
        ai_sy_de_ma_ba_ex=null : blob                         # 
        ca_do_po_de_ma=null  : float                        # 
        mi_di_fr_so_in_de_on=null : int unsigned                 # 
        mi_di_fr_so_ex_de_on=null : int unsigned                 # 
        n_sy_pr_mi_de_on_ax=null : int unsigned                 # 
        sy_po_pe_mi_de_on_ax=null : float                        # 
        sp_de_mi_de_on_ax=null : float                        # 
        de_wi_mi_de_on_ax=null : int unsigned                 # 
        de_sk_le_mi_de_on_ax=null : int unsigned                 # 
        co_de_fi=null        : tinyint unsigned             # 
        co_de_ax_wi_mi=null  : int unsigned                 # 
        co_de_sy_po_pe_mi=null : float                        # 
        co_de_n_sy_po_mi=null : int unsigned                 # 
        co_de_n_sp_mi=null   : int unsigned                 # 
        co_de_sp_de=null     : float                        # 
        sy_po_pe_do_mi_de_on=null : float                        # 
        n_sy_pr_do_ma_de_on_=null : int unsigned                 # 
        fi_aw_sp_br_de_on_ax=null : tinyint unsigned             # 
        n_sy_po_sp_ma_de_on_=null : int unsigned                 # 
        sp_de_ma_de_on_ax=null : float                        # 
        wi_ma_ax_on_de=null  : int unsigned                 # 
        n_sp_ma_ax_on_de=null : int unsigned                 # 
        n_sy_po_sp_ma_ax_on_=null : int unsigned                 # 
        n_sy_pr_mi_ax_on_de=null : int unsigned                 # 
        sy_pr_pe_mi_ax_on_de=null : float                        # 
        sy_pr_pe_do_mi_ax_on=null : float                        # 
        ax_sk_le_mi_ax_on_de=null : int unsigned                 # 
        fi_aw_th_br_ax_on_de=null : tinyint unsigned             # 
        de_wi_mi_ax_on_de=null : int unsigned                 # 
        th_ax_sk_le_mi_ax_on=null : int unsigned                 # 
        th_ax_n_sy_po_do_ma_=null : int unsigned                 # 
        me_ar_mi_ax_on_de=null : int unsigned                 # 
        cl_me_sk_di_ma_ax_on=null : int unsigned                 # 
        fi_aw_my_my=null     : tinyint unsigned             # 
        mi_sk_le_my=null     : int unsigned                 # 
        ma_sy_de_my=null     : float                        # 
        ma_sy_de_pa_2_my=null : float                        # 
        mi_sk_le_pa_2_my=null : int unsigned                 # 
        mi_di_fr_so_pa_2_my=null : int                          # 
        ma_wi_my=null        : int unsigned                 # 
        mi_di_fr_so_my=null  : int unsigned                 # 
        sk_le_do_mi_ax_on_de=null : int unsigned                 # 
        n_sy_po_do_ma_my=null : int unsigned                 # 
        co_cl_sk_no_th_me_ax=null : int unsigned                 # 
        fi_en_no_le_me_ax=null : int unsigned                 # 
        fi_en_no_le_ax=null  : int unsigned                 # 
        in_d_ax=null         : int unsigned                 # 
        sm_ne_ax=null        : int unsigned                 # 
        me_se_si_ax=null     : int unsigned                 # 
        st_fl_ax_pi=null     : tinyint unsigned             # 
        ma_st_di_hi_fi_ax=null : int unsigned                 # 
        fl_pi_fa_th_hi_fi_ax=null : int unsigned                 # 
        no_ai_wi_ax=null     : int unsigned                 # 
        ai_wi_ax=null        : int unsigned                 # 
        ma_n_sp_ax=null      : int unsigned                 # 
        ma_sp_de_ax=null     : float                        # 
        ma_sk_le_lo_br_cl_de=null : int unsigned                 # 
        mi_n_no_in_cl_lo_br_=null : int unsigned                 # 
        ma_sk_le_lo_br_cl_ax=null : int unsigned                 # 
        min_n_nodes_in_cluster_low_branch_clusters_axon=null : int unsigned                 # 
        sk_di_fr_so_mi_ax=null : int unsigned                 # 
        name=null            : varchar(24)                  # 
        description=null     : varchar(120)                 # 
        """


@schema
class DecompositionMethodMeshSet(djp.Lookup):
    hash_name = 'decomposition_method_mesh_set'
    hashed_attrs = 'decomposition_method', 'mesh_set'
    hash_group = True
    definition = """
    decomposition_method_mesh_set : varchar(8)                   # hash
    ---
    name=null            : varchar(24)                  # 
    description=null     : varchar(120)                 # 
    timestamp=CURRENT_TIMESTAMP : timestamp                    # 
    """
            
    class Member(djp.Part):
        definition = """
        -> master
        -> DecompositionMethod
        -> m65mor.MeshSet
        """     


@schema
class DecompositionSplitMethodMeshSet(djp.Lookup):
    enable_hashing = True
    hash_name = 'decomposition_split_method_mesh_set'
    hashed_attrs = 'decomposition_split_method', 'mesh_set'
    hash_group = True
    definition = """
    decomposition_split_method_mesh_set : varchar(8)                   # hash
    ---
    name=null            : varchar(24)                  # 
    description=null     : varchar(120)                 # 
    timestamp=CURRENT_TIMESTAMP : timestamp                    # 
    """
            
    class Member(djp.Part):
        definition = """
        -> master
        -> DecompositionSplitMethod
        -> m65mor.MeshSet
        """


@schema
class DecompositionCellTypeMethodMeshSet(djp.Lookup):
    enable_hashing = True
    hash_name = 'decomposition_cell_type_method_mesh_set'
    hashed_attrs = 'decomposition_cell_type_method', 'mesh_set'
    definition = """
    decomposition_cell_type_method_mesh_set : varchar(8)                   # hash
    ---
    name=null            : varchar(24)                  # 
    description=null     : varchar(120)                 # 
    timestamp=CURRENT_TIMESTAMP : timestamp                    # 
    """
            
    class Member(djp.Part):
        definition = """
        -> master
        -> DecompositionCellTypeMethod
        -> m65or.MeshSet
        """


@schema
class Decomposition(djp.Computed):
    definition = """
    -> m65mor.MeshFragment
    -> DecompositionMethod
    ---
    multiplicity=null    : tinyint unsigned             # the number of somas found for this base segment
    n_vertices           : int unsigned                 # number of vertices
    n_faces              : int unsigned                 # number of faces
    n_not_processed_soma_containing_meshes : int unsigned                 # the number of meshes with somas that were not processed
    n_error_limbs        : int                          # the number of limbs that are touching multiple somas or 1 soma in multiple places
    n_same_soma_multi_touching_limbs : int                          # number of limbs that touch the same soma multiple times
    n_multi_soma_touching_limbs : int                          # number of limbs that touch multiple somas
    n_somas              : int                          # number of soma meshes detected
    n_limbs              : int                          # 
    n_branches           : int                          # 
    max_limb_n_branches=null : int                          # 
    skeletal_length=null : double                       # 
    max_limb_skeletal_length=null : double                       # 
    median_branch_length=null : double                       # gives information on average skeletal length to next branch point
    width_median=null    : double                       # median width from mesh center without spines removed
    width_no_spine_median=null : double                       # median width from mesh center with spines removed
    width_90_perc=null   : double                       # 90th percentile for width without spines removed
    width_no_spine_90_perc=null : double                       # 90th percentile for width with spines removed
    n_spines             : bigint                       # 
    spine_density=null   : double                       # n_spines/ skeletal_length
    spines_per_branch=null : double                       # 
    skeletal_length_eligible=null : double                       # the skeletal length for all branches searched for spines
    n_spine_eligible_branches=null : int                          # the number of branches that were checked for spines because passed width threshold
    spine_density_eligible=null : double                       # n_spines/skeletal_length_eligible
    spines_per_branch_eligible=null : double                       # n_spines/n_spine_eligible_branches
    total_spine_volume=null : double                       # the sum of all spine volume
    spine_volume_median=null : double                       # median of the spine volume for those spines with able to calculate volume
    spine_volume_density=null : double                       # total_spine_volume/skeletal_length
    spine_volume_density_eligible=null : double                       # total_spine_volume/skeletal_length_eligible
    spine_volume_per_branch_eligible=null : double                       # total_spine_volume/n_spine_eligible_branches
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
    run_time=null        : double                       # the amount of time to run (seconds)
    """
            
    class Object(djp.Part):
        definition = """
        -> master
        ---
        decomposition        : <minnie65_decomposition>     # in-place path to the hdf5 mesh file
        """


@schema
class DecompositionSplit(djp.Computed):
    definition = """
    -> Decomposition
    -> DecompositionSplitMethod
    split_index          : tinyint unsigned             # the index of the neuron object that resulted AFTER THE SPLITTING ALGORITHM
    ---
    multiplicity         : tinyint unsigned             # the number of somas found for this base segment
    n_vertices           : int unsigned                 # number of vertices
    n_faces              : int unsigned                 # number of faces
    n_not_processed_soma_containing_meshes : int unsigned                 # the number of meshes with somas that were not processed
    n_error_limbs        : int                          # the number of limbs that are touching multiple somas or 1 soma in multiple places
    n_same_soma_multi_touching_limbs : int                          # number of limbs that touch the same soma multiple times
    n_multi_soma_touching_limbs : int                          # number of limbs that touch multiple somas
    n_somas              : int                          # number of soma meshes detected
    n_limbs              : int                          # 
    n_branches           : int                          # 
    max_limb_n_branches=null : int                          # 
    skeletal_length=null : double                       # 
    max_limb_skeletal_length=null : double                       # 
    median_branch_length=null : double                       # gives information on average skeletal length to next branch point
    width_median=null    : double                       # median width from mesh center without spines removed
    width_no_spine_median=null : double                       # median width from mesh center with spines removed
    width_90_perc=null   : double                       # 90th percentile for width without spines removed
    width_no_spine_90_perc=null : double                       # 90th percentile for width with spines removed
    n_spines             : bigint                       # 
    spine_density=null   : double                       # n_spines/ skeletal_length
    spines_per_branch=null : double                       # 
    skeletal_length_eligible=null : double                       # the skeletal length for all branches searched for spines
    n_spine_eligible_branches=null : int                          # the number of branches that were checked for spines because passed width threshold
    spine_density_eligible=null : double                       # n_spines/skeletal_length_eligible
    spines_per_branch_eligible=null : double                       # n_spines/n_spine_eligible_branches
    total_spine_volume=null : double                       # the sum of all spine volume
    spine_volume_median=null : double                       # median of the spine volume for those spines with able to calculate volume
    spine_volume_density=null : double                       # total_spine_volume/skeletal_length
    spine_volume_density_eligible=null : double                       # total_spine_volume/skeletal_length_eligible
    spine_volume_per_branch_eligible=null : double                       # total_spine_volume/n_spine_eligible_branches
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
    n_splits             : int unsigned                 # the number of cuts required to help split the neuron
    split_success        : tinyint unsigned             # the successfulness of the splitting
    n_error_limbs_cancelled : tinyint unsigned             # number of limbs that couldn't be resolved and cancelled out
    n_same_soma_limbs_cancelled : tinyint unsigned             # number of same soma touching limbs that couldn't be resolved and cancelled out
    n_multi_soma_limbs_cancelled : tinyint unsigned             # number of multi soma touching limbs that couldn't be resolved and cancelled out
    error_imbs_cancelled_area=null : double                       # the total area (in microns^2) of the limbs that was cancelled out because touching the same soma multiple times or multiple somas
    error_imbs_cancelled_skeletal_length=null : double                       # the total skeletal length (in microns) of the limbs that were called out because could not be resolved
    split_results=null   : longblob                     # will store the results of how to split the limbs of neuron objects from original neuron
    run_time=null        : double                       # the amount of time to run (seconds)
    """
            
    class Object(djp.Part):
        definition = """
        -> master
        ---
        decomposition        : <minnie65_decomposition>     # in-place path to the hdf5 mesh file
        """


@schema
class DecompositionCellType(djp.Computed):
    definition = """
    -> Decomposition
    -> DecompositionSplitMethod
    -> DecompositionCellTypeMethod
    split_index          : tinyint unsigned             # the index of the neuron object that resulted AFTER THE SPLITTING ALGORITHM
    ---
    nucleus_id           : int unsigned                 # id of nucleus from the flat segmentation  Equivalent to Allen: 'id'.
    nuclei_distance      : double                       # the distance to the closest nuclei (even if no matching nuclei found)
    n_nuclei_in_radius   : tinyint unsigned             # the number of nuclei within the search radius of 15000 belonging to that segment
    n_nuclei_in_bbox     : tinyint unsigned             # the number of nuclei within the bounding box of that soma
    baylor_cell_type=null : enum('excitatory','inhibitory','other','unknown') # 
    external_cell_type=null : enum('excitatory','inhibitory','other','unknown') # 
    cell_type_used=null  : enum('external','baylor')    # 
    cell_type=null       : enum('excitatory','inhibitory','other','unknown') # 
    external_cell_type_n_nuc=null : tinyint unsigned             # 
    external_cell_type_fine=null : varchar(256)                 # 
    syn_density_post     : double                       # 
    syn_density_head     : double                       # 
    syn_density_neck     : double                       # 
    syn_density_shaft    : double                       # 
    skeletal_length_processed_syn : double                       # 
    spine_density        : double                       # 
    skeletal_length_processed_spine : double                       # 
    n_syn_pre            : int unsigned                 # 
    n_syn_post           : int unsigned                 # 
    axon_angle_max=null  : double                       # 
    axon_angle_min=null  : double                       # 
    n_axon_angles        : tinyint unsigned             # 
    external_layer=null  : enum('LAYER_1','LAYER_2','LAYER_3','LAYER_4','LAYER_5','LAYER_6','UNCLASSIFIED','WHITE_MATTER') # 
    low_branch_length_clusters_dendrite_error_area=null : double                       # 
    low_branch_length_clusters_dendrite_error_length=null : double                       # 
    dendrite_on_axon_merges_error_area=null : double                       # the area (in um ^ 2) of the faces canceled out by filter
    dendrite_on_axon_merges_error_length=null : double                       # the length (in um) of skeleton distance canceled out by filter
    n_vertices           : int unsigned                 # number of vertices
    n_faces              : int unsigned                 # number of faces
    max_soma_volume=null : double                       # 
    max_soma_n_faces=null : int unsigned                 # 
    max_soma_area=null   : int unsigned                 # 
    n_limbs              : int                          # 
    n_branches           : int                          # 
    max_limb_n_branches=null : int                          # 
    skeletal_length=null : double                       # 
    max_limb_skeletal_length=null : double                       # 
    median_branch_length=null : double                       # gives information on average skeletal length to next branch point
    width_median=null    : double                       # median width from mesh center without spines removed
    width_no_spine_median=null : double                       # median width from mesh center with spines removed
    width_90_perc=null   : double                       # 90th percentile for width without spines removed
    width_no_spine_90_perc=null : double                       # 90th percentile for width with spines removed
    n_spines             : int unsigned                 # 
    n_boutons            : int unsigned                 # 
    spines_per_branch=null : double                       # 
    skeletal_length_eligible=null : double                       # the skeletal length for all branches searched for spines
    n_spine_eligible_branches=null : int                          # the number of branches that were checked for spines because passed width threshold
    spine_density_eligible=null : double                       # n_spines/skeletal_length_eligible
    spines_per_branch_eligible=null : double                       # n_spines/n_spine_eligible_branches
    total_spine_volume=null : double                       # the sum of all spine volume
    spine_volume_median=null : double                       # median of the spine volume for those spines with able to calculate volume
    spine_volume_density=null : double                       # total_spine_volume/skeletal_length
    spine_volume_density_eligible=null : double                       # total_spine_volume/skeletal_length_eligible
    spine_volume_per_branch_eligible=null : double                       # total_spine_volume/n_spine_eligible_branches
    centroid_x=null      : int unsigned                 # (EM voxels)
    centroid_y=null      : int unsigned                 # (EM voxels)
    centroid_z=null      : int unsigned                 # (EM voxels)
    centroid_x_nm=null   : double                       # nm x coordinate of soma
    centroid_y_nm=null   : double                       # nm y coordinate of soma
    centroid_z_nm=null   : double                       # nm z coordinate of soma
    centroid_volume      : double                       # 
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
    run_time=null        : double                       # the amount of time to run (seconds)
    """
            
    class Object(djp.Part):
        definition = """
        -> master
        ---
        decomposition        : <minnie65_decomposition>     # in-place path to the hdf5 mesh file
        neuron_graph         : <minnie65_graph>             # graph
        neuron_graph_high_fid_axon : <minnie65_graph>             # graph
        """

@schema
class DecompositionSplitMultiSoma(djp.Computed):
    definition = """
    -> Decomposition
    -> DecompositionSplitMethod
    ---
    n_somas              : tinyint unsigned             # the number of somas found for this base segment
    n_splits             : int unsigned                 # the number of cuts required to help split the neuron
    split_results        : longblob                     # will store the results of how to split the limbs of neuron objects from original neuron
    red_blue_split_results : longblob                     # 
    run_time=null        : double                       # the amount of time to run (seconds)
    """


@schema
class DecompositionSplitMultiSomaLinks(djp.Computed):
    definition = """
    -> DecompositionSplitMultiSoma
    cut_index            : tinyint unsigned             # the version of the splitting algorithm used
    ---
    cut_id=null          : varchar(60)                  # 
    cut_reason=null      : varchar(60)                  # 
    link=null            : varchar(200)                 # 
    allen_link=null      : varchar(200)                 # 
    api_id=null          : varchar(40)                  # 
    split_generated=null : tinyint                      # 
    """


@schema
class DecompositionCellTypeBranchSample(djp.Computed):
    definition = """
    -> DecompositionCellType
    limb_idx             : int unsigned                 # 
    branch_idx           : int unsigned                 # 
    ---
    width_new=null       : float                        # 
    n_spines             : int unsigned                 # 
    skeletal_length      : float                        # 
    """
            
    class Object(djp.Part):
        definition = """
        -> master
        limb_idx             : int unsigned                 # 
        branch_idx           : int unsigned                 # 
        ---
        branch_obj           : <minnie65_decomposition>     # the branch object stored
        """


@schema
class DecompositionValidation(djp.Manual):
    definition = """
    segment_id           : bigint unsigned              # 
    annotation_index     : tinyint unsigned             # 
    user_name            : varchar(30)                  # 
    ---
    category             : enum('soma','axon','glia','other') # 
    exist                : enum('yes','no','unsure')    # 
    label                : enum('yes','yes_refinement','no','unsure') # 
    percentage           : tinyint unsigned             # 
    notes                : varchar(500)                 # 
    timestamp=CURRENT_TIMESTAMP : timestamp                    # 
    """


@schema
class AutoProofreadNeuronMethod(djp.Lookup):
    hash_name = 'auto_proofread_neuron_method'
    definition = """
    auto_proofread_neuron_method : varchar(8)                   # hash
    ---
    timestamp=CURRENT_TIMESTAMP : timestamp                    # 
    """
            
    class Standard(djp.Part):
        enable_hashing = True
        hash_name = "auto_proofread_neuron_method"
        hashed_attrs = (
            "wi_ma_hi_lo_de_in", "up_wi_ma_hi_lo_de_in", "ma_de_to_re_ab_lo_de_in", "wi_ma_hi_hi_de_in_de", 
            "up_wi_ma_hi_hi_de_in_de", "de_br_fi", "de_br_fi_in", "do_ba_th_in_do_b", "do_ba_th_ax_th_in", 
            "double_back_threshold_axon_thin_inh", "mi_up_sk_di", "mi_di_fr_so_fo_pr", "mi_de_to_re", "ma_de_to_re_ab", 
            "ma_de_to_re", "ma_de_to_re_wi", "ma_de_to_re_wi_th", "wi_mi", "wi_ma", "up_wi_ma", "ax_de", "sk_di_po_x", 
            "sk_di_po_y", "of_hi_d_ma", "co_di_hi_d_ma", "wo_ca_sk_an_ma_th_hi_d_ma", "wi_di_ma_hi_d_ma", 
            "wi_di_pe_hi_d_ma", "pe_sy_fi_hi_d_ma", "sy_de_di_th_hi_d_ma", "n_sy_di_th_hi_d_ma", "sk_an_ma_th_hi_d_ma", 
            "sk_an_bu_hi_d_ma", "wi_di_pe_th_hi_d_ma", "wi_di_pe_bu_hi_d_ma", "ki_ch_hi_d_ma", "ki_ch_bb_lo_si_th_hi_d_ma", 
            "ma_me_hi_d_ma", "us_ex_pa_hi_d_ma", "us_hi_de_fa_po_fi", "wi_mi_hi_de_fa_po", "si_sk_an_ma_hi_de_fa_po", 
            "sk_di_lo_d_ma", "mi_up_sk_di_lo_d_ma", "mi_de_to_re_lo_d_ma", "ma_de_to_re_wi_lo_d_ma", 
            "ma_de_to_re_ab_lo_d_ma", "ma_de_to_re_lo_d_ma", "wi_ma_lo_d_ma", "up_wi_ma_lo_d_ma", "of_lo_d_ma", 
            "co_di_lo_d_ma", "wo_ca_sk_an_ma_th_lo_d_ma", "wi_di_ma_lo_d_ma", "wi_di_pe_lo_d_ma", "pe_sy_fi_lo_d_ma", 
            "sy_de_di_th_lo_d_ma", "n_sy_di_th_lo_d_ma", "wi_ma_de_re", "wi_ma_de_do_ba_re", "up_sk_le_mi_de_re", 
            "up_sk_le_mi_wi_j_de", "br_sk_le_mi_wi_j_de", "up_sk_le_mi_fo_mi_wi_j_de", "wi_ju_ma_wi_j_de", 
            "up_sk_le_mi_wi_j_ax", "br_sk_le_mi_wi_j_ax", "up_sk_le_mi_fo_mi_wi_j_ax", "wi_ju_ma_wi_j_ax", 
            "ax_wi_th_ma_wi_j_ax", "do_ba_th_do_b_de", "co_di_do_b_de", "of_do_b_de", "br_sk_le_mi_do_b_de", 
            "up_sk_le_mi_fo_mi_wi_j_de", "wi_ju_ma_wi_j_de", "up_sk_le_mi_wi_j_ax", "br_sk_le_mi_wi_j_ax", 
            "up_sk_le_mi_fo_mi_wi_j_ax", "wi_ju_ma_wi_j_ax", "ax_wi_th_ma_wi_j_ax", "do_ba_th_do_b_de", "co_di_do_b_de", 
            "of_do_b_de", "br_sk_le_mi_do_b_de", "so_an_to_ap", "mu_ap_he", "ma_up_an_sh_li", "mi_up_le_sh_li", 
            "mi_up_pe_ma_sh_li", "mi_up_le_ba_sh_li", "mi_up_pe_ma_ba_sh_li", "wi_mi_sh_li", "mi_sk_le_fi_ap", 
            "mi_di_ab_so_fi_ap", "ca_co_co_ra_ap", "mu_ap_po_ap", "wi_mi_ap_hi_so", "di_fr_so_ap_hi_so", 
            "mi_th_ne_so_sk_le_ap_hi_s", "no_up_sk_di_up_bu_fi_ap_o", "so_di_bu_fi_ap_on", "do_ve_di_bu_fi_ap_on", 
            "de_ti_br_fi_ap_on", "ad_lo_de_ap_of_sh_tu", "lo_de_ap_mi_an_tu", "lo_de_ap_ma_an_tu", "mi_an_ob", 
            "ma_an_ob", "pe_ma_re_ve_mi_ob", "di_ma_re_ve_mi_ob"
        )
        definition = """
        # parameters for automatic proofreading
        -> master
        ---
        wi_ma_hi_lo_de_in=null : int unsigned                 # 
        up_wi_ma_hi_lo_de_in=null : int unsigned                 # 
        ma_de_to_re_ab_lo_de_in=null : int unsigned                 # 
        wi_ma_hi_hi_de_in_de=null : int unsigned                 # 
        up_wi_ma_hi_hi_de_in_de=null : int unsigned                 # 
        de_br_fi=null        : tinyint unsigned             # 
        de_br_fi_in=null     : tinyint unsigned             # 
        do_ba_th_in_do_b=null : blob                         # 
        do_ba_th_ax_th_in=null : int unsigned                 # 
        double_back_threshold_axon_thin_inh=null : int unsigned                 # 
        mi_up_sk_di=null     : int unsigned                 # 
        mi_di_fr_so_fo_pr=null : int unsigned                 # 
        mi_de_to_re=null     : int unsigned                 # 
        ma_de_to_re_ab=null  : int unsigned                 # 
        ma_de_to_re=null     : int unsigned                 # 
        ma_de_to_re_wi=null  : int unsigned                 # 
        ma_de_to_re_wi_th=null : int unsigned                 # 
        wi_mi=null           : int unsigned                 # 
        wi_ma=null           : int unsigned                 # 
        up_wi_ma=null        : int unsigned                 # 
        ax_de=null           : tinyint unsigned             # 
        sk_di_po_x=null      : blob                         # 
        sk_di_po_y=null      : blob                         # 
        of_hi_d_ma=null      : int unsigned                 # 
        co_di_hi_d_ma=null   : int unsigned                 # 
        wo_ca_sk_an_ma_th_hi_d_ma=null : int unsigned                 # 
        wi_di_ma_hi_d_ma=null : int unsigned                 # 
        wi_di_pe_hi_d_ma=null : float                        # 
        pe_sy_fi_hi_d_ma=null : tinyint unsigned             # 
        sy_de_di_th_hi_d_ma=null : float                        # 
        n_sy_di_th_hi_d_ma=null : int unsigned                 # 
        sk_an_ma_th_hi_d_ma=null : int unsigned                 # 
        sk_an_bu_hi_d_ma=null : int unsigned                 # 
        wi_di_pe_th_hi_d_ma=null : float                        # 
        wi_di_pe_bu_hi_d_ma=null : float                        # 
        ki_ch_hi_d_ma=null   : tinyint unsigned             # 
        ki_ch_bb_lo_si_th_hi_d_ma=null : int unsigned                 # 
        ma_me_hi_d_ma=null   : varchar(36)                  # 
        us_ex_pa_hi_d_ma=null : tinyint unsigned             # 
        us_hi_de_fa_po_fi=null : tinyint unsigned             # 
        wi_mi_hi_de_fa_po=null : int unsigned                 # 
        si_sk_an_ma_hi_de_fa_po=null : int unsigned                 # 
        sk_di_lo_d_ma=null   : int unsigned                 # 
        mi_up_sk_di_lo_d_ma=null : int unsigned                 # 
        mi_de_to_re_lo_d_ma=null : int unsigned                 # 
        ma_de_to_re_wi_lo_d_ma=null : int unsigned                 # 
        ma_de_to_re_ab_lo_d_ma=null : int unsigned                 # 
        ma_de_to_re_lo_d_ma=null : int unsigned                 # 
        wi_ma_lo_d_ma=null   : int unsigned                 # 
        up_wi_ma_lo_d_ma=null : int unsigned                 # 
        of_lo_d_ma=null      : int unsigned                 # 
        co_di_lo_d_ma=null   : int unsigned                 # 
        wo_ca_sk_an_ma_th_lo_d_ma=null : int unsigned                 # 
        wi_di_ma_lo_d_ma=null : int unsigned                 # 
        wi_di_pe_lo_d_ma=null : float                        # 
        pe_sy_fi_lo_d_ma=null : tinyint unsigned             # 
        sy_de_di_th_lo_d_ma=null : float                        # 
        n_sy_di_th_lo_d_ma=null : int unsigned                 # 
        wi_ma_de_re=null     : int unsigned                 # 
        wi_ma_de_do_ba_re=null : int unsigned                 # 
        up_sk_le_mi_de_re=null : int unsigned                 # 
        up_sk_le_mi_wi_j_de=null : int unsigned                 # 
        br_sk_le_mi_wi_j_de=null : int unsigned                 # 
        up_sk_le_mi_fo_mi_wi_j_de=null : int unsigned                 # 
        wi_ju_ma_wi_j_de=null : int unsigned                 # 
        up_sk_le_mi_wi_j_ax=null : int unsigned                 # 
        br_sk_le_mi_wi_j_ax=null : int unsigned                 # 
        up_sk_le_mi_fo_mi_wi_j_ax=null : int unsigned                 # 
        wi_ju_ma_wi_j_ax=null : int unsigned                 # 
        ax_wi_th_ma_wi_j_ax=null : int unsigned                 # 
        do_ba_th_do_b_de=null : int unsigned                 # 
        co_di_do_b_de=null   : int unsigned                 # 
        of_do_b_de=null      : int unsigned                 # 
        br_sk_le_mi_do_b_de=null : int unsigned                 # 
        so_an_to_ap=null     : int unsigned                 # 
        mu_ap_he=null        : int                          # 
        ma_up_an_sh_li=null  : int unsigned                 # 
        mi_up_le_sh_li=null  : int unsigned                 # 
        mi_up_pe_ma_sh_li=null : float                        # 
        mi_up_le_ba_sh_li=null : int unsigned                 # 
        mi_up_pe_ma_ba_sh_li=null : float                        # 
        wi_mi_sh_li=null     : int unsigned                 # 
        mi_sk_le_fi_ap=null  : int unsigned                 # 
        mi_di_ab_so_fi_ap=null : int unsigned                 # 
        ca_co_co_ra_ap=null  : int unsigned                 # 
        mu_ap_po_ap=null     : tinyint unsigned             # 
        wi_mi_ap_hi_so=null  : int unsigned                 # 
        di_fr_so_ap_hi_so=null : int unsigned                 # 
        mi_th_ne_so_sk_le_ap_hi_s=null : int unsigned                 # 
        no_up_sk_di_up_bu_fi_ap_o=null : int                          # 
        so_di_bu_fi_ap_on=null : int                          # 
        do_ve_di_bu_fi_ap_on=null : int                          # 
        de_ti_br_fi_ap_on=null : varchar(25)                  # 
        ad_lo_de_ap_of_sh_tu=null : tinyint unsigned             # 
        lo_de_ap_mi_an_tu=null : int unsigned                 # 
        lo_de_ap_ma_an_tu=null : int unsigned                 # 
        mi_an_ob=null        : int unsigned                 # 
        ma_an_ob=null        : int unsigned                 # 
        pe_ma_re_ve_mi_ob=null : float                        # 
        di_ma_re_ve_mi_ob=null : int unsigned                 # 
        name=null            : varchar(24)                  # 
        description=null     : varchar(120)                 # 
        """


@schema
class AutoProofreadNeuronMethodMeshSet(djp.Lookup):
    enable_hashing = True
    hash_name = 'auto_proofread_neuron_method_mesh_set'
    hashed_attrs = 'auto_proofread_neuron_method', 'mesh_set'
    hash_group = True
    definition = """
    #
    auto_proofread_neuron_method_mesh_set : varchar(8)                   # hash
    ---
    name=null            : varchar(24)                  # 
    description=null     : varchar(120)                 # 
    timestamp=CURRENT_TIMESTAMP : timestamp                    # 
    """
            
    class Member(djp.Part):
        definition = """
        -> master
        -> AutoProofreadNeuronMethod
        -> m65mor.MeshSet
        """


@schema
class AutoProofreadNeuron(djp.Computed):
    definition = """
    -> DecompositionCellType
    -> AutoProofreadNeuronMethod
    ---
    multiplicity         : tinyint unsigned             # the total number of neurons that came from the parent segment id
    cell_type_used=null  : enum('external','baylor')    # 
    cell_type=null       : enum('excitatory','inhibitory','other','unknown') # 
    nucleus_id           : int unsigned                 # id of nucleus from the flat segmentation  Equivalent to Allen: 'id'.
    nuclei_distance      : double                       # the distance to the closest nuclei (even if no matching nuclei found)
    n_nuclei_in_radius   : tinyint unsigned             # the number of nuclei within the search radius of 15000 belonging to that segment
    n_nuclei_in_bbox     : tinyint unsigned             # the number of nuclei within the bounding box of that soma
    centroid_x=null      : int unsigned                 # (EM voxels)
    centroid_y=null      : int unsigned                 # (EM voxels)
    centroid_z=null      : int unsigned                 # (EM voxels)
    centroid_x_nm=null   : double                       # nm x coordinate of soma
    centroid_y_nm=null   : double                       # nm y coordinate of soma
    centroid_z_nm=null   : double                       # nm z coordinate of soma
    centroid_volume      : double                       # 
    max_soma_n_faces     : int unsigned                 # The largest number of faces of the somas
    max_soma_volume      : int unsigned                 # The largest volume of the somas the (volume in billions (10*9 nm^3))
    max_soma_area        : int unsigned                 # The largest surface area of the somas  (area in um)
    syn_density_post_after_proof : double                       # 
    syn_density_head_after_proof : double                       # 
    syn_density_neck_after_proof : double                       # 
    syn_density_shaft_after_proof : double                       # 
    skeletal_length_processed_syn_after_proof : double                       # 
    spine_density_after_proof : double                       # 
    skeletal_length_processed_spine_after_proof : double                       # 
    baylor_cell_type_after_proof=null : enum('excitatory','inhibitory','other','unknown') # 
    baylor_cell_type_exc_probability_after_proof=null : double                       # 
    baylor_cell_type=null : enum('excitatory','inhibitory','other','unknown') # 
    baylor_cell_type_exc_probability=null : double                       # 
    external_cell_type=null : enum('excitatory','inhibitory','other','unknown') # 
    cell_type_used_for_axon=null : enum('external','baylor')    # 
    cell_type_for_axon=null : enum('excitatory','inhibitory','other','unknown') # 
    external_cell_type_n_nuc=null : tinyint unsigned             # 
    external_cell_type_fine=null : varchar(256)                 # 
    external_layer=null  : enum('LAYER_1','LAYER_2/3','LAYER_2','LAYER_3','LAYER_4','LAYER_5','LAYER_6','UNCLASSIFIED','WHITE_MATTER') # 
    external_visual_area=null : enum('V1','RL','AL')         # 
    axon_angle_max=null  : double                       # 
    axon_angle_min=null  : double                       # 
    n_axon_angles        : tinyint unsigned             # 
    axon_start_distance_from_soma=null : double                       # 
    n_vertices           : int unsigned                 # number of vertices
    n_faces              : int unsigned                 # number of faces
    n_limbs              : int                          # 
    n_branches           : int                          # 
    max_limb_n_branches=null : int                          # 
    skeletal_length=null : double                       # 
    max_limb_skeletal_length=null : double                       # 
    median_branch_length=null : double                       # gives information on average skeletal length to next branch point
    width_median=null    : double                       # median width from mesh center without spines removed
    width_no_spine_median=null : double                       # median width from mesh center with spines removed
    width_90_perc=null   : double                       # 90th percentile for width without spines removed
    width_no_spine_90_perc=null : double                       # 90th percentile for width with spines removed
    n_spines             : bigint                       # 
    n_boutons            : bigint                       # 
    spines_per_branch=null : double                       # 
    skeletal_length_eligible=null : double                       # the skeletal length for all branches searched for spines
    n_spine_eligible_branches=null : int                          # the number of branches that were checked for spines because passed width threshold
    spine_density_eligible=null : double                       # n_spines/skeletal_length_eligible
    spines_per_branch_eligible=null : double                       # n_spines/n_spine_eligible_branches
    total_spine_volume=null : double                       # the sum of all spine volume
    spine_volume_median=null : double                       # median of the spine volume for those spines with able to calculate volume
    spine_volume_density=null : double                       # total_spine_volume/skeletal_length
    spine_volume_density_eligible=null : double                       # total_spine_volume/skeletal_length_eligible
    spine_volume_per_branch_eligible=null : double                       # total_spine_volume/n_spine_eligible_branches
    dendrite_skeletal_length : int unsigned                 # 
    dendrite_area        : int unsigned                 # 
    dendrite_mesh_volume : int unsigned                 # 
    dendrite_n_branches  : int unsigned                 # 
    axon_skeletal_length : int unsigned                 # 
    axon_area            : int unsigned                 # 
    axon_mesh_volume     : int unsigned                 # 
    axon_n_branches      : int unsigned                 # 
    basal_skeletal_length : int unsigned                 # 
    basal_area           : int unsigned                 # 
    basal_mesh_volume    : int unsigned                 # 
    basal_n_branches     : int unsigned                 # 
    apical_skeletal_length : int unsigned                 # 
    apical_area          : int unsigned                 # 
    apical_mesh_volume   : int unsigned                 # 
    apical_n_branches    : int unsigned                 # 
    apical_tuft_skeletal_length : int unsigned                 # 
    apical_tuft_area     : int unsigned                 # 
    apical_tuft_mesh_volume : int unsigned                 # 
    apical_tuft_n_branches : int unsigned                 # 
    apical_shaft_skeletal_length : int unsigned                 # 
    apical_shaft_area    : int unsigned                 # 
    apical_shaft_mesh_volume : int unsigned                 # 
    apical_shaft_n_branches : int unsigned                 # 
    oblique_skeletal_length : int unsigned                 # 
    oblique_area         : int unsigned                 # 
    oblique_mesh_volume  : int unsigned                 # 
    oblique_n_branches   : int unsigned                 # 
    apical_total_skeletal_length : int unsigned                 # 
    apical_total_area    : int unsigned                 # 
    apical_total_mesh_volume : int unsigned                 # 
    apical_total_n_branches : int unsigned                 # 
    n_syn_valid          : int unsigned                 # 
    n_syn_valid_pre      : int unsigned                 # 
    n_syn_valid_post     : int unsigned                 # 
    n_syn_error          : int unsigned                 # 
    n_syn_error_pre      : int unsigned                 # 
    n_syn_error_post     : int unsigned                 # 
    n_syn_presyns_on_dendrite : int unsigned                 # 
    n_syn_mesh_errored   : int unsigned                 # 
    n_syn_distance_errored : int unsigned                 # 
    n_syn_no_label       : int unsigned                 # 
    n_syn_head           : int unsigned                 # 
    n_syn_neck           : int unsigned                 # 
    n_syn_shaft          : int unsigned                 # 
    n_syn_no_head        : int unsigned                 # 
    n_syn_bouton         : int unsigned                 # 
    n_syn_non_bouton     : int unsigned                 # 
    n_syn_dendrite       : int unsigned                 # 
    n_syn_axon           : int unsigned                 # 
    n_syn_basal          : int unsigned                 # 
    n_syn_apical         : int unsigned                 # 
    n_syn_apical_tuft    : int unsigned                 # 
    n_syn_apical_shaft   : int unsigned                 # 
    n_syn_oblique        : int unsigned                 # 
    n_syn_soma           : int unsigned                 # 
    n_syn_apical_total   : int unsigned                 # 
    n_syn_dendrite_head_postsyn : int unsigned                 # 
    n_syn_dendrite_neck_postsyn : int unsigned                 # 
    n_syn_dendrite_shaft_postsyn : int unsigned                 # 
    n_syn_dendrite_no_head_postsyn : int unsigned                 # 
    n_syn_axon_bouton_presyn : int unsigned                 # 
    n_syn_axon_bouton_postsyn : int unsigned                 # 
    n_syn_axon_non_bouton_presyn : int unsigned                 # 
    n_syn_axon_non_bouton_postsyn : int unsigned                 # 
    n_syn_basal_head_postsyn : int unsigned                 # 
    n_syn_basal_neck_postsyn : int unsigned                 # 
    n_syn_basal_shaft_postsyn : int unsigned                 # 
    n_syn_basal_no_head_postsyn : int unsigned                 # 
    n_syn_apical_head_postsyn : int unsigned                 # 
    n_syn_apical_neck_postsyn : int unsigned                 # 
    n_syn_apical_shaft_postsyn : int unsigned                 # 
    n_syn_apical_no_head_postsyn : int unsigned                 # 
    n_syn_apical_tuft_head_postsyn : int unsigned                 # 
    n_syn_apical_tuft_neck_postsyn : int unsigned                 # 
    n_syn_apical_tuft_shaft_postsyn : int unsigned                 # 
    n_syn_apical_tuft_no_head_postsyn : int unsigned                 # 
    n_syn_apical_shaft_head_postsyn : int unsigned                 # 
    n_syn_apical_shaft_neck_postsyn : int unsigned                 # 
    n_syn_apical_shaft_shaft_postsyn : int unsigned                 # 
    n_syn_apical_shaft_no_head_postsyn : int unsigned                 # 
    n_syn_oblique_head_postsyn : int unsigned                 # 
    n_syn_oblique_neck_postsyn : int unsigned                 # 
    n_syn_oblique_shaft_postsyn : int unsigned                 # 
    n_syn_oblique_no_head_postsyn : int unsigned                 # 
    n_syn_soma_no_label_presyn : int unsigned                 # 
    n_syn_soma_no_label_postsyn : int unsigned                 # 
    n_syn_apical_total_head_presyn : int unsigned                 # 
    n_syn_apical_total_head_postsyn : int unsigned                 # 
    n_syn_apical_total_neck_presyn : int unsigned                 # 
    n_syn_apical_total_neck_postsyn : int unsigned                 # 
    n_syn_apical_total_shaft_presyn : int unsigned                 # 
    n_syn_apical_total_shaft_postsyn : int unsigned                 # 
    n_syn_apical_total_no_head_presyn : int unsigned                 # 
    n_syn_apical_total_no_head_postsyn : int unsigned                 # 
    n_syn_axon_ais_postsyn=null : int unsigned                 # 
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
    axon_n_limbs=null    : int unsigned                 # 
    axon_soma_angle_max=null : double                       # 
    axon_soma_angle_min=null : double                       # 
    apical_branch_length_median=null : double                       # 
    apical_branch_length_mean=null : double                       # 
    apical_n_short_branches=null : int unsigned                 # 
    apical_n_long_branches=null : int unsigned                 # 
    apical_n_medium_branches=null : int unsigned                 # 
    apical_bbox_volume=null : double                       # 
    apical_bbox_x_min=null : double                       # 
    apical_bbox_y_min=null : double                       # 
    apical_bbox_z_min=null : double                       # 
    apical_bbox_x_max=null : double                       # 
    apical_bbox_y_max=null : double                       # 
    apical_bbox_z_max=null : double                       # 
    apical_bbox_x_min_soma_relative=null : double                       # 
    apical_bbox_y_min_soma_relative=null : double                       # 
    apical_bbox_z_min_soma_relative=null : double                       # 
    apical_bbox_x_max_soma_relative=null : double                       # 
    apical_bbox_y_max_soma_relative=null : double                       # 
    apical_bbox_z_max_soma_relative=null : double                       # 
    apical_n_limbs=null  : int unsigned                 # 
    apical_soma_angle_max=null : double                       # 
    apical_soma_angle_min=null : double                       # 
    basal_branch_length_median=null : double                       # 
    basal_branch_length_mean=null : double                       # 
    basal_n_short_branches=null : int unsigned                 # 
    basal_n_long_branches=null : int unsigned                 # 
    basal_n_medium_branches=null : int unsigned                 # 
    basal_bbox_volume=null : double                       # 
    basal_bbox_x_min=null : double                       # 
    basal_bbox_y_min=null : double                       # 
    basal_bbox_z_min=null : double                       # 
    basal_bbox_x_max=null : double                       # 
    basal_bbox_y_max=null : double                       # 
    basal_bbox_z_max=null : double                       # 
    basal_bbox_x_min_soma_relative=null : double                       # 
    basal_bbox_y_min_soma_relative=null : double                       # 
    basal_bbox_z_min_soma_relative=null : double                       # 
    basal_bbox_x_max_soma_relative=null : double                       # 
    basal_bbox_y_max_soma_relative=null : double                       # 
    basal_bbox_z_max_soma_relative=null : double                       # 
    basal_n_limbs=null   : int unsigned                 # 
    basal_soma_angle_max=null : double                       # 
    basal_soma_angle_min=null : double                       # 
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
    dendrite_n_limbs=null : int unsigned                 # 
    dendrite_soma_angle_max=null : double                       # 
    dendrite_soma_angle_min=null : double                       # 
    run_time=null        : double                       # the amount of time to run (seconds)
    """
            
    class BoundingBox(djp.Part):
        definition = """
        -> master
        ---
        bbox_x_min           : float                        # 
        bbox_y_min           : float                        # 
        bbox_z_min           : float                        # 
        bbox_x_max           : float                        # 
        bbox_y_max           : float                        # 
        bbox_z_max           : float                        # 
        """
                    
    class ErrorStats(djp.Part):
        definition = """
        -> master
        ---
        axon_on_dendrite_merges_error_area=null : double                       # the area (in um ^ 2) of the faces canceled out by filter
        axon_on_dendrite_merges_error_length=null : double                       # the length (in um) of skeleton distance canceled out by filter
        high_degree_branching_error_area=null : double                       # the area (in um ^ 2) of the faces canceled out by filter
        high_degree_branching_error_length=null : double                       # the length (in um) of skeleton distance canceled out by filter
        low_degree_branching_error_area=null : double                       # the area (in um ^ 2) of the faces canceled out by filter
        low_degree_branching_error_length=null : double                       # the length (in um) of skeleton distance canceled out by filter
        high_degree_branching_dendrite_error_area=null : double                       # the area (in um ^ 2) of the faces canceled out by filter
        high_degree_branching_dendrite_error_length=null : double                       # the length (in um) of skeleton distance canceled out by filter
        width_jump_up_dendrite_error_area=null : double                       # the area (in um ^ 2) of the faces canceled out by filter
        width_jump_up_dendrite_error_length=null : double                       # the length (in um) of skeleton distance canceled out by filter
        width_jump_up_axon_error_area=null : double                       # the area (in um ^ 2) of the faces canceled out by filter
        width_jump_up_axon_error_length=null : double                       # the length (in um) of skeleton distance canceled out by filter
        double_back_dendrite_error_area=null : double                       # the area (in um ^ 2) of the faces canceled out by filter
        double_back_dendrite_error_length=null : double                       # the length (in um) of skeleton distance canceled out by filter
        """
                    
    class Object(djp.Part):
        definition = """
        -> master
        ---
        neuron_mesh_faces    : <minnie65_auto_proof_meshes> # face indices for neuron_mesh_faces of final proofread neuron
        neuron_skeleton      : <minnie65_auto_proof_skeletons> # skeleton array for neuron_skeleton of final proofread neuron
        dendrite_mesh_faces  : <minnie65_auto_proof_meshes> # face indices for dendrite_mesh_faces of final proofread neuron
        axon_mesh_faces      : <minnie65_auto_proof_meshes> # face indices for axon_mesh_faces of final proofread neuron
        basal_mesh_faces     : <minnie65_auto_proof_meshes> # face indices for basal_mesh_faces of final proofread neuron
        apical_mesh_faces    : <minnie65_auto_proof_meshes> # face indices for apical_mesh_faces of final proofread neuron
        apical_tuft_mesh_faces : <minnie65_auto_proof_meshes> # face indices for apical_tuft_mesh_faces of final proofread neuron
        apical_shaft_mesh_faces : <minnie65_auto_proof_meshes> # face indices for apical_shaft_mesh_faces of final proofread neuron
        oblique_mesh_faces   : <minnie65_auto_proof_meshes> # face indices for oblique_mesh_faces of final proofread neuron
        dendrite_skeleton    : <minnie65_auto_proof_skeletons> # skeleton array for dendrite_skeleton of final proofread neuron
        axon_skeleton        : <minnie65_auto_proof_skeletons> # skeleton array for axon_skeleton of final proofread neuron
        basal_skeleton       : <minnie65_auto_proof_skeletons> # skeleton array for basal_skeleton of final proofread neuron
        apical_skeleton      : <minnie65_auto_proof_skeletons> # skeleton array for apical_skeleton of final proofread neuron
        apical_tuft_skeleton : <minnie65_auto_proof_skeletons> # skeleton array for apical_tuft_skeleton of final proofread neuron
        apical_shaft_skeleton : <minnie65_auto_proof_skeletons> # skeleton array for apical_shaft_skeleton of final proofread neuron
        oblique_skeleton     : <minnie65_auto_proof_skeletons> # skeleton array for oblique_skeleton of final proofread neuron
        limb_branch_to_cancel : longblob                     # stores the limb information from
        red_blue_suggestions=null : longblob                     # 
        split_locations=null : longblob                     # 
        split_locations_before_filter=null : longblob                     # 
        neuron_graph=null    : <minnie65_graph>             # the graph for the
        decomposition=null   : <minnie65_decomposition>     # 
        """
                    
    class Synapse(djp.Part):
        definition = """
        -> master
        ---
        secondary_seg_id     : bigint unsigned              # segment_id of the cell. Equivalent to Allen 'pt_root_id
        primary_nucleus_id   : int unsigned                 # id of nucleus from the flat segmentation  Equivalent to Allen: 'id'.
        synapse_type         : enum('presyn','postsyn')     # 
        skeletal_distance_to_soma=null : double                       # the length (in um) of skeleton distance from synapse to soma (-2 if on the soma)
        limb_idx=null        : tinyint unsigned             # 
        branch_idx=null      : int unsigned                 # 
        spine_bouton         : enum('head','neck','shaft','no_head','bouton','non_bouton','no_label') # 
        compartment_coarse=null : enum('soma','axon','dendrite') # 
        compartment_fine=null : enum('basal','apical','apical_tuft','apical_shaft','oblique','inhibitory') # 
        """
                    
    class SynapseErrors(djp.Part):
        definition = """
        -> master
        synapse_id           : bigint unsigned              # synapse index within the segmentation
        ---
        secondary_seg_id     : bigint unsigned              # segment_id of the cell. Equivalent to Allen 'pt_root_id
        primary_nucleus_id   : int unsigned                 # id of nucleus from the flat segmentation  Equivalent to Allen: 'id'.
        synapse_type         : enum('presyn','postsyn')     # 
        """
                    
    class SynapseErrorsPreDend(djp.Part):
        definition = """
        -> master
        synapse_id           : bigint unsigned              # synapse index within the segmentation
        ---
        secondary_seg_id     : bigint unsigned              # segment_id of the cell. Equivalent to Allen 'pt_root_id
        primary_nucleus_id   : int unsigned                 # id of nucleus from the flat segmentation  Equivalent to Allen: 'id'.
        synapse_type         : enum('presyn','postsyn')     # 
        skeletal_distance_to_soma=null : double                       # the length (in um) of skeleton distance from synapse to soma (-2 if on the soma)
        limb_idx=null        : tinyint unsigned             # 
        branch_idx=null      : int unsigned                 # 
        """
                    
    class SynapseErrorsPreDendr(djp.Part):
        definition = """
        -> master.proj(primary_seg_id="segment_id")
        synapse_id           : bigint unsigned              # synapse index within the segmentation
        ---
        secondary_seg_id     : bigint unsigned              # segment_id of the cell. Equivalent to Allen 'pt_root_id
        primary_nucleus_id   : int unsigned                 # id of nucleus from the flat segmentation  Equivalent to Allen: 'id'.
        synapse_type         : enum('presyn','postsyn')     # 
        skeletal_distance_to_soma=null : double                       # the length (in um) of skeleton distance from synapse to soma (-2 if on the soma)
        limb_idx=null        : tinyint unsigned             # 
        branch_idx=null      : int unsigned                 # 
        """


@schema
class AutoProofreadNeuronGnnEmbedMethod(djp.Lookup):
    hash_name = 'gnn_embed_method'
    definition = """
    gnn_embed_method     : varchar(8)                   # hash
    ---
    timestamp=CURRENT_TIMESTAMP : timestamp                    # 
    """
            
    class Standard(djp.Part):
        hash_name = 'gnn_embed_method'
        hashed_attrs = (
            "n_hidden_channels", "global_pool_type", "n_layers", "use_bn", "norm_mean_mesh_volume", "norm_mean_n_spines", 
            "norm_mean_n_synapses_head", "norm_mean_n_synapses_neck", "norm_mean_n_synapses_post", "norm_mean_n_synapses_pre", 
            "norm_mean_skeletal_length", "norm_mean_total_spine_volume", "norm_mean_width_upstream", "norm_mean_width_downstream", 
            "norm_mean_apical_label", "norm_mean_basal_label", "norm_mean_skeleton_vector_downstream_phi", 
            "norm_mean_skeleton_vector_downstream_theta", "norm_mean_skeleton_vector_upstream_phi", 
            "norm_mean_skeleton_vector_upstream_theta", "norm_mean_width_no_spine", "norm_std_mesh_volume", "norm_std_n_spines", 
            "norm_std_n_synapses_head", "norm_std_n_synapses_neck", "norm_std_n_synapses_post", "norm_std_n_synapses_pre", 
            "norm_std_skeletal_length", "norm_std_total_spine_volume", "norm_std_width_upstream", "norm_std_width_downstream", 
            "norm_std_apical_label", "norm_std_basal_label", "norm_std_skeleton_vector_downstream_phi", 
            "norm_std_skeleton_vector_downstream_theta", "norm_std_skeleton_vector_upstream_phi", 
            "norm_std_skeleton_vector_upstream_theta", "norm_std_width_no_spine", "model_name"
        )
        definition = """
        -> master
        ---
        n_hidden_channels=null : int unsigned                 # 
        global_pool_type=null : varchar(14)                  # 
        n_layers=null        : int unsigned                 # 
        use_bn=null          : tinyint unsigned             # 
        norm_mean_mesh_volume=null : float                        # 
        norm_mean_n_spines=null : float                        # 
        norm_mean_n_synapses_head=null : float                        # 
        norm_mean_n_synapses_neck=null : float                        # 
        norm_mean_n_synapses_post=null : float                        # 
        norm_mean_n_synapses_pre=null : float                        # 
        norm_mean_skeletal_length=null : float                        # 
        norm_mean_total_spine_volume=null : float                        # 
        norm_mean_width_upstream=null : float                        # 
        norm_mean_width_downstream=null : float                        # 
        norm_mean_apical_label=null : float                        # 
        norm_mean_basal_label=null : float                        # 
        norm_mean_skeleton_vector_downstream_phi=null : float                        # 
        norm_mean_skeleton_vector_downstream_theta=null : float                        # 
        norm_mean_skeleton_vector_upstream_phi=null : float                        # 
        norm_mean_skeleton_vector_upstream_theta=null : float                        # 
        norm_mean_width_no_spine=null : float                        # 
        norm_std_mesh_volume=null : float                        # 
        norm_std_n_spines=null : float                        # 
        norm_std_n_synapses_head=null : float                        # 
        norm_std_n_synapses_neck=null : float                        # 
        norm_std_n_synapses_post=null : float                        # 
        norm_std_n_synapses_pre=null : float                        # 
        norm_std_skeletal_length=null : float                        # 
        norm_std_total_spine_volume=null : float                        # 
        norm_std_width_upstream=null : float                        # 
        norm_std_width_downstream=null : float                        # 
        norm_std_apical_label=null : float                        # 
        norm_std_basal_label=null : float                        # 
        norm_std_skeleton_vector_downstream_phi=null : float                        # 
        norm_std_skeleton_vector_downstream_theta=null : float                        # 
        norm_std_skeleton_vector_upstream_phi=null : float                        # 
        norm_std_skeleton_vector_upstream_theta=null : float                        # 
        norm_std_width_no_spine=null : float                        # 
        model_name=null      : varchar(17)                  # 
        name=null            : varchar(24)                  # 
        description=null     : varchar(120)                 # 
        model_state_dict=null : longblob                     # 
        class_labels_mapping=null : longblob                     # 
        """
                    
    class TrainTestSets(djp.Part):
        definition = """
        -> master
        segment_id           : bigint unsigned              # 
        split_index          : bigint unsigned              # 
        ---
        cell_type_fine       : enum('23P','4P','5P-IT','5P-NP','5P-PT','6P-CT','6P-IT','BC','BPC','MC','NGC') # 
        split_type           : enum('train','val','test')   # 
        table_of_origin      : varchar(200)                 # 
        """
                    
    class WeightedPool(djp.Part):
        enable_hashing = True
        hash_name = 'gnn_embed_method'
        hashed_attrs = (
            "n_hidden_channels", "global_pool_type", "n_layers", "use_bn", "n_pool", "edge_weight", 
            "norm_mean_skeletal_length", "norm_mean_skeleton_vector_upstream_theta", "norm_mean_skeleton_vector_upstream_phi", 
            "norm_mean_skeleton_vector_downstream_theta", "norm_mean_skeleton_vector_downstream_phi", 
            "norm_mean_width_upstream", "norm_mean_width_no_spine", "norm_mean_width_downstream", 
            "norm_mean_n_synapses_post", "norm_mean_n_synapses_pre", "norm_mean_n_synapses_head_postsyn", 
            "norm_mean_n_synapses_neck_postsyn", "norm_mean_n_synapses_shaft_postsyn", 
            "norm_mean_n_synapses_no_head_postsyn", "norm_mean_synapse_volume_shaft_postsyn_sum", 
            "norm_mean_synapse_volume_head_postsyn_sum", "norm_mean_synapse_volume_no_head_postsyn_sum", 
            "norm_mean_synapse_volume_neck_postsyn_sum", "norm_mean_synapse_volume_postsyn_sum", 
            "norm_mean_n_spines", "norm_mean_spine_volume_sum", "norm_mean_soma_start_angle_max", 
            "norm_mean_max_soma_volume", "norm_mean_n_syn_soma", "norm_std_skeletal_length", 
            "norm_std_skeleton_vector_upstream_theta", "norm_std_skeleton_vector_upstream_phi", 
            "norm_std_skeleton_vector_downstream_theta", "norm_std_skeleton_vector_downstream_phi", 
            "norm_std_width_upstream", "norm_std_width_no_spine", "norm_std_width_downstream", 
            "norm_std_n_synapses_post", "norm_std_n_synapses_pre", "norm_std_n_synapses_head_postsyn", 
            "norm_std_n_synapses_neck_postsyn", "norm_std_n_synapses_shaft_postsyn", 
            "norm_std_n_synapses_no_head_postsyn", "norm_std_synapse_volume_shaft_postsyn_sum", 
            "norm_std_synapse_volume_head_postsyn_sum", "norm_std_synapse_volume_no_head_postsyn_sum", 
            "norm_std_synapse_volume_neck_postsyn_sum", "norm_std_synapse_volume_postsyn_sum", 
            "norm_std_n_spines", "norm_std_spine_volume_sum", "norm_std_soma_start_angle_max", 
            "norm_std_max_soma_volume", "norm_std_n_syn_soma", "model_name"
        )
        definition = """
        -> master
        ---
        n_hidden_channels=null : int unsigned                 # 
        global_pool_type=null : varchar(23)                  # 
        n_layers=null        : int unsigned                 # 
        use_bn=null          : tinyint unsigned             # 
        n_pool=null          : int unsigned                 # 
        edge_weight=null     : tinyint unsigned             # 
        norm_mean_skeletal_length=null : float                        # 
        norm_mean_skeleton_vector_upstream_theta=null : float                        # 
        norm_mean_skeleton_vector_upstream_phi=null : float                        # 
        norm_mean_skeleton_vector_downstream_theta=null : float                        # 
        norm_mean_skeleton_vector_downstream_phi=null : float                        # 
        norm_mean_width_upstream=null : float                        # 
        norm_mean_width_no_spine=null : float                        # 
        norm_mean_width_downstream=null : float                        # 
        norm_mean_n_synapses_post=null : float                        # 
        norm_mean_n_synapses_pre=null : float                        # 
        norm_mean_n_synapses_head_postsyn=null : float                        # 
        norm_mean_n_synapses_neck_postsyn=null : float                        # 
        norm_mean_n_synapses_shaft_postsyn=null : float                        # 
        norm_mean_n_synapses_no_head_postsyn=null : float                        # 
        norm_mean_synapse_volume_shaft_postsyn_sum=null : float                        # 
        norm_mean_synapse_volume_head_postsyn_sum=null : float                        # 
        norm_mean_synapse_volume_no_head_postsyn_sum=null : float                        # 
        norm_mean_synapse_volume_neck_postsyn_sum=null : float                        # 
        norm_mean_synapse_volume_postsyn_sum=null : float                        # 
        norm_mean_n_spines=null : float                        # 
        norm_mean_spine_volume_sum=null : float                        # 
        norm_mean_soma_start_angle_max=null : float                        # 
        norm_mean_max_soma_volume=null : float                        # 
        norm_mean_n_syn_soma=null : float                        # 
        norm_std_skeletal_length=null : float                        # 
        norm_std_skeleton_vector_upstream_theta=null : float                        # 
        norm_std_skeleton_vector_upstream_phi=null : float                        # 
        norm_std_skeleton_vector_downstream_theta=null : float                        # 
        norm_std_skeleton_vector_downstream_phi=null : float                        # 
        norm_std_width_upstream=null : float                        # 
        norm_std_width_no_spine=null : float                        # 
        norm_std_width_downstream=null : float                        # 
        norm_std_n_synapses_post=null : float                        # 
        norm_std_n_synapses_pre=null : float                        # 
        norm_std_n_synapses_head_postsyn=null : float                        # 
        norm_std_n_synapses_neck_postsyn=null : float                        # 
        norm_std_n_synapses_shaft_postsyn=null : float                        # 
        norm_std_n_synapses_no_head_postsyn=null : float                        # 
        norm_std_synapse_volume_shaft_postsyn_sum=null : float                        # 
        norm_std_synapse_volume_head_postsyn_sum=null : float                        # 
        norm_std_synapse_volume_no_head_postsyn_sum=null : float                        # 
        norm_std_synapse_volume_neck_postsyn_sum=null : float                        # 
        norm_std_synapse_volume_postsyn_sum=null : float                        # 
        norm_std_n_spines=null : float                        # 
        norm_std_spine_volume_sum=null : float                        # 
        norm_std_soma_start_angle_max=null : float                        # 
        norm_std_max_soma_volume=null : float                        # 
        norm_std_n_syn_soma=null : float                        # 
        model_name=null      : varchar(25)                  # 
        name=null            : varchar(24)                  # 
        description=null     : varchar(120)                 # 
        model_state_dict=null : longblob                     # 
        class_labels_mapping=null : longblob                     # 
        cell_type_fine_classifier_weights=null : longblob                     # 
        """


@schema
class AutoProofreadNeuronGnnEmbed(djp.Manual):
    definition = """
    -> AutoProofreadNeuronGnnEmbedMethod
    segment_id           : bigint unsigned              # 
    split_index          : bigint unsigned              # 
    ---
    embedding=null       : blob                         # 
    cell_type=null       : varchar(24)                  # 
    cell_type_predicted=null : varchar(24)                  # 
    e_i=null             : enum('excitatory','inhibitory') # 
    e_i_predicted=null   : enum('excitatory','inhibitory') # 
    """


@schema
class AutoProofreadNeuronGnnEmbedding(djp.Manual):
    definition = """
    -> AutoProofreadNeuronGnnEmbedMethod
    segment_id           : bigint unsigned              # 
    split_index          : bigint unsigned              # 
    ---
    embedding=null       : blob                         # 
    cell_type=null       : varchar(24)                  # 
    cell_type_predicted=null : varchar(24)                  # 
    e_i=null             : enum('excitatory','inhibitory') # 
    e_i_predicted=null   : enum('excitatory','inhibitory') # 
    cell_type_predicted_prob=null : double                       # 
    """
            
    class Embedding1(djp.Part):
        definition = """
        -> master
        ---
        cell_type_predicted_2=null : varchar(24)                  # 
        cell_type_predicted_prob_2=null : double                       # 
        e_i_predicted_2=null : enum('excitatory','inhibitory') # 
        cell_type_predicted_3=null : varchar(24)                  # 
        cell_type_predicted_prob_3=null : double                       # 
        e_i_predicted_3=null : enum('excitatory','inhibitory') # 
        cell_type_predicted_4=null : varchar(24)                  # 
        cell_type_predicted_prob_4=null : double                       # 
        e_i_predicted_4=null : enum('excitatory','inhibitory') # 
        cell_type_predicted_5=null : varchar(24)                  # 
        cell_type_predicted_prob_5=null : double                       # 
        e_i_predicted_5=null : enum('excitatory','inhibitory') # 
        cell_type_predicted_6=null : varchar(24)                  # 
        cell_type_predicted_prob_6=null : double                       # 
        e_i_predicted_6=null : enum('excitatory','inhibitory') # 
        cell_type_predicted_7=null : varchar(24)                  # 
        cell_type_predicted_prob_7=null : double                       # 
        e_i_predicted_7=null : enum('excitatory','inhibitory') # 
        cell_type_predicted_8=null : varchar(24)                  # 
        cell_type_predicted_prob_8=null : double                       # 
        e_i_predicted_8=null : enum('excitatory','inhibitory') # 
        cell_type_predicted_9=null : varchar(24)                  # 
        cell_type_predicted_prob_9=null : double                       # 
        e_i_predicted_9=null : enum('excitatory','inhibitory') # 
        cell_type_predicted_10=null : varchar(24)                  # 
        cell_type_predicted_prob_10=null : double                       # 
        e_i_predicted_10=null : enum('excitatory','inhibitory') # 
        cell_type_predicted_11=null : varchar(24)                  # 
        cell_type_predicted_prob_11=null : double                       # 
        e_i_predicted_11=null : enum('excitatory','inhibitory') # 
        cell_type_predicted_12=null : varchar(24)                  # 
        cell_type_predicted_prob_12=null : double                       # 
        e_i_predicted_12=null : enum('excitatory','inhibitory') # 
        cell_type_predicted_13=null : varchar(24)                  # 
        cell_type_predicted_prob_13=null : double                       # 
        e_i_predicted_13=null : enum('excitatory','inhibitory') # 
        """
                    
    class Embedding2(djp.Part):
        definition = """
        -> master
        ---
        cell_type_predicted_2=null : varchar(24)                  # 
        cell_type_predicted_prob_2=null : double                       # 
        e_i_predicted_2=null : enum('excitatory','inhibitory') # 
        cell_type_predicted_3=null : varchar(24)                  # 
        cell_type_predicted_prob_3=null : double                       # 
        e_i_predicted_3=null : enum('excitatory','inhibitory') # 
        cell_type_predicted_4=null : varchar(24)                  # 
        cell_type_predicted_prob_4=null : double                       # 
        e_i_predicted_4=null : enum('excitatory','inhibitory') # 
        cell_type_predicted_5=null : varchar(24)                  # 
        cell_type_predicted_prob_5=null : double                       # 
        e_i_predicted_5=null : enum('excitatory','inhibitory') # 
        cell_type_predicted_6=null : varchar(24)                  # 
        cell_type_predicted_prob_6=null : double                       # 
        e_i_predicted_6=null : enum('excitatory','inhibitory') # 
        cell_type_predicted_7=null : varchar(24)                  # 
        cell_type_predicted_prob_7=null : double                       # 
        e_i_predicted_7=null : enum('excitatory','inhibitory') # 
        cell_type_predicted_8=null : varchar(24)                  # 
        cell_type_predicted_prob_8=null : double                       # 
        e_i_predicted_8=null : enum('excitatory','inhibitory') # 
        cell_type_predicted_9=null : varchar(24)                  # 
        cell_type_predicted_prob_9=null : double                       # 
        e_i_predicted_9=null : enum('excitatory','inhibitory') # 
        cell_type_predicted_10=null : varchar(24)                  # 
        cell_type_predicted_prob_10=null : double                       # 
        e_i_predicted_10=null : enum('excitatory','inhibitory') # 
        cell_type_predicted_11=null : varchar(24)                  # 
        cell_type_predicted_prob_11=null : double                       # 
        e_i_predicted_11=null : enum('excitatory','inhibitory') # 
        """
                    
    class EmbeddingUmap1(djp.Part):
        definition = """
        -> master
        ---
        umap0=null           : double                       # 
        umap1=null           : double                       # 
        """
                    
    class EmbeddingUmap2(djp.Part):
        definition = """
        -> master
        ---
        umap0=null           : double                       # 
        umap1=null           : double                       # 
        """
                    
    class EmbeddingWeighted(djp.Part):
        definition = """
        -> master
        ---
        cell_type_predicted_2=null : varchar(24)                  # 
        cell_type_predicted_prob_2=null : double                       # 
        e_i_predicted_2=null : enum('excitatory','inhibitory') # 
        cell_type_predicted_3=null : varchar(24)                  # 
        cell_type_predicted_prob_3=null : double                       # 
        e_i_predicted_3=null : enum('excitatory','inhibitory') # 
        cell_type_predicted_4=null : varchar(24)                  # 
        cell_type_predicted_prob_4=null : double                       # 
        e_i_predicted_4=null : enum('excitatory','inhibitory') # 
        cell_type_predicted_5=null : varchar(24)                  # 
        cell_type_predicted_prob_5=null : double                       # 
        e_i_predicted_5=null : enum('excitatory','inhibitory') # 
        cell_type_predicted_6=null : varchar(24)                  # 
        cell_type_predicted_prob_6=null : double                       # 
        e_i_predicted_6=null : enum('excitatory','inhibitory') # 
        cell_type_predicted_7=null : varchar(24)                  # 
        cell_type_predicted_prob_7=null : double                       # 
        e_i_predicted_7=null : enum('excitatory','inhibitory') # 
        cell_type_predicted_8=null : varchar(24)                  # 
        cell_type_predicted_prob_8=null : double                       # 
        e_i_predicted_8=null : enum('excitatory','inhibitory') # 
        cell_type_predicted_9=null : varchar(24)                  # 
        cell_type_predicted_prob_9=null : double                       # 
        e_i_predicted_9=null : enum('excitatory','inhibitory') # 
        cell_type_predicted_10=null : varchar(24)                  # 
        cell_type_predicted_prob_10=null : double                       # 
        e_i_predicted_10=null : enum('excitatory','inhibitory') # 
        cell_type_predicted_11=null : varchar(24)                  # 
        cell_type_predicted_prob_11=null : double                       # 
        e_i_predicted_11=null : enum('excitatory','inhibitory') # 
        """


@schema
class AutoProofreadNeuronGnnEmbeddingLin(djp.Manual):
    definition = """
    -> AutoProofreadNeuronGnnEmbedding
    ---
    embedding            : blob                         # 
    """
            
    class EmbeddingUmap(djp.Part):
        definition = """
        -> master
        ---
        umap0=null           : double                       # 
        umap1=null           : double                       # 
        """
                    

@schema
class AutoProofreadNeuronGnnEmbeddingBefLin(djp.Manual):
    definition = """
    -> AutoProofreadNeuronGnnEmbedding
    ---
    embedding            : blob                         # 
    """
            

@schema
class AutoProofreadNeuronGnnEmbeddingBeforeLinear(djp.Manual):
    definition = """
    -> AutoProofreadNeuronGnnEmbedding
    ---
    embedding            : blob                         # 
    """
            

@schema
class AutoProofreadNeuronGnnLimbValStats(djp.Manual):
    definition = """
    split_type           : enum('train','val','test','total','other') # 
    ---
    confusion_matrix     : blob                         # 
    """
            

@schema
class AutoProofreadNeuronHighDegreeToSpine(djp.Manual):
    definition = """
    segment_id           : bigint unsigned              # 
    split_index          : tinyint unsigned             # 
    """


@schema
class AutoProofreadNeuronSpines(djp.Computed):
    definition = """
    segment_id           : bigint unsigned              # 
    split_index          : tinyint unsigned             # 
    ---
    n_spine_one_head     : int unsigned                 # 
    n_spine_no_head      : int unsigned                 # 
    n_spine_multi_head   : int unsigned                 # 
    spine_head_n_faces   : int unsigned                 # 
    spine_neck_n_faces   : int unsigned                 # 
    spine_no_head_n_faces : int unsigned                 # 
    """

    class Object(djp.Part):
        definition = """
        -> master
        ---
        spine_head_face_idx  : <minnie65_auto_proof_meshes> # 
        spine_neck_face_idx  : <minnie65_auto_proof_meshes> # 
        spine_no_head_face_idx : <minnie65_auto_proof_meshes> # 
        """
                    
    class Spine(djp.Part):
        definition = """
        -> master
        spine_id             : bigint unsigned              # synapse index within the segmentation
        ---
        compartment=null     : enum('basal','apical','apical_tuft','apical_shaft','oblique','dendrite','axon') # 
        n_heads=null         : int unsigned                 # 
        shaft_border_area=null : float                        # 
        downstream_dist=null : float                        # 
        upstream_dist=null   : float                        # 
        soma_distance_euclidean=null : float                        # 
        soma_distance=null   : float                        # 
        spine_area=null      : float                        # 
        spine_n_faces=null   : int unsigned                 # 
        spine_volume=null    : float                        # 
        spine_skeletal_length=null : float                        # 
        spine_width_ray=null : float                        # 
        spine_width_ray_80_perc=null : float                        # 
        spine_bbox_oriented_side_max=null : float                        # 
        spine_bbox_oriented_side_middle=null : float                        # 
        spine_bbox_oriented_side_min=null : float                        # 
        head_area=null       : float                        # 
        head_n_faces=null    : float                        # 
        head_volume=null     : float                        # 
        head_skeletal_length=null : float                        # 
        head_width_ray=null  : float                        # 
        head_width_ray_80_perc=null : float                        # 
        head_bbox_oriented_side_max=null : float                        # 
        head_bbox_oriented_side_middle=null : float                        # 
        head_bbox_oriented_side_min=null : float                        # 
        neck_area=null       : float                        # 
        neck_n_faces=null    : int unsigned                 # 
        neck_volume=null     : float                        # 
        neck_skeletal_length=null : float                        # 
        neck_width_ray=null  : float                        # 
        neck_width_ray_80_perc=null : float                        # 
        neck_bbox_oriented_side_max=null : float                        # 
        neck_bbox_oriented_side_middle=null : float                        # 
        neck_bbox_oriented_side_min=null : float                        # 
        base_coordinate_x_nm=null : float                        # 
        base_coordinate_y_nm=null : float                        # 
        base_coordinate_z_nm=null : float                        # 
        mesh_center_x_nm=null : float                        # 
        mesh_center_y_nm=null : float                        # 
        mesh_center_z_nm=null : float                        # 
        """
                    
    class SpineSynapse(djp.Part):
        definition = """
        -> master
        synapse_id           : bigint unsigned              # synapse index within the segmentation
        ---
        spine_id=null        : int unsigned                 # 
        spine_compartment=null : enum('head','neck','shaft','no_head') # 
        spine_volume=null    : float                        # 
        spine_area=null      : float                        # 
        spine_width_ray_80_perc=null : float                        # 
        """

@schema
class AutoProofreadNeuronSpines2(djp.Computed):
    definition = """
    -> 
    ---
    n_spine_one_head     : int unsigned                 # 
    n_spine_no_head      : int unsigned                 # 
    n_spine_multi_head   : int unsigned                 # 
    spine_head_n_faces   : int unsigned                 # 
    spine_neck_n_faces   : int unsigned                 # 
    spine_no_head_n_faces : int unsigned                 # 
    """
            
    class Object(djp.Part):
        definition = """
        -> master
        ---
        spine_head_face_idx  : <minnie65_auto_proof_meshes> # 
        spine_neck_face_idx  : <minnie65_auto_proof_meshes> # 
        spine_no_head_face_idx : <minnie65_auto_proof_meshes> # 
        """
                    
    class Spine(djp.Part):
        definition = """
        -> master
        spine_id             : bigint unsigned              # synapse index within the segmentation
        ---
        compartment=null     : enum('basal','apical','apical_tuft','apical_shaft','oblique','dendrite','axon') # 
        n_heads=null         : int unsigned                 # 
        shaft_border_area=null : float                        # 
        downstream_dist=null : float                        # 
        upstream_dist=null   : float                        # 
        soma_distance_euclidean=null : float                        # 
        soma_distance=null   : float                        # 
        branch_width_overall=null : float                        # 
        branch_skeletal_length=null : float                        # 
        branch_width_at_base=null : float                        # 
        spine_area=null      : float                        # 
        spine_n_faces=null   : int unsigned                 # 
        spine_volume=null    : float                        # 
        spine_skeletal_length=null : float                        # 
        spine_width_ray=null : float                        # 
        spine_width_ray_80_perc=null : float                        # 
        spine_bbox_oriented_side_max=null : float                        # 
        spine_bbox_oriented_side_middle=null : float                        # 
        spine_bbox_oriented_side_min=null : float                        # 
        head_area=null       : float                        # 
        head_n_faces=null    : float                        # 
        head_volume=null     : float                        # 
        head_skeletal_length=null : float                        # 
        head_width_ray=null  : float                        # 
        head_width_ray_80_perc=null : float                        # 
        head_bbox_oriented_side_max=null : float                        # 
        head_bbox_oriented_side_middle=null : float                        # 
        head_bbox_oriented_side_min=null : float                        # 
        neck_area=null       : float                        # 
        neck_n_faces=null    : int unsigned                 # 
        neck_volume=null     : float                        # 
        neck_skeletal_length=null : float                        # 
        neck_width_ray=null  : float                        # 
        neck_width_ray_80_perc=null : float                        # 
        neck_bbox_oriented_side_max=null : float                        # 
        neck_bbox_oriented_side_middle=null : float                        # 
        neck_bbox_oriented_side_min=null : float                        # 
        base_coordinate_x_nm=null : float                        # 
        base_coordinate_y_nm=null : float                        # 
        base_coordinate_z_nm=null : float                        # 
        mesh_center_x_nm=null : float                        # 
        mesh_center_y_nm=null : float                        # 
        mesh_center_z_nm=null : float                        # 
        """
                    
    class SpineSynapse(djp.Part):
        definition = """
        -> master
        synapse_id           : bigint unsigned              # synapse index within the segmentation
        ---
        spine_id=null        : int unsigned                 # 
        spine_compartment=null : enum('head','neck','shaft','no_head') # 
        spine_volume=null    : float                        # 
        spine_area=null      : float                        # 
        spine_width_ray_80_perc=null : float                        # 
        """


@schema
class AutoProofreadNeuronSpines2Stats(djp.Computed):
    definition = """
    -> AutoProofreadNeuronSpines2
    min_skeletal_length  : float                        # 
    """
            
    class Spine(djp.Part):
        definition = """
        -> master
        ---
        sp_head_apical_head_area=null : float                        # 
        sp_head_apical_shaft_head_area=null : float                        # 
        sp_head_apical_tuft_head_area=null : float                        # 
        sp_head_basal_head_area=null : float                        # 
        sp_head_oblique_head_area=null : float                        # 
        sp_head_apical_head_n_faces=null : float                        # 
        sp_head_apical_shaft_head_n_faces=null : float                        # 
        sp_head_apical_tuft_head_n_faces=null : float                        # 
        sp_head_basal_head_n_faces=null : float                        # 
        sp_head_oblique_head_n_faces=null : float                        # 
        sp_head_apical_head_skeletal_length=null : float                        # 
        sp_head_apical_shaft_head_skeletal_length=null : float                        # 
        sp_head_apical_tuft_head_skeletal_length=null : float                        # 
        sp_head_basal_head_skeletal_length=null : float                        # 
        sp_head_oblique_head_skeletal_length=null : float                        # 
        sp_head_apical_head_volume=null : float                        # 
        sp_head_apical_shaft_head_volume=null : float                        # 
        sp_head_apical_tuft_head_volume=null : float                        # 
        sp_head_basal_head_volume=null : float                        # 
        sp_head_oblique_head_volume=null : float                        # 
        sp_head_apical_head_width_ray=null : float                        # 
        sp_head_apical_shaft_head_width_ray=null : float                        # 
        sp_head_apical_tuft_head_width_ray=null : float                        # 
        sp_head_basal_head_width_ray=null : float                        # 
        sp_head_oblique_head_width_ray=null : float                        # 
        sp_head_apical_head_width_ray_80_perc=null : float                        # 
        sp_head_apical_shaft_head_width_ray_80_perc=null : float                        # 
        sp_head_apical_tuft_head_width_ray_80_perc=null : float                        # 
        sp_head_basal_head_width_ray_80_perc=null : float                        # 
        sp_head_oblique_head_width_ray_80_perc=null : float                        # 
        sp_head_apical_neck_area=null : float                        # 
        sp_head_apical_shaft_neck_area=null : float                        # 
        sp_head_apical_tuft_neck_area=null : float                        # 
        sp_head_basal_neck_area=null : float                        # 
        sp_head_oblique_neck_area=null : float                        # 
        sp_head_apical_neck_n_faces=null : float                        # 
        sp_head_apical_shaft_neck_n_faces=null : float                        # 
        sp_head_apical_tuft_neck_n_faces=null : float                        # 
        sp_head_basal_neck_n_faces=null : float                        # 
        sp_head_oblique_neck_n_faces=null : float                        # 
        sp_head_apical_neck_skeletal_length=null : float                        # 
        sp_head_apical_shaft_neck_skeletal_length=null : float                        # 
        sp_head_apical_tuft_neck_skeletal_length=null : float                        # 
        sp_head_basal_neck_skeletal_length=null : float                        # 
        sp_head_oblique_neck_skeletal_length=null : float                        # 
        sp_head_apical_neck_volume=null : float                        # 
        sp_head_apical_shaft_neck_volume=null : float                        # 
        sp_head_apical_tuft_neck_volume=null : float                        # 
        sp_head_basal_neck_volume=null : float                        # 
        sp_head_oblique_neck_volume=null : float                        # 
        sp_head_apical_neck_width_ray=null : float                        # 
        sp_head_apical_shaft_neck_width_ray=null : float                        # 
        sp_head_apical_tuft_neck_width_ray=null : float                        # 
        sp_head_basal_neck_width_ray=null : float                        # 
        sp_head_oblique_neck_width_ray=null : float                        # 
        sp_head_apical_neck_width_ray_80_perc=null : float                        # 
        sp_head_apical_shaft_neck_width_ray_80_perc=null : float                        # 
        sp_head_apical_tuft_neck_width_ray_80_perc=null : float                        # 
        sp_head_basal_neck_width_ray_80_perc=null : float                        # 
        sp_head_oblique_neck_width_ray_80_perc=null : float                        # 
        sp_head_n_apical=null : int unsigned                 # 
        sp_head_n_apical_shaft=null : int unsigned                 # 
        sp_head_n_apical_tuft=null : int unsigned                 # 
        sp_head_n_basal=null : int unsigned                 # 
        sp_head_n_oblique=null : int unsigned                 # 
        sp_head_dendrite_head_area=null : float                        # 
        sp_head_dendrite_head_n_faces=null : float                        # 
        sp_head_dendrite_head_skeletal_length=null : float                        # 
        sp_head_dendrite_head_volume=null : float                        # 
        sp_head_dendrite_head_width_ray=null : float                        # 
        sp_head_dendrite_head_width_ray_80_perc=null : float                        # 
        sp_head_dendrite_neck_area=null : float                        # 
        sp_head_dendrite_neck_n_faces=null : float                        # 
        sp_head_dendrite_neck_skeletal_length=null : float                        # 
        sp_head_dendrite_neck_volume=null : float                        # 
        sp_head_dendrite_neck_width_ray=null : float                        # 
        sp_head_dendrite_neck_width_ray_80_perc=null : float                        # 
        sp_head_n_dendrite=null : int unsigned                 # 
        sp_no_head_apical_spine_area=null : float                        # 
        sp_no_head_apical_shaft_spine_area=null : float                        # 
        sp_no_head_apical_tuft_spine_area=null : float                        # 
        sp_no_head_basal_spine_area=null : float                        # 
        sp_no_head_oblique_spine_area=null : float                        # 
        sp_no_head_apical_spine_n_faces=null : float                        # 
        sp_no_head_apical_shaft_spine_n_faces=null : float                        # 
        sp_no_head_apical_tuft_spine_n_faces=null : float                        # 
        sp_no_head_basal_spine_n_faces=null : float                        # 
        sp_no_head_oblique_spine_n_faces=null : float                        # 
        sp_no_head_apical_spine_skeletal_length=null : float                        # 
        sp_no_head_apical_shaft_spine_skeletal_length=null : float                        # 
        sp_no_head_apical_tuft_spine_skeletal_length=null : float                        # 
        sp_no_head_basal_spine_skeletal_length=null : float                        # 
        sp_no_head_oblique_spine_skeletal_length=null : float                        # 
        sp_no_head_apical_spine_volume=null : float                        # 
        sp_no_head_apical_shaft_spine_volume=null : float                        # 
        sp_no_head_apical_tuft_spine_volume=null : float                        # 
        sp_no_head_basal_spine_volume=null : float                        # 
        sp_no_head_oblique_spine_volume=null : float                        # 
        sp_no_head_apical_spine_width_ray=null : float                        # 
        sp_no_head_apical_shaft_spine_width_ray=null : float                        # 
        sp_no_head_apical_tuft_spine_width_ray=null : float                        # 
        sp_no_head_basal_spine_width_ray=null : float                        # 
        sp_no_head_oblique_spine_width_ray=null : float                        # 
        sp_no_head_n_apical=null : int unsigned                 # 
        sp_no_head_n_apical_shaft=null : int unsigned                 # 
        sp_no_head_n_apical_tuft=null : int unsigned                 # 
        sp_no_head_n_basal=null : int unsigned                 # 
        sp_no_head_n_oblique=null : int unsigned                 # 
        sp_no_head_dendrite_spine_area=null : float                        # 
        sp_no_head_dendrite_spine_n_faces=null : float                        # 
        sp_no_head_dendrite_spine_skeletal_length=null : float                        # 
        sp_no_head_dendrite_spine_volume=null : float                        # 
        sp_no_head_dendrite_spine_width_ray=null : float                        # 
        sp_no_head_n_dendrite=null : int unsigned                 #
        """
                    
    class SpineSynapse(djp.Part):
        definition = """
        -> master
        ---
        syn_apical_head_spine_area=null : float                        # 
        syn_apical_neck_spine_area=null : float                        # 
        syn_apical_no_head_spine_area=null : float                        # 
        syn_apical_shaft_spine_area=null : float                        # 
        syn_apical_shaft_head_spine_area=null : float                        # 
        syn_apical_shaft_no_head_spine_area=null : float                        # 
        syn_apical_shaft_shaft_spine_area=null : float                        # 
        syn_apical_tuft_head_spine_area=null : float                        # 
        syn_apical_tuft_no_head_spine_area=null : float                        # 
        syn_apical_tuft_shaft_spine_area=null : float                        # 
        syn_axon_shaft_spine_area=null : float                        # 
        syn_basal_head_spine_area=null : float                        # 
        syn_basal_neck_spine_area=null : float                        # 
        syn_basal_no_head_spine_area=null : float                        # 
        syn_basal_shaft_spine_area=null : float                        # 
        syn_oblique_head_spine_area=null : float                        # 
        syn_oblique_neck_spine_area=null : float                        # 
        syn_oblique_no_head_spine_area=null : float                        # 
        syn_oblique_shaft_spine_area=null : float                        # 
        syn_soma_shaft_spine_area=null : float                        # 
        syn_apical_head_spine_n_faces=null : float                        # 
        syn_apical_neck_spine_n_faces=null : float                        # 
        syn_apical_no_head_spine_n_faces=null : float                        # 
        syn_apical_shaft_spine_n_faces=null : float                        # 
        syn_apical_shaft_head_spine_n_faces=null : float                        # 
        syn_apical_shaft_no_head_spine_n_faces=null : float                        # 
        syn_apical_shaft_shaft_spine_n_faces=null : float                        # 
        syn_apical_tuft_head_spine_n_faces=null : float                        # 
        syn_apical_tuft_no_head_spine_n_faces=null : float                        # 
        syn_apical_tuft_shaft_spine_n_faces=null : float                        # 
        syn_axon_shaft_spine_n_faces=null : float                        # 
        syn_basal_head_spine_n_faces=null : float                        # 
        syn_basal_neck_spine_n_faces=null : float                        # 
        syn_basal_no_head_spine_n_faces=null : float                        # 
        syn_basal_shaft_spine_n_faces=null : float                        # 
        syn_oblique_head_spine_n_faces=null : float                        # 
        syn_oblique_neck_spine_n_faces=null : float                        # 
        syn_oblique_no_head_spine_n_faces=null : float                        # 
        syn_oblique_shaft_spine_n_faces=null : float                        # 
        syn_soma_shaft_spine_n_faces=null : float                        # 
        syn_apical_head_spine_skeletal_length=null : float                        # 
        syn_apical_neck_spine_skeletal_length=null : float                        # 
        syn_apical_no_head_spine_skeletal_length=null : float                        # 
        syn_apical_shaft_spine_skeletal_length=null : float                        # 
        syn_apical_shaft_head_spine_skeletal_length=null : float                        # 
        syn_apical_shaft_no_head_spine_skeletal_length=null : float                        # 
        syn_apical_shaft_shaft_spine_skeletal_length=null : float                        # 
        syn_apical_tuft_head_spine_skeletal_length=null : float                        # 
        syn_apical_tuft_no_head_spine_skeletal_length=null : float                        # 
        syn_apical_tuft_shaft_spine_skeletal_length=null : float                        # 
        syn_axon_shaft_spine_skeletal_length=null : float                        # 
        syn_basal_head_spine_skeletal_length=null : float                        # 
        syn_basal_neck_spine_skeletal_length=null : float                        # 
        syn_basal_no_head_spine_skeletal_length=null : float                        # 
        syn_basal_shaft_spine_skeletal_length=null : float                        # 
        syn_oblique_head_spine_skeletal_length=null : float                        # 
        syn_oblique_neck_spine_skeletal_length=null : float                        # 
        syn_oblique_no_head_spine_skeletal_length=null : float                        # 
        syn_oblique_shaft_spine_skeletal_length=null : float                        # 
        syn_soma_shaft_spine_skeletal_length=null : float                        # 
        syn_apical_head_spine_volume=null : float                        # 
        syn_apical_neck_spine_volume=null : float                        # 
        syn_apical_no_head_spine_volume=null : float                        # 
        syn_apical_shaft_spine_volume=null : float                        # 
        syn_apical_shaft_head_spine_volume=null : float                        # 
        syn_apical_shaft_no_head_spine_volume=null : float                        # 
        syn_apical_shaft_shaft_spine_volume=null : float                        # 
        syn_apical_tuft_head_spine_volume=null : float                        # 
        syn_apical_tuft_no_head_spine_volume=null : float                        # 
        syn_apical_tuft_shaft_spine_volume=null : float                        # 
        syn_axon_shaft_spine_volume=null : float                        # 
        syn_basal_head_spine_volume=null : float                        # 
        syn_basal_neck_spine_volume=null : float                        # 
        syn_basal_no_head_spine_volume=null : float                        # 
        syn_basal_shaft_spine_volume=null : float                        # 
        syn_oblique_head_spine_volume=null : float                        # 
        syn_oblique_neck_spine_volume=null : float                        # 
        syn_oblique_no_head_spine_volume=null : float                        # 
        syn_oblique_shaft_spine_volume=null : float                        # 
        syn_soma_shaft_spine_volume=null : float                        # 
        syn_apical_head_spine_width_ray=null : float                        # 
        syn_apical_neck_spine_width_ray=null : float                        # 
        syn_apical_no_head_spine_width_ray=null : float                        # 
        syn_apical_shaft_spine_width_ray=null : float                        # 
        syn_apical_shaft_head_spine_width_ray=null : float                        # 
        syn_apical_shaft_no_head_spine_width_ray=null : float                        # 
        syn_apical_shaft_shaft_spine_width_ray=null : float                        # 
        syn_apical_tuft_head_spine_width_ray=null : float                        # 
        syn_apical_tuft_no_head_spine_width_ray=null : float                        # 
        syn_apical_tuft_shaft_spine_width_ray=null : float                        # 
        syn_axon_shaft_spine_width_ray=null : float                        # 
        syn_basal_head_spine_width_ray=null : float                        # 
        syn_basal_neck_spine_width_ray=null : float                        # 
        syn_basal_no_head_spine_width_ray=null : float                        # 
        syn_basal_shaft_spine_width_ray=null : float                        # 
        syn_oblique_head_spine_width_ray=null : float                        # 
        syn_oblique_neck_spine_width_ray=null : float                        # 
        syn_oblique_no_head_spine_width_ray=null : float                        # 
        syn_oblique_shaft_spine_width_ray=null : float                        # 
        syn_soma_shaft_spine_width_ray=null : float                        # 
        syn_apical_head_syn_spine_area=null : float                        # 
        syn_apical_neck_syn_spine_area=null : float                        # 
        syn_apical_no_head_syn_spine_area=null : float                        # 
        syn_apical_shaft_syn_spine_area=null : float                        # 
        syn_apical_shaft_head_syn_spine_area=null : float                        # 
        syn_apical_shaft_no_head_syn_spine_area=null : float                        # 
        syn_apical_shaft_shaft_syn_spine_area=null : float                        # 
        syn_apical_tuft_head_syn_spine_area=null : float                        # 
        syn_apical_tuft_no_head_syn_spine_area=null : float                        # 
        syn_apical_tuft_shaft_syn_spine_area=null : float                        # 
        syn_axon_shaft_syn_spine_area=null : float                        # 
        syn_basal_head_syn_spine_area=null : float                        # 
        syn_basal_neck_syn_spine_area=null : float                        # 
        syn_basal_no_head_syn_spine_area=null : float                        # 
        syn_basal_shaft_syn_spine_area=null : float                        # 
        syn_oblique_head_syn_spine_area=null : float                        # 
        syn_oblique_neck_syn_spine_area=null : float                        # 
        syn_oblique_no_head_syn_spine_area=null : float                        # 
        syn_oblique_shaft_syn_spine_area=null : float                        # 
        syn_soma_shaft_syn_spine_area=null : float                        # 
        syn_apical_head_syn_spine_volume=null : float                        # 
        syn_apical_neck_syn_spine_volume=null : float                        # 
        syn_apical_no_head_syn_spine_volume=null : float                        # 
        syn_apical_shaft_syn_spine_volume=null : float                        # 
        syn_apical_shaft_head_syn_spine_volume=null : float                        # 
        syn_apical_shaft_no_head_syn_spine_volume=null : float                        # 
        syn_apical_shaft_shaft_syn_spine_volume=null : float                        # 
        syn_apical_tuft_head_syn_spine_volume=null : float                        # 
        syn_apical_tuft_no_head_syn_spine_volume=null : float                        # 
        syn_apical_tuft_shaft_syn_spine_volume=null : float                        # 
        syn_axon_shaft_syn_spine_volume=null : float                        # 
        syn_basal_head_syn_spine_volume=null : float                        # 
        syn_basal_neck_syn_spine_volume=null : float                        # 
        syn_basal_no_head_syn_spine_volume=null : float                        # 
        syn_basal_shaft_syn_spine_volume=null : float                        # 
        syn_oblique_head_syn_spine_volume=null : float                        # 
        syn_oblique_neck_syn_spine_volume=null : float                        # 
        syn_oblique_no_head_syn_spine_volume=null : float                        # 
        syn_oblique_shaft_syn_spine_volume=null : float                        # 
        syn_soma_shaft_syn_spine_volume=null : float                        # 
        syn_apical_head_syn_spine_width_ray_80_perc=null : float                        # 
        syn_apical_neck_syn_spine_width_ray_80_perc=null : float                        # 
        syn_apical_no_head_syn_spine_width_ray_80_perc=null : float                        # 
        syn_apical_shaft_syn_spine_width_ray_80_perc=null : float                        # 
        syn_apical_shaft_head_syn_spine_width_ray_80_perc=null : float                        # 
        syn_apical_shaft_no_head_syn_spine_width_ray_80_perc=null : float                        # 
        syn_apical_shaft_shaft_syn_spine_width_ray_80_perc=null : float                        # 
        syn_apical_tuft_head_syn_spine_width_ray_80_perc=null : float                        # 
        syn_apical_tuft_no_head_syn_spine_width_ray_80_perc=null : float                        # 
        syn_apical_tuft_shaft_syn_spine_width_ray_80_perc=null : float                        # 
        syn_axon_shaft_syn_spine_width_ray_80_perc=null : float                        # 
        syn_basal_head_syn_spine_width_ray_80_perc=null : float                        # 
        syn_basal_neck_syn_spine_width_ray_80_perc=null : float                        # 
        syn_basal_no_head_syn_spine_width_ray_80_perc=null : float                        # 
        syn_basal_shaft_syn_spine_width_ray_80_perc=null : float                        # 
        syn_oblique_head_syn_spine_width_ray_80_perc=null : float                        # 
        syn_oblique_neck_syn_spine_width_ray_80_perc=null : float                        # 
        syn_oblique_no_head_syn_spine_width_ray_80_perc=null : float                        # 
        syn_oblique_shaft_syn_spine_width_ray_80_perc=null : float                        # 
        syn_soma_shaft_syn_spine_width_ray_80_perc=null : float                        # 
        syn_apical_head_synapse_size=null : float                        # 
        syn_apical_neck_synapse_size=null : float                        # 
        syn_apical_no_head_synapse_size=null : float                        # 
        syn_apical_shaft_synapse_size=null : float                        # 
        syn_apical_shaft_head_synapse_size=null : float                        # 
        syn_apical_shaft_no_head_synapse_size=null : float                        # 
        syn_apical_shaft_shaft_synapse_size=null : float                        # 
        syn_apical_tuft_head_synapse_size=null : float                        # 
        syn_apical_tuft_no_head_synapse_size=null : float                        # 
        syn_apical_tuft_shaft_synapse_size=null : float                        # 
        syn_axon_shaft_synapse_size=null : float                        # 
        syn_basal_head_synapse_size=null : float                        # 
        syn_basal_neck_synapse_size=null : float                        # 
        syn_basal_no_head_synapse_size=null : float                        # 
        syn_basal_shaft_synapse_size=null : float                        # 
        syn_oblique_head_synapse_size=null : float                        # 
        syn_oblique_neck_synapse_size=null : float                        # 
        syn_oblique_no_head_synapse_size=null : float                        # 
        syn_oblique_shaft_synapse_size=null : float                        # 
        syn_soma_shaft_synapse_size=null : float                        # 
        syn_n_apical_head=null : int unsigned                 # 
        syn_n_apical_neck=null : int unsigned                 # 
        syn_n_apical_no_head=null : int unsigned                 # 
        syn_n_apical_shaft=null : int unsigned                 # 
        syn_n_apical_shaft_head=null : int unsigned                 # 
        syn_n_apical_shaft_no_head=null : int unsigned                 # 
        syn_n_apical_shaft_shaft=null : int unsigned                 # 
        syn_n_apical_tuft_head=null : int unsigned                 # 
        syn_n_apical_tuft_no_head=null : int unsigned                 # 
        syn_n_apical_tuft_shaft=null : int unsigned                 # 
        syn_n_axon_shaft=null : int unsigned                 # 
        syn_n_basal_head=null : int unsigned                 # 
        syn_n_basal_neck=null : int unsigned                 # 
        syn_n_basal_no_head=null : int unsigned                 # 
        syn_n_basal_shaft=null : int unsigned                 # 
        syn_n_oblique_head=null : int unsigned                 # 
        syn_n_oblique_neck=null : int unsigned                 # 
        syn_n_oblique_no_head=null : int unsigned                 # 
        syn_n_oblique_shaft=null : int unsigned                 # 
        syn_n_soma_shaft=null : int unsigned                 # 
        syn_dendrite_head_spine_area=null : float                        # 
        syn_dendrite_neck_spine_area=null : float                        # 
        syn_dendrite_no_head_spine_area=null : float                        # 
        syn_dendrite_shaft_spine_area=null : float                        # 
        syn_dendrite_head_spine_n_faces=null : float                        # 
        syn_dendrite_neck_spine_n_faces=null : float                        # 
        syn_dendrite_no_head_spine_n_faces=null : float                        # 
        syn_dendrite_shaft_spine_n_faces=null : float                        # 
        syn_dendrite_head_spine_skeletal_length=null : float                        # 
        syn_dendrite_neck_spine_skeletal_length=null : float                        # 
        syn_dendrite_no_head_spine_skeletal_length=null : float                        # 
        syn_dendrite_shaft_spine_skeletal_length=null : float                        # 
        syn_dendrite_head_spine_volume=null : float                        # 
        syn_dendrite_neck_spine_volume=null : float                        # 
        syn_dendrite_no_head_spine_volume=null : float                        # 
        syn_dendrite_shaft_spine_volume=null : float                        # 
        syn_dendrite_head_spine_width_ray=null : float                        # 
        syn_dendrite_neck_spine_width_ray=null : float                        # 
        syn_dendrite_no_head_spine_width_ray=null : float                        # 
        syn_dendrite_shaft_spine_width_ray=null : float                        # 
        syn_dendrite_head_syn_spine_area=null : float                        # 
        syn_dendrite_neck_syn_spine_area=null : float                        # 
        syn_dendrite_no_head_syn_spine_area=null : float                        # 
        syn_dendrite_shaft_syn_spine_area=null : float                        # 
        syn_dendrite_head_syn_spine_volume=null : float                        # 
        syn_dendrite_neck_syn_spine_volume=null : float                        # 
        syn_dendrite_no_head_syn_spine_volume=null : float                        # 
        syn_dendrite_shaft_syn_spine_volume=null : float                        # 
        syn_dendrite_head_syn_spine_width_ray_80_perc=null : float                        # 
        syn_dendrite_neck_syn_spine_width_ray_80_perc=null : float                        # 
        syn_dendrite_no_head_syn_spine_width_ray_80_perc=null : float                        # 
        syn_dendrite_shaft_syn_spine_width_ray_80_perc=null : float                        # 
        syn_dendrite_head_synapse_size=null : float                        # 
        syn_dendrite_neck_synapse_size=null : float                        # 
        syn_dendrite_no_head_synapse_size=null : float                        # 
        syn_dendrite_shaft_synapse_size=null : float                        # 
        syn_n_dendrite_head=null : int unsigned                 # 
        syn_n_dendrite_neck=null : int unsigned                 # 
        syn_n_dendrite_no_head=null : int unsigned                 # 
        syn_n_dendrite_shaft=null : int unsigned                 # 
        """


@schema
class AutoProofreadNeuronSpines2Stats2(djp.Computed):
    definition = """
    -> AutoProofreadNeuronSpines2
    min_skeletal_length  : float                        # 
    """
            
    class Spine(djp.Part):
        definition = """
        -> master
        ---
        sp_head_apical_head_area=null : float                        # 
        sp_head_apical_head_n_faces=null : float                        # 
        sp_head_apical_head_skeletal_length=null : float                        # 
        sp_head_apical_head_volume=null : float                        # 
        sp_head_apical_head_width_ray=null : float                        # 
        sp_head_apical_head_width_ray_80_perc=null : float                        # 
        sp_head_apical_neck_area=null : float                        # 
        sp_head_apical_neck_n_faces=null : float                        # 
        sp_head_apical_neck_skeletal_length=null : float                        # 
        sp_head_apical_neck_volume=null : float                        # 
        sp_head_apical_neck_width_ray=null : float                        # 
        sp_head_apical_neck_width_ray_80_perc=null : float                        # 
        sp_head_apical_shaft_head_area=null : float                        # 
        sp_head_apical_shaft_head_n_faces=null : float                        # 
        sp_head_apical_shaft_head_skeletal_length=null : float                        # 
        sp_head_apical_shaft_head_volume=null : float                        # 
        sp_head_apical_shaft_head_width_ray=null : float                        # 
        sp_head_apical_shaft_head_width_ray_80_perc=null : float                        # 
        sp_head_apical_shaft_neck_area=null : float                        # 
        sp_head_apical_shaft_neck_n_faces=null : float                        # 
        sp_head_apical_shaft_neck_skeletal_length=null : float                        # 
        sp_head_apical_shaft_neck_volume=null : float                        # 
        sp_head_apical_shaft_neck_width_ray=null : float                        # 
        sp_head_apical_shaft_neck_width_ray_80_perc=null : float                        # 
        sp_head_apical_shaft_spine_max_head_sp_vol=null : float                        # 
        sp_head_apical_shaft_spine_max_head_syn_size=null : float                        # 
        sp_head_apical_shaft_spine_max_neck_sp_vol=null : float                        # 
        sp_head_apical_shaft_spine_max_neck_syn_size=null : float                        # 
        sp_head_apical_shaft_spine_n_head_syn=null : float                        # 
        sp_head_apical_shaft_spine_n_neck_syn=null : float                        # 
        sp_head_apical_spine_max_head_sp_vol=null : float                        # 
        sp_head_apical_spine_max_head_syn_size=null : float                        # 
        sp_head_apical_spine_max_neck_sp_vol=null : float                        # 
        sp_head_apical_spine_max_neck_syn_size=null : float                        # 
        sp_head_apical_spine_n_head_syn=null : float                        # 
        sp_head_apical_spine_n_neck_syn=null : float                        # 
        sp_head_apical_tuft_head_area=null : float                        # 
        sp_head_apical_tuft_head_n_faces=null : float                        # 
        sp_head_apical_tuft_head_skeletal_length=null : float                        # 
        sp_head_apical_tuft_head_volume=null : float                        # 
        sp_head_apical_tuft_head_width_ray=null : float                        # 
        sp_head_apical_tuft_head_width_ray_80_perc=null : float                        # 
        sp_head_apical_tuft_neck_area=null : float                        # 
        sp_head_apical_tuft_neck_n_faces=null : float                        # 
        sp_head_apical_tuft_neck_skeletal_length=null : float                        # 
        sp_head_apical_tuft_neck_volume=null : float                        # 
        sp_head_apical_tuft_neck_width_ray=null : float                        # 
        sp_head_apical_tuft_neck_width_ray_80_perc=null : float                        # 
        sp_head_apical_tuft_spine_max_head_sp_vol=null : float                        # 
        sp_head_apical_tuft_spine_max_head_syn_size=null : float                        # 
        sp_head_apical_tuft_spine_max_neck_sp_vol=null : float                        # 
        sp_head_apical_tuft_spine_max_neck_syn_size=null : float                        # 
        sp_head_apical_tuft_spine_n_head_syn=null : float                        # 
        sp_head_apical_tuft_spine_n_neck_syn=null : float                        # 
        sp_head_area=null    : float                        # 
        sp_head_basal_head_area=null : float                        # 
        sp_head_basal_head_n_faces=null : float                        # 
        sp_head_basal_head_skeletal_length=null : float                        # 
        sp_head_basal_head_volume=null : float                        # 
        sp_head_basal_head_width_ray=null : float                        # 
        sp_head_basal_head_width_ray_80_perc=null : float                        # 
        sp_head_basal_neck_area=null : float                        # 
        sp_head_basal_neck_n_faces=null : float                        # 
        sp_head_basal_neck_skeletal_length=null : float                        # 
        sp_head_basal_neck_volume=null : float                        # 
        sp_head_basal_neck_width_ray=null : float                        # 
        sp_head_basal_neck_width_ray_80_perc=null : float                        # 
        sp_head_basal_spine_max_head_sp_vol=null : float                        # 
        sp_head_basal_spine_max_head_syn_size=null : float                        # 
        sp_head_basal_spine_max_neck_sp_vol=null : float                        # 
        sp_head_basal_spine_max_neck_syn_size=null : float                        # 
        sp_head_basal_spine_n_head_syn=null : float                        # 
        sp_head_basal_spine_n_neck_syn=null : float                        # 
        sp_head_dendrite_head_area=null : float                        # 
        sp_head_dendrite_head_n_faces=null : float                        # 
        sp_head_dendrite_head_skeletal_length=null : float                        # 
        sp_head_dendrite_head_volume=null : float                        # 
        sp_head_dendrite_head_width_ray=null : float                        # 
        sp_head_dendrite_head_width_ray_80_perc=null : float                        # 
        sp_head_dendrite_neck_area=null : float                        # 
        sp_head_dendrite_neck_n_faces=null : float                        # 
        sp_head_dendrite_neck_skeletal_length=null : float                        # 
        sp_head_dendrite_neck_volume=null : float                        # 
        sp_head_dendrite_neck_width_ray=null : float                        # 
        sp_head_dendrite_neck_width_ray_80_perc=null : float                        # 
        sp_head_dendrite_spine_max_head_sp_vol=null : float                        # 
        sp_head_dendrite_spine_max_head_syn_size=null : float                        # 
        sp_head_dendrite_spine_max_neck_sp_vol=null : float                        # 
        sp_head_dendrite_spine_max_neck_syn_size=null : float                        # 
        sp_head_dendrite_spine_n_head_syn=null : float                        # 
        sp_head_dendrite_spine_n_neck_syn=null : float                        # 
        sp_head_n_apical=null : int unsigned                 # 
        sp_head_n_apical_shaft=null : int unsigned                 # 
        sp_head_n_apical_tuft=null : int unsigned                 # 
        sp_head_n_basal=null : int unsigned                 # 
        sp_head_n_dendrite=null : int unsigned                 # 
        sp_head_n_faces=null : float                        # 
        sp_head_n_oblique=null : int unsigned                 # 
        sp_head_number=null  : int unsigned                 # 
        sp_head_oblique_head_area=null : float                        # 
        sp_head_oblique_head_n_faces=null : float                        # 
        sp_head_oblique_head_skeletal_length=null : float                        # 
        sp_head_oblique_head_volume=null : float                        # 
        sp_head_oblique_head_width_ray=null : float                        # 
        sp_head_oblique_head_width_ray_80_perc=null : float                        # 
        sp_head_oblique_neck_area=null : float                        # 
        sp_head_oblique_neck_n_faces=null : float                        # 
        sp_head_oblique_neck_skeletal_length=null : float                        # 
        sp_head_oblique_neck_volume=null : float                        # 
        sp_head_oblique_neck_width_ray=null : float                        # 
        sp_head_oblique_neck_width_ray_80_perc=null : float                        # 
        sp_head_oblique_spine_max_head_sp_vol=null : float                        # 
        sp_head_oblique_spine_max_head_syn_size=null : float                        # 
        sp_head_oblique_spine_max_neck_sp_vol=null : float                        # 
        sp_head_oblique_spine_max_neck_syn_size=null : float                        # 
        sp_head_oblique_spine_n_head_syn=null : float                        # 
        sp_head_oblique_spine_n_neck_syn=null : float                        # 
        sp_head_skeletal_length=null : float                        # 
        sp_head_volume=null  : float                        # 
        sp_head_width_ray=null : float                        # 
        sp_head_width_ray_80_perc=null : float                        # 
        sp_neck_area=null    : float                        # 
        sp_neck_n_faces=null : float                        # 
        sp_neck_skeletal_length=null : float                        # 
        sp_neck_volume=null  : float                        # 
        sp_neck_width_ray=null : float                        # 
        sp_neck_width_ray_80_perc=null : float                        # 
        sp_no_head_apical_shaft_spine_area=null : float                        # 
        sp_no_head_apical_shaft_spine_max_no_head_sp_vol=null : float                        # 
        sp_no_head_apical_shaft_spine_max_no_head_syn_size=null : float                        # 
        sp_no_head_apical_shaft_spine_n_faces=null : float                        # 
        sp_no_head_apical_shaft_spine_n_no_head_syn=null : float                        # 
        sp_no_head_apical_shaft_spine_skeletal_length=null : float                        # 
        sp_no_head_apical_shaft_spine_volume=null : float                        # 
        sp_no_head_apical_shaft_spine_width_ray=null : float                        # 
        sp_no_head_apical_spine_area=null : float                        # 
        sp_no_head_apical_spine_max_no_head_sp_vol=null : float                        # 
        sp_no_head_apical_spine_max_no_head_syn_size=null : float                        # 
        sp_no_head_apical_spine_n_faces=null : float                        # 
        sp_no_head_apical_spine_n_no_head_syn=null : float                        # 
        sp_no_head_apical_spine_skeletal_length=null : float                        # 
        sp_no_head_apical_spine_volume=null : float                        # 
        sp_no_head_apical_spine_width_ray=null : float                        # 
        sp_no_head_apical_tuft_spine_area=null : float                        # 
        sp_no_head_apical_tuft_spine_max_no_head_sp_vol=null : float                        # 
        sp_no_head_apical_tuft_spine_max_no_head_syn_size=null : float                        # 
        sp_no_head_apical_tuft_spine_n_faces=null : float                        # 
        sp_no_head_apical_tuft_spine_n_no_head_syn=null : float                        # 
        sp_no_head_apical_tuft_spine_skeletal_length=null : float                        # 
        sp_no_head_apical_tuft_spine_volume=null : float                        # 
        sp_no_head_apical_tuft_spine_width_ray=null : float                        # 
        sp_no_head_basal_spine_area=null : float                        # 
        sp_no_head_basal_spine_max_no_head_sp_vol=null : float                        # 
        sp_no_head_basal_spine_max_no_head_syn_size=null : float                        # 
        sp_no_head_basal_spine_n_faces=null : float                        # 
        sp_no_head_basal_spine_n_no_head_syn=null : float                        # 
        sp_no_head_basal_spine_skeletal_length=null : float                        # 
        sp_no_head_basal_spine_volume=null : float                        # 
        sp_no_head_basal_spine_width_ray=null : float                        # 
        sp_no_head_dendrite_spine_area=null : float                        # 
        sp_no_head_dendrite_spine_max_no_head_sp_vol=null : float                        # 
        sp_no_head_dendrite_spine_max_no_head_syn_size=null : float                        # 
        sp_no_head_dendrite_spine_n_faces=null : float                        # 
        sp_no_head_dendrite_spine_n_no_head_syn=null : float                        # 
        sp_no_head_dendrite_spine_skeletal_length=null : float                        # 
        sp_no_head_dendrite_spine_volume=null : float                        # 
        sp_no_head_dendrite_spine_width_ray=null : float                        # 
        sp_no_head_n_apical=null : int unsigned                 # 
        sp_no_head_n_apical_shaft=null : int unsigned                 # 
        sp_no_head_n_apical_tuft=null : int unsigned                 # 
        sp_no_head_n_basal=null : int unsigned                 # 
        sp_no_head_n_dendrite=null : int unsigned                 # 
        sp_no_head_n_oblique=null : int unsigned                 # 
        sp_no_head_number=null : int unsigned                 # 
        sp_no_head_oblique_spine_area=null : float                        # 
        sp_no_head_oblique_spine_max_no_head_sp_vol=null : float                        # 
        sp_no_head_oblique_spine_max_no_head_syn_size=null : float                        # 
        sp_no_head_oblique_spine_n_faces=null : float                        # 
        sp_no_head_oblique_spine_n_no_head_syn=null : float                        # 
        sp_no_head_oblique_spine_skeletal_length=null : float                        # 
        sp_no_head_oblique_spine_volume=null : float                        # 
        sp_no_head_oblique_spine_width_ray=null : float                        # 
        sp_spine_area=null   : float                        # 
        sp_spine_max_head_sp_vol=null : float                        # 
        sp_spine_max_head_syn_size=null : float                        # 
        sp_spine_max_neck_sp_vol=null : float                        # 
        sp_spine_max_neck_syn_size=null : float                        # 
        sp_spine_max_no_head_sp_vol=null : float                        # 
        sp_spine_max_no_head_syn_size=null : float                        # 
        sp_spine_n_faces=null : float                        # 
        sp_spine_n_head_syn=null : float                        # 
        sp_spine_n_neck_syn=null : float                        # 
        sp_spine_n_no_head_syn=null : float                        # 
        sp_spine_skeletal_length=null : float                        # 
        sp_spine_volume=null : float                        # 
        sp_spine_width_ray=null : float                        # 
        """
                    
    class SpineSynapse(djp.Part):
        definition = """
        -> master
        ---
        syn_apical_head_spine_area=null : float                        # 
        syn_apical_head_spine_n_faces=null : float                        # 
        syn_apical_head_spine_skeletal_length=null : float                        # 
        syn_apical_head_spine_volume=null : float                        # 
        syn_apical_head_spine_width_ray=null : float                        # 
        syn_apical_head_syn_spine_area=null : float                        # 
        syn_apical_head_syn_spine_volume=null : float                        # 
        syn_apical_head_syn_spine_width_ray_80_perc=null : float                        # 
        syn_apical_head_synapse_size=null : float                        # 
        syn_apical_neck_spine_area=null : float                        # 
        syn_apical_neck_spine_n_faces=null : float                        # 
        syn_apical_neck_spine_skeletal_length=null : float                        # 
        syn_apical_neck_spine_volume=null : float                        # 
        syn_apical_neck_spine_width_ray=null : float                        # 
        syn_apical_neck_syn_spine_area=null : float                        # 
        syn_apical_neck_syn_spine_volume=null : float                        # 
        syn_apical_neck_syn_spine_width_ray_80_perc=null : float                        # 
        syn_apical_neck_synapse_size=null : float                        # 
        syn_apical_no_head_spine_area=null : float                        # 
        syn_apical_no_head_spine_n_faces=null : float                        # 
        syn_apical_no_head_spine_skeletal_length=null : float                        # 
        syn_apical_no_head_spine_volume=null : float                        # 
        syn_apical_no_head_spine_width_ray=null : float                        # 
        syn_apical_no_head_syn_spine_area=null : float                        # 
        syn_apical_no_head_syn_spine_volume=null : float                        # 
        syn_apical_no_head_syn_spine_width_ray_80_perc=null : float                        # 
        syn_apical_no_head_synapse_size=null : float                        # 
        syn_apical_shaft_head_spine_area=null : float                        # 
        syn_apical_shaft_head_spine_n_faces=null : float                        # 
        syn_apical_shaft_head_spine_skeletal_length=null : float                        # 
        syn_apical_shaft_head_spine_volume=null : float                        # 
        syn_apical_shaft_head_spine_width_ray=null : float                        # 
        syn_apical_shaft_head_syn_spine_area=null : float                        # 
        syn_apical_shaft_head_syn_spine_volume=null : float                        # 
        syn_apical_shaft_head_syn_spine_width_ray_80_perc=null : float                        # 
        syn_apical_shaft_head_synapse_size=null : float                        # 
        syn_apical_shaft_neck_spine_area=null : float                        # 
        syn_apical_shaft_neck_spine_n_faces=null : float                        # 
        syn_apical_shaft_neck_spine_skeletal_length=null : float                        # 
        syn_apical_shaft_neck_spine_volume=null : float                        # 
        syn_apical_shaft_neck_spine_width_ray=null : float                        # 
        syn_apical_shaft_neck_syn_spine_area=null : float                        # 
        syn_apical_shaft_neck_syn_spine_volume=null : float                        # 
        syn_apical_shaft_neck_syn_spine_width_ray_80_perc=null : float                        # 
        syn_apical_shaft_neck_synapse_size=null : float                        # 
        syn_apical_shaft_no_head_spine_area=null : float                        # 
        syn_apical_shaft_no_head_spine_n_faces=null : float                        # 
        syn_apical_shaft_no_head_spine_skeletal_length=null : float                        # 
        syn_apical_shaft_no_head_spine_volume=null : float                        # 
        syn_apical_shaft_no_head_spine_width_ray=null : float                        # 
        syn_apical_shaft_no_head_syn_spine_area=null : float                        # 
        syn_apical_shaft_no_head_syn_spine_volume=null : float                        # 
        syn_apical_shaft_no_head_syn_spine_width_ray_80_perc=null : float                        # 
        syn_apical_shaft_no_head_synapse_size=null : float                        # 
        syn_apical_shaft_shaft_spine_area=null : float                        # 
        syn_apical_shaft_shaft_spine_n_faces=null : float                        # 
        syn_apical_shaft_shaft_spine_skeletal_length=null : float                        # 
        syn_apical_shaft_shaft_spine_volume=null : float                        # 
        syn_apical_shaft_shaft_spine_width_ray=null : float                        # 
        syn_apical_shaft_shaft_syn_spine_area=null : float                        # 
        syn_apical_shaft_shaft_syn_spine_volume=null : float                        # 
        syn_apical_shaft_shaft_syn_spine_width_ray_80_perc=null : float                        # 
        syn_apical_shaft_shaft_synapse_size=null : float                        # 
        syn_apical_shaft_spine_area=null : float                        # 
        syn_apical_shaft_spine_n_faces=null : float                        # 
        syn_apical_shaft_spine_skeletal_length=null : float                        # 
        syn_apical_shaft_spine_volume=null : float                        # 
        syn_apical_shaft_spine_width_ray=null : float                        # 
        syn_apical_shaft_syn_spine_area=null : float                        # 
        syn_apical_shaft_syn_spine_volume=null : float                        # 
        syn_apical_shaft_syn_spine_width_ray_80_perc=null : float                        # 
        syn_apical_shaft_synapse_size=null : float                        # 
        syn_apical_tuft_head_spine_area=null : float                        # 
        syn_apical_tuft_head_spine_n_faces=null : float                        # 
        syn_apical_tuft_head_spine_skeletal_length=null : float                        # 
        syn_apical_tuft_head_spine_volume=null : float                        # 
        syn_apical_tuft_head_spine_width_ray=null : float                        # 
        syn_apical_tuft_head_syn_spine_area=null : float                        # 
        syn_apical_tuft_head_syn_spine_volume=null : float                        # 
        syn_apical_tuft_head_syn_spine_width_ray_80_perc=null : float                        # 
        syn_apical_tuft_head_synapse_size=null : float                        # 
        syn_apical_tuft_neck_spine_area=null : float                        # 
        syn_apical_tuft_neck_spine_n_faces=null : float                        # 
        syn_apical_tuft_neck_spine_skeletal_length=null : float                        # 
        syn_apical_tuft_neck_spine_volume=null : float                        # 
        syn_apical_tuft_neck_spine_width_ray=null : float                        # 
        syn_apical_tuft_neck_syn_spine_area=null : float                        # 
        syn_apical_tuft_neck_syn_spine_volume=null : float                        # 
        syn_apical_tuft_neck_syn_spine_width_ray_80_perc=null : float                        # 
        syn_apical_tuft_neck_synapse_size=null : float                        # 
        syn_apical_tuft_no_head_spine_area=null : float                        # 
        syn_apical_tuft_no_head_spine_n_faces=null : float                        # 
        syn_apical_tuft_no_head_spine_skeletal_length=null : float                        # 
        syn_apical_tuft_no_head_spine_volume=null : float                        # 
        syn_apical_tuft_no_head_spine_width_ray=null : float                        # 
        syn_apical_tuft_no_head_syn_spine_area=null : float                        # 
        syn_apical_tuft_no_head_syn_spine_volume=null : float                        # 
        syn_apical_tuft_no_head_syn_spine_width_ray_80_perc=null : float                        # 
        syn_apical_tuft_no_head_synapse_size=null : float                        # 
        syn_apical_tuft_shaft_spine_area=null : float                        # 
        syn_apical_tuft_shaft_spine_n_faces=null : float                        # 
        syn_apical_tuft_shaft_spine_skeletal_length=null : float                        # 
        syn_apical_tuft_shaft_spine_volume=null : float                        # 
        syn_apical_tuft_shaft_spine_width_ray=null : float                        # 
        syn_apical_tuft_shaft_syn_spine_area=null : float                        # 
        syn_apical_tuft_shaft_syn_spine_volume=null : float                        # 
        syn_apical_tuft_shaft_syn_spine_width_ray_80_perc=null : float                        # 
        syn_apical_tuft_shaft_synapse_size=null : float                        # 
        syn_axon_shaft_spine_area=null : float                        # 
        syn_axon_shaft_spine_n_faces=null : float                        # 
        syn_axon_shaft_spine_skeletal_length=null : float                        # 
        syn_axon_shaft_spine_volume=null : float                        # 
        syn_axon_shaft_spine_width_ray=null : float                        # 
        syn_axon_shaft_syn_spine_area=null : float                        # 
        syn_axon_shaft_syn_spine_volume=null : float                        # 
        syn_axon_shaft_syn_spine_width_ray_80_perc=null : float                        # 
        syn_axon_shaft_synapse_size=null : float                        # 
        syn_basal_head_spine_area=null : float                        # 
        syn_basal_head_spine_n_faces=null : float                        # 
        syn_basal_head_spine_skeletal_length=null : float                        # 
        syn_basal_head_spine_volume=null : float                        # 
        syn_basal_head_spine_width_ray=null : float                        # 
        syn_basal_head_syn_spine_area=null : float                        # 
        syn_basal_head_syn_spine_volume=null : float                        # 
        syn_basal_head_syn_spine_width_ray_80_perc=null : float                        # 
        syn_basal_head_synapse_size=null : float                        # 
        syn_basal_neck_spine_area=null : float                        # 
        syn_basal_neck_spine_n_faces=null : float                        # 
        syn_basal_neck_spine_skeletal_length=null : float                        # 
        syn_basal_neck_spine_volume=null : float                        # 
        syn_basal_neck_spine_width_ray=null : float                        # 
        syn_basal_neck_syn_spine_area=null : float                        # 
        syn_basal_neck_syn_spine_volume=null : float                        # 
        syn_basal_neck_syn_spine_width_ray_80_perc=null : float                        # 
        syn_basal_neck_synapse_size=null : float                        # 
        syn_basal_no_head_spine_area=null : float                        # 
        syn_basal_no_head_spine_n_faces=null : float                        # 
        syn_basal_no_head_spine_skeletal_length=null : float                        # 
        syn_basal_no_head_spine_volume=null : float                        # 
        syn_basal_no_head_spine_width_ray=null : float                        # 
        syn_basal_no_head_syn_spine_area=null : float                        # 
        syn_basal_no_head_syn_spine_volume=null : float                        # 
        syn_basal_no_head_syn_spine_width_ray_80_perc=null : float                        # 
        syn_basal_no_head_synapse_size=null : float                        # 
        syn_basal_shaft_spine_area=null : float                        # 
        syn_basal_shaft_spine_n_faces=null : float                        # 
        syn_basal_shaft_spine_skeletal_length=null : float                        # 
        syn_basal_shaft_spine_volume=null : float                        # 
        syn_basal_shaft_spine_width_ray=null : float                        # 
        syn_basal_shaft_syn_spine_area=null : float                        # 
        syn_basal_shaft_syn_spine_volume=null : float                        # 
        syn_basal_shaft_syn_spine_width_ray_80_perc=null : float                        # 
        syn_basal_shaft_synapse_size=null : float                        # 
        syn_dendrite_head_spine_area=null : float                        # 
        syn_dendrite_head_spine_n_faces=null : float                        # 
        syn_dendrite_head_spine_skeletal_length=null : float                        # 
        syn_dendrite_head_spine_volume=null : float                        # 
        syn_dendrite_head_spine_width_ray=null : float                        # 
        syn_dendrite_head_syn_spine_area=null : float                        # 
        syn_dendrite_head_syn_spine_volume=null : float                        # 
        syn_dendrite_head_syn_spine_width_ray_80_perc=null : float                        # 
        syn_dendrite_head_synapse_size=null : float                        # 
        syn_dendrite_neck_spine_area=null : float                        # 
        syn_dendrite_neck_spine_n_faces=null : float                        # 
        syn_dendrite_neck_spine_skeletal_length=null : float                        # 
        syn_dendrite_neck_spine_volume=null : float                        # 
        syn_dendrite_neck_spine_width_ray=null : float                        # 
        syn_dendrite_neck_syn_spine_area=null : float                        # 
        syn_dendrite_neck_syn_spine_volume=null : float                        # 
        syn_dendrite_neck_syn_spine_width_ray_80_perc=null : float                        # 
        syn_dendrite_neck_synapse_size=null : float                        # 
        syn_dendrite_no_head_spine_area=null : float                        # 
        syn_dendrite_no_head_spine_n_faces=null : float                        # 
        syn_dendrite_no_head_spine_skeletal_length=null : float                        # 
        syn_dendrite_no_head_spine_volume=null : float                        # 
        syn_dendrite_no_head_spine_width_ray=null : float                        # 
        syn_dendrite_no_head_syn_spine_area=null : float                        # 
        syn_dendrite_no_head_syn_spine_volume=null : float                        # 
        syn_dendrite_no_head_syn_spine_width_ray_80_perc=null : float                        # 
        syn_dendrite_no_head_synapse_size=null : float                        # 
        syn_dendrite_shaft_spine_area=null : float                        # 
        syn_dendrite_shaft_spine_n_faces=null : float                        # 
        syn_dendrite_shaft_spine_skeletal_length=null : float                        # 
        syn_dendrite_shaft_spine_volume=null : float                        # 
        syn_dendrite_shaft_spine_width_ray=null : float                        # 
        syn_dendrite_shaft_syn_spine_area=null : float                        # 
        syn_dendrite_shaft_syn_spine_volume=null : float                        # 
        syn_dendrite_shaft_syn_spine_width_ray_80_perc=null : float                        # 
        syn_dendrite_shaft_synapse_size=null : float                        # 
        syn_head_spine_area=null : float                        # 
        syn_head_spine_n_faces=null : float                        # 
        syn_head_spine_skeletal_length=null : float                        # 
        syn_head_spine_volume=null : float                        # 
        syn_head_spine_width_ray=null : float                        # 
        syn_head_syn_spine_area=null : float                        # 
        syn_head_syn_spine_volume=null : float                        # 
        syn_head_syn_spine_width_ray_80_perc=null : float                        # 
        syn_head_synapse_size=null : float                        # 
        syn_n_apical_head=null : int unsigned                 # 
        syn_n_apical_neck=null : int unsigned                 # 
        syn_n_apical_no_head=null : int unsigned                 # 
        syn_n_apical_shaft=null : int unsigned                 # 
        syn_n_apical_shaft_head=null : int unsigned                 # 
        syn_n_apical_shaft_neck=null : int unsigned                 # 
        syn_n_apical_shaft_no_head=null : int unsigned                 # 
        syn_n_apical_shaft_shaft=null : int unsigned                 # 
        syn_n_apical_tuft_head=null : int unsigned                 # 
        syn_n_apical_tuft_neck=null : int unsigned                 # 
        syn_n_apical_tuft_no_head=null : int unsigned                 # 
        syn_n_apical_tuft_shaft=null : int unsigned                 # 
        syn_n_axon_shaft=null : int unsigned                 # 
        syn_n_basal_head=null : int unsigned                 # 
        syn_n_basal_neck=null : int unsigned                 # 
        syn_n_basal_no_head=null : int unsigned                 # 
        syn_n_basal_shaft=null : int unsigned                 # 
        syn_n_dendrite_head=null : int unsigned                 # 
        syn_n_dendrite_neck=null : int unsigned                 # 
        syn_n_dendrite_no_head=null : int unsigned                 # 
        syn_n_dendrite_shaft=null : int unsigned                 # 
        syn_n_head=null      : int unsigned                 # 
        syn_n_neck=null      : int unsigned                 # 
        syn_n_no_head=null   : int unsigned                 # 
        syn_n_oblique_head=null : int unsigned                 # 
        syn_n_oblique_neck=null : int unsigned                 # 
        syn_n_oblique_no_head=null : int unsigned                 # 
        syn_n_oblique_shaft=null : int unsigned                 # 
        syn_n_shaft=null     : int unsigned                 # 
        syn_n_soma_shaft=null : int unsigned                 # 
        syn_neck_spine_area=null : float                        # 
        syn_neck_spine_n_faces=null : float                        # 
        syn_neck_spine_skeletal_length=null : float                        # 
        syn_neck_spine_volume=null : float                        # 
        syn_neck_spine_width_ray=null : float                        # 
        syn_neck_syn_spine_area=null : float                        # 
        syn_neck_syn_spine_volume=null : float                        # 
        syn_neck_syn_spine_width_ray_80_perc=null : float                        # 
        syn_neck_synapse_size=null : float                        # 
        syn_no_head_spine_area=null : float                        # 
        syn_no_head_spine_n_faces=null : float                        # 
        syn_no_head_spine_skeletal_length=null : float                        # 
        syn_no_head_spine_volume=null : float                        # 
        syn_no_head_spine_width_ray=null : float                        # 
        syn_no_head_syn_spine_area=null : float                        # 
        syn_no_head_syn_spine_volume=null : float                        # 
        syn_no_head_syn_spine_width_ray_80_perc=null : float                        # 
        syn_no_head_synapse_size=null : float                        # 
        syn_oblique_head_spine_area=null : float                        # 
        syn_oblique_head_spine_n_faces=null : float                        # 
        syn_oblique_head_spine_skeletal_length=null : float                        # 
        syn_oblique_head_spine_volume=null : float                        # 
        syn_oblique_head_spine_width_ray=null : float                        # 
        syn_oblique_head_syn_spine_area=null : float                        # 
        syn_oblique_head_syn_spine_volume=null : float                        # 
        syn_oblique_head_syn_spine_width_ray_80_perc=null : float                        # 
        syn_oblique_head_synapse_size=null : float                        # 
        syn_oblique_neck_spine_area=null : float                        # 
        syn_oblique_neck_spine_n_faces=null : float                        # 
        syn_oblique_neck_spine_skeletal_length=null : float                        # 
        syn_oblique_neck_spine_volume=null : float                        # 
        syn_oblique_neck_spine_width_ray=null : float                        # 
        syn_oblique_neck_syn_spine_area=null : float                        # 
        syn_oblique_neck_syn_spine_volume=null : float                        # 
        syn_oblique_neck_syn_spine_width_ray_80_perc=null : float                        # 
        syn_oblique_neck_synapse_size=null : float                        # 
        syn_oblique_no_head_spine_area=null : float                        # 
        syn_oblique_no_head_spine_n_faces=null : float                        # 
        syn_oblique_no_head_spine_skeletal_length=null : float                        # 
        syn_oblique_no_head_spine_volume=null : float                        # 
        syn_oblique_no_head_spine_width_ray=null : float                        # 
        syn_oblique_no_head_syn_spine_area=null : float                        # 
        syn_oblique_no_head_syn_spine_volume=null : float                        # 
        syn_oblique_no_head_syn_spine_width_ray_80_perc=null : float                        # 
        syn_oblique_no_head_synapse_size=null : float                        # 
        syn_oblique_shaft_spine_area=null : float                        # 
        syn_oblique_shaft_spine_n_faces=null : float                        # 
        syn_oblique_shaft_spine_skeletal_length=null : float                        # 
        syn_oblique_shaft_spine_volume=null : float                        # 
        syn_oblique_shaft_spine_width_ray=null : float                        # 
        syn_oblique_shaft_syn_spine_area=null : float                        # 
        syn_oblique_shaft_syn_spine_volume=null : float                        # 
        syn_oblique_shaft_syn_spine_width_ray_80_perc=null : float                        # 
        syn_oblique_shaft_synapse_size=null : float                        # 
        syn_shaft_spine_area=null : float                        # 
        syn_shaft_spine_n_faces=null : float                        # 
        syn_shaft_spine_skeletal_length=null : float                        # 
        syn_shaft_spine_volume=null : float                        # 
        syn_shaft_spine_width_ray=null : float                        # 
        syn_shaft_syn_spine_area=null : float                        # 
        syn_shaft_syn_spine_volume=null : float                        # 
        syn_shaft_syn_spine_width_ray_80_perc=null : float                        # 
        syn_shaft_synapse_size=null : float                        # 
        syn_soma_shaft_spine_area=null : float                        # 
        syn_soma_shaft_spine_n_faces=null : float                        # 
        syn_soma_shaft_spine_skeletal_length=null : float                        # 
        syn_soma_shaft_spine_volume=null : float                        # 
        syn_soma_shaft_spine_width_ray=null : float                        # 
        syn_soma_shaft_syn_spine_area=null : float                        # 
        syn_soma_shaft_syn_spine_volume=null : float                        # 
        syn_soma_shaft_syn_spine_width_ray_80_perc=null : float                        # 
        syn_soma_shaft_synapse_size=null : float                        # 
        """
            

@schema
class AutoProofreadNeuronPreDendr(djp.Computed):
    definition = """
    primary_seg_id       : bigint unsigned              # segment id unique within each Segmentation
    synapse_id           : bigint unsigned              # 
    ---
    synapse_type         : enum('presyn','postsyn')     # 
    """


@schema
class ValidationSkeletonStats(djp.Computed):
    definition = """
    segment_id           : bigint unsigned              # 
    split_index          : tinyint unsigned             # 
    extension            : tinyint                      # 
    ---
    axon_tp_skeleton=null : longblob                     # 
    axon_fp_skeleton=null : longblob                     # 
    axon_fn_skeleton=null : longblob                     # 
    axon_tp_skeleton_length=null : int unsigned                 # 
    axon_fp_skeleton_length=null : float                        # 
    axon_fn_skeleton_length=null : float                        # 
    axon_total_length=null : float                        # 
    axon_precision=null  : float                        # 
    axon_recall=null     : float                        # 
    axon_f1=null         : float                        # 
    axon_tp_skeleton_raw=null : longblob                     # 
    axon_fp_skeleton_raw=null : longblob                     # 
    axon_fn_skeleton_raw=null : longblob                     # 
    axon_tp_skeleton_length_raw=null : int unsigned                 # 
    axon_fp_skeleton_length_raw=null : float                        # 
    axon_fn_skeleton_length_raw=null : float                        # 
    axon_total_length_raw=null : float                        # 
    axon_precision_raw=null : float                        # 
    axon_recall_raw=null : float                        # 
    axon_f1_raw=null     : float                        # 
    dendrite_tp_skeleton=null : longblob                     # 
    dendrite_fp_skeleton=null : longblob                     # 
    dendrite_fn_skeleton=null : longblob                     # 
    dendrite_tp_skeleton_length=null : float                        # 
    dendrite_fp_skeleton_length=null : float                        # 
    dendrite_fn_skeleton_length=null : float                        # 
    dendrite_total_length=null : float                        # 
    dendrite_precision=null : float                        # 
    dendrite_recall=null : float                        # 
    dendrite_f1=null     : float                        # 
    dendrite_tp_skeleton_raw=null : longblob                     # 
    dendrite_fp_skeleton_raw=null : longblob                     # 
    dendrite_fn_skeleton_raw=null : longblob                     # 
    dendrite_tp_skeleton_length_raw=null : float                        # 
    dendrite_fp_skeleton_length_raw=null : float                        # 
    dendrite_fn_skeleton_length_raw=null : float                        # 
    dendrite_total_length_raw=null : float                        # 
    dendrite_precision_raw=null : float                        # 
    dendrite_recall_raw=null : float                        # 
    dendrite_f1_raw=null : float                        # 
    """
            

@schema
class ValidationSegmentMap(djp.Manual):
    definition = """
    ver                  : double                       # 
    nucleus_id           : bigint unsigned              # nucleus id
    segment_id           : bigint unsigned              # the segment id in the proofread version
    old_ver              : double                       # 
    ---
    old_segment_id       : bigint unsigned              # the segment id in the proofread version--
    cell_type            : enum('excitatory','inhibitory') # 
    cell_type_fine=null  : varchar(8)                   # 
    n_somas=null         : tinyint unsigned             # 
    n_soma_mergers=null  : tinyint unsigned             # 
    n_glia=null          : tinyint unsigned             # 
    amount_of_merges=null : varchar(512)                 # 
    proof_pre_post_link=null : varchar(1000)                # 
    notes=null           : varchar(256)                 # 
    """


@schema
class ValidationSynapseStats(djp.Computed):
    definition = """
    -> ValidationSegmentMap
    count_pre_on_dendr_correct : tinyint                      # 
    extension            : tinyint                      # 
    ---
    presyn_tp=null       : int unsigned                 # 
    presyn_tn=null       : int unsigned                 # 
    presyn_fp=null       : int unsigned                 # 
    presyn_fn=null       : int unsigned                 # 
    presyn_total=null    : int unsigned                 # 
    postsyn_tp=null      : int unsigned                 # 
    postsyn_tn=null      : int unsigned                 # 
    postsyn_fp=null      : int unsigned                 # 
    postsyn_fn=null      : int unsigned                 # 
    postsyn_total=null   : int unsigned                 # 
    presyn_precision=null : float                        # 
    presyn_recall=null   : float                        # 
    presyn_f1=null       : float                        # 
    postsyn_precision=null : float                        # 
    postsyn_recall=null  : float                        # 
    postsyn_f1=null      : float                        # 
    presyn_tp_raw=null   : int unsigned                 # 
    presyn_tn_raw=null   : int unsigned                 # 
    presyn_fp_raw=null   : int unsigned                 # 
    presyn_fn_raw=null   : int unsigned                 # 
    presyn_total_raw=null : int unsigned                 # 
    postsyn_tp_raw=null  : int unsigned                 # 
    postsyn_tn_raw=null  : int unsigned                 # 
    postsyn_fp_raw=null  : int unsigned                 # 
    postsyn_fn_raw=null  : int unsigned                 # 
    postsyn_total_raw=null : int unsigned                 # 
    presyn_precision_raw=null : float                        # 
    presyn_recall_raw=null : float                        # 
    presyn_f1_raw=null   : float                        # 
    postsyn_precision_raw=null : float                        # 
    postsyn_recall_raw=null : float                        # 
    postsyn_f1_raw=null  : float                        # 
    synapse_df=null      : longblob                     # dictionary that is the dataframe the following was generate from
    cell_type=null       : varchar(30)                  # 
    n_somas=null         : tinyint unsigned             # 
    n_glia=null          : tinyint unsigned             # 
    old_split_index      : tinyint unsigned             # 
    """
            

@schema
class ValidationSynapseStats2(djp.Computed):
    definition = """
    -> ValidationSegmentMap
    count_pre_on_dendr_correct : tinyint                      # 
    extension            : tinyint                      # 
    ---
    presyn_tp=null       : int unsigned                 # 
    presyn_tn=null       : int unsigned                 # 
    presyn_fp=null       : int unsigned                 # 
    presyn_fn=null       : int unsigned                 # 
    presyn_total=null    : int unsigned                 # 
    postsyn_tp=null      : int unsigned                 # 
    postsyn_tn=null      : int unsigned                 # 
    postsyn_fp=null      : int unsigned                 # 
    postsyn_fn=null      : int unsigned                 # 
    postsyn_total=null   : int unsigned                 # 
    presyn_precision=null : float                        # 
    presyn_recall=null   : float                        # 
    presyn_f1=null       : float                        # 
    postsyn_precision=null : float                        # 
    postsyn_recall=null  : float                        # 
    postsyn_f1=null      : float                        # 
    presyn_tp_raw=null   : int unsigned                 # 
    presyn_tn_raw=null   : int unsigned                 # 
    presyn_fp_raw=null   : int unsigned                 # 
    presyn_fn_raw=null   : int unsigned                 # 
    presyn_total_raw=null : int unsigned                 # 
    postsyn_tp_raw=null  : int unsigned                 # 
    postsyn_tn_raw=null  : int unsigned                 # 
    postsyn_fp_raw=null  : int unsigned                 # 
    postsyn_fn_raw=null  : int unsigned                 # 
    postsyn_total_raw=null : int unsigned                 # 
    presyn_precision_raw=null : float                        # 
    presyn_recall_raw=null : float                        # 
    presyn_f1_raw=null   : float                        # 
    postsyn_precision_raw=null : float                        # 
    postsyn_recall_raw=null : float                        # 
    postsyn_f1_raw=null  : float                        # 
    synapse_df=null      : longblob                     # dictionary that is the dataframe the following was generate from
    cell_type=null       : varchar(30)                  # 
    n_somas=null         : tinyint unsigned             # 
    n_glia=null          : tinyint unsigned             # 
    old_split_index      : tinyint unsigned             # 
    """


@schema
class ValidationProofreadAxonDendrite(djp.Computed):
    definition = """
    -> ValidationSegmentMap
    ---
    axon_skeleton_manual=null : longblob                     # 
    axon_skeleton_manual_length=null : float                        # 
    dendrite_skeleton_manual=null : longblob                     # 
    dendrite_skeleton_manual_length=null : float                        # 
    exclude_skeleton_manual=null : longblob                     # 
    exclude_skeleton_manual_length=null : float                        # 
    axon_skeleton_auto=null : longblob                     # 
    axon_skeleton_auto_length=null : float                        # 
    dendrite_skeleton_auto=null : longblob                     # 
    dendrite_skeleton_auto_length=null : float                        # 
    """


@schema
class ValidationProofreadAxonDendrite2(djp.Computed):
    definition = """
    -> ValidationSegmentMap
    ---
    axon_skeleton_manual=null : longblob                     # 
    axon_skeleton_manual_length=null : float                        # 
    dendrite_skeleton_manual=null : longblob                     # 
    dendrite_skeleton_manual_length=null : float                        # 
    exclude_skeleton_manual=null : longblob                     # 
    exclude_skeleton_manual_length=null : float                        # 
    axon_skeleton_auto=null : longblob                     # 
    axon_skeleton_auto_length=null : float                        # 
    dendrite_skeleton_auto=null : longblob                     # 
    dendrite_skeleton_auto_length=null : float                        # 
    axon_skeleton_raw=null : longblob                     # 
    axon_skeleton_raw_length=null : float                        # 
    dendrite_skeleton_raw=null : longblob                     # 
    dendrite_skeleton_raw_length=null : float                        # 
    """


@schema
class ValidationSegmentExclude(djp.Manual):
    definition = """
    segment_id           : bigint unsigned              # the segment id in the proofread version
    ---
    criteria             : varchar(256)                 # why the segments were excluded
    """


@schema
class AutoProofreadNeuronInterAreaPresyn(djp.Manual):
    definition = """
    segment_id           : bigint unsigned              # 
    split_index          : int unsigned                 # 
    """
            

@schema
class AutoProofreadNeuronLeafMatch(djp.Computed):
    definition = """
    segment_id           : bigint unsigned              # 
    split_index          : int unsigned                 # 
    subgraph_idx         : int unsigned                 # 
    leaf_node            : varchar(14)                  # 
    match_segment_id     : bigint unsigned              # 
    match_split_index    : int unsigned                 # 
    match_subgraph_idx   : int unsigned                 # 
    match_leaf_node      : varchar(14)                  # 
    scholl_adjusted      : tinyint                      # 
    n_axes               : tinyint unsigned             # 
    ---
    similarity_n_points=null : int unsigned                 # 
    similarity_max_scholl_point=null : float                        # 
    similarity=null      : float                        # 
    match_soma_soma_dist_x_nm=null : float                        # 
    match_soma_soma_dist_y_nm=null : float                        # 
    match_soma_soma_dist_z_nm=null : float                        # 
    match_endpoint_endpoint_dist_x_nm=null : float                        # 
    match_endpoint_endpoint_dist_y_nm=null : float                        # 
    match_endpoint_endpoint_dist_z_nm=null : float                        # 
    skeleton_vector_to_top_angle=null : float                        # 
    match_skeleton_vector_to_top_angle=null : float                        # 
    """


@schema
class AutoProofreadNeuronFunctional(djp.Manual):
    definition = """
    segment_id           : bigint unsigned              # 
    split_index          : int unsigned                 # 
    ---
    nucleus_id           : int unsigned                 # 
    ori_rad              : float                        # orientational tuning
    dir_rad              : float                        # directional tuning
    tuning_fidelity      : float                        # derived from the osi
    oracle               : float                        # 
    method               : enum('auto','manual')        # 
    """
            

@schema
class SynapseManualCellsProofread(djp.Manual):
    definition = """
    # Synapses for the cells that were manually proofread after proofreading (Will be populated from AutoProofreadValidationManualSynapse4)
    primary_seg_id       : bigint unsigned              # id of the segment that is synaptically paired to primary_segment_id.
    secondary_seg_id     : bigint unsigned              # id of the segment that is synaptically paired to primary_segment_id.
    synapse_id           : bigint unsigned              # synapse index within the segmentation
    ---
    prepost              : varchar(16)                  # whether the primary_seg_id is "presyn" or "postsyn"
    synapse_x            : int unsigned                 # x coordinate of synapse centroid in EM voxels (x: 4nm, y: 4nm, z: 40nm). From Allen 'ctr_pt_position'.
    synapse_y            : int unsigned                 # y coordinate of centroid in EM voxels (x: 4nm, y: 4nm, z: 40nm). From Allen 'ctr_pt_position'.
    synapse_z            : int unsigned                 # z coordinate of centroid in EM voxels (x: 4nm, y: 4nm, z: 40nm). From Allen 'ctr_pt_position'.
    synapse_size         : int unsigned                 # (EM voxels) scaled by (4x4x40)
    """
            

@schema
class AutoProofreadNeuronFuncControl(djp.Manual):
    definition = """
    segment_id           : bigint unsigned              # 
    split_index          : int unsigned                 # 
    """
            

@schema
class AutoProofreadNeuronExclude(djp.Manual):
    definition = """
    segment_id           : bigint unsigned              # 
    split_index          : bigint unsigned              # 
    ---
    criteria=null        : varchar(300)                 # 
    insertion_time=CURRENT_TIMESTAMP : timestamp                    # 
    """
            
            
@schema
class AutoProofreadNeuronDirectConnections(djp.Manual):
    definition = """
    synapse_id           : bigint unsigned              # 
    """


@schema
class AutoProofreadNeuronDirectConnectionsFull(djp.Manual):
    definition = """
    synapse_id           : bigint unsigned              # 
    """
    

@schema
class AutoProofreadNeuronConnetome(djp.Manual):
    definition = """
    iteration            : int                          # 
    auto_proof           : tinyint                      # 
    ---
    connectome           : <minnie65_graph>             # 
    notes                : varchar(500)                 # 
    timestamp=CURRENT_TIMESTAMP : timestamp                    # 
    """


@schema
class AutoProofreadNeuronConnetomeEdges(djp.Manual):
    definition = """
    primary_seg_id       : bigint unsigned              # 
    primary_split_index  : int unsigned                 # 
    secondary_seg_id     : bigint unsigned              # 
    secondary_split_index : int unsigned                 # 
    synapse_id           : bigint unsigned              # 
    -> AutoProofreadNeuronConnetome 
    ---
    synapse_size=null    : float                        # 
    synapse_x=null       : int unsigned                 # 
    synapse_y=null       : int unsigned                 # 
    synapse_z=null       : int unsigned                 # 
    presyn_soma_euclid_dist=null : float                        # 
    postsyn_soma_euclid_dist=null : float                        # 
    presyn_skeletal_distance_to_soma=null : float                        # 
    postsyn_skeletal_distance_to_soma=null : float                        # 
    presyn_limb_idx=null : tinyint unsigned             # 
    presyn_branch_idx=null : int unsigned                 # 
    postsyn_limb_idx=null : tinyint unsigned             # 
    postsyn_branch_idx=null : int unsigned                 # 
    presyn_compartment_coarse=null : enum('soma','axon','dendrite') # 
    presyn_compartment_fine=null : enum('basal','apical','apicaltuft','apicalshaft','oblique','inhibitory') # 
    postsyn_compartment_coarse=null : enum('soma','axon','dendrite') # 
    postsyn_compartment_fine=null : enum('basal','apical','apicaltuft','apicalshaft','oblique','inhibitory') # 
    presyn_spine_bouton=null : enum('head','neck','shaft','nohead','bouton','nonbouton','nolabel') # 
    postsyn_spine_bouton=null : enum('head','neck','shaft','nohead','bouton','nonbouton','nolabel') # 
    presyn_cell_type=null : enum('excitatory','inhibitory') # 
    postsyn_cell_type=null : enum('excitatory','inhibitory') # 
    presyn_gnn_cell_type_fine=null : enum('23P','4P','5P-IT','5P-NP','5P-PT','6P-CT','6P-IT','BC','BPC','MC','NGC') # 
    postsyn_gnn_cell_type_fine=null : enum('23P','4P','5P-IT','5P-NP','5P-PT','6P-CT','6P-IT','BC','BPC','MC','NGC') # 
    """


@schema
class AutoProofreadNeuronConnMotifMethod(djp.Manual):
    definition = """
    motif                : varchar(500)                 # 
    graph_type="DiGraph" : enum('MultiGraph','MultiDiGraph','DiGraph','Graph') # 
    ---
    n_nodes=null         : int                          # 
    notes=null           : varchar(300)                 # 
    timestamp=CURRENT_TIMESTAMP : timestamp                    # 
    """
            

@schema
class AutoProofreadNeuronConnMotif(djp.Computed):
    definition = """
    -> AutoProofreadNeuronConnMotifMethod
    index                : bigint unsigned              # 
    ---
    run_time=null        : double                       # the amount of time to run (seconds)
    """
    
    class Motif1(djp.Part):
        definition = """
        -> master
        ---
        a_segment_id         : bigint unsigned              # 
        a_split_index        : tinyint unsigned             # 
        """
                    
    class Motif2(djp.Part):
        definition = """
        -> master
        ---
        a_segment_id         : bigint unsigned              # 
        a_split_index        : tinyint unsigned             # 
        b_segment_id         : bigint unsigned              # 
        b_split_index        : tinyint unsigned             # 
        """
                    
    class Motif3(djp.Part):
        definition = """
        -> master
        ---
        a_segment_id         : bigint unsigned              # 
        a_split_index        : tinyint unsigned             # 
        b_segment_id         : bigint unsigned              # 
        b_split_index        : tinyint unsigned             # 
        c_segment_id         : bigint unsigned              # 
        c_split_index        : tinyint unsigned             # 
        """
                    
    class Motif4(djp.Part):
        definition = """
        -> master
        ---
        a_segment_id         : bigint unsigned              # 
        a_split_index        : tinyint unsigned             # 
        b_segment_id         : bigint unsigned              # 
        b_split_index        : tinyint unsigned             # 
        c_segment_id         : bigint unsigned              # 
        c_split_index        : tinyint unsigned             # 
        d_segment_id         : bigint unsigned              # 
        d_split_index        : tinyint unsigned             # 
        """
                    
    class Motif5(djp.Part):
        definition = """
        -> master
        ---
        a_segment_id         : bigint unsigned              # 
        a_split_index        : tinyint unsigned             # 
        b_segment_id         : bigint unsigned              # 
        b_split_index        : tinyint unsigned             # 
        c_segment_id         : bigint unsigned              # 
        c_split_index        : tinyint unsigned             # 
        d_segment_id         : bigint unsigned              # 
        d_split_index        : tinyint unsigned             # 
        e_segment_id         : bigint unsigned              # 
        e_split_index        : tinyint unsigned             # 
        """
                    
    class Motif6(djp.Part):
        definition = """
        -> master
        ---
        a_segment_id         : bigint unsigned              # 
        a_split_index        : tinyint unsigned             # 
        b_segment_id         : bigint unsigned              # 
        b_split_index        : tinyint unsigned             # 
        c_segment_id         : bigint unsigned              # 
        c_split_index        : tinyint unsigned             # 
        d_segment_id         : bigint unsigned              # 
        d_split_index        : tinyint unsigned             # 
        e_segment_id         : bigint unsigned              # 
        e_split_index        : tinyint unsigned             # 
        f_segment_id         : bigint unsigned              # 
        f_split_index        : tinyint unsigned             # 
        """
                    
    class Motif7(djp.Part):
        definition = """
        -> master
        ---
        a_segment_id         : bigint unsigned              # 
        a_split_index        : tinyint unsigned             # 
        b_segment_id         : bigint unsigned              # 
        b_split_index        : tinyint unsigned             # 
        c_segment_id         : bigint unsigned              # 
        c_split_index        : tinyint unsigned             # 
        d_segment_id         : bigint unsigned              # 
        d_split_index        : tinyint unsigned             # 
        e_segment_id         : bigint unsigned              # 
        e_split_index        : tinyint unsigned             # 
        f_segment_id         : bigint unsigned              # 
        f_split_index        : tinyint unsigned             # 
        g_segment_id         : bigint unsigned              # 
        g_split_index        : tinyint unsigned             # 
        """
                    
    class Motif8(djp.Part):
        definition = """
        -> master
        ---
        a_segment_id         : bigint unsigned              # 
        a_split_index        : tinyint unsigned             # 
        b_segment_id         : bigint unsigned              # 
        b_split_index        : tinyint unsigned             # 
        c_segment_id         : bigint unsigned              # 
        c_split_index        : tinyint unsigned             # 
        d_segment_id         : bigint unsigned              # 
        d_split_index        : tinyint unsigned             # 
        e_segment_id         : bigint unsigned              # 
        e_split_index        : tinyint unsigned             # 
        f_segment_id         : bigint unsigned              # 
        f_split_index        : tinyint unsigned             # 
        g_segment_id         : bigint unsigned              # 
        g_split_index        : tinyint unsigned             # 
        h_segment_id         : bigint unsigned              # 
        h_split_index        : tinyint unsigned             # 
        """
                    
    class Motif9(djp.Part):
        definition = """
        -> master
        ---
        a_segment_id         : bigint unsigned              # 
        a_split_index        : tinyint unsigned             # 
        b_segment_id         : bigint unsigned              # 
        b_split_index        : tinyint unsigned             # 
        c_segment_id         : bigint unsigned              # 
        c_split_index        : tinyint unsigned             # 
        d_segment_id         : bigint unsigned              # 
        d_split_index        : tinyint unsigned             # 
        e_segment_id         : bigint unsigned              # 
        e_split_index        : tinyint unsigned             # 
        f_segment_id         : bigint unsigned              # 
        f_split_index        : tinyint unsigned             # 
        g_segment_id         : bigint unsigned              # 
        g_split_index        : tinyint unsigned             # 
        h_segment_id         : bigint unsigned              # 
        h_split_index        : tinyint unsigned             # 
        i_segment_id         : bigint unsigned              # 
        i_split_index        : tinyint unsigned             # 
        """
    
    class Motif10(djp.Part):
        definition = """
        -> master
        ---
        a_segment_id         : bigint unsigned              # 
        a_split_index        : tinyint unsigned             # 
        b_segment_id         : bigint unsigned              # 
        b_split_index        : tinyint unsigned             # 
        c_segment_id         : bigint unsigned              # 
        c_split_index        : tinyint unsigned             # 
        d_segment_id         : bigint unsigned              # 
        d_split_index        : tinyint unsigned             # 
        e_segment_id         : bigint unsigned              # 
        e_split_index        : tinyint unsigned             # 
        f_segment_id         : bigint unsigned              # 
        f_split_index        : tinyint unsigned             # 
        g_segment_id         : bigint unsigned              # 
        g_split_index        : tinyint unsigned             # 
        h_segment_id         : bigint unsigned              # 
        h_split_index        : tinyint unsigned             # 
        i_segment_id         : bigint unsigned              # 
        i_split_index        : tinyint unsigned             # 
        j_segment_id         : bigint unsigned              # 
        j_split_index        : tinyint unsigned             # 
        """

@schema
class AutoProofreadNeuronCommonUpstream(djp.Manual):
    definition = """
    segment_id           : bigint unsigned              # 
    split_index          : int unsigned                 # 
    """
            

@schema
class AutoProofreadNeuronAttributeSamplingComp(djp.Manual):
    definition = """
    segment_id           : bigint unsigned              # 
    split_index          : tinyint unsigned             # 
    branch               : varchar(10)                  # 
    """


@schema
class SynapseManualCellsRaw(djp.Manual):
    definition = """
    # Synapses for the cells that were manually proofread but before they were proofread in their raw form
    primary_seg_id       : bigint unsigned              # id of the segment that is synaptically paired to primary_segment_id.
    secondary_seg_id     : bigint unsigned              # id of the segment that is synaptically paired to primary_segment_id.
    synapse_id           : bigint unsigned              # synapse index within the segmentation
    ---
    prepost              : varchar(16)                  # whether the primary_seg_id is "presyn" or "postsyn"
    synapse_x            : int unsigned                 # x coordinate of synapse centroid in EM voxels (x: 4nm, y: 4nm, z: 40nm). From Allen 'ctr_pt_position'.
    synapse_y            : int unsigned                 # y coordinate of centroid in EM voxels (x: 4nm, y: 4nm, z: 40nm). From Allen 'ctr_pt_position'.
    synapse_z            : int unsigned                 # z coordinate of centroid in EM voxels (x: 4nm, y: 4nm, z: 40nm). From Allen 'ctr_pt_position'.
    synapse_size         : int unsigned                 # (EM voxels) scaled by (4x4x40)
    """
                           

@schema
class AutoProofreadNeuronSubgraphVectors(djp.Computed):
    definition = """
    -> AutoProofreadNeuron
    subgraph_idx         : tinyint unsigned             # 
    ---
    compartment=null     : varchar(16)                  # 
    node=null            : varchar(14)                  # 
    endpoint_upstream_x_nm=null : float                        # 
    endpoint_upstream_y_nm=null : float                        # 
    endpoint_upstream_z_nm=null : float                        # 
    endpoint_downstream_x_nm=null : float                        # 
    endpoint_downstream_y_nm=null : float                        # 
    endpoint_downstream_z_nm=null : float                        # 
    soma_vector_x_nm=null : float                        # 
    soma_vector_y_nm=null : float                        # 
    soma_vector_z_nm=null : float                        # 
    skeleton_vector_x_nm=null : float                        # 
    skeleton_vector_y_nm=null : float                        # 
    skeleton_vector_z_nm=null : float                        # 
    width=null           : float                        # 
    skeletal_length=null : float                        # 
    y_soma_relative=null : float                        # 
    scholl_coords=null   : longblob                     # 
    """
          

@schema
class AutoProofreadNeuronSubgraphVectorsCdist(djp.Computed):
    definition = """
    segment_id           : bigint unsigned              # 
    split_index          : int unsigned                 # 
    subgraph_idx         : int unsigned                 # 
    match_segment_id     : bigint unsigned              # 
    match_split_index    : int unsigned                 # 
    match_subgraph_idx   : int unsigned                 # 
    ---
    compartment=null     : varchar(16)                  # 
    node=null            : varchar(14)                  # 
    width=null           : float                        # 
    skeletal_length=null : float                        # 
    y_soma_relative=null : float                        # 
    skeleton_vector_to_top_angle=null : float                        # 
    match_compartment=null : varchar(15)                  # 
    match_node=null      : varchar(14)                  # 
    match_width=null     : float                        # 
    match_skeletal_length=null : float                        # 
    match_y_soma_relative=null : float                        # 
    match_skeleton_vector_to_top_angle=null : float                        # 
    cdist=null           : float                        # 
    n_basal=null         : int unsigned                 # 
    data_type=null       : varchar(21)                  # 
    """


@schema
class AutoProofreadNeuronSubgraphVectorsScholl(djp.Computed):
    definition = """
    segment_id           : bigint unsigned              # 
    split_index          : int unsigned                 # 
    match_segment_id     : bigint unsigned              # 
    match_split_index    : int unsigned                 # 
    match_subgraph_idx   : int unsigned                 # 
    ---
    n_basal=null         : int unsigned                 # 
    data_type=null       : varchar(21)                  # 
    match_compartment=null : varchar(17)                  # 
    match_width=null     : float                        # 
    match_skeletal_length=null : float                        # 
    match_y_soma_relative=null : float                        # 
    match_mean_cdist_10000=null : float                        # 
    match_n_cdist_10000=null : float                        # 
    match_mean_cdist_20000=null : float                        # 
    match_n_cdist_20000=null : float                        # 
    match_mean_cdist_30000=null : float                        # 
    match_n_cdist_30000=null : float                        # 
    match_mean_cdist_40000=null : float                        # 
    match_n_cdist_40000=null : float                        # 
    match_mean_cdist_50000=null : float                        # 
    match_n_cdist_50000=null : float                        # 
    match_mean_cdist_60000=null : float                        # 
    match_n_cdist_60000=null : float                        # 
    match_mean_cdist_70000=null : float                        # 
    match_n_cdist_70000=null : float                        # 
    match_mean_cdist_80000=null : float                        # 
    match_n_cdist_80000=null : float                        # 
    match_mean_cdist_90000=null : float                        # 
    match_n_cdist_90000=null : float                        # 
    match_mean_cdist_100000=null : float                        # 
    match_n_cdist_100000=null : float                        # 
    match_mean_cdist_110000=null : float                        # 
    match_n_cdist_110000=null : float                        # 
    match_mean_cdist_120000=null : float                        # 
    match_n_cdist_120000=null : float                        # 
    match_mean_cdist_130000=null : float                        # 
    match_n_cdist_130000=null : float                        # 
    match_mean_cdist_140000=null : float                        # 
    match_n_cdist_140000=null : float                        # 
    match_mean_cdist_150000=null : float                        # 
    match_n_cdist_150000=null : float                        # 
    """


@schema
class AutoProofreadNeuronSplits(djp.Computed):
    definition = """ 
    segment_id           : bigint unsigned              # 
    split_index          : tinyint unsigned             # 
    cut_id               : int                          # 
    ---
    error_type=null      : varchar(100)                 # 
    filter_cut_id=null   : int unsigned                 # 
    limb_name=null       : varchar(10)                  # 
    skeletal_length=null : double                       # the skeletal length of axon on dendrite
    merge_reason=null    : varchar(30)                  # 
    parent_branch_width=null : double                       # 
    n_error_branches=null : int unsigned                 # 
    n_red_pts_with_syn=null : int unsigned                 # 
    n_blue_pts_with_syn=null : int unsigned                 # 
    link_with_syn=null   : varchar(300)                 # 
    apl_id_with_syn=null : varchar(30)                  # 
    n_red_pts=null       : int unsigned                 # 
    n_blue_pts=null      : int unsigned                 # 
    link=null            : varchar(300)                 # 
    apl_id=null          : varchar(30)                  # 
    run_time=null        : double                       # the amount of time to run (seconds)
    """


@schema
class AutoProofreadNeuronSplitsVp2(djp.Computed):
    definition = """
    segment_id           : bigint unsigned              # 
    split_index          : tinyint unsigned             # 
    cut_id               : int                          # 
    ---
    error_type=null      : varchar(100)                 # 
    filter_cut_id=null   : int unsigned                 # 
    limb_name=null       : varchar(10)                  # 
    skeletal_length=null : double                       # the skeletal length of axon on dendrite
    merge_reason=null    : varchar(30)                  # 
    parent_branch_width=null : double                       # 
    n_error_branches=null : int unsigned                 # 
    merge_coordinate_x_nm=null : float                        # 
    merge_coordinate_y_nm=null : float                        # 
    merge_coordinate_z_nm=null : float                        # 
    n_red_pts_with_syn=null : int unsigned                 # 
    n_blue_pts_with_syn=null : int unsigned                 # 
    link_with_syn=null   : varchar(300)                 # 
    apl_id_with_syn=null : varchar(30)                  # 
    n_red_pts=null       : int unsigned                 # 
    n_blue_pts=null      : int unsigned                 # 
    link=null            : varchar(300)                 # 
    apl_id=null          : varchar(30)                  # 
    run_time=null        : double                       # the amount of time to run (seconds)
    """
          

@schema
class AutoProofreadNeuronSplitsVp3(djp.Computed):
    definition = """
    segment_id           : bigint unsigned              # 
    split_index          : tinyint unsigned             # 
    cut_id               : int                          # 
    ---
    error_type=null      : varchar(100)                 # 
    filter_cut_id=null   : int unsigned                 # 
    limb_name=null       : varchar(10)                  # 
    limb_split_idx=null  : int unsigned                 # 
    skeletal_length=null : double                       # the skeletal length of axon on dendrite
    merge_reason=null    : varchar(30)                  # 
    parent_branch_width=null : double                       # 
    n_error_branches=null : int unsigned                 # 
    merge_coordinate_x_nm=null : float                        # 
    merge_coordinate_y_nm=null : float                        # 
    merge_coordinate_z_nm=null : float                        # 
    n_red_pts_with_syn=null : int unsigned                 # 
    n_blue_pts_with_syn=null : int unsigned                 # 
    link_with_syn=null   : varchar(300)                 # 
    apl_id_with_syn=null : varchar(30)                  # 
    n_red_pts=null       : int unsigned                 # 
    n_blue_pts=null      : int unsigned                 # 
    link=null            : varchar(300)                 # 
    apl_id=null          : varchar(30)                  # 
    run_time=null        : double                       # the amount of time to run (seconds)
    """


@schema
class AutoProofreadNeuronSplitsVp4(djp.Computed):
    definition = """
    segment_id           : bigint unsigned              # 
    split_index          : tinyint unsigned             # 
    cut_id               : int                          # 
    ---
    error_type=null      : varchar(33)                  # 
    filter_cut_id=null   : int unsigned                 # 
    limb_name=null       : varchar(12)                  # 
    limb_split_idx=null  : int unsigned                 # 
    skeletal_length=null : float                        # 
    parent_branch_width=null : float                        # 
    merge_coordinate_x_nm=null : float                        # 
    merge_coordinate_y_nm=null : float                        # 
    merge_coordinate_z_nm=null : float                        # 
    n_error_branches=null : int unsigned                 # 
    blue_points_with_syn=null : longblob                     # 
    red_points_with_syn=null : longblob                     # 
    n_red_pts_with_syn=null : tinyint unsigned             # 
    n_blue_pts_with_syn=null : tinyint unsigned             # 
    red_points=null      : longblob                     # 
    blue_points=null     : longblob                     # 
    n_red_pts=null       : tinyint unsigned             # 
    n_blue_pts=null      : tinyint unsigned             # 
    apl_id=null          : varchar(30)                  # 
    apl_id_with_syn=null : varchar(30)                  # 
    link=null            : varchar(150)                 # 
    link_with_syn=null   : varchar(150)                 # 
    centroid_x_nm=null   : float                        # 
    centroid_y_nm=null   : float                        # 
    centroid_z_nm=null   : float                        # 
    cell_type=null       : varchar(20)                  # 
    nucleus_id=null      : int unsigned                 # 
    gnn_cell_type_fine=null : varchar(12)                  # 
    gnn_cell_type_coarse=null : varchar(20)                  # 
    gnn_cell_type_fine_prob=null : float                        # 
    valid_coordinate_order=null : int unsigned                 # 
    valid_mean_proj_dist=null : float                        # 
    valid_mean_residual=null : float                        # 
    valid_max_shortest_euclid_dist=null : float                        # 
    valid_min_distance_from_coordinate=null : float                        # 
    error_coordinate_order=null : int unsigned                 # 
    error_mean_proj_dist=null : float                        # 
    error_mean_residual=null : float                        # 
    error_max_shortest_euclid_dist=null : float                        # 
    error_min_distance_from_coordinate=null : float                        # 
    distance_from_center=null : float                        # 
    run_time=null        : double                       # the amount of time to run (seconds)
    """
            

@schema
class GnnTrainingLabels(djp.Manual):
    definition = """
    segment_id           : bigint unsigned              # 
    nucleus_id           : bigint unsigned              # 
    table_of_origin      : varchar(50)                  # 
    ---
    cell_type_fine=null  : varchar(10)                  # 
    cell_type_fine_prob=null : double                       # 
    cell_type_coarse=null : enum('excitatory','inhibitory','other') # 
    """


@schema
class GnnTrainingLabels2(djp.Manual):
    definition = """
    segment_id           : bigint unsigned              # 
    nucleus_id           : bigint unsigned              # 
    table_of_origin      : varchar(50)                  # 
    ---
    cell_type_fine=null  : varchar(10)                  # 
    """
            

@schema
class AutoProofreadNeuronLimb(djp.Computed):
    definition = """
    -> GnnTrainingLabels
    split_index          : tinyint unsigned             # 
    limb_idx             : int unsigned                 # 
    ---
    cell_type            : enum('excitatory','inhibitory','other','unknown') # 
    baylor_cell_type_exc_probability : double                       # 
    external_layer=null  : enum('LAYER_1','LAYER_2/3','LAYER_2','LAYER_3','LAYER_4','LAYER_5','LAYER_6','UNCLASSIFIED','WHITE_MATTER') # 
    external_visual_area=null : enum('V1','RL','AL')         # 
    n_branches=null      : int unsigned                 # 
    skeletal_length=null : int unsigned                 # 
    n_spines=null        : int unsigned                 # 
    spine_volume_sum=null : int unsigned                 # 
    n_synapses=null      : int unsigned                 # 
    n_synapses_post=null : int unsigned                 # 
    n_synapses_pre=null  : int unsigned                 # 
    n_synapses_head_postsyn=null : int unsigned                 # 
    n_synapses_neck_postsyn=null : int unsigned                 # 
    n_synapses_no_head_postsyn=null : int unsigned                 # 
    n_synapses_shaft_postsyn=null : int unsigned                 # 
    synapse_volume_shaft_postsyn_sum=null : int unsigned                 # 
    synapse_volume_head_postsyn_sum=null : int unsigned                 # 
    synapse_volume_neck_postsyn_sum=null : int unsigned                 # 
    synapse_volume_no_head_postsyn_sum=null : int unsigned                 # 
    width_no_spine=null  : int unsigned                 # 
    soma_start_angle_max=null : int unsigned                 # 
    soma_start_angle_min=null : int unsigned                 # 
    starting_coordinate_x=null : int unsigned                 # 
    starting_coordinate_y=null : int unsigned                 # 
    starting_coordinate_z=null : int unsigned                 # 
    bbox_x_min=null      : int                          # 
    bbox_y_min=null      : int                          # 
    bbox_z_min=null      : int                          # 
    bbox_x_max=null      : int                          # 
    bbox_y_max=null      : int                          # 
    bbox_z_max=null      : int                          # 
    bbox_x_min_soma_relative=null : int                          # 
    bbox_y_min_soma_relative=null : int                          # 
    bbox_z_min_soma_relative=null : int                          # 
    bbox_x_max_soma_relative=null : int                          # 
    bbox_y_max_soma_relative=null : int                          # 
    bbox_z_max_soma_relative=null : int                          # 
    basal_n_branches=null : int unsigned                 # 
    basal_skeletal_length=null : int unsigned                 # 
    basal_n_spines=null  : int unsigned                 # 
    basal_spine_volume_sum=null : int unsigned                 # 
    basal_n_synapses=null : int unsigned                 # 
    basal_n_synapses_post=null : int unsigned                 # 
    basal_n_synapses_pre=null : int unsigned                 # 
    basal_n_synapses_head_postsyn=null : int unsigned                 # 
    basal_n_synapses_neck_postsyn=null : int unsigned                 # 
    basal_n_synapses_no_head_postsyn=null : int unsigned                 # 
    basal_n_synapses_shaft_postsyn=null : int unsigned                 # 
    basal_synapse_volume_shaft_postsyn_sum=null : int unsigned                 # 
    basal_synapse_volume_head_postsyn_sum=null : int unsigned                 # 
    basal_synapse_volume_neck_postsyn_sum=null : int unsigned                 # 
    basal_synapse_volume_no_head_postsyn_sum=null : int unsigned                 # 
    basal_width_no_spine=null : int unsigned                 # 
    basal_soma_start_angle_max=null : int unsigned                 # 
    basal_soma_start_angle_min=null : int unsigned                 # 
    basal_starting_coordinate_x=null : int unsigned                 # 
    basal_starting_coordinate_y=null : int unsigned                 # 
    basal_starting_coordinate_z=null : int unsigned                 # 
    basal_bbox_x_min=null : int                          # 
    basal_bbox_y_min=null : int                          # 
    basal_bbox_z_min=null : int                          # 
    basal_bbox_x_max=null : int                          # 
    basal_bbox_y_max=null : int                          # 
    basal_bbox_z_max=null : int                          # 
    basal_bbox_x_min_soma_relative=null : int                          # 
    basal_bbox_y_min_soma_relative=null : int                          # 
    basal_bbox_z_min_soma_relative=null : int                          # 
    basal_bbox_x_max_soma_relative=null : int                          # 
    basal_bbox_y_max_soma_relative=null : int                          # 
    basal_bbox_z_max_soma_relative=null : int                          # 
    oblique_n_branches=null : int unsigned                 # 
    oblique_skeletal_length=null : int unsigned                 # 
    oblique_n_spines=null : int unsigned                 # 
    oblique_spine_volume_sum=null : int unsigned                 # 
    oblique_n_synapses=null : int unsigned                 # 
    oblique_n_synapses_post=null : int unsigned                 # 
    oblique_n_synapses_pre=null : int unsigned                 # 
    oblique_n_synapses_head_postsyn=null : int unsigned                 # 
    oblique_n_synapses_neck_postsyn=null : int unsigned                 # 
    oblique_n_synapses_no_head_postsyn=null : int unsigned                 # 
    oblique_n_synapses_shaft_postsyn=null : int unsigned                 # 
    oblique_synapse_volume_shaft_postsyn_sum=null : int unsigned                 # 
    oblique_synapse_volume_head_postsyn_sum=null : int unsigned                 # 
    oblique_synapse_volume_neck_postsyn_sum=null : int unsigned                 # 
    oblique_synapse_volume_no_head_postsyn_sum=null : int unsigned                 # 
    oblique_width_no_spine=null : int unsigned                 # 
    oblique_starting_coordinate_x=null : int unsigned                 # 
    oblique_starting_coordinate_y=null : int unsigned                 # 
    oblique_starting_coordinate_z=null : int unsigned                 # 
    oblique_bbox_x_min=null : int                          # 
    oblique_bbox_y_min=null : int                          # 
    oblique_bbox_z_min=null : int                          # 
    oblique_bbox_x_max=null : int                          # 
    oblique_bbox_y_max=null : int                          # 
    oblique_bbox_z_max=null : int                          # 
    oblique_bbox_x_min_soma_relative=null : int                          # 
    oblique_bbox_y_min_soma_relative=null : int                          # 
    oblique_bbox_z_min_soma_relative=null : int                          # 
    oblique_bbox_x_max_soma_relative=null : int                          # 
    oblique_bbox_y_max_soma_relative=null : int                          # 
    oblique_bbox_z_max_soma_relative=null : int                          # 
    apical_n_branches=null : int unsigned                 # 
    apical_skeletal_length=null : int unsigned                 # 
    apical_n_spines=null : int unsigned                 # 
    apical_spine_volume_sum=null : int unsigned                 # 
    apical_n_synapses=null : int unsigned                 # 
    apical_n_synapses_post=null : int unsigned                 # 
    apical_n_synapses_pre=null : int unsigned                 # 
    apical_n_synapses_head_postsyn=null : int unsigned                 # 
    apical_n_synapses_no_head_postsyn=null : int unsigned                 # 
    apical_n_synapses_shaft_postsyn=null : int unsigned                 # 
    apical_synapse_volume_shaft_postsyn_sum=null : int unsigned                 # 
    apical_synapse_volume_head_postsyn_sum=null : int unsigned                 # 
    apical_synapse_volume_no_head_postsyn_sum=null : int unsigned                 # 
    apical_width_no_spine=null : int unsigned                 # 
    apical_starting_coordinate_x=null : int unsigned                 # 
    apical_starting_coordinate_y=null : int unsigned                 # 
    apical_starting_coordinate_z=null : int unsigned                 # 
    apical_bbox_x_min=null : int                          # 
    apical_bbox_y_min=null : int                          # 
    apical_bbox_z_min=null : int                          # 
    apical_bbox_x_max=null : int                          # 
    apical_bbox_y_max=null : int                          # 
    apical_bbox_z_max=null : int                          # 
    apical_bbox_x_min_soma_relative=null : int                          # 
    apical_bbox_y_min_soma_relative=null : int                          # 
    apical_bbox_z_min_soma_relative=null : int                          # 
    apical_bbox_x_max_soma_relative=null : int                          # 
    apical_bbox_y_max_soma_relative=null : int                          # 
    apical_bbox_z_max_soma_relative=null : int                          # 
    apical_shaft_n_branches=null : int unsigned                 # 
    apical_shaft_skeletal_length=null : int unsigned                 # 
    apical_shaft_n_spines=null : int unsigned                 # 
    apical_shaft_spine_volume_sum=null : int unsigned                 # 
    apical_shaft_n_synapses=null : int unsigned                 # 
    apical_shaft_n_synapses_post=null : int unsigned                 # 
    apical_shaft_n_synapses_pre=null : int unsigned                 # 
    apical_shaft_n_synapses_head_postsyn=null : int unsigned                 # 
    apical_shaft_n_synapses_neck_postsyn=null : int unsigned                 # 
    apical_shaft_n_synapses_no_head_postsyn=null : int unsigned                 # 
    apical_shaft_n_synapses_shaft_postsyn=null : int unsigned                 # 
    apical_shaft_synapse_volume_shaft_postsyn_sum=null : int unsigned                 # 
    apical_shaft_synapse_volume_head_postsyn_sum=null : int unsigned                 # 
    apical_shaft_synapse_volume_neck_postsyn_sum=null : int unsigned                 # 
    apical_shaft_synapse_volume_no_head_postsyn_sum=null : int unsigned                 # 
    apical_shaft_width_no_spine=null : int unsigned                 # 
    apical_shaft_soma_start_angle_max=null : int unsigned                 # 
    apical_shaft_soma_start_angle_min=null : int unsigned                 # 
    apical_shaft_starting_coordinate_x=null : int unsigned                 # 
    apical_shaft_starting_coordinate_y=null : int unsigned                 # 
    apical_shaft_starting_coordinate_z=null : int unsigned                 # 
    apical_shaft_bbox_x_min=null : int                          # 
    apical_shaft_bbox_y_min=null : int                          # 
    apical_shaft_bbox_z_min=null : int                          # 
    apical_shaft_bbox_x_max=null : int                          # 
    apical_shaft_bbox_y_max=null : int                          # 
    apical_shaft_bbox_z_max=null : int                          # 
    apical_shaft_bbox_x_min_soma_relative=null : int                          # 
    apical_shaft_bbox_y_min_soma_relative=null : int                          # 
    apical_shaft_bbox_z_min_soma_relative=null : int                          # 
    apical_shaft_bbox_x_max_soma_relative=null : int                          # 
    apical_shaft_bbox_y_max_soma_relative=null : int                          # 
    apical_shaft_bbox_z_max_soma_relative=null : int                          # 
    apical_tuft_n_branches=null : int unsigned                 # 
    apical_tuft_skeletal_length=null : int unsigned                 # 
    apical_tuft_n_spines=null : int unsigned                 # 
    apical_tuft_spine_volume_sum=null : int unsigned                 # 
    apical_tuft_n_synapses=null : int unsigned                 # 
    apical_tuft_n_synapses_post=null : int unsigned                 # 
    apical_tuft_n_synapses_pre=null : int unsigned                 # 
    apical_tuft_n_synapses_head_postsyn=null : int unsigned                 # 
    apical_tuft_n_synapses_neck_postsyn=null : int unsigned                 # 
    apical_tuft_n_synapses_no_head_postsyn=null : int unsigned                 # 
    apical_tuft_n_synapses_shaft_postsyn=null : int unsigned                 # 
    apical_tuft_synapse_volume_shaft_postsyn_sum=null : int unsigned                 # 
    apical_tuft_synapse_volume_head_postsyn_sum=null : int unsigned                 # 
    apical_tuft_synapse_volume_neck_postsyn_sum=null : int unsigned                 # 
    apical_tuft_synapse_volume_no_head_postsyn_sum=null : int unsigned                 # 
    apical_tuft_width_no_spine=null : int unsigned                 # 
    apical_tuft_soma_start_angle_max=null : int unsigned                 # 
    apical_tuft_soma_start_angle_min=null : int unsigned                 # 
    apical_tuft_starting_coordinate_x=null : int unsigned                 # 
    apical_tuft_starting_coordinate_y=null : int unsigned                 # 
    apical_tuft_starting_coordinate_z=null : int unsigned                 # 
    apical_tuft_bbox_x_min=null : int                          # 
    apical_tuft_bbox_y_min=null : int                          # 
    apical_tuft_bbox_z_min=null : int                          # 
    apical_tuft_bbox_x_max=null : int                          # 
    apical_tuft_bbox_y_max=null : int                          # 
    apical_tuft_bbox_z_max=null : int                          # 
    apical_tuft_bbox_x_min_soma_relative=null : int                          # 
    apical_tuft_bbox_y_min_soma_relative=null : int                          # 
    apical_tuft_bbox_z_min_soma_relative=null : int                          # 
    apical_tuft_bbox_x_max_soma_relative=null : int                          # 
    apical_tuft_bbox_y_max_soma_relative=null : int                          # 
    apical_tuft_bbox_z_max_soma_relative=null : int                          # 
    run_time=null        : double                       # the amount of time to run (seconds)
    """
            
    class Object(djp.Part):
        definition = """
        -> master
        ---
        graph_data=null      : longblob                     # 
        """


@schema
class GnnTrainingData(djp.Computed):
    definition = """
    -> GnnTrainingLabels
    split_index          : tinyint unsigned             # 
    ---
    cell_type_fine=null  : varchar(10)                  # 
    cell_type            : enum('excitatory','inhibitory','other','unknown') # 
    baylor_cell_type_exc_probability : double                       # 
    external_layer=null  : enum('LAYER_1','LAYER_2/3','LAYER_2','LAYER_3','LAYER_4','LAYER_5','LAYER_6','UNCLASSIFIED','WHITE_MATTER') # 
    external_visual_area=null : enum('V1','RL','AL')         # 
    run_time=null        : double                       # the amount of time to run (seconds)
    """
            
    class Object(djp.Part):
        definition = """
        -> master
        ---
        graph_data=null      : longblob                     # 
        """
                    

@schema
class GnnTrainingDataLimb(djp.Computed):
    definition = """
    -> GnnTrainingLabels
    split_index          : tinyint unsigned             # 
    limb_idx             : int unsigned                 # 
    ---
    cell_type_fine=null  : varchar(10)                  # 
    cell_type            : enum('excitatory','inhibitory','other','unknown') # 
    baylor_cell_type_exc_probability : double                       # 
    external_layer=null  : enum('LAYER_1','LAYER_2/3','LAYER_2','LAYER_3','LAYER_4','LAYER_5','LAYER_6','UNCLASSIFIED','WHITE_MATTER') # 
    external_visual_area=null : enum('V1','RL','AL')         # 
    n_branches=null      : int unsigned                 # 
    skeletal_length=null : int unsigned                 # 
    n_spines=null        : int unsigned                 # 
    spine_volume_sum=null : int unsigned                 # 
    n_synapses=null      : int unsigned                 # 
    n_synapses_post=null : int unsigned                 # 
    n_synapses_pre=null  : int unsigned                 # 
    n_synapses_head_postsyn=null : int unsigned                 # 
    n_synapses_neck_postsyn=null : int unsigned                 # 
    n_synapses_no_head_postsyn=null : int unsigned                 # 
    n_synapses_shaft_postsyn=null : int unsigned                 # 
    synapse_volume_shaft_postsyn_sum=null : int unsigned                 # 
    synapse_volume_head_postsyn_sum=null : int unsigned                 # 
    synapse_volume_neck_postsyn_sum=null : int unsigned                 # 
    synapse_volume_no_head_postsyn_sum=null : int unsigned                 # 
    width_no_spine=null  : int unsigned                 # 
    soma_start_angle_max=null : int unsigned                 # 
    soma_start_angle_min=null : int unsigned                 # 
    starting_coordinate_x=null : int unsigned                 # 
    starting_coordinate_y=null : int unsigned                 # 
    starting_coordinate_z=null : int unsigned                 # 
    bbox_x_min=null      : int                          # 
    bbox_y_min=null      : int                          # 
    bbox_z_min=null      : int                          # 
    bbox_x_max=null      : int                          # 
    bbox_y_max=null      : int                          # 
    bbox_z_max=null      : int                          # 
    bbox_x_min_soma_relative=null : int                          # 
    bbox_y_min_soma_relative=null : int                          # 
    bbox_z_min_soma_relative=null : int                          # 
    bbox_x_max_soma_relative=null : int                          # 
    bbox_y_max_soma_relative=null : int                          # 
    bbox_z_max_soma_relative=null : int                          # 
    basal_n_branches=null : int unsigned                 # 
    basal_skeletal_length=null : int unsigned                 # 
    basal_n_spines=null  : int unsigned                 # 
    basal_spine_volume_sum=null : int unsigned                 # 
    basal_n_synapses=null : int unsigned                 # 
    basal_n_synapses_post=null : int unsigned                 # 
    basal_n_synapses_pre=null : int unsigned                 # 
    basal_n_synapses_head_postsyn=null : int unsigned                 # 
    basal_n_synapses_neck_postsyn=null : int unsigned                 # 
    basal_n_synapses_no_head_postsyn=null : int unsigned                 # 
    basal_n_synapses_shaft_postsyn=null : int unsigned                 # 
    basal_synapse_volume_shaft_postsyn_sum=null : int unsigned                 # 
    basal_synapse_volume_head_postsyn_sum=null : int unsigned                 # 
    basal_synapse_volume_neck_postsyn_sum=null : int unsigned                 # 
    basal_synapse_volume_no_head_postsyn_sum=null : int unsigned                 # 
    basal_width_no_spine=null : int unsigned                 # 
    basal_soma_start_angle_max=null : int unsigned                 # 
    basal_soma_start_angle_min=null : int unsigned                 # 
    basal_starting_coordinate_x=null : int unsigned                 # 
    basal_starting_coordinate_y=null : int unsigned                 # 
    basal_starting_coordinate_z=null : int unsigned                 # 
    basal_bbox_x_min=null : int                          # 
    basal_bbox_y_min=null : int                          # 
    basal_bbox_z_min=null : int                          # 
    basal_bbox_x_max=null : int                          # 
    basal_bbox_y_max=null : int                          # 
    basal_bbox_z_max=null : int                          # 
    basal_bbox_x_min_soma_relative=null : int                          # 
    basal_bbox_y_min_soma_relative=null : int                          # 
    basal_bbox_z_min_soma_relative=null : int                          # 
    basal_bbox_x_max_soma_relative=null : int                          # 
    basal_bbox_y_max_soma_relative=null : int                          # 
    basal_bbox_z_max_soma_relative=null : int                          # 
    oblique_n_branches=null : int unsigned                 # 
    oblique_skeletal_length=null : int unsigned                 # 
    oblique_n_spines=null : int unsigned                 # 
    oblique_spine_volume_sum=null : int unsigned                 # 
    oblique_n_synapses=null : int unsigned                 # 
    oblique_n_synapses_post=null : int unsigned                 # 
    oblique_n_synapses_pre=null : int unsigned                 # 
    oblique_n_synapses_head_postsyn=null : int unsigned                 # 
    oblique_n_synapses_neck_postsyn=null : int unsigned                 # 
    oblique_n_synapses_no_head_postsyn=null : int unsigned                 # 
    oblique_n_synapses_shaft_postsyn=null : int unsigned                 # 
    oblique_synapse_volume_shaft_postsyn_sum=null : int unsigned                 # 
    oblique_synapse_volume_head_postsyn_sum=null : int unsigned                 # 
    oblique_synapse_volume_neck_postsyn_sum=null : int unsigned                 # 
    oblique_synapse_volume_no_head_postsyn_sum=null : int unsigned                 # 
    oblique_width_no_spine=null : int unsigned                 # 
    oblique_starting_coordinate_x=null : int unsigned                 # 
    oblique_starting_coordinate_y=null : int unsigned                 # 
    oblique_starting_coordinate_z=null : int unsigned                 # 
    oblique_bbox_x_min=null : int                          # 
    oblique_bbox_y_min=null : int                          # 
    oblique_bbox_z_min=null : int                          # 
    oblique_bbox_x_max=null : int                          # 
    oblique_bbox_y_max=null : int                          # 
    oblique_bbox_z_max=null : int                          # 
    oblique_bbox_x_min_soma_relative=null : int                          # 
    oblique_bbox_y_min_soma_relative=null : int                          # 
    oblique_bbox_z_min_soma_relative=null : int                          # 
    oblique_bbox_x_max_soma_relative=null : int                          # 
    oblique_bbox_y_max_soma_relative=null : int                          # 
    oblique_bbox_z_max_soma_relative=null : int                          # 
    apical_n_branches=null : int unsigned                 # 
    apical_skeletal_length=null : int unsigned                 # 
    apical_n_spines=null : int unsigned                 # 
    apical_spine_volume_sum=null : int unsigned                 # 
    apical_n_synapses=null : int unsigned                 # 
    apical_n_synapses_post=null : int unsigned                 # 
    apical_n_synapses_pre=null : int unsigned                 # 
    apical_n_synapses_head_postsyn=null : int unsigned                 # 
    apical_n_synapses_no_head_postsyn=null : int unsigned                 # 
    apical_n_synapses_shaft_postsyn=null : int unsigned                 # 
    apical_synapse_volume_shaft_postsyn_sum=null : int unsigned                 # 
    apical_synapse_volume_head_postsyn_sum=null : int unsigned                 # 
    apical_synapse_volume_no_head_postsyn_sum=null : int unsigned                 # 
    apical_width_no_spine=null : int unsigned                 # 
    apical_starting_coordinate_x=null : int unsigned                 # 
    apical_starting_coordinate_y=null : int unsigned                 # 
    apical_starting_coordinate_z=null : int unsigned                 # 
    apical_bbox_x_min=null : int                          # 
    apical_bbox_y_min=null : int                          # 
    apical_bbox_z_min=null : int                          # 
    apical_bbox_x_max=null : int                          # 
    apical_bbox_y_max=null : int                          # 
    apical_bbox_z_max=null : int                          # 
    apical_bbox_x_min_soma_relative=null : int                          # 
    apical_bbox_y_min_soma_relative=null : int                          # 
    apical_bbox_z_min_soma_relative=null : int                          # 
    apical_bbox_x_max_soma_relative=null : int                          # 
    apical_bbox_y_max_soma_relative=null : int                          # 
    apical_bbox_z_max_soma_relative=null : int                          # 
    apical_shaft_n_branches=null : int unsigned                 # 
    apical_shaft_skeletal_length=null : int unsigned                 # 
    apical_shaft_n_spines=null : int unsigned                 # 
    apical_shaft_spine_volume_sum=null : int unsigned                 # 
    apical_shaft_n_synapses=null : int unsigned                 # 
    apical_shaft_n_synapses_post=null : int unsigned                 # 
    apical_shaft_n_synapses_pre=null : int unsigned                 # 
    apical_shaft_n_synapses_head_postsyn=null : int unsigned                 # 
    apical_shaft_n_synapses_neck_postsyn=null : int unsigned                 # 
    apical_shaft_n_synapses_no_head_postsyn=null : int unsigned                 # 
    apical_shaft_n_synapses_shaft_postsyn=null : int unsigned                 # 
    apical_shaft_synapse_volume_shaft_postsyn_sum=null : int unsigned                 # 
    apical_shaft_synapse_volume_head_postsyn_sum=null : int unsigned                 # 
    apical_shaft_synapse_volume_neck_postsyn_sum=null : int unsigned                 # 
    apical_shaft_synapse_volume_no_head_postsyn_sum=null : int unsigned                 # 
    apical_shaft_width_no_spine=null : int unsigned                 # 
    apical_shaft_soma_start_angle_max=null : int unsigned                 # 
    apical_shaft_soma_start_angle_min=null : int unsigned                 # 
    apical_shaft_starting_coordinate_x=null : int unsigned                 # 
    apical_shaft_starting_coordinate_y=null : int unsigned                 # 
    apical_shaft_starting_coordinate_z=null : int unsigned                 # 
    apical_shaft_bbox_x_min=null : int                          # 
    apical_shaft_bbox_y_min=null : int                          # 
    apical_shaft_bbox_z_min=null : int                          # 
    apical_shaft_bbox_x_max=null : int                          # 
    apical_shaft_bbox_y_max=null : int                          # 
    apical_shaft_bbox_z_max=null : int                          # 
    apical_shaft_bbox_x_min_soma_relative=null : int                          # 
    apical_shaft_bbox_y_min_soma_relative=null : int                          # 
    apical_shaft_bbox_z_min_soma_relative=null : int                          # 
    apical_shaft_bbox_x_max_soma_relative=null : int                          # 
    apical_shaft_bbox_y_max_soma_relative=null : int                          # 
    apical_shaft_bbox_z_max_soma_relative=null : int                          # 
    apical_tuft_n_branches=null : int unsigned                 # 
    apical_tuft_skeletal_length=null : int unsigned                 # 
    apical_tuft_n_spines=null : int unsigned                 # 
    apical_tuft_spine_volume_sum=null : int unsigned                 # 
    apical_tuft_n_synapses=null : int unsigned                 # 
    apical_tuft_n_synapses_post=null : int unsigned                 # 
    apical_tuft_n_synapses_pre=null : int unsigned                 # 
    apical_tuft_n_synapses_head_postsyn=null : int unsigned                 # 
    apical_tuft_n_synapses_neck_postsyn=null : int unsigned                 # 
    apical_tuft_n_synapses_no_head_postsyn=null : int unsigned                 # 
    apical_tuft_n_synapses_shaft_postsyn=null : int unsigned                 # 
    apical_tuft_synapse_volume_shaft_postsyn_sum=null : int unsigned                 # 
    apical_tuft_synapse_volume_head_postsyn_sum=null : int unsigned                 # 
    apical_tuft_synapse_volume_neck_postsyn_sum=null : int unsigned                 # 
    apical_tuft_synapse_volume_no_head_postsyn_sum=null : int unsigned                 # 
    apical_tuft_width_no_spine=null : int unsigned                 # 
    apical_tuft_soma_start_angle_max=null : int unsigned                 # 
    apical_tuft_soma_start_angle_min=null : int unsigned                 # 
    apical_tuft_starting_coordinate_x=null : int unsigned                 # 
    apical_tuft_starting_coordinate_y=null : int unsigned                 # 
    apical_tuft_starting_coordinate_z=null : int unsigned                 # 
    apical_tuft_bbox_x_min=null : int                          # 
    apical_tuft_bbox_y_min=null : int                          # 
    apical_tuft_bbox_z_min=null : int                          # 
    apical_tuft_bbox_x_max=null : int                          # 
    apical_tuft_bbox_y_max=null : int                          # 
    apical_tuft_bbox_z_max=null : int                          # 
    apical_tuft_bbox_x_min_soma_relative=null : int                          # 
    apical_tuft_bbox_y_min_soma_relative=null : int                          # 
    apical_tuft_bbox_z_min_soma_relative=null : int                          # 
    apical_tuft_bbox_x_max_soma_relative=null : int                          # 
    apical_tuft_bbox_y_max_soma_relative=null : int                          # 
    apical_tuft_bbox_z_max_soma_relative=null : int                          # 
    run_time=null        : double                       # the amount of time to run (seconds)
    """
            
    class Object(djp.Part):
        definition = """
        -> master
        ---
        graph_data=null      : longblob                     # 
        """
            


@schema
class SpineValidation(djp.Manual):
    definition = """
    -> DecompositionCellTypeBranchSample
    spine_idx            : int unsigned                 # 
    user_name            : varchar(30)                  # 
    ---
    classification=null  : varchar(30)                  # enum('positive_yes','positive_yes_refinement','positive_no','positive_multi_spine','positive_unsure','positive_merge_error',false_negative',)
    volume=null          : float                        # 
    skeletal_length=null : float                        # 
    coordinate_x_nm=null : float                        # 
    coordinate_y_nm=null : float                        # 
    coordinate_z_nm=null : float                        # 
    endpoint_dist_min=null : float                        # 
    endpoint_dist_max=null : float                        # 
    n_faces=null         : int unsigned                 # 
    """
                    

@schema
class SynapseErrorsPreDend(djp.Manual):
    definition = """
    -> AutoProofreadNeuron
    synapse_id           : bigint unsigned              # synapse index within the segmentation
    ---
    secondary_seg_id     : bigint unsigned              # segment_id of the cell. Equivalent to Allen 'pt_root_id
    primary_nucleus_id   : int unsigned                 # id of nucleus from the flat segmentation  Equivalent to Allen: 'id'.
    synapse_type         : enum('presyn','postsyn')     # 
    skeletal_distance_to_soma=null : double                       # the length (in um) of skeleton distance from synapse to soma (-2 if on the soma)
    limb_idx=null        : tinyint unsigned             # 
    branch_idx=null      : int unsigned                 # 
    """
            

@schema
class AutoProofreadNeuronReconstruction(djp.Computed):
    definition = """
    -> AutoProofreadNeuron
    ---
    axon_raw_skeleton    : longblob                     # 
    axon_raw_skeleton_skeletal_length : double                       # 
    axon_auto_skeleton   : longblob                     # 
    axon_auto_skeleton_skeletal_length : double                       # 
    axon_diff_skeleton   : longblob                     # 
    axon_diff_skeleton_skeletal_length : double                       # 
    dendrite_raw_skeleton : longblob                     # 
    dendrite_raw_skeleton_skeletal_length : double                       # 
    dendrite_auto_skeleton : longblob                     # 
    dendrite_auto_skeleton_skeletal_length : double                       # 
    dendrite_diff_skeleton : longblob                     # 
    dendrite_diff_skeleton_skeletal_length : double                       # 
    """
            

@schema
class AutoProofreadNeuronEditData(djp.Computed):
    definition = """
    -> AutoProofreadNeuron
    edit_type            : varchar(33)                  # 
    edit_index           : int unsigned                 # 
    ---
    x=null               : float                        # 
    y=null               : float                        # 
    z=null               : float                        # 
    limb_idx=null        : varchar(8)                   # 
    error_branches_skeleton_length=null : float                        # 
    n_error_branches=null : int unsigned                 # 
    parent_branch_width=null : float                        #
    """


@schema
class AutoProofreadNeuronGnn(djp.Computed):
    definition = """
    -> AutoProofreadNeuron
    ---
    nucleus_id           : int unsigned                 # 
    cell_type            : enum('excitatory','inhibitory','other','unknown') # 
    baylor_cell_type_exc_probability : double                       # 
    external_layer=null  : enum('LAYER_1','LAYER_2/3','LAYER_2','LAYER_3','LAYER_4','LAYER_5','LAYER_6','UNCLASSIFIED','WHITE_MATTER') # 
    external_visual_area=null : enum('V1','RL','AL')         # 
    run_time=null        : double                       # the amount of time to run (seconds)
    """
            
    class Object(djp.Part):
        definition = """
        -> master
        ---
        axon_vs_dendrite=null : longblob                     # 
        axon_vs_dendrite_limbs=null : longblob                     # 
        axon_vs_dendrite_limbs_dist_thresh_exc=null : longblob                     # 
        axon_vs_dendrite_limbs_dist_thresh_inh=null : longblob                     # 
        compartment_proof=null : longblob                     # 
        compartment_proof_limbs=null : longblob                     # 
        compartment_proof_limbs_dist_thresh_exc=null : longblob                     # 
        compartment_proof_limbs_dist_thresh_inh=null : longblob                     # 
        merge_errors=null    : longblob                     # 
        merge_errors_limbs=null : longblob                     # 
        merge_errors_limbs_dist_thresh_exc=null : longblob                     # 
        merge_errors_limbs_dist_thresh_inh=null : longblob                     # 
        cell_type_fine=null  : longblob                     # 
        cell_type_fine_limbs=null : longblob                     # 
        cell_type_fine_limbs_dist_thresh_exc=null : longblob                     # 
        cell_type_fine_limbs_dist_thresh_inh=null : longblob                     # 
        morphometrics=null   : longblob                     # 
        """


@schema
class AutoProofreadNeuronCompVectors(djp.Computed):
    definition = """
    -> AutoProofreadNeuron
    ---
    axon_node=null       : varchar(14)                  # 
    axon_endpoint_upstream_x_nm=null : float                        # 
    axon_endpoint_upstream_y_nm=null : float                        # 
    axon_endpoint_upstream_z_nm=null : float                        # 
    axon_endpoint_downstream_x_nm=null : float                        # 
    axon_endpoint_downstream_y_nm=null : float                        # 
    axon_endpoint_downstream_z_nm=null : float                        # 
    axon_soma_vector_x_nm=null : float                        # 
    axon_soma_vector_y_nm=null : float                        # 
    axon_soma_vector_z_nm=null : float                        # 
    axon_skeleton_vector_x_nm=null : float                        # 
    axon_skeleton_vector_y_nm=null : float                        # 
    axon_skeleton_vector_z_nm=null : float                        # 
    axon_width=null      : float                        # 
    axon_n_limbs=null    : int unsigned                 # 
    axon_soma_vector_weighted_x_nm=null : float                        # 
    axon_soma_vector_weighted_y_nm=null : float                        # 
    axon_soma_vector_weighted_z_nm=null : float                        # 
    axon_skeleton_vector_weighted_x_nm=null : float                        # 
    axon_skeleton_vector_weighted_y_nm=null : float                        # 
    axon_skeleton_vector_weighted_z_nm=null : float                        # 
    axon_skeletal_length=null : float                        # 
    apical_node=null     : varchar(15)                  # 
    apical_endpoint_upstream_x_nm=null : float                        # 
    apical_endpoint_upstream_y_nm=null : float                        # 
    apical_endpoint_upstream_z_nm=null : float                        # 
    apical_endpoint_downstream_x_nm=null : float                        # 
    apical_endpoint_downstream_y_nm=null : float                        # 
    apical_endpoint_downstream_z_nm=null : float                        # 
    apical_soma_vector_x_nm=null : float                        # 
    apical_soma_vector_y_nm=null : float                        # 
    apical_soma_vector_z_nm=null : float                        # 
    apical_skeleton_vector_x_nm=null : float                        # 
    apical_skeleton_vector_y_nm=null : float                        # 
    apical_skeleton_vector_z_nm=null : float                        # 
    apical_width=null    : float                        # 
    apical_n_limbs=null  : int unsigned                 # 
    apical_soma_vector_weighted_x_nm=null : float                        # 
    apical_soma_vector_weighted_y_nm=null : float                        # 
    apical_soma_vector_weighted_z_nm=null : float                        # 
    apical_skeleton_vector_weighted_x_nm=null : float                        # 
    apical_skeleton_vector_weighted_y_nm=null : float                        # 
    apical_skeleton_vector_weighted_z_nm=null : float                        # 
    apical_skeletal_length=null : float                        # 
    basal_node=null      : varchar(14)                  # 
    basal_endpoint_upstream_x_nm=null : float                        # 
    basal_endpoint_upstream_y_nm=null : float                        # 
    basal_endpoint_upstream_z_nm=null : float                        # 
    basal_endpoint_downstream_x_nm=null : float                        # 
    basal_endpoint_downstream_y_nm=null : float                        # 
    basal_endpoint_downstream_z_nm=null : float                        # 
    basal_soma_vector_x_nm=null : float                        # 
    basal_soma_vector_y_nm=null : float                        # 
    basal_soma_vector_z_nm=null : float                        # 
    basal_skeleton_vector_x_nm=null : float                        # 
    basal_skeleton_vector_y_nm=null : float                        # 
    basal_skeleton_vector_z_nm=null : float                        # 
    basal_width=null     : float                        # 
    basal_n_limbs=null   : int unsigned                 # 
    basal_soma_vector_weighted_x_nm=null : float                        # 
    basal_soma_vector_weighted_y_nm=null : float                        # 
    basal_soma_vector_weighted_z_nm=null : float                        # 
    basal_skeleton_vector_weighted_x_nm=null : float                        # 
    basal_skeleton_vector_weighted_y_nm=null : float                        # 
    basal_skeleton_vector_weighted_z_nm=null : float                        # 
    basal_skeletal_length=null : float                        # 
    dendrite_node=null   : varchar(15)                  # 
    dendrite_endpoint_upstream_x_nm=null : float                        # 
    dendrite_endpoint_upstream_y_nm=null : float                        # 
    dendrite_endpoint_upstream_z_nm=null : float                        # 
    dendrite_endpoint_downstream_x_nm=null : float                        # 
    dendrite_endpoint_downstream_y_nm=null : float                        # 
    dendrite_endpoint_downstream_z_nm=null : float                        # 
    dendrite_soma_vector_x_nm=null : float                        # 
    dendrite_soma_vector_y_nm=null : float                        # 
    dendrite_soma_vector_z_nm=null : float                        # 
    dendrite_skeleton_vector_x_nm=null : float                        # 
    dendrite_skeleton_vector_y_nm=null : float                        # 
    dendrite_skeleton_vector_z_nm=null : float                        # 
    dendrite_width=null  : float                        # 
    dendrite_n_limbs=null : int unsigned                 # 
    dendrite_soma_vector_weighted_x_nm=null : float                        # 
    dendrite_soma_vector_weighted_y_nm=null : float                        # 
    dendrite_soma_vector_weighted_z_nm=null : float                        # 
    dendrite_skeleton_vector_weighted_x_nm=null : float                        # 
    dendrite_skeleton_vector_weighted_y_nm=null : float                        # 
    dendrite_skeleton_vector_weighted_z_nm=null : float                        # 
    dendrite_skeletal_length=null : float                        # 
    """

         
@schema
class AutoProofreadNeuronBoundingBox(djp.Computed):
    definition = """
    -> AutoProofreadNeuron
    ---
    bbox_x_min           : double                       # 
    bbox_y_min           : double                       # 
    bbox_z_min           : double                       # 
    bbox_x_max           : double                       # 
    bbox_y_max           : double                       # 
    bbox_z_max           : double                       # 
    """


@schema
class AutoProofreadNeuronAttributeSampling(djp.Computed):
    definition = """
    -> AutoProofreadNeuron
    branch               : varchar(10)                  # 
    iteration            : int unsigned                 # 
    ---
    skeletal_distance_to_soma=null : double                       # 
    compartment=null     : enum('axon','oblique','apicalshaft','apicaltuft','apical','basal','dendrite','other') # 
    skeletal_length=null : double                       # 
    width=null           : double                       # 
    n_spine=null         : int unsigned                 # 
    n_synapse=null       : int unsigned                 # 
    spine_intervals_1=null : longblob                     # 
    spine_intervals_2=null : longblob                     # 
    spine_intervals_3=null : longblob                     # 
    spine_upstream_dist=null : longblob                     # 
    synapse_intervals_1=null : longblob                     # 
    synapse_intervals_2=null : longblob                     # 
    synapse_intervals_3=null : longblob                     # 
    synapse_upstream_dist=null : longblob                     # 
    mesh_volume=null     : double                       # 
    n_synapses_head=null : int unsigned                 # 
    n_synapses_neck=null : int unsigned                 # 
    n_synapses_no_head=null : int unsigned                 # 
    n_synapses_post=null : int unsigned                 # 
    n_synapses_pre=null  : int unsigned                 # 
    n_synapses_shaft=null : int unsigned                 # 
    n_synapses_spine=null : int unsigned                 # 
    total_spine_volume=null : double                       # 
    soma_distance_euclidean=null : double                       # 
    parent_skeletal_angle=null : double                       # 
    siblings_skeletal_angle_max=null : double                       # 
    width_upstream=null  : double                       # 
    width_downstream=null : double                       # 
    run_time=null        : double                       # the amount of time to run (seconds)
    """
            

@schema
class AutoProofreadNeuronAttributeIntervals(djp.Computed):
    definition = """
    -> AutoProofreadNeuron
    branch               : varchar(10)                  # 
    ---
    skeletal_distance_to_soma=null : double                       # 
    compartment=null     : enum('axon','oblique','apicalshaft','apicaltuft','apical','basal','dendrite','other') # 
    skeletal_length=null : double                       # 
    width=null           : double                       # 
    n_spine=null         : int unsigned                 # 
    n_synapse=null       : int unsigned                 # 
    spine_intervals_1=null : longblob                     # 
    spine_intervals_2=null : longblob                     # 
    spine_intervals_3=null : longblob                     # 
    spine_upstream_dist=null : longblob                     # 
    synapse_intervals_1=null : longblob                     # 
    synapse_intervals_2=null : longblob                     # 
    synapse_intervals_3=null : longblob                     # 
    synapse_upstream_dist=null : longblob                     # 
    mesh_volume=null     : double                       # 
    n_synapses_head=null : int unsigned                 # 
    n_synapses_neck=null : int unsigned                 # 
    n_synapses_no_head=null : int unsigned                 # 
    n_synapses_post=null : int unsigned                 # 
    n_synapses_pre=null  : int unsigned                 # 
    n_synapses_shaft=null : int unsigned                 # 
    n_synapses_spine=null : int unsigned                 # 
    total_spine_volume=null : double                       # 
    soma_distance_euclidean=null : double                       # 
    parent_skeletal_angle=null : double                       # 
    siblings_skeletal_angle_max=null : double                       # 
    width_upstream=null  : double                       # 
    width_downstream=null : double                       # 
    run_time=null        : double                       # the amount of time to run (seconds)
    """


@schema
class AutoProofreadNeuronOffshoot(djp.Computed):
    definition = """
    -> AutoProofreadNeuron
    subgraph_idx         : tinyint unsigned             # 
    ---
    compartment=null     : varchar(14)                  # 
    node=null            : varchar(15)                  # 
    endpoint_upstream_x_nm=null : float                        # 
    endpoint_upstream_y_nm=null : float                        # 
    endpoint_upstream_z_nm=null : float                        # 
    endpoint_downstream_x_nm=null : float                        # 
    endpoint_downstream_y_nm=null : float                        # 
    endpoint_downstream_z_nm=null : float                        # 
    skeleton_vector_x_nm=null : float                        # 
    skeleton_vector_y_nm=null : float                        # 
    skeleton_vector_z_nm=null : float                        # 
    width=null           : float                        # 
    soma_vector_x_nm=null : float                        # 
    soma_vector_y_nm=null : float                        # 
    soma_vector_z_nm=null : float                        # 
    skeletal_length=null : float                        # 
    y_soma_relative=null : float                        # 
    n_nodes=null         : int unsigned                 # 
    n_leaf_nodes=null    : int unsigned                 # 
    scholl_coords=null   : blob                         # 
    n_scholl_10000=null  : tinyint unsigned             # 
    n_scholl_20000=null  : tinyint unsigned             # 
    n_scholl_30000=null  : tinyint unsigned             # 
    n_scholl_40000=null  : tinyint unsigned             # 
    n_scholl_50000=null  : tinyint unsigned             # 
    n_scholl_60000=null  : tinyint unsigned             # 
    n_scholl_70000=null  : tinyint unsigned             # 
    n_scholl_80000=null  : tinyint unsigned             # 
    n_scholl_90000=null  : tinyint unsigned             # 
    n_scholl_100000=null : tinyint unsigned             # 
    n_scholl_110000=null : tinyint unsigned             # 
    n_scholl_120000=null : tinyint unsigned             # 
    n_scholl_130000=null : tinyint unsigned             # 
    n_scholl_140000=null : tinyint unsigned             # 
    n_scholl_150000=null : tinyint unsigned             # 
    scholl_coords_adjusted=null : blob                         # 
    n_scholl_adjusted_10000=null : tinyint unsigned             # 
    n_scholl_adjusted_20000=null : tinyint unsigned             # 
    n_scholl_adjusted_30000=null : tinyint unsigned             # 
    n_scholl_adjusted_40000=null : tinyint unsigned             # 
    n_scholl_adjusted_50000=null : tinyint unsigned             # 
    n_scholl_adjusted_60000=null : tinyint unsigned             # 
    n_scholl_adjusted_70000=null : tinyint unsigned             # 
    n_scholl_adjusted_80000=null : tinyint unsigned             # 
    n_scholl_adjusted_90000=null : tinyint unsigned             # 
    n_scholl_adjusted_100000=null : tinyint unsigned             # 
    n_scholl_adjusted_110000=null : tinyint unsigned             # 
    n_scholl_adjusted_120000=null : tinyint unsigned             # 
    n_scholl_adjusted_130000=null : tinyint unsigned             # 
    n_scholl_adjusted_140000=null : tinyint unsigned             # 
    n_scholl_adjusted_150000=null : tinyint unsigned             # 
    n_internal_branching=null : int unsigned                 # 
    internal_branch_coordinate_max_x_nm=null : float                        # 
    internal_branch_coordinate_max_y_nm=null : float                        # 
    internal_branch_coordinate_max_z_nm=null : float                        # 
    internal_branch_coordinate_min_x_nm=null : float                        # 
    internal_branch_coordinate_min_y_nm=null : float                        # 
    internal_branch_coordinate_min_z_nm=null : float                        # 
    internal_branch_coordinate_max_dist_nm=null : float                        # 
    internal_branch_coordinate_min_dist_nm=null : float                        # 
    bbox_min_x_nm=null   : float                        # 
    bbox_min_y_nm=null   : float                        # 
    bbox_min_z_nm=null   : float                        # 
    bbox_max_x_nm=null   : float                        # 
    bbox_max_y_nm=null   : float                        # 
    bbox_max_z_nm=null   : float                        # 
    """
            
    class Leaf(djp.Part):
        definition = """
        -> master
        leaf_node_idx        : int unsigned                 # 
        ---
        leaf_node=null       : varchar(14)                  # 
        leaf_node_coordinate_x_nm=null : float                        # 
        leaf_node_coordinate_y_nm=null : float                        # 
        leaf_node_coordinate_z_nm=null : float                        # 
        leaf_node_dist=null  : float                        # 
        skeletal_length=null : float                        # 
        scholl_coords=null   : blob                         # 
        n_scholl_10000=null  : tinyint unsigned             # 
        n_scholl_20000=null  : tinyint unsigned             # 
        n_scholl_30000=null  : tinyint unsigned             # 
        n_scholl_40000=null  : tinyint unsigned             # 
        n_scholl_50000=null  : tinyint unsigned             # 
        n_scholl_60000=null  : tinyint unsigned             # 
        n_scholl_70000=null  : tinyint unsigned             # 
        n_scholl_80000=null  : tinyint unsigned             # 
        n_scholl_90000=null  : tinyint unsigned             # 
        n_scholl_100000=null : tinyint unsigned             # 
        n_scholl_110000=null : tinyint unsigned             # 
        n_scholl_120000=null : tinyint unsigned             # 
        n_scholl_130000=null : tinyint unsigned             # 
        n_scholl_140000=null : tinyint unsigned             # 
        n_scholl_150000=null : tinyint unsigned             # 
        scholl_coords_adjusted=null : blob                         # 
        n_scholl_adjusted_10000=null : tinyint unsigned             # 
        n_scholl_adjusted_20000=null : tinyint unsigned             # 
        n_scholl_adjusted_30000=null : tinyint unsigned             # 
        n_scholl_adjusted_40000=null : tinyint unsigned             # 
        n_scholl_adjusted_50000=null : tinyint unsigned             # 
        n_scholl_adjusted_60000=null : tinyint unsigned             # 
        n_scholl_adjusted_70000=null : tinyint unsigned             # 
        n_scholl_adjusted_80000=null : tinyint unsigned             # 
        n_scholl_adjusted_90000=null : tinyint unsigned             # 
        n_scholl_adjusted_100000=null : tinyint unsigned             # 
        n_scholl_adjusted_110000=null : tinyint unsigned             # 
        n_scholl_adjusted_120000=null : tinyint unsigned             # 
        n_scholl_adjusted_130000=null : tinyint unsigned             # 
        n_scholl_adjusted_140000=null : tinyint unsigned             # 
        n_scholl_adjusted_150000=null : tinyint unsigned             # 
        n_internal_branching=null : int unsigned                 # 
        internal_branch_coordinate_max_x_nm=null : float                        # 
        internal_branch_coordinate_max_y_nm=null : float                        # 
        internal_branch_coordinate_max_z_nm=null : float                        # 
        internal_branch_coordinate_min_x_nm=null : float                        # 
        internal_branch_coordinate_min_y_nm=null : float                        # 
        internal_branch_coordinate_min_z_nm=null : float                        # 
        internal_branch_coordinate_max_dist_nm=null : float                        # 
        internal_branch_coordinate_min_dist_nm=null : float                        # 
        bbox_min_x_nm=null   : float                        # 
        bbox_min_y_nm=null   : float                        # 
        bbox_min_z_nm=null   : float                        # 
        bbox_max_x_nm=null   : float                        # 
        bbox_max_y_nm=null   : float                        # 
        bbox_max_z_nm=null   : float                        # 
        """
                    

@schema
class AutoProofreadNeuronMorphopy(djp.Computed):
    definition = """
    -> AutoProofreadNeuron
    ---
    nucleus_id           : int unsigned                 # 
    cell_type            : enum('excitatory','inhibitory','other','unknown') # 
    baylor_cell_type_exc_probability : double                       # 
    external_layer=null  : enum('LAYER_1','LAYER_2/3','LAYER_2','LAYER_3','LAYER_4','LAYER_5','LAYER_6','UNCLASSIFIED','WHITE_MATTER') # 
    external_visual_area=null : enum('V1','RL','AL')         # 
    run_time=null        : double                       # the amount of time to run (seconds)
    """
            
    class Object(djp.Part):
        definition = """
        -> master
        ---
        morphometrics=null   : longblob                     # 
        """


@schema
class CompartmentValidation(djp.Manual):
    definition = """
    -> AutoProofreadNeuron
    user_name            : varchar(30)                  # 
    ---
    apical_proof_apical=null : double                       # 
    apical_proof_apical_shaft=null : double                       # 
    apical_proof_apical_tuft=null : double                       # 
    apical_proof_basal=null : double                       # 
    apical_proof_axon=null : double                       # 
    apical_proof_oblique=null : double                       # 
    apical_proof_dendrite=null : double                       # 
    apical_proof_apical_total=null : double                       # 
    apical_proof_merge=null : double                       # 
    apical_proof_unsure=null : double                       # 
    apical_shaft_proof_apical=null : double                       # 
    apical_shaft_proof_apical_shaft=null : double                       # 
    apical_shaft_proof_apical_tuft=null : double                       # 
    apical_shaft_proof_basal=null : double                       # 
    apical_shaft_proof_axon=null : double                       # 
    apical_shaft_proof_oblique=null : double                       # 
    apical_shaft_proof_dendrite=null : double                       # 
    apical_shaft_proof_apical_total=null : double                       # 
    apical_shaft_proof_merge=null : double                       # 
    apical_shaft_proof_unsure=null : double                       # 
    apical_tuft_proof_apical=null : double                       # 
    apical_tuft_proof_apical_shaft=null : double                       # 
    apical_tuft_proof_apical_tuft=null : double                       # 
    apical_tuft_proof_basal=null : double                       # 
    apical_tuft_proof_axon=null : double                       # 
    apical_tuft_proof_oblique=null : double                       # 
    apical_tuft_proof_dendrite=null : double                       # 
    apical_tuft_proof_apical_total=null : double                       # 
    apical_tuft_proof_merge=null : double                       # 
    apical_tuft_proof_unsure=null : double                       # 
    basal_proof_apical=null : double                       # 
    basal_proof_apical_shaft=null : double                       # 
    basal_proof_apical_tuft=null : double                       # 
    basal_proof_basal=null : double                       # 
    basal_proof_axon=null : double                       # 
    basal_proof_oblique=null : double                       # 
    basal_proof_dendrite=null : double                       # 
    basal_proof_apical_total=null : double                       # 
    basal_proof_merge=null : double                       # 
    basal_proof_unsure=null : double                       # 
    axon_proof_apical=null : double                       # 
    axon_proof_apical_shaft=null : double                       # 
    axon_proof_apical_tuft=null : double                       # 
    axon_proof_basal=null : double                       # 
    axon_proof_axon=null : double                       # 
    axon_proof_oblique=null : double                       # 
    axon_proof_dendrite=null : double                       # 
    axon_proof_apical_total=null : double                       # 
    axon_proof_merge=null : double                       # 
    axon_proof_unsure=null : double                       # 
    oblique_proof_apical=null : double                       # 
    oblique_proof_apical_shaft=null : double                       # 
    oblique_proof_apical_tuft=null : double                       # 
    oblique_proof_basal=null : double                       # 
    oblique_proof_axon=null : double                       # 
    oblique_proof_oblique=null : double                       # 
    oblique_proof_dendrite=null : double                       # 
    oblique_proof_apical_total=null : double                       # 
    oblique_proof_merge=null : double                       # 
    oblique_proof_unsure=null : double                       # 
    dendrite_proof_apical=null : double                       # 
    dendrite_proof_apical_shaft=null : double                       # 
    dendrite_proof_apical_tuft=null : double                       # 
    dendrite_proof_basal=null : double                       # 
    dendrite_proof_axon=null : double                       # 
    dendrite_proof_oblique=null : double                       # 
    dendrite_proof_dendrite=null : double                       # 
    dendrite_proof_apical_total=null : double                       # 
    dendrite_proof_merge=null : double                       # 
    dendrite_proof_unsure=null : double                       # 
    apical_total_proof_apical=null : double                       # 
    apical_total_proof_apical_shaft=null : double                       # 
    apical_total_proof_apical_tuft=null : double                       # 
    apical_total_proof_basal=null : double                       # 
    apical_total_proof_axon=null : double                       # 
    apical_total_proof_oblique=null : double                       # 
    apical_total_proof_dendrite=null : double                       # 
    apical_total_proof_apical_total=null : double                       # 
    apical_total_proof_merge=null : double                       # 
    apical_total_proof_unsure=null : double                       # 
    """
            
    class EdgeLabels(djp.Part):
        definition = """
        -> master
        ---
        edge_labels=null     : mediumblob                   # 
        """



@schema
class AutoProofreadNeuronValidationValidation(djp.Computed):
    definition = """
    -> DecompositionCellType
    -> AutoProofreadNeuronMethod
    ---
    multiplicity         : tinyint unsigned             # the total number of neurons that came from the parent segment id
    cell_type_used=null  : enum('external','baylor')    # 
    cell_type=null       : enum('excitatory','inhibitory','other','unknown') # 
    nucleus_id           : int unsigned                 # id of nucleus from the flat segmentation  Equivalent to Allen: 'id'.
    nuclei_distance      : double                       # the distance to the closest nuclei (even if no matching nuclei found)
    n_nuclei_in_radius   : tinyint unsigned             # the number of nuclei within the search radius of 15000 belonging to that segment
    n_nuclei_in_bbox     : tinyint unsigned             # the number of nuclei within the bounding box of that soma
    centroid_x=null      : int unsigned                 # (EM voxels)
    centroid_y=null      : int unsigned                 # (EM voxels)
    centroid_z=null      : int unsigned                 # (EM voxels)
    centroid_x_nm=null   : double                       # nm x coordinate of soma
    centroid_y_nm=null   : double                       # nm y coordinate of soma
    centroid_z_nm=null   : double                       # nm z coordinate of soma
    centroid_volume      : double                       # 
    max_soma_n_faces     : int unsigned                 # The largest number of faces of the somas
    max_soma_volume      : int unsigned                 # The largest volume of the somas the (volume in billions (10*9 nm^3))
    max_soma_area        : int unsigned                 # The largest surface area of the somas  (area in um)
    syn_density_post_after_proof : double                       # 
    syn_density_head_after_proof : double                       # 
    syn_density_neck_after_proof : double                       # 
    syn_density_shaft_after_proof : double                       # 
    skeletal_length_processed_syn_after_proof : double                       # 
    spine_density_after_proof : double                       # 
    skeletal_length_processed_spine_after_proof : double                       # 
    baylor_cell_type_after_proof=null : enum('excitatory','inhibitory','other','unknown') # 
    baylor_cell_type_exc_probability_after_proof=null : double                       # 
    baylor_cell_type=null : enum('excitatory','inhibitory','other','unknown') # 
    baylor_cell_type_exc_probability=null : double                       # 
    external_cell_type=null : enum('excitatory','inhibitory','other','unknown') # 
    cell_type_used_for_axon=null : enum('external','baylor')    # 
    cell_type_for_axon=null : enum('excitatory','inhibitory','other','unknown') # 
    external_cell_type_n_nuc=null : tinyint unsigned             # 
    external_cell_type_fine=null : varchar(256)                 # 
    external_layer=null  : enum('LAYER_1','LAYER_2/3','LAYER_2','LAYER_3','LAYER_4','LAYER_5','LAYER_6','UNCLASSIFIED','WHITE_MATTER') # 
    external_visual_area=null : enum('V1','RL','AL')         # 
    axon_angle_max=null  : double                       # 
    axon_angle_min=null  : double                       # 
    n_axon_angles        : tinyint unsigned             # 
    axon_start_distance_from_soma=null : double                       # 
    n_vertices           : int unsigned                 # number of vertices
    n_faces              : int unsigned                 # number of faces
    n_limbs              : int                          # 
    n_branches           : int                          # 
    max_limb_n_branches=null : int                          # 
    skeletal_length=null : double                       # 
    max_limb_skeletal_length=null : double                       # 
    median_branch_length=null : double                       # gives information on average skeletal length to next branch point
    width_median=null    : double                       # median width from mesh center without spines removed
    width_no_spine_median=null : double                       # median width from mesh center with spines removed
    width_90_perc=null   : double                       # 90th percentile for width without spines removed
    width_no_spine_90_perc=null : double                       # 90th percentile for width with spines removed
    n_spines             : bigint                       # 
    n_boutons            : bigint                       # 
    spines_per_branch=null : double                       # 
    skeletal_length_eligible=null : double                       # the skeletal length for all branches searched for spines
    n_spine_eligible_branches=null : int                          # the number of branches that were checked for spines because passed width threshold
    spine_density_eligible=null : double                       # n_spines/skeletal_length_eligible
    spines_per_branch_eligible=null : double                       # n_spines/n_spine_eligible_branches
    total_spine_volume=null : double                       # the sum of all spine volume
    spine_volume_median=null : double                       # median of the spine volume for those spines with able to calculate volume
    spine_volume_density=null : double                       # total_spine_volume/skeletal_length
    spine_volume_density_eligible=null : double                       # total_spine_volume/skeletal_length_eligible
    spine_volume_per_branch_eligible=null : double                       # total_spine_volume/n_spine_eligible_branches
    dendrite_skeletal_length : int unsigned                 # 
    dendrite_area        : int unsigned                 # 
    dendrite_mesh_volume : int unsigned                 # 
    dendrite_n_branches  : int unsigned                 # 
    axon_skeletal_length : int unsigned                 # 
    axon_area            : int unsigned                 # 
    axon_mesh_volume     : int unsigned                 # 
    axon_n_branches      : int unsigned                 # 
    basal_skeletal_length : int unsigned                 # 
    basal_area           : int unsigned                 # 
    basal_mesh_volume    : int unsigned                 # 
    basal_n_branches     : int unsigned                 # 
    apical_skeletal_length : int unsigned                 # 
    apical_area          : int unsigned                 # 
    apical_mesh_volume   : int unsigned                 # 
    apical_n_branches    : int unsigned                 # 
    apical_tuft_skeletal_length : int unsigned                 # 
    apical_tuft_area     : int unsigned                 # 
    apical_tuft_mesh_volume : int unsigned                 # 
    apical_tuft_n_branches : int unsigned                 # 
    apical_shaft_skeletal_length : int unsigned                 # 
    apical_shaft_area    : int unsigned                 # 
    apical_shaft_mesh_volume : int unsigned                 # 
    apical_shaft_n_branches : int unsigned                 # 
    oblique_skeletal_length : int unsigned                 # 
    oblique_area         : int unsigned                 # 
    oblique_mesh_volume  : int unsigned                 # 
    oblique_n_branches   : int unsigned                 # 
    apical_total_skeletal_length : int unsigned                 # 
    apical_total_area    : int unsigned                 # 
    apical_total_mesh_volume : int unsigned                 # 
    apical_total_n_branches : int unsigned                 # 
    n_syn_valid          : int unsigned                 # 
    n_syn_valid_pre      : int unsigned                 # 
    n_syn_valid_post     : int unsigned                 # 
    n_syn_error          : int unsigned                 # 
    n_syn_error_pre      : int unsigned                 # 
    n_syn_error_post     : int unsigned                 # 
    n_syn_presyns_on_dendrite : int unsigned                 # 
    n_syn_mesh_errored   : int unsigned                 # 
    n_syn_distance_errored : int unsigned                 # 
    n_syn_no_label       : int unsigned                 # 
    n_syn_head           : int unsigned                 # 
    n_syn_neck           : int unsigned                 # 
    n_syn_shaft          : int unsigned                 # 
    n_syn_no_head        : int unsigned                 # 
    n_syn_bouton         : int unsigned                 # 
    n_syn_non_bouton     : int unsigned                 # 
    n_syn_dendrite       : int unsigned                 # 
    n_syn_axon           : int unsigned                 # 
    n_syn_basal          : int unsigned                 # 
    n_syn_apical         : int unsigned                 # 
    n_syn_apical_tuft    : int unsigned                 # 
    n_syn_apical_shaft   : int unsigned                 # 
    n_syn_oblique        : int unsigned                 # 
    n_syn_soma           : int unsigned                 # 
    n_syn_apical_total   : int unsigned                 # 
    n_syn_dendrite_head_postsyn : int unsigned                 # 
    n_syn_dendrite_neck_postsyn : int unsigned                 # 
    n_syn_dendrite_shaft_postsyn : int unsigned                 # 
    n_syn_dendrite_no_head_postsyn : int unsigned                 # 
    n_syn_axon_bouton_presyn : int unsigned                 # 
    n_syn_axon_bouton_postsyn : int unsigned                 # 
    n_syn_axon_non_bouton_presyn : int unsigned                 # 
    n_syn_axon_non_bouton_postsyn : int unsigned                 # 
    n_syn_basal_head_postsyn : int unsigned                 # 
    n_syn_basal_neck_postsyn : int unsigned                 # 
    n_syn_basal_shaft_postsyn : int unsigned                 # 
    n_syn_basal_no_head_postsyn : int unsigned                 # 
    n_syn_apical_head_postsyn : int unsigned                 # 
    n_syn_apical_neck_postsyn : int unsigned                 # 
    n_syn_apical_shaft_postsyn : int unsigned                 # 
    n_syn_apical_no_head_postsyn : int unsigned                 # 
    n_syn_apical_tuft_head_postsyn : int unsigned                 # 
    n_syn_apical_tuft_neck_postsyn : int unsigned                 # 
    n_syn_apical_tuft_shaft_postsyn : int unsigned                 # 
    n_syn_apical_tuft_no_head_postsyn : int unsigned                 # 
    n_syn_apical_shaft_head_postsyn : int unsigned                 # 
    n_syn_apical_shaft_neck_postsyn : int unsigned                 # 
    n_syn_apical_shaft_shaft_postsyn : int unsigned                 # 
    n_syn_apical_shaft_no_head_postsyn : int unsigned                 # 
    n_syn_oblique_head_postsyn : int unsigned                 # 
    n_syn_oblique_neck_postsyn : int unsigned                 # 
    n_syn_oblique_shaft_postsyn : int unsigned                 # 
    n_syn_oblique_no_head_postsyn : int unsigned                 # 
    n_syn_soma_no_label_presyn : int unsigned                 # 
    n_syn_soma_no_label_postsyn : int unsigned                 # 
    n_syn_apical_total_head_presyn : int unsigned                 # 
    n_syn_apical_total_head_postsyn : int unsigned                 # 
    n_syn_apical_total_neck_presyn : int unsigned                 # 
    n_syn_apical_total_neck_postsyn : int unsigned                 # 
    n_syn_apical_total_shaft_presyn : int unsigned                 # 
    n_syn_apical_total_shaft_postsyn : int unsigned                 # 
    n_syn_apical_total_no_head_presyn : int unsigned                 # 
    n_syn_apical_total_no_head_postsyn : int unsigned                 # 
    n_syn_axon_ais_postsyn=null : int unsigned                 # 
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
    axon_n_limbs=null    : int unsigned                 # 
    axon_soma_angle_max=null : double                       # 
    axon_soma_angle_min=null : double                       # 
    apical_branch_length_median=null : double                       # 
    apical_branch_length_mean=null : double                       # 
    apical_n_short_branches=null : int unsigned                 # 
    apical_n_long_branches=null : int unsigned                 # 
    apical_n_medium_branches=null : int unsigned                 # 
    apical_bbox_volume=null : double                       # 
    apical_bbox_x_min=null : double                       # 
    apical_bbox_y_min=null : double                       # 
    apical_bbox_z_min=null : double                       # 
    apical_bbox_x_max=null : double                       # 
    apical_bbox_y_max=null : double                       # 
    apical_bbox_z_max=null : double                       # 
    apical_bbox_x_min_soma_relative=null : double                       # 
    apical_bbox_y_min_soma_relative=null : double                       # 
    apical_bbox_z_min_soma_relative=null : double                       # 
    apical_bbox_x_max_soma_relative=null : double                       # 
    apical_bbox_y_max_soma_relative=null : double                       # 
    apical_bbox_z_max_soma_relative=null : double                       # 
    apical_n_limbs=null  : int unsigned                 # 
    apical_soma_angle_max=null : double                       # 
    apical_soma_angle_min=null : double                       # 
    basal_branch_length_median=null : double                       # 
    basal_branch_length_mean=null : double                       # 
    basal_n_short_branches=null : int unsigned                 # 
    basal_n_long_branches=null : int unsigned                 # 
    basal_n_medium_branches=null : int unsigned                 # 
    basal_bbox_volume=null : double                       # 
    basal_bbox_x_min=null : double                       # 
    basal_bbox_y_min=null : double                       # 
    basal_bbox_z_min=null : double                       # 
    basal_bbox_x_max=null : double                       # 
    basal_bbox_y_max=null : double                       # 
    basal_bbox_z_max=null : double                       # 
    basal_bbox_x_min_soma_relative=null : double                       # 
    basal_bbox_y_min_soma_relative=null : double                       # 
    basal_bbox_z_min_soma_relative=null : double                       # 
    basal_bbox_x_max_soma_relative=null : double                       # 
    basal_bbox_y_max_soma_relative=null : double                       # 
    basal_bbox_z_max_soma_relative=null : double                       # 
    basal_n_limbs=null   : int unsigned                 # 
    basal_soma_angle_max=null : double                       # 
    basal_soma_angle_min=null : double                       # 
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
    dendrite_n_limbs=null : int unsigned                 # 
    dendrite_soma_angle_max=null : double                       # 
    dendrite_soma_angle_min=null : double                       # 
    run_time=null        : double                       # the amount of time to run (seconds)
    """
            

@schema
class AutoProofreadNeuronVal(djp.Computed):
    definition = """
    -> DecompositionCellType
    -> AutoProofreadNeuronMethod
    ---
    multiplicity         : tinyint unsigned             # the total number of neurons that came from the parent segment id
    cell_type_used=null  : enum('external','baylor')    # 
    cell_type=null       : enum('excitatory','inhibitory','other','unknown') # 
    nucleus_id           : int unsigned                 # id of nucleus from the flat segmentation  Equivalent to Allen: 'id'.
    nuclei_distance      : double                       # the distance to the closest nuclei (even if no matching nuclei found)
    n_nuclei_in_radius   : tinyint unsigned             # the number of nuclei within the search radius of 15000 belonging to that segment
    n_nuclei_in_bbox     : tinyint unsigned             # the number of nuclei within the bounding box of that soma
    centroid_x=null      : int unsigned                 # (EM voxels)
    centroid_y=null      : int unsigned                 # (EM voxels)
    centroid_z=null      : int unsigned                 # (EM voxels)
    centroid_x_nm=null   : double                       # nm x coordinate of soma
    centroid_y_nm=null   : double                       # nm y coordinate of soma
    centroid_z_nm=null   : double                       # nm z coordinate of soma
    centroid_volume      : double                       # 
    max_soma_n_faces     : int unsigned                 # The largest number of faces of the somas
    max_soma_volume      : int unsigned                 # The largest volume of the somas the (volume in billions (10*9 nm^3))
    max_soma_area        : int unsigned                 # The largest surface area of the somas  (area in um)
    syn_density_post_after_proof : double                       # 
    syn_density_head_after_proof : double                       # 
    syn_density_neck_after_proof : double                       # 
    syn_density_shaft_after_proof : double                       # 
    skeletal_length_processed_syn_after_proof : double                       # 
    spine_density_after_proof : double                       # 
    skeletal_length_processed_spine_after_proof : double                       # 
    baylor_cell_type_after_proof=null : enum('excitatory','inhibitory','other','unknown') # 
    baylor_cell_type_exc_probability_after_proof=null : double                       # 
    baylor_cell_type=null : enum('excitatory','inhibitory','other','unknown') # 
    baylor_cell_type_exc_probability=null : double                       # 
    external_cell_type=null : enum('excitatory','inhibitory','other','unknown') # 
    cell_type_used_for_axon=null : enum('external','baylor')    # 
    cell_type_for_axon=null : enum('excitatory','inhibitory','other','unknown') # 
    external_cell_type_n_nuc=null : tinyint unsigned             # 
    external_cell_type_fine=null : varchar(256)                 # 
    external_layer=null  : enum('LAYER_1','LAYER_2/3','LAYER_2','LAYER_3','LAYER_4','LAYER_5','LAYER_6','UNCLASSIFIED','WHITE_MATTER') # 
    external_visual_area=null : enum('V1','RL','AL')         # 
    axon_angle_max=null  : double                       # 
    axon_angle_min=null  : double                       # 
    n_axon_angles        : tinyint unsigned             # 
    axon_start_distance_from_soma=null : double                       # 
    n_vertices           : int unsigned                 # number of vertices
    n_faces              : int unsigned                 # number of faces
    n_limbs              : int                          # 
    n_branches           : int                          # 
    max_limb_n_branches=null : int                          # 
    skeletal_length=null : double                       # 
    max_limb_skeletal_length=null : double                       # 
    median_branch_length=null : double                       # gives information on average skeletal length to next branch point
    width_median=null    : double                       # median width from mesh center without spines removed
    width_no_spine_median=null : double                       # median width from mesh center with spines removed
    width_90_perc=null   : double                       # 90th percentile for width without spines removed
    width_no_spine_90_perc=null : double                       # 90th percentile for width with spines removed
    n_spines             : bigint                       # 
    n_boutons            : bigint                       # 
    spines_per_branch=null : double                       # 
    skeletal_length_eligible=null : double                       # the skeletal length for all branches searched for spines
    n_spine_eligible_branches=null : int                          # the number of branches that were checked for spines because passed width threshold
    spine_density_eligible=null : double                       # n_spines/skeletal_length_eligible
    spines_per_branch_eligible=null : double                       # n_spines/n_spine_eligible_branches
    total_spine_volume=null : double                       # the sum of all spine volume
    spine_volume_median=null : double                       # median of the spine volume for those spines with able to calculate volume
    spine_volume_density=null : double                       # total_spine_volume/skeletal_length
    spine_volume_density_eligible=null : double                       # total_spine_volume/skeletal_length_eligible
    spine_volume_per_branch_eligible=null : double                       # total_spine_volume/n_spine_eligible_branches
    dendrite_skeletal_length : int unsigned                 # 
    dendrite_area        : int unsigned                 # 
    dendrite_mesh_volume : int unsigned                 # 
    dendrite_n_branches  : int unsigned                 # 
    axon_skeletal_length : int unsigned                 # 
    axon_area            : int unsigned                 # 
    axon_mesh_volume     : int unsigned                 # 
    axon_n_branches      : int unsigned                 # 
    basal_skeletal_length : int unsigned                 # 
    basal_area           : int unsigned                 # 
    basal_mesh_volume    : int unsigned                 # 
    basal_n_branches     : int unsigned                 # 
    apical_skeletal_length : int unsigned                 # 
    apical_area          : int unsigned                 # 
    apical_mesh_volume   : int unsigned                 # 
    apical_n_branches    : int unsigned                 # 
    apical_tuft_skeletal_length : int unsigned                 # 
    apical_tuft_area     : int unsigned                 # 
    apical_tuft_mesh_volume : int unsigned                 # 
    apical_tuft_n_branches : int unsigned                 # 
    apical_shaft_skeletal_length : int unsigned                 # 
    apical_shaft_area    : int unsigned                 # 
    apical_shaft_mesh_volume : int unsigned                 # 
    apical_shaft_n_branches : int unsigned                 # 
    oblique_skeletal_length : int unsigned                 # 
    oblique_area         : int unsigned                 # 
    oblique_mesh_volume  : int unsigned                 # 
    oblique_n_branches   : int unsigned                 # 
    apical_total_skeletal_length : int unsigned                 # 
    apical_total_area    : int unsigned                 # 
    apical_total_mesh_volume : int unsigned                 # 
    apical_total_n_branches : int unsigned                 # 
    n_syn_valid          : int unsigned                 # 
    n_syn_valid_pre      : int unsigned                 # 
    n_syn_valid_post     : int unsigned                 # 
    n_syn_error          : int unsigned                 # 
    n_syn_error_pre      : int unsigned                 # 
    n_syn_error_post     : int unsigned                 # 
    n_syn_presyns_on_dendrite : int unsigned                 # 
    n_syn_mesh_errored   : int unsigned                 # 
    n_syn_distance_errored : int unsigned                 # 
    n_syn_no_label       : int unsigned                 # 
    n_syn_head           : int unsigned                 # 
    n_syn_neck           : int unsigned                 # 
    n_syn_shaft          : int unsigned                 # 
    n_syn_no_head        : int unsigned                 # 
    n_syn_bouton         : int unsigned                 # 
    n_syn_non_bouton     : int unsigned                 # 
    n_syn_dendrite       : int unsigned                 # 
    n_syn_axon           : int unsigned                 # 
    n_syn_basal          : int unsigned                 # 
    n_syn_apical         : int unsigned                 # 
    n_syn_apical_tuft    : int unsigned                 # 
    n_syn_apical_shaft   : int unsigned                 # 
    n_syn_oblique        : int unsigned                 # 
    n_syn_soma           : int unsigned                 # 
    n_syn_apical_total   : int unsigned                 # 
    n_syn_dendrite_head_postsyn : int unsigned                 # 
    n_syn_dendrite_neck_postsyn : int unsigned                 # 
    n_syn_dendrite_shaft_postsyn : int unsigned                 # 
    n_syn_dendrite_no_head_postsyn : int unsigned                 # 
    n_syn_axon_bouton_presyn : int unsigned                 # 
    n_syn_axon_bouton_postsyn : int unsigned                 # 
    n_syn_axon_non_bouton_presyn : int unsigned                 # 
    n_syn_axon_non_bouton_postsyn : int unsigned                 # 
    n_syn_basal_head_postsyn : int unsigned                 # 
    n_syn_basal_neck_postsyn : int unsigned                 # 
    n_syn_basal_shaft_postsyn : int unsigned                 # 
    n_syn_basal_no_head_postsyn : int unsigned                 # 
    n_syn_apical_head_postsyn : int unsigned                 # 
    n_syn_apical_neck_postsyn : int unsigned                 # 
    n_syn_apical_shaft_postsyn : int unsigned                 # 
    n_syn_apical_no_head_postsyn : int unsigned                 # 
    n_syn_apical_tuft_head_postsyn : int unsigned                 # 
    n_syn_apical_tuft_neck_postsyn : int unsigned                 # 
    n_syn_apical_tuft_shaft_postsyn : int unsigned                 # 
    n_syn_apical_tuft_no_head_postsyn : int unsigned                 # 
    n_syn_apical_shaft_head_postsyn : int unsigned                 # 
    n_syn_apical_shaft_neck_postsyn : int unsigned                 # 
    n_syn_apical_shaft_shaft_postsyn : int unsigned                 # 
    n_syn_apical_shaft_no_head_postsyn : int unsigned                 # 
    n_syn_oblique_head_postsyn : int unsigned                 # 
    n_syn_oblique_neck_postsyn : int unsigned                 # 
    n_syn_oblique_shaft_postsyn : int unsigned                 # 
    n_syn_oblique_no_head_postsyn : int unsigned                 # 
    n_syn_soma_no_label_presyn : int unsigned                 # 
    n_syn_soma_no_label_postsyn : int unsigned                 # 
    n_syn_apical_total_head_presyn : int unsigned                 # 
    n_syn_apical_total_head_postsyn : int unsigned                 # 
    n_syn_apical_total_neck_presyn : int unsigned                 # 
    n_syn_apical_total_neck_postsyn : int unsigned                 # 
    n_syn_apical_total_shaft_presyn : int unsigned                 # 
    n_syn_apical_total_shaft_postsyn : int unsigned                 # 
    n_syn_apical_total_no_head_presyn : int unsigned                 # 
    n_syn_apical_total_no_head_postsyn : int unsigned                 # 
    n_syn_axon_ais_postsyn=null : int unsigned                 # 
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
    axon_n_limbs=null    : int unsigned                 # 
    axon_soma_angle_max=null : double                       # 
    axon_soma_angle_min=null : double                       # 
    apical_branch_length_median=null : double                       # 
    apical_branch_length_mean=null : double                       # 
    apical_n_short_branches=null : int unsigned                 # 
    apical_n_long_branches=null : int unsigned                 # 
    apical_n_medium_branches=null : int unsigned                 # 
    apical_bbox_volume=null : double                       # 
    apical_bbox_x_min=null : double                       # 
    apical_bbox_y_min=null : double                       # 
    apical_bbox_z_min=null : double                       # 
    apical_bbox_x_max=null : double                       # 
    apical_bbox_y_max=null : double                       # 
    apical_bbox_z_max=null : double                       # 
    apical_bbox_x_min_soma_relative=null : double                       # 
    apical_bbox_y_min_soma_relative=null : double                       # 
    apical_bbox_z_min_soma_relative=null : double                       # 
    apical_bbox_x_max_soma_relative=null : double                       # 
    apical_bbox_y_max_soma_relative=null : double                       # 
    apical_bbox_z_max_soma_relative=null : double                       # 
    apical_n_limbs=null  : int unsigned                 # 
    apical_soma_angle_max=null : double                       # 
    apical_soma_angle_min=null : double                       # 
    basal_branch_length_median=null : double                       # 
    basal_branch_length_mean=null : double                       # 
    basal_n_short_branches=null : int unsigned                 # 
    basal_n_long_branches=null : int unsigned                 # 
    basal_n_medium_branches=null : int unsigned                 # 
    basal_bbox_volume=null : double                       # 
    basal_bbox_x_min=null : double                       # 
    basal_bbox_y_min=null : double                       # 
    basal_bbox_z_min=null : double                       # 
    basal_bbox_x_max=null : double                       # 
    basal_bbox_y_max=null : double                       # 
    basal_bbox_z_max=null : double                       # 
    basal_bbox_x_min_soma_relative=null : double                       # 
    basal_bbox_y_min_soma_relative=null : double                       # 
    basal_bbox_z_min_soma_relative=null : double                       # 
    basal_bbox_x_max_soma_relative=null : double                       # 
    basal_bbox_y_max_soma_relative=null : double                       # 
    basal_bbox_z_max_soma_relative=null : double                       # 
    basal_n_limbs=null   : int unsigned                 # 
    basal_soma_angle_max=null : double                       # 
    basal_soma_angle_min=null : double                       # 
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
    dendrite_n_limbs=null : int unsigned                 # 
    dendrite_soma_angle_max=null : double                       # 
    dendrite_soma_angle_min=null : double                       # 
    run_time=null        : double                       # the amount of time to run (seconds)
    """
            
    class ErrorStats(djp.Part):
        definition = """
        -> master
        ---
        axon_on_dendrite_merges_error_area=null : double                       # the area (in um ^ 2) of the faces canceled out by filter
        axon_on_dendrite_merges_error_length=null : double                       # the length (in um) of skeleton distance canceled out by filter
        high_degree_branching_error_area=null : double                       # the area (in um ^ 2) of the faces canceled out by filter
        high_degree_branching_error_length=null : double                       # the length (in um) of skeleton distance canceled out by filter
        low_degree_branching_error_area=null : double                       # the area (in um ^ 2) of the faces canceled out by filter
        low_degree_branching_error_length=null : double                       # the length (in um) of skeleton distance canceled out by filter
        high_degree_branching_dendrite_error_area=null : double                       # the area (in um ^ 2) of the faces canceled out by filter
        high_degree_branching_dendrite_error_length=null : double                       # the length (in um) of skeleton distance canceled out by filter
        width_jump_up_dendrite_error_area=null : double                       # the area (in um ^ 2) of the faces canceled out by filter
        width_jump_up_dendrite_error_length=null : double                       # the length (in um) of skeleton distance canceled out by filter
        width_jump_up_axon_error_area=null : double                       # the area (in um ^ 2) of the faces canceled out by filter
        width_jump_up_axon_error_length=null : double                       # the length (in um) of skeleton distance canceled out by filter
        double_back_dendrite_error_area=null : double                       # the area (in um ^ 2) of the faces canceled out by filter
        double_back_dendrite_error_length=null : double                       # the length (in um) of skeleton distance canceled out by filter
        """
                    
    class Object(djp.Part):
        definition = """
        -> master
        ---
        neuron_mesh_faces    : <minnie65_auto_proof_meshes> # face indices for neuron_mesh_faces of final proofread neuron
        neuron_skeleton      : <minnie65_auto_proof_skeletons> # skeleton array for neuron_skeleton of final proofread neuron
        dendrite_mesh_faces  : <minnie65_auto_proof_meshes> # face indices for dendrite_mesh_faces of final proofread neuron
        axon_mesh_faces      : <minnie65_auto_proof_meshes> # face indices for axon_mesh_faces of final proofread neuron
        basal_mesh_faces     : <minnie65_auto_proof_meshes> # face indices for basal_mesh_faces of final proofread neuron
        apical_mesh_faces    : <minnie65_auto_proof_meshes> # face indices for apical_mesh_faces of final proofread neuron
        apical_tuft_mesh_faces : <minnie65_auto_proof_meshes> # face indices for apical_tuft_mesh_faces of final proofread neuron
        apical_shaft_mesh_faces : <minnie65_auto_proof_meshes> # face indices for apical_shaft_mesh_faces of final proofread neuron
        oblique_mesh_faces   : <minnie65_auto_proof_meshes> # face indices for oblique_mesh_faces of final proofread neuron
        dendrite_skeleton    : <minnie65_auto_proof_skeletons> # skeleton array for dendrite_skeleton of final proofread neuron
        axon_skeleton        : <minnie65_auto_proof_skeletons> # skeleton array for axon_skeleton of final proofread neuron
        basal_skeleton       : <minnie65_auto_proof_skeletons> # skeleton array for basal_skeleton of final proofread neuron
        apical_skeleton      : <minnie65_auto_proof_skeletons> # skeleton array for apical_skeleton of final proofread neuron
        apical_tuft_skeleton : <minnie65_auto_proof_skeletons> # skeleton array for apical_tuft_skeleton of final proofread neuron
        apical_shaft_skeleton : <minnie65_auto_proof_skeletons> # skeleton array for apical_shaft_skeleton of final proofread neuron
        oblique_skeleton     : <minnie65_auto_proof_skeletons> # skeleton array for oblique_skeleton of final proofread neuron
        limb_branch_to_cancel : longblob                     # stores the limb information from
        red_blue_suggestions=null : longblob                     # 
        split_locations=null : longblob                     # 
        split_locations_before_filter=null : longblob                     # 
        neuron_graph=null    : <minnie65_graph>             # the graph for the
        decomposition=null   : <minnie65_decomposition>     # 
        """
                    
    class Synapse(djp.Part):
        definition = """
        -> master
        synapse_id           : bigint unsigned              # synapse index within the segmentation
        ---
        secondary_seg_id     : bigint unsigned              # segment_id of the cell. Equivalent to Allen 'pt_root_id
        primary_nucleus_id   : int unsigned                 # id of nucleus from the flat segmentation  Equivalent to Allen: 'id'.
        synapse_type         : enum('presyn','postsyn')     # 
        skeletal_distance_to_soma=null : double                       # the length (in um) of skeleton distance from synapse to soma (-2 if on the soma)
        limb_idx=null        : tinyint unsigned             # 
        branch_idx=null      : int unsigned                 # 
        spine_bouton         : enum('head','neck','shaft','no_head','bouton','non_bouton','no_label') # 
        compartment_coarse=null : enum('soma','axon','dendrite') # 
        compartment_fine=null : enum('basal','apical','apical_tuft','apical_shaft','oblique','inhibitory') # 

        """
                    
    class SynapseErrors(djp.Part):
        definition = """
        -> master
        synapse_id           : bigint unsigned              # synapse index within the segmentation
        ---
        secondary_seg_id     : bigint unsigned              # segment_id of the cell. Equivalent to Allen 'pt_root_id
        primary_nucleus_id   : int unsigned                 # id of nucleus from the flat segmentation  Equivalent to Allen: 'id'.
        synapse_type         : enum('presyn','postsyn')     # 
        """
                    
    class SynapseErrorsPreDendr(djp.Part):
        definition = """
        -> master
        synapse_id           : bigint unsigned              # synapse index within the segmentation
        ---
        secondary_seg_id     : bigint unsigned              # segment_id of the cell. Equivalent to Allen 'pt_root_id
        primary_nucleus_id   : int unsigned                 # id of nucleus from the flat segmentation  Equivalent to Allen: 'id'.
        synapse_type         : enum('presyn','postsyn')     # 
        skeletal_distance_to_soma=null : double                       # the length (in um) of skeleton distance from synapse to soma (-2 if on the soma)
        limb_idx=null        : tinyint unsigned             # 
        branch_idx=null      : int unsigned                 # 
        """


@schema
class AutoProofreadNeuronProximity(djp.Computed):
    definition = """
    segment_id           : bigint unsigned              # 
    split_index          : int unsigned                 # 
    segment_id_post      : bigint unsigned              # 
    split_index_post     : int unsigned                 # 
    prox_id              : int                          # 
    ---
    proximity_dist=null  : float                        # 
    proximity_dist_non_adjusted=null : float                        # 
    presyn_proximity_x_nm=null : float                        # 
    presyn_proximity_y_nm=null : float                        # 
    presyn_proximity_z_nm=null : float                        # 
    postsyn_proximity_x_nm=null : float                        # 
    postsyn_proximity_y_nm=null : float                        # 
    postsyn_proximity_z_nm=null : float                        # 
    postsyn_compartment=null : enum('apical','apical_shaft','apical_tuft','basal','axon','oblique','dendrite','apical_total','soma') # 
    presyn_width=null    : float                        # 
    postsyn_width=null   : float                        # 
    presyn_euclidean_distance_to_soma=null : float                        # 
    postsyn_euclidean_distance_to_soma=null : float                        # 
    presyn_skeletal_distance_to_soma=null : float                        # 
    postsyn_skeletal_distance_to_soma=null : float                        # 
    synapse_id=null      : bigint unsigned              # 
    synapse_id_dist=null : float                        # 
    n_synapses=null      : int unsigned                 # 
    n_synapse_post=null  : int unsigned                 # 
    n_spine_post=null    : int unsigned                 # 
    n_synapse_pre_raw=null : int unsigned                 # 
    n_synapse_pre_proof=null : int unsigned                 # 
    """
            
    class Errors(djp.Part):
        definition = """
        -> master
        ---
        error_str            : varchar(500)                 # 
        """


@schema
class AutoProofreadNeuronProximityConfigMotifs(djp.Manual):
    definition = """
    seed                 : int unsigned                 # 
    edges_func           : varchar(20)                  # 
    ---
    n_motif_3=null       : int unsigned                 # 
    n_motif_4=null       : int unsigned                 # 
    n_motif_5=null       : int unsigned                 # 
    n_motif_6=null       : int unsigned                 # 
    n_motif_7=null       : int unsigned                 # 
    n_motif_8=null       : int unsigned                 # 
    n_motif_9=null       : int unsigned                 # 
    n_motif_10=null      : int unsigned                 # 
    n_motif_11=null      : int unsigned                 # 
    n_motif_12=null      : int unsigned                 # 
    n_motif_13=null      : int unsigned                 # 
    n_motif_14=null      : int unsigned                 # 
    n_motif_15=null      : int unsigned                 # 
    comp_time=null       : float                        # 
    """
            

@schema
class AutoProofreadNeuronProximityConnetome(djp.Manual):
    definition = """
    iteration            : int                          # 
    graph_type           : enum('DiGraph','MultiGraph','Graph','MultiDiGraph') # 
    ---
    connectome           : <minnie65_graph>             # 
    notes=null           : varchar(500)                 # 
    timestamp=CURRENT_TIMESTAMP : timestamp                    # 
    """


@schema
class AutoProofreadNeuronProximityPairwise(djp.Computed):
    definition = """
    segment_id           : bigint unsigned              # 
    split_index          : int unsigned                 # 
    pairwise_idx         : int unsigned                 # 
    ---
    pre_1_segment_id=null : bigint unsigned              # 
    pre_1_split_index=null : int unsigned                 # 
    pre_1_prox_id=null   : int unsigned                 # 
    pre_1_n_synapses=null : int unsigned                 # 
    pre_2_segment_id=null : bigint unsigned              # 
    pre_2_split_index=null : int unsigned                 # 
    pre_2_prox_id=null   : int unsigned                 # 
    pre_2_n_synapses=null : int unsigned                 # 
    skeletal_distance=null : float                        # 
    euclidean_distance=null : float                        # 
    """
    

@schema
class AutoProofreadNeuronProximityProcessed(djp.Manual):
    definition = """
    segment_id           : bigint unsigned              # 
    split_index          : int unsigned                 # 
    """


@schema
class AutoProofreadNeuronProximitySearch(djp.Computed):
    definition = """
    -> AutoProofreadNeuron
    ---
    n_targets            : int unsigned                 # 
    targets_segment_id   : longblob                     # 
    targets_split_index  : longblob                     # 
    """


@schema
class AutoProofreadNeuronProximityMotifs(djp.Manual):
    definition = """
    seed                 : int unsigned                 # 
    edges_func           : varchar(20)                  # 
    ---
    n_motif_3=null       : bigint unsigned              # 
    n_motif_4=null       : bigint unsigned              # 
    n_motif_5=null       : bigint unsigned              # 
    n_motif_6=null       : bigint unsigned              # 
    n_motif_7=null       : bigint unsigned              # 
    n_motif_8=null       : bigint unsigned              # 
    n_motif_9=null       : bigint unsigned              # 
    n_motif_10=null      : bigint unsigned              # 
    n_motif_11=null      : bigint unsigned              # 
    n_motif_12=null      : bigint unsigned              # 
    n_motif_13=null      : bigint unsigned              # 
    n_motif_14=null      : bigint unsigned              # 
    n_motif_15=null      : bigint unsigned              # 
    comp_time=null       : float                        # 
    """

@schema
class AutoProofreadNeuronProximityMotifNulls(djp.Manual):
    definition = """
    seed                 : int unsigned                 # 
    edges_func           : varchar(20)                  # 
    graph_type           : varchar(20)                  # 
    ---
    n_nodes              : bigint unsigned              # 
    n_edges              : bigint unsigned              # 
    n_reciprocal         : bigint unsigned              # 
    n_motif_3=null       : bigint unsigned              # 
    n_motif_4=null       : bigint unsigned              # 
    n_motif_5=null       : bigint unsigned              # 
    n_motif_6=null       : bigint unsigned              # 
    n_motif_7=null       : bigint unsigned              # 
    n_motif_8=null       : bigint unsigned              # 
    n_motif_9=null       : bigint unsigned              # 
    n_motif_10=null      : bigint unsigned              # 
    n_motif_11=null      : bigint unsigned              # 
    n_motif_12=null      : bigint unsigned              # 
    n_motif_13=null      : bigint unsigned              # 
    n_motif_14=null      : bigint unsigned              # 
    n_motif_15=null      : bigint unsigned              # 
    comp_time=null       : float                        # 
    """
            

@schema
class AutoProofreadNeuronProximityMotifsNoMan(djp.Manual):
    definition = """
    seed                 : int unsigned                 # 
    edges_func           : varchar(20)                  # 
    ---
    n_motif_3=null       : bigint unsigned              # 
    n_motif_4=null       : bigint unsigned              # 
    n_motif_5=null       : bigint unsigned              # 
    n_motif_6=null       : bigint unsigned              # 
    n_motif_7=null       : bigint unsigned              # 
    n_motif_8=null       : bigint unsigned              # 
    n_motif_9=null       : bigint unsigned              # 
    n_motif_10=null      : bigint unsigned              # 
    n_motif_11=null      : bigint unsigned              # 
    n_motif_12=null      : bigint unsigned              # 
    n_motif_13=null      : bigint unsigned              # 
    n_motif_14=null      : bigint unsigned              # 
    n_motif_15=null      : bigint unsigned              # 
    comp_time=null       : float                        # 
    """
            

@schema
class AutoProofreadNeuronProximityMotifsAuto(djp.Manual):
    definition = """
    seed                 : int unsigned                 # 
    edges_func           : varchar(20)                  # 
    ---
    n_motif_3=null       : bigint unsigned              # 
    n_motif_4=null       : bigint unsigned              # 
    n_motif_5=null       : bigint unsigned              # 
    n_motif_6=null       : bigint unsigned              # 
    n_motif_7=null       : bigint unsigned              # 
    n_motif_8=null       : bigint unsigned              # 
    n_motif_9=null       : bigint unsigned              # 
    n_motif_10=null      : bigint unsigned              # 
    n_motif_11=null      : bigint unsigned              # 
    n_motif_12=null      : bigint unsigned              # 
    n_motif_13=null      : bigint unsigned              # 
    n_motif_14=null      : bigint unsigned              # 
    n_motif_15=null      : bigint unsigned              # 
    comp_time=null       : float                        # 
    """


@schema
class ManuallyProofreadAllenNeuron(djp.Computed):
    definition = """
    -> m65mat.Meshwork
    segment_id           : bigint unsigned              # 
    split_index          : tinyint unsigned             # 
    """

@schema
class ManuallyProofreadAllenNeuronProximity(djp.Computed):
    definition = """
    -> ManuallyProofreadAllenNeuron
    segment_id_post      : bigint unsigned              # 
    split_index_post     : int unsigned                 # 
    prox_id              : int                          # 
    ---
    proximity_dist=null  : float                        # 
    proximity_dist_non_adjusted=null : float                        # 
    presyn_proximity_x_nm=null : float                        # 
    presyn_proximity_y_nm=null : float                        # 
    presyn_proximity_z_nm=null : float                        # 
    postsyn_proximity_x_nm=null : float                        # 
    postsyn_proximity_y_nm=null : float                        # 
    postsyn_proximity_z_nm=null : float                        # 
    postsyn_compartment=null : enum('apical','apical_shaft','apical_tuft','basal','axon','oblique','dendrite','apical_total','soma') # 
    presyn_width=null    : float                        # 
    postsyn_width=null   : float                        # 
    presyn_euclidean_distance_to_soma=null : float                        # 
    postsyn_euclidean_distance_to_soma=null : float                        # 
    presyn_skeletal_distance_to_soma=null : float                        # 
    postsyn_skeletal_distance_to_soma=null : float                        # 
    synapse_id=null      : bigint unsigned              # 
    synapse_id_dist=null : float                        # 
    n_synapses=null      : int unsigned                 # 
    n_synapse_post=null  : int unsigned                 # 
    n_spine_post=null    : int unsigned                 # 
    n_synapse_pre_raw=null : int unsigned                 # 
    n_synapse_pre_proof=null : int unsigned                 # 
    """
            
    class Errors(djp.Part):
        definition = """
        -> master
        ---
        error_str            : varchar(500)                 # 
        """
                

@schema
class ManuallyProofreadAllenNeuronProximitySearch(djp.Computed):
    definition = """
    -> ManuallyProofreadAllenNeuron
    ---
    n_targets            : int unsigned                 # 
    targets_segment_id   : longblob                     # 
    targets_split_index  : longblob                     # 
    """        


@schema
class ManuallyProofreadAllenNeuronProximityProcessed(djp.Manual):
    definition = """
    -> ManuallyProofreadAllenNeuron
    """
