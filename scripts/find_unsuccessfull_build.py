import jenkins
import argparse
from jira import JIRA

JOB = 'geo2tag-test'
JENKINS_URL = 'http://jenkins.osll.ru'
JENKINS_USERNAME = 'test.user'
JIRA_USERNAME = 'jira.test.user.geomongo'
PASSWORD = 'iJwF4aLg5FLQXP3a'
JIRA_PROJECT = 'https://geo2tag.atlassian.net'
options = {
    'server': JIRA_PROJECT
}

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


def find_unsuccessfull_build_for_branch(branch):
    server = get_jenkins_server()
    last_build_number = server.get_job_info(
        JOB)[LAST_COMPLETED_BUILD][NUMBER]
    print "Last Build Number: ", last_build_number
    for i in range(last_build_number, 0, -1):
        inf = server.get_build_info(JOB, i)
        print '----------------'
        print len(inf[ACTIONS])
        print inf[ACTIONS]
        print '----------------'
        if len(
            inf[ACTIONS]) == 7 or len(
            inf[ACTIONS]) == 8 or len(
                inf[ACTIONS]) == 6:
            if LAST_BUILD_REVISION in inf[ACTIONS][2]:
                number = 2
            elif LAST_BUILD_REVISION in inf[ACTIONS][3]:
                number = 3
            else:
                print 'branch number for', i, 'build not found'
                continue
        else:
            print 'branch number for', i, 'build not found'
            continue
        index_branch = inf[ACTIONS][number][LAST_BUILD_REVISION][
            BRANCH][0][NAME].find('/') + 1
        found_branch = inf[ACTIONS][number][LAST_BUILD_REVISION][
            BRANCH][0][NAME][index_branch:index_branch + 7]
        if found_branch == branch:
            if inf[RESULT] == SUCCESS or inf[RESULT] == FIXED:
                print 'This task', branch, 'is successfully completed'
            else:
                print 'This task', branch, 'is unsuccessfully completed'
                reopened_task(branch)
            break


def reopened_task(branch):
    jira = JIRA(options, basic_auth=(JIRA_USERNAME, PASSWORD))
    issue = jira.issue(branch)
    jira.transition_issue(issue, u'Reopened')
    jira.add_comment(branch, 'Autotest fail')


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
    branch = get_branch_number()
    find_unsuccessfull_build_for_branch(branch)
