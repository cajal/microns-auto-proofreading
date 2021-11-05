import datajoint as dj


import microns_morphology_config as config
schema_name = 'microns_minnie65_auto_proofreading'

config.register_adapters(schema_name)
config.register_externals(schema_name)

schema = dj.schema(schema_name, create_tables=True)
schema.spawn_missing_classes()

