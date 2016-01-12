#! /bin/bash

export SITE=geo2tag.org
export SSH='ssh -p 20522 wpbackup@188.40.64.219'
export BACKUP_DIRS='/var/www/geo2tag.org/'
export PRE_COMMAND='/var/www/geo2tag.org/dump_db.sh'
exec ./scripts/copy-any-rootfs
