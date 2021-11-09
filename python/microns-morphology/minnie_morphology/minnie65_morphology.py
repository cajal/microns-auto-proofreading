import datajoint as dj

import microns_morphology_config as config
schema_name = 'microns_minnie65_morphology'

config.register_adapters(schema_name, context=locals())
config.register_externals(schema_name)

schema = dj.schema(schema_name)
