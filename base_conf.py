import configparser
import os

# Setup base directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
configFile = os.path.join(BASE_DIR, "config.ini")
# Load environment variables
config = configparser.ConfigParser()
config.read(configFile)
print("-------------------------")
print(configFile)
print(config.get("database", "username"))
# get database configurations
DATABASE = {
    'USERNAME': config['database']['username'],
    'PASSWORD': config['database']['password'],
    'HOST': config['database']['host'],
    'PORT': config['database']['port'],
    'NAME': config['database']['name'],
}