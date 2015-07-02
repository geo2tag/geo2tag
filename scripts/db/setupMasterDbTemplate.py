import os
from configparser import ConfigParser



CONFIG_PATH =  'config/config.ini'
SECTION = 'main'
OPTION_DBNAME = 'db_name'
TEMPLATE_PATH = 'master_db_template/'
def import_db(db_name, template_path):
    str_forsh = 'scripts/db/mongo.sh -l -H localhost:27017 ' + db_name
    os.system(str_forsh)
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