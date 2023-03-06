import configparser
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# FILES
configFile = os.path.join(BASE_DIR, "settings/config.ini")

# ENVIRONMENT VARIABLES
config = configparser.ConfigParser()
config.read(configFile)
