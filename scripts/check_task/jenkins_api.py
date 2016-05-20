import jenkins

JOB = 'geo2tag-test'
JENKINS_URL = 'http://jenkins.osll.ru'
JENKINS_USERNAME = 'test.user'
PASSWORD = 'iJwF4aLg5FLQXP3a'
JOB_URL = 'jenkins.osll.ru/job/geo2tag-test/'


def get_jenkins_server():
    server = jenkins.Jenkins(
        JENKINS_URL,
        username=JENKINS_USERNAME,
        password=PASSWORD)
    return server


def get_jenkins_build_result(build_number):
    result = JOB_URL + str(build_number) + '/console'
    return result
