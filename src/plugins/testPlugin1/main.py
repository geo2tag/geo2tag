import sys
sys.path.append('../../')
from url_utils import getPathWithPrefix

def getPluginResources():
	print '1111111111'
    return {getPathWithPrefix('/service/GT_1416'): 'testResource_GT_1416'}

def getPluginInfo():
	return 'testPlugin1'