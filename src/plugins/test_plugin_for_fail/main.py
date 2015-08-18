import sys
from test_resource_2 import TestResource2
from test_resource_1 import TestResource1
"""def getPluginResources():
    result = {'res2':TestResource2, 'res1': TestResource1}
    return result"""


def getPluginInfo():
    info = 'This plugin was creating for present plugins feature. The function getPluginResources is for return TestResource1 and TestResource2 '
    return info
