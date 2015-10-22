#!/bin/bash

echo
echo "==================== PYLINT CHECK ====================="
echo

pylint --msg-template='{path}:{line}: {msg}' --disable=all --enable=typecheck,exception,basic,string,variables --disable=C,W0141,W0603,E1101 `find ./ | grep .py$`
