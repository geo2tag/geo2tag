import sys
sys.path.append("../../")
from test_resource_1 import TestResource1
from test_resource_2 import TestResource2

def getPluginResources():
    result = {'/res2': TestResource1, '/res2':TestResource2}    
    return result

def getPluginInfo():
    info = 'This plugin was creating for present plugins feature. The function getPluginResources for return TestResource1 and TestResource2 '
    return info

def getPluginUrl():
    url = '/instance/plugin/TestPlugin/'
    return url
