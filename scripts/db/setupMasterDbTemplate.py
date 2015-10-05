import os
import sys
from configparser import ConfigParser
import config_reader

TEMPLATE_PATH = 'master_db_template/'


def import_db(db_name, template_path):
    str_forsh = 'scripts/db/mongo.sh -l -H localhost:27017 ' + db_name
    os.system(str_forsh)


def run():
    if len(sys.argv) == 1:
        db_name = config_reader.getDbName()
    elif len(sys.argv) == 2:
        db_name = sys.argv[1]
    else:
        print "Error agrs!!!"
    import_db(db_name, TEMPLATE_PATH)
if __name__ == '__main__':
    run()
