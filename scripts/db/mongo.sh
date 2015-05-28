#!/bin/bash

LOADING=false

usage()
{
    cat << EOF
    usage: $0 [options] dbname

    OPTIONS:
        -h      Show this help.
        -l      Load instead of export
        -u      Mongo username
        -p      Mongo password
        -H      Mongo host string (ex. localhost:27017)
EOF
}

while getopts "hlu:p:H:" opt; do
    MAXOPTIND=$OPTIND

    case $opt in
        h)
            usage
            exit
            ;;
        l)
            LOADING=true
            ;;
        u)
            USERNAME="$OPTARG"
            ;;
        p)
            PASSWORD="$OPTARG"
            ;;
        H)
            HOST="$OPTARG"
            ;;
        \?)
            echo "Invalid option $opt"
            exit 1
            ;;
    esac
done

shift $(($MAXOPTIND-1))

if [ -z "$1" ]; then
    echo "Usage: export-mongo [opts] <dbname>"
    exit 1
fi

dumpPath='testdump';
DB="$1"
path_="${dumpPath}/$DB-dump"
if [ -z "$2" ]; then
    path_="${dumpPath}/$DB-dump"
else
    path_="${dumpPath}/$2"
fi

if [ -z "$HOST" ]; then
    CONN="localhost:27017/$DB"
else
    CONN="$HOST/$DB"
fi

ARGS=""
if [ -n "$USERNAME" ]; then
    ARGS="-u $USERNAME"
fi
if [ -n "$PASSWORD" ]; then
    ARGS="$ARGS -p $PASSWORD"
fi
echo "$ARGS"
echo "*************************** Mongo Export ************************"
echo "**** Host:      $HOST"
echo "**** Database:  $DB"
echo "**** Username:  $USERNAME"
echo "**** Password:  $PASSWORD"
echo "**** Loading:   $LOADING"
echo "*****************************************************************"

if $LOADING ; then
    echo "Loading into $CONN"
    pushd $path_ >/dev/null
    echo $path_

    for path in *.json; do
        collection=${path%.json}
        echo "Loading into $DB/$collection from $path"
       mongoimport --upsert --host $HOST -d $DB -c $collection $path
    done

    popd >/dev/null
else
    DATABASE_COLLECTIONS=$(mongo $CONN $ARGS --quiet --eval 'db.getCollectionNames()' | sed 's/,/ /g')

    mkdir /tmp/$DB
    mkdir -p $(pwd)/${dumpPath}/$DB-dump
    pushd /tmp/$DB 2>/dev/null

    for collection in $DATABASE_COLLECTIONS; do
        mongoexport --host $HOST -db $DB -c $collection -o $collection.json >/dev/null
    done

    popd 2>/dev/null
    mv /tmp/$DB/* ./${dumpPath}/$DB-dump 2>/dev/null
    rm -rf /tmp/$DB 2>/dev/null
fi
