import warnings
from microns_utils import config_utils

_repo = 'microns-morphology'
_package = 'microns-morphology-api'

try:
    __version__ = config_utils.get_package_version(repo=_repo, package=_package)
except:
    warnings.warn('Package version not able to be determined.')