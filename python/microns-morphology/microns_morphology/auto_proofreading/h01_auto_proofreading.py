import datajoint as dj
from datajoint import datajoint_plus as djp

from microns_morphology_api import config
schema_obj = config.SCHEMAS.H01_AUTO_PROOFREADING

config.register_adapters(schema_obj, context=locals())
config.register_externals(schema_obj)

schema = dj.schema(schema_obj.value)
schema.spawn_missing_classes()
schema.connection.dependencies.load()

