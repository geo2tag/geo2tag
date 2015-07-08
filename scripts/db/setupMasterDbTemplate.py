import os
import sys
from configparser import ConfigParser

sys.path.append("src/")
import config_reader

TEMPLATE_PATH = 'master_db_template/'
db_name = None


def import_db(db_name, template_path):
    str_forsh = 'scripts/db/mongo.sh -l -H localhost:27017 ' + db_name
    os.system(str_forsh)
def getDbName():
    return config_reader.getDbName()
def run():
    db_name = getDbName();
    import_db(db_name,TEMPLATE_PATH)

if __name__ == '__main__':
    run()