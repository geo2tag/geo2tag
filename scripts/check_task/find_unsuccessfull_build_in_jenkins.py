from jenkins_api import get_jenkins_server

un_esc = 'unicode-escape'
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
SOURCE = u'source'
JOB = 'geo2tag-test'


def find_unsuccessfull_build_for_branch(branch):
    server = get_jenkins_server()
    last_build_number = server.get_job_info(
        JOB)[LAST_COMPLETED_BUILD][NUMBER]
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
                return True
            else:
                return False
    return False
