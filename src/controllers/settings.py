import pathlib
from types import SimpleNamespace
from pyflexconfig import bootstrap

config = SimpleNamespace()

_default_config_path = pathlib.Path(__file__).resolve().parent / "../config/defaultSettings.py"
bootstrap(config, defaults_path=_default_config_path)
