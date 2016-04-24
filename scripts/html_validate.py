import sys
import argparse
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


def read_url_request(host, list_str):
    num_error = 0
    for i in list_str:
        file1 = host + i
        fread = url_request(file1)
        num_error = validate_tidy(fread.read(), file1)
    if num_error == 0:
        print 'HTML files not contain warning or errors'
    else:
        print 'HTML files contain warning or errors'
    sys.exit(num_error)


def url_request(url):
    return urllib.urlopen(url)


def web_scanning(conf, list_url):
    url_without_str = HTTP + \
        get_host(conf) + CH_SLASH + get_instance_prefix(conf) + CH_SLASH
    if list_url is not None:
        read_url_request(url_without_str, get_list_parser_param(list_url))
    else:
        read_url_request(url_without_str, get_list_parser_param(get_str(conf)))


def validate_tidy(file_context, file_name):
    num_error = 0
    print '========================' + file_name + '========================'
    document, errors = tidy_document(
        file_context, options={"literal-attributes": '0'})
    print document, errors
    if len(errors) != 0:
        num_error = 1
    return num_error


def run():
    parser = argparse.ArgumentParser(description='Script HTML lint')
    parser.add_argument('--url', help='List url')
    parser.add_argument('--conf', help='Config name')
    args = parser.parse_args()
    web_scanning(args.conf, args.url)

if __name__ == '__main__':
    run()
