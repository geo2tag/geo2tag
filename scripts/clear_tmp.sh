find /tmp -mtime +7 -name 'tmp*' -print0 | xargs -0 ls -exec rm -r {} \;
