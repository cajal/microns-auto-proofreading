import datajoint as dj
from datajoint import datajoint_plus as djp

from ..config import minnie65_morphology_config as config

config.register_adapters(context=locals())
config.register_externals()

schema = dj.schema(config.schema_name)

schema.spawn_missing_classes()
schema.connection.dependencies.load()