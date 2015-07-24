import sys
sys.path.append('../../')
from url_utils import getPathWithPrefix
from testResource_GT_1416 import Resource_GT_1416

def getPluginResources():
    print '1111111111'
    return [{'/service/GT_1416': Resource_GT_1416}]

def getPluginInfo():
    return 'testPlugin1'