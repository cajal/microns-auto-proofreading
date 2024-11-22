import numpy as np
from pathlib import Path

from neurd import vdi_default as vdi_def
from neurd.parameter_configs import parameters_config_microns as param
from microns_morphology_api import data_interface
default_settings = dict(
    source="microns",
    parameters_config_filepaths=param.parameters,
    synapse_filepath=None,   
)

class DataInterfaceMicrons(vdi_def.DataInterfaceDefault):
    def __init__(
        self,
        data_interface=None,
        **kwargs
        ):
        
        kwargs.update(default_settings)
        super().__init__(
            **kwargs
        )
        self.data_interface = data_interface
        
    @property
    def voxel_to_nm_scaling(self):
        return np.array([4,4,40])
    
    def segment_id_to_synapse_df(
        self,
        segment_id,
        **kwargs
        ):

        return self.data_interface.segment_id_to_synapse_df(segment_id, **kwargs)

    def fetch_undecimated_segment_id_mesh(
        self,
        segment_id,
        **kwargs
        ):
        return self.data_interface.fetch_undecimated_segment_id_mesh(segment_id, **kwargs)

    def fetch_segment_id_mesh(
        self,
        segment_id,
        **kwargs
        ):
        return self.data_interface.fetch_segment_id_mesh(segment_id, **kwargs)

    def get_align_matrix(self, *args, **kwargs):
        return None 
    

vdi = DataInterfaceMicrons(data_interface=data_interface)