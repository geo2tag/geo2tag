#!/bin/bash
echo "Before cleaning /tmp/"
df -h
LIST=`find /tmp -mtime +7 -print0 -name 'tmp*' -exec rm -fr "{}" \;`
echo "`echo $LIST | grep -o '/tmp/' | wc -w` files where deleted"
echo "Disk space statistics after old files removing"
df -h
