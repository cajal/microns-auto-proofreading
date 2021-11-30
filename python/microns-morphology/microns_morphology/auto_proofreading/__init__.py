from microns_morphology_api import config
from . import h01_auto_proofreading, minnie65_auto_proofreading

config.register_bases(config.SCHEMAS.H01_AUTO_PROOFREADING, h01_auto_proofreading)
config.register_bases(config.SCHEMAS.MINNIE65_AUTO_PROOFREADING, minnie65_auto_proofreading)