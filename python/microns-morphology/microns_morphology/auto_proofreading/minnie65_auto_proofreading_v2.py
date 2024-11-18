import datajoint as dj
import datajoint_plus as djp

from microns_morphology_api.schemas import minnie65_auto_proofreading_v2 as m65auto2

schema = m65auto2.schema
config = m65auto2.config

logger = djp.getLogger(__name__)
