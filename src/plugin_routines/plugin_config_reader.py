from configparser import RawConfigParser
import os

class PluginConfigReader:

    def __init__(self, pluginName):
        self.file_path = os.path.dirname(os.path.realpath(__file__)) + \
            '/config.ini'

    # Return content of the config.ini in a form of a dictionary
    def getConfigContent(self):
        content = {}
        conf = RawConfigParser()
        conf.read(self.file_path)
        sections = conf.sections()
        for section in sections:
            options = conf.options(section)
            parametres = {}
            for option in options:
                value = conf.get(section, option)
                parametres.update({option: value})
            content.update({section: parametres})            
        return content

    # Sets plugin config.ini content to content dictionary
    def setConfigContent(self, content):
        conf = RawConfigParser()
        conf.read(self.file_path)
        for section in content:
            section_items = content[section].items()
            for option, value in section_items:
                if conf.has_section(section) == False:
                    conf.add_section(section)
                conf.set(section, option, value)
        conf.write(open(self.file_path, "w"))

