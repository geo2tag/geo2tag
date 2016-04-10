import argparse
import os
import urllib
from configparser import SafeConfigParser
from tidylib import tidy_document

SECTION = 'main'
HOST = 'host'
INSTANCE_PREFI = 'instance_path'
DEFAULT_HOST = 'geomongo'
DEFAULT_PREFIX = 'instance'
STR = 'str'
DEFAULT_STR = 'status'
CH_SLASH = '/'
ARG_YES = 'yes'
ARG_NO = 'no'
HTML = '.html'
HTTP = 'http://'


def getConfigParser(config_name):
    config = SafeConfigParser(
        {HOST: DEFAULT_HOST, INSTANCE_PREFI: DEFAULT_PREFIX})
    config.read(config_name)
    return config


def getHost(config_name):
    return getConfigParser(config_name).get(SECTION, HOST)


def getInstancePrefix(config_name):
    return getConfigParser(config_name).get(SECTION, INSTANCE_PREFI)


def getInstancePrefix(config_name):
    return getConfigParser(config_name).get(SECTION, INSTANCE_PREFI)


def getStr(config_name):
    return getConfigParser(config_name).get(SECTION, STR)


def getListParserParam(str):
    return str.split(' ')


def readFiles(path_file):
    new_file = open(path_file)
    new_str = new_file.read()
    new_file.close()
    return new_str


def makeListPathFile(name_dir, listfile):
    ch = ''
    if name_dir[-1] != CH_SLASH:
        ch = CH_SLASH
    i = 0
    while i < len(listfile):
        listfile[i] = name_dir + ch + listfile[i]
        i += 1
    return listfile


def LocaleScanning(name_dir, listfile):
    if name_dir is not None:
        files = os.listdir(name_dir)
        html_filter = mytxt = filter(lambda x: x.endswith(HTML), files)
        html_filter = makeListPathFile(name_dir, html_filter)
        for file in html_filter:
            validate_file = readFiles(file)
            ValidateTidy(validate_file, file)
    else:
        files = getListParserParam(listfile)
        ValidateTidy(files)


def readUrlRequest(host, list_str):
    for i in list_str:
        file = host + i
        f = urllib.urlopen(file)
        ValidateTidy(f.read(), file)


def WebScanning(conf, list_url):
    url_without_str = HTTP + \
        getHost(conf) + CH_SLASH + getInstancePrefix(conf) + CH_SLASH
    if list_url is not None:
        readUrlRequest(url_without_str, getListParserParam(list_url))
    else:
        readUrlRequest(url_without_str, getListParserParam(getStr(conf)))


def ValidateTidy(file_context, file):
    print '========================' + file + '========================'
    document, errors = tidy_document(
        file_context, options={"literal-attributes": '0'})
    print document, errors


def run():
    parser = argparse.ArgumentParser(description='Script HTML lint')
    parser.add_argument('--locale', help='Locale validate')
    parser.add_argument('--directory', help='Directory containing files')
    parser.add_argument('--files', help='List file name')
    parser.add_argument('--url', help='List url')
    parser.add_argument('--conf', help='Config name')
    args = parser.parse_args()
    if args.locale == ARG_YES or args.locale == '1':
        LocaleScanning(args.directory, args.files)
    if args.locale == ARG_NO or args.locale == '0':
        WebScanning(args.conf, args.url)

if __name__ == '__main__':
    run()
