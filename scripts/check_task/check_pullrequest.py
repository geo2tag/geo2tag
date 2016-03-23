import json
import requests

BITBUCKET_URL = 'https://api.bitbucket.org/2.0/repositories/'
TEAM = 'osll'
REPOSITORY = 'geomongo'
VALUES = u'values'
SOURCE = u'source'
NAME = u'name'
BRANCH = u'branch'
un_esc = 'unicode-escape'


def get_url(team, repository):
    return BITBUCKET_URL + team + '/' + repository + \
        '/pullrequests?state=[OPEN]'


def check_pullrequest(branch):
    response = requests.get(get_url(TEAM, REPOSITORY))
    responseText = json.loads(response.text)
    for pullrequest in responseText[VALUES]:
        if BRANCH in pullrequest[SOURCE]:
            if NAME in pullrequest[SOURCE][BRANCH]:
                if unicode(branch, un_esc) == pullrequest[
                        SOURCE][BRANCH][NAME]:
                    print 'pullrequest exists'
                    return True
    print 'pullrequest is missed'
    return False
