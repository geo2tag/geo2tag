import sys
sys.path.append('../../')
from testResource_GT_1417 import Resource_GT_1417

def getPluginResources():
    return {'service/GT_1417': Resource_GT_1417}

def getPluginInfo():
    return 'testPlugin1'