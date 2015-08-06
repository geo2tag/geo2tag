from config_reader import getInstancePrefix


def getPathWithPrefix(url):
    path = '/' + getInstancePrefix() + url
    return path
