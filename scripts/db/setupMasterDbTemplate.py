import os
import sys
import config_reader



def import_db(db_name):
    str_forsh = 'scripts/db/mongo.sh -l -H localhost:27017 ' + db_name
    os.system(str_forsh)


def run():
    if len(sys.argv) == 1:
        db_name = config_reader.getDbName()
    elif len(sys.argv) == 2:
        db_name = sys.argv[1]
    else:
        print "Error agrs!!!"
    import_db(db_name)

if __name__ == '__main__':
    run()
