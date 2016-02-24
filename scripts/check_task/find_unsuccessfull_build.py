import json
import jenkins
import argparse
from jira import JIRA
from check_test_scenario_field import check_test_scenario_field
import requests

JOB = 'geo2tag-test'
JENKINS_URL = 'http://jenkins.osll.ru'
JENKINS_USERNAME = 'test.user'
JIRA_USERNAME = 'jira.test.user.geomongo'
PASSWORD = 'iJwF4aLg5FLQXP3a'
JIRA_PROJECT = 'https://geo2tag.atlassian.net'
options = {
    'server': JIRA_PROJECT
}
BITBUCKET_URL = 'https://api.bitbucket.org/2.0/repositories/'
TEAM = 'osll'
REPOSITORY = 'geomongo'
un_esc = 'unicode-escape'
# for search branch number
ACTIONS = u'actions'
LAST_BUILD_REVISION = u'lastBuiltRevision'
NAME = u'name'
BRANCH = u'branch'
RESULT = u'result'
SUCCESS = u'SUCCESS'
FIXED = u'FIXED'
ARG_BRANCH = '--branch'
NUMBER = 'number'
LAST_COMPLETED_BUILD = 'lastCompletedBuild'
VALUES = u'values'
SOURCE = u'source'


def get_url(team, repository):
    return BITBUCKET_URL + team + '/' + repository + \
        '/pullrequests?state=[OPEN]'


def get_jira_server():
    jira = JIRA(options, basic_auth=(JIRA_USERNAME, PASSWORD))
    return jira


def check_issue(branch):
    jira = get_jira_server()
    issue = get_jira_issue(jira, branch)
    test_scenario_field = check_test_scenario_field(issue)
    pullrequest = check_pullrequest(branch)
    print 'Pullrequest ', pullrequest
    if test_scenario_field:
        find_unsuccessfull_build_for_branch(jira, issue, branch)


def check_pullrequest(branch):
    response = requests.get(get_url(TEAM, REPOSITORY))
    responseText = json.loads(response.text)
    for pullrequest in responseText[VALUES]:
        if BRANCH in pullrequest[SOURCE]:
            if NAME in pullrequest[SOURCE][BRANCH]:
                if unicode(branch, un_esc) == pullrequest[
                        SOURCE][BRANCH][NAME]:
                    return True
    return False


def find_unsuccessfull_build_for_branch(jira, issue, branch):
    server = get_jenkins_server()
    last_build_number = server.get_job_info(
        JOB)[LAST_COMPLETED_BUILD][NUMBER]
    print "Last Build Number: ", last_build_number
    for i in range(last_build_number, 0, -1):
        inf = server.get_build_info(JOB, i)
        if LAST_BUILD_REVISION in inf[ACTIONS][2]:
            number = 2
        elif LAST_BUILD_REVISION in inf[ACTIONS][3]:
            number = 3
        else:
            print 'branch number for', i, 'build not found'
            continue
        index_branch = inf[ACTIONS][number][LAST_BUILD_REVISION][
            BRANCH][0][NAME].find('/') + 1
        found_branch = inf[ACTIONS][number][LAST_BUILD_REVISION][
            BRANCH][0][NAME][index_branch:index_branch + 7]
        if found_branch == branch:
            if inf[RESULT] == SUCCESS or inf[RESULT] == FIXED:
                print 'This issue', branch, 'is successfully completed'
            else:
                print 'This issue', branch, 'is unsuccessfully completed'
                reopen_issue(jira, issue, branch)
            break


def get_jira_issue(jira, branch):
    branch = branch[0:7]
    issue = jira.issue(branch)
    return issue


def reopen_issue(jira, issue, branch, comment='Autotest fail'):
    transition_issue(jira, issue, u'Reopened')
    add_comment(jira, branch, comment)


def transition_issue(jira, issue, status):
    jira.transition_issue(issue, status)


def add_comment(jira, branch, comment):
    jira.add_comment(branch, comment)


def get_branch_number():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        ARG_BRANCH,
        required=True)
    args = parser.parse_args()
    return args.branch


def get_jenkins_server():
    server = jenkins.Jenkins(
        JENKINS_URL,
        username=JENKINS_USERNAME,
        password=PASSWORD)
    return server


if __name__ == '__main__':
    check_issue(get_branch_number())
