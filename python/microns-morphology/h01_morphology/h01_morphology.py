import datajoint as dj

import microns_morphology_config as config
schema_name = 'microns_h01_morphology'

config.register_adapters(schema_name)
config.register_externals(schema_name)

schema = dj.schema(schema_name)
