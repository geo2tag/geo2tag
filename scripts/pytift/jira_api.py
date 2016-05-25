from jira import JIRA

JIRA_USERNAME = 'jira.test.user.geomongo'
PASSWORD = 'iJwF4aLg5FLQXP3a'
JIRA_PROJECT = 'https://geo2tag.atlassian.net'
options = {
    'server': JIRA_PROJECT
}


def get_jira_server():
    jira = JIRA(options, basic_auth=(JIRA_USERNAME, PASSWORD))
    return jira


def get_jira_issue(jira, branch):
    branch = branch[0:7]
    issue = jira.issue(branch)
    return issue


def get_test_scenario_field(issue):
    return issue.fields.customfield_10800


def reopen_issue(jira, issue, branch, comment='Autotest fail'):
    transition_issue(jira, issue, u'Reopened')
    add_comment(jira, branch, comment)


def transition_issue(jira, issue, status):
    jira.transition_issue(issue, status)


def add_comment(jira, branch, comment):
    jira.add_comment(branch, comment)
