import datajoint as dj
import datajoint_plus as djp

from ..config import h01_morphology_config as config

config.register_adapters(context=locals())
config.register_externals()

schema = djp.schema(config.schema_name)

schema.spawn_missing_classes()
