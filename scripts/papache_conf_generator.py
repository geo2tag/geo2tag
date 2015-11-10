#!/usr/bin/python
import argparse

TEMPLATE_CONF = 'config/template.conf'
SAVE_FOLDER = 'config/'

SERVER_NAME = '%server_name%'
SERVER_FOLDER = '%geomongo_path%'
SERVER_ERROR_LOG = '%error_log%'
SERVER_PORT = '%server_port%'
PRE_DERECTIVES = '%pre_derectives%'

DEFAULT_PORT = 80


def generate(site_name, site_folder, file_name, error_log, port):
    with open(TEMPLATE_CONF, 'r') as conf_file:
        template = conf_file.read()

    template = template \
        .replace(SERVER_NAME, site_name) \
        .replace(SERVER_FOLDER, site_folder) \
        .replace(SERVER_ERROR_LOG, error_log) \
        .replace(SERVER_PORT, unicode(port))

    pre_derectives = ''
    if port != DEFAULT_PORT:
        pre_derectives = 'Listen {}'.format(port)

    template = template \
        .replace(PRE_DERECTIVES, pre_derectives)

    with open(SAVE_FOLDER + file_name, 'w') as res_file:
        res_file.write(template)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', '--name', required=True)
    parser.add_argument('-o', '--output', default='output.conf')
    parser.add_argument('-f', '--folder', default='geomongo')
    parser.add_argument('-e', '--error', default='error')
    parser.add_argument('-p', '--port', default=DEFAULT_PORT, type=int)
    args = parser.parse_args()
    generate(args.name, args.folder, args.output, args.error, args.port)
