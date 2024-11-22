import datajoint_plus as djp
import microns_utils.datajoint_utils as dju

from ..config import minnie65_auto_proofreading_v2_config as config
config.register_adapters(context=locals())
config.register_externals()

schema = djp.schema(config.schema_name)

@schema
class Tag(dju.VersionLookup):
    package = 'microns-morphology-api'
    attr_name = 'tag'