#! /bin/bash

BACKUP_STORAGE=$1
export SITE=geo2tag.org
export SSH='ssh -p 20522 wpbackup@188.40.64.219'
export BACKUP_DIRS='/var/www/geo2tag.org'
PWD=`pwd`
cd ${BACKUP_STORAGE}
exec {$PWD}/scripts/copy-any-rootfs
