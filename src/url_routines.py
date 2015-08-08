from config_reader import getInstancePrefix


def getPluginUrl(url, pluginName):
    return '/' + getInstancePrefix() + '/plugin/' + pluginName + '/' + url


def isPluginUrl(url):
    substrUrl = getInstancePrefix() + '/plugin/'
    if url.find(substrUrl) != -1:
        return True
    return False
