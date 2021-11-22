from microns_morphology_api import config
from . import h01_morphology

config.register_bases(config.SCHEMAS.H01_MORPHOLOGY, h01_morphology)