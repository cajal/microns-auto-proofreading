import datajoint as dj
from datajoint import datajoint_plus as djp

from ..config import minnie65_morphology_config

minnie65_morphology_config.register_adapters(context=locals())
minnie65_morphology_config.register_externals()

schema = dj.schema(minnie65_morphology_config.schema_name)

schema.spawn_missing_classes()
schema.connection.dependencies.load()