import pandas as pd

from microns_materialization_api.schemas import minnie65_materialization as m65mat
from microns_morphology_api.schemas import minnie65_morphology_v2 as m65mor2

default_mat_ver = 343

def segment_id_to_synapse_df(
    segment_id, 
    ver=default_mat_ver, 
    **kwargs
):
    """
    Retrieve a DataFrame containing synapse information related to a given segment ID.

    Parameters:
    segment_id (int): The primary segment ID to filter the synapse information.
    ver (int, optional): The materialization version to query. 
                         Defaults to 'default_mat_ver' if not specified.
    **kwargs: Additional keyword arguments can be passed, which may be used in the query or projection.

    Returns:
    pandas.DataFrame: A DataFrame containing the synapse information where the rows correspond to 
                      the filtered synapse data based on the given segment ID and version.
    """
    syn_rel = m65mat.Synapse.Info2 & {'ver': ver, 'primary_seg_id': segment_id}
    return pd.DataFrame(syn_rel.proj(..., segment_id='primary_seg_id', segment_id_secondary='secondary_seg_id').fetch())


def fetch_undecimated_segment_id_mesh(
    segment_id=None,
    mesh_id=None,
    **kwargs
):
    key = {}
    if mesh_id is not None:
        key.update('mesh_id', mesh_id)
    if segment_id is not None:
        key.update('segment_id', segment_id)
    return m65mor2.Mesh.get1(key).mesh

def fetch_segment_id_mesh(
    segment_id=None,
    mesh_id=None,
    dec_mesh_id=None,
    **kwargs
):
    key = {}
    if dec_mesh_id is not None:
        key.update('dec_mesh_id', dec_mesh_id)
    if mesh_id is not None:
        key.update('mesh_id', mesh_id)
    if segment_id is not None:
        key.update('segment_id', segment_id)
    return m65mor2.DecimatedMesh.get1(key).dec_mesh