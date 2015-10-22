from astroid import MANAGER
from astroid import scoped_nodes

NAME_DEF_GET_PLUGIN_RESOURCE = 'getPluginResources'
NAME_DEF_GET_PLUGIN_INFO = 'getPluginInfo'


def transform(cls):

    check = 0
    if NAME_DEF_GET_PLUGIN_RESOURCE not in cls.locals \
            and NAME_DEF_GET_PLUGIN_INFO not in cls.locals:
        print '======= Module: ' + cls.name + ' ======='
    if NAME_DEF_GET_PLUGIN_RESOURCE not in cls.locals:
        print 'No required function ' + NAME_DEF_GET_PLUGIN_RESOURCE

    if NAME_DEF_GET_PLUGIN_INFO not in cls.locals:
        print 'No required function ' + NAME_DEF_GET_PLUGIN_INFO


def register(linter):
    pass

MANAGER.register_transform(scoped_nodes.Module, transform)
