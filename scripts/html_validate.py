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


def get_config_parser(config_name):
    config = SafeConfigParser(
        {HOST: DEFAULT_HOST, INSTANCE_PREFI: DEFAULT_PREFIX})
    config.read(config_name)
    return config


def get_host(config_name):
    return get_config_parser(config_name).get(SECTION, HOST)


def get_instance_prefix(config_name):
    return get_config_parser(config_name).get(SECTION, INSTANCE_PREFI)


def get_str(config_name):
    return get_config_parser(config_name).get(SECTION, STR)


def get_list_parser_param(strs):
    return strs.split(' ')


def read_files(path_file):
    new_file = open(path_file)
    new_str = new_file.read()
    new_file.close()
    return new_str


def make_list_pathfile(name_dir, listfile):
    char = ''
    if name_dir[-1] != CH_SLASH:
        char = CH_SLASH
    i = 0
    while i < len(listfile):
        listfile[i] = name_dir + char + listfile[i]
        i += 1
    return listfile


def locale_scanning(name_dir, listfile):
    html_filter_list = []
    if name_dir is not None:
        files = os.listdir(name_dir)
        html_filter = filter(lambda x: x.endswith(HTML), files)
        html_filter_list = make_list_pathfile(name_dir, html_filter)
    else:
        html_filter_list = get_list_parser_param(listfile)
    for filear in html_filter_list:
        validate_file = read_files(filear)
        validate_tidy(validate_file, filear)


def read_url_request(host, list_str):
    for i in list_str:
        file1 = host + i
        fread = urllib.urlopen(file1)
        validate_tidy(fread.read(), file1)


def web_scanning(conf, list_url):
    url_without_str = HTTP + \
        get_host(conf) + CH_SLASH + get_instance_prefix(conf) + CH_SLASH
    if list_url is not None:
        read_url_request(url_without_str, get_list_parser_param(list_url))
    else:
        read_url_request(url_without_str, get_list_parser_param(get_str(conf)))


def validate_tidy(file_context, file):
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
        locale_scanning(args.directory, args.files)
    if args.locale == ARG_NO or args.locale == '0':
        web_scanning(args.conf, args.url)

if __name__ == '__main__':
    run()
