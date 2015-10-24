#!/usr/bin/python
import argparse
import sys

TEMPLATE_CONF = 'config/template.conf'
SAVE_FOLDER = 'config/'


def generate(site_name, site_folder, file_name, error_log):
    with open(TEMPLATE_CONF, 'r') as conf_file:
        template = conf_file.read()

    template = template.replace('%server_name%', site_name) \
        .replace('%geomongo_path%', site_folder) \
        .replace('%error_log%', error_log)

    with open(SAVE_FOLDER + file_name + '.conf', 'w') as res_file:
        res_file.write(template)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', '--name', required=True)
    parser.add_argument('-o', '--output', default="output")
    parser.add_argument('-f', '--folder', default='/var/www/geomongo')
    parser.add_argument('-e', '--error', default='error')
    args = parser.parse_args()

    generate(args.name, args.folder, args.output, args.error)