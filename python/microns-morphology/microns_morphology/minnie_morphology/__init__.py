from microns_morphology_api import config
from . import minnie65_morphology

config.register_bases(config.SCHEMAS.MINNIE65_MORPHOLOGY, minnie65_morphology)