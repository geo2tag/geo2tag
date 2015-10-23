import sys, os
sys.path.insert(0, os.path.dirname(os.path.realpath(__file__)))
import logging
# set all errors output to stderr
logging.basicConfig(stream=sys.stderr)

from main import addResources
from rest_api_routines import getApp

addResources()
application = getApp()
