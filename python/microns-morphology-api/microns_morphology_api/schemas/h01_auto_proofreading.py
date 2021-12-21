import datajoint as dj
from datajoint import datajoint_plus as djp

from ..config import h01_auto_proofreading_config

h01_auto_proofreading_config.register_adapters(context=locals())
h01_auto_proofreading_config.register_externals()

schema = dj.schema(h01_auto_proofreading_config.schema_name)

schema.spawn_missing_classes()
schema.connection.dependencies.load()

