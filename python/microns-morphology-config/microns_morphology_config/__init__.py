"""
Configuration package/module for microns-morphology.
"""

from . import adapters
from . import externals

import traceback

try:
    import datajoint as dj
except:
    traceback.print_exc()
    raise ImportError('DataJoint package not found.')

from enum import Enum

from microns_utils import config_utils
    
config_utils.enable_datajoint_flags()

def register_externals(schema_name:str):
    """
    Registers the external stores for a schema_name in this module.
    """
    return config_utils.register_externals(config_mapping[SCHEMAS(schema_name)]["externals"])


def register_adapters(schema_name:str, context=None):
    """
    Imports the adapters for a schema_name into the global namespace.
    """
    return config_utils.register_adapters(config_mapping[SCHEMAS(schema_name)]["adapters"], context=context)


def create_vm(schema_name:str):
    """
    Creates a virtual module after registering the external stores, and includes the adapter objects in the vm.
    """
    schema = SCHEMAS(schema_name)
    return config_utils.create_vm(schema.value, 
                                  external_stores=config_mapping[schema]["externals"],
                                  adapter_objects=config_mapping[schema]["adapters"])


class SCHEMAS(Enum):
    H01_MORPHOLOGY = "microns_h01_morphology"
    MINNIE65_AUTO_PROOFREADING = "microns_minnie65_auto_proofreading"
    H01_AUTO_PROOFREADING = "microns_h01_auto_proofreading"
    MINNIE65_MORPHOLOGY = "microns_minnie65_morphology"




config_mapping = {
    SCHEMAS.H01_MORPHOLOGY: {
        "externals": externals.h01_morphology,
        "adapters": adapters.h01_morphology_adapter_objects,
    },
    SCHEMAS.H01_AUTO_PROOFREADING: {
        "externals": externals.h01_auto_proofreading,
        "adapters": adapters.h01_auto_proofreading_adapter_objects,
    },
    SCHEMAS.MINNIE65_AUTO_PROOFREADING: {
        "externals": externals.minnie65_auto_proofreading,
        "adapters": adapters.minnie65_auto_proofreading_adapter_objects,
    },
    SCHEMAS.MINNIE65_MORPHOLOGY: {
        "externals": externals.minnie65_morphology,
        "adapters": adapters.minnie65_morphology_adapter_objects,
        
    },

}