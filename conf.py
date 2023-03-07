import configparser
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# FOLDERS
settingsFolder = os.path.join(BASE_DIR, "settings")

# FILES
configFile = os.path.join(settingsFolder, "config.ini")

# ENVIRONMENT VARIABLES
config = configparser.ConfigParser()
config.read(configFile)
