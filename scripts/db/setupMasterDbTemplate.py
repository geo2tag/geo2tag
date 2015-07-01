import os
from configparser import ConfigParser
import sys
CONFIG_PATH =  'config/config.ini'
SECTION = 'main'
OPTION_DBNAME = 'db_name'
TEMPLATE_PATH = 'master_db_template/'
def import_db(db_name, template_path):
    print db_name + ' ' + template_path
   
def getConfigParser():
    config = ConfigParser()
    config.read(CONFIG_PATH)
    return config
def getDbName():
    return getConfigParser().get(SECTION,OPTION_DBNAME)
def run():
    db_name = getDbName();
    import_db(db_name,TEMPLATE_PATH)

if __name__ == '__main__':
    run()