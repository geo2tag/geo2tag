#!/bin/bash

echo
echo "==================== PYLINT CHECK ====================="
echo

pylint --reports=n  --msg-template='{path}:{line}: {msg} [{msg_id}]' --disable=all --enable=typecheck,exception,basic,string,variables --disable=C,W0141,W0603,E1101 --enable=W0404,R0401,W0401 `find ./ | grep .py$`

