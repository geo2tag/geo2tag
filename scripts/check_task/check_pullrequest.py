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
URL_ENDING = '?page='



def get_url(team, repository, page):
    if page == 1:
        return BITBUCKET_URL + team + '/' + repository + \
            '/pullrequests'
    else:
        return BITBUCKET_URL + team + '/' + repository + \
            '/pullrequests' + URL_ENDING + str(page)


def check_pullrequest(branch):
    page = 1
    flag = True
    while flag:
        response = requests.get(get_url(TEAM, REPOSITORY, page))
        responseText = json.loads(response.text)
        if responseText[VALUES] == []:
            flag = False
        else:
            for pullrequest in responseText[VALUES]:
                if BRANCH in pullrequest[SOURCE]:
                    if NAME in pullrequest[SOURCE][BRANCH]:
                        if unicode(branch, un_esc) == pullrequest[
                                SOURCE][BRANCH][NAME]:
                            print 'pullrequest exists'
                            return True
        page += 1
    print 'pullrequest is missed'
    return False
