import datajoint as dj

from microns_morphology_api import config
schema_name = 'microns_minnie65_auto_proofreading'

config.register_adapters(schema_name, context=locals())
config.register_externals(schema_name)

schema = dj.schema(schema_name)
schema.spawn_missing_classes()

