from configparser import RawConfigParser


class PluginConfigReader:

    def __init__(self, pluginName):
        self.file_path = os.path.dirname(os.path.realpath(__file__)) + \
            'config.ini'

    # Return content of the config.ini in a form of a dictionary
    def getConfigContent(self):
        print '---------------------------'
        conf = ConfigParser.RawConfigParser()
        conf.read(self.file_path)
        print conf.sections()
        print '---------------------------'
        return conf

    # Sets plugin config.ini content to content dictionary
    def setConfigContent(self, content):
        pass
