from requests import get
from argparse import ArgumentParser
import sys

SUCCESS_CODE = 200


def checkSingleUrl(hostName, url):
    fullUrl = hostName + url
    response = get(fullUrl)
    code = response.status_code
    print "Checking url={} , code={}".format(fullUrl, code)
    if code != SUCCESS_CODE:
        print "Error!"
        sys.exit(1)


def checkUrlList(hostName, fileName):
    with open(fileName) as urlFile:
        for url in urlFile:
            checkSingleUrl(hostName, url)


def parseArguments():
    parser = ArgumentParser(description='Url list checker (by return code)')
    parser.add_argument(
        '--hostName',
        help='base address (e.g. http://site/)',
        type=unicode,
        required=True)
    parser.add_argument(
        '--fileName',
        help='file with url list, one on new line',
        type=unicode,
        required=True)
    return parser.parse_args()


if __name__ == '__main__':
    arguments = parseArguments()
    print arguments
    checkUrlList(arguments.hostName, arguments.fileName)
