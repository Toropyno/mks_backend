from configparser import ConfigParser
from os import path

from pyramid.paster import setup_logging


def get_settings_from_config(config_uri: str) -> dict:

    config = ConfigParser()
    config.optionxform = str
    config.read(config_uri)
    return dict(config.items('app:main'))


PROJECT_DIRECTORY = path.dirname(path.dirname(path.abspath(__file__)))
BASE_DIRECTORY = path.join(PROJECT_DIRECTORY, 'mks_backend')

CONFIG_PATH = path.join(PROJECT_DIRECTORY, 'development.ini')
setup_logging(CONFIG_PATH)

SETTINGS = get_settings_from_config(CONFIG_PATH)
