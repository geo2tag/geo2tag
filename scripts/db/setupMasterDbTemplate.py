import os
import argparse
from configparser import SafeConfigParser

SECTION = 'main'
OPTION_DBNAME = 'db_name'
DBNAME = 'geomongo'


def import_db(db_name):
    str_forsh = 'scripts/db/mongo.sh -l -H localhost:27017 ' + db_name
    os.system(str_forsh)


def getConfigParser(config_name):
    config = SafeConfigParser({OPTION_DBNAME: DBNAME})
    config.read(config_name)
    return config


def getDbName(config_name):
    return getConfigParser(config_name).get(SECTION, OPTION_DBNAME)


def run():
    parser = argparse.ArgumentParser(description='Setup master db')
    parser.add_argument('--dbName', help='Name db')
    parser.add_argument('--config', help='Config name')
    args = parser.parse_args()
    if unicode(args.config) == 'None':
        import_db(unicode(args.dbName))
    else:
        db_name = getDbName(args.config)
        import_db(unicode(db_name))

if __name__ == '__main__':
    run()
