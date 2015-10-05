#!/bin/bash
echo -e "Install Selenium"
pip install selenium

echo -e "Start xvfb"
exec -a xvfb Xvfb :1 -screen 0 1024x768x16 &> xvfb.log  &

DISPLAY=:1.0
export DISPLAY

echo -e "Run tests"
./scripts/run_selenium_tests.sh
echo -e "Stop xvfb"
kill $(pgrep -f xvfb)