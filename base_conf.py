import configparser
import os

# Setup base directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Load environment variables
config = configparser.ConfigParser()
config.read(BASE_DIR.joinpath("config.ini"))

# get database configurations
DATABASE = {
    'USERNAME': config['database']['username'],
    'PASSWORD': config['database']['password'],
    'HOST': config['database']['host'],
    'PORT': config['database']['port'],
    'NAME': config['database']['name'],
}