"""
Configuration package/module for microns-morphology.
"""
import datajoint_plus as djp
from microns_utils.config_utils import SchemaConfig
from . import adapters
from . import externals

djp.enable_datajoint_flags()

h01_morphology_config = SchemaConfig(
    module_name='h01_morphology',
    schema_name='microns_h01_morphology',
    externals=externals.h01_morphology,
    adapters=adapters.h01_morphology
)

minnie65_auto_proofreading_config = SchemaConfig(
    module_name='minnie65_auto_proofreading',
    schema_name='microns_minnie65_auto_proofreading',
    externals=externals.minnie65_auto_proofreading,
    adapters=adapters.minnie65_auto_proofreading
)

h01_auto_proofreading_config = SchemaConfig(
    module_name='h01_auto_proofreading',
    schema_name='microns_h01_auto_proofreading',
    externals=externals.h01_auto_proofreading,
    adapters=adapters.h01_auto_proofreading
)

minnie65_morphology_config = SchemaConfig(
    module_name='minnie65_morphology',
    schema_name='microns_minnie65_morphology',
    externals=externals.minnie65_morphology,
    adapters=adapters.minnie65_morphology
)

minnie65_auto_proofreading_v2_config = SchemaConfig(
    module_name='minnie65_auto_proofreading_v2',
    schema_name='microns_minnie65_auto_proofreading_v2',
    externals=externals.minnie65_auto_proofreading_v2,
    adapters=adapters.minnie65_auto_proofreading_v2
)

minnie65_morphology_v2_config = SchemaConfig(
    module_name='minnie65_morphology_v2',
    schema_name='microns_minnie65_morphology_v2',
    externals=externals.minnie65_morphology_v2,
    adapters=adapters.minnie65_morphology_v2
)