from config_reader import getInstancePrefix
def getPluginUrl(url, pluginName):
    return '/' + getInstancePrefix() + '/plugin/' + pluginName + '/' + url
