from redmine import Redmine
from get_args_pytift import get_branch_number
from check_test_scenario_field import check_test_scenario_field

USER = 'pytift.test.bot'
PASSWORD = 'pytift.test.bot'
COMPANY = 'https://dev.osll.ru'
TEST_COMMENT = 'test comment'
REOPENED = 14
DONE = 3
RESOURCES = u'resources'
NAME = u'name'
TEST_SCENARIO = u'Test scenario'
VALUE = u'value'


def get_redmine_server():
    redmine = Redmine(COMPANY, username=USER, password=PASSWORD)
    return redmine


def get_redmine_issue(redmine, branch):
    issue = redmine.issue.get(branch)
    return issue


def add_comment(issue, comment):
    issue.notes = comment
    issue.save()


def is_issue_resolved(issue):
    return issue.status_id == DONE


def transition_issue(issue, status):
    issue.status_id = status
    issue.save()


def get_test_scenario_field(issue):
    list_resources = issue.custom_fields[RESOURCES]
    for resource in list_resources:
        if resource[NAME] == TEST_SCENARIO:
            return resource[VALUE]
    return None


# for tests
def main(branch):
    redmine = get_redmine_server()
    issue = get_redmine_issue(redmine, branch)
    check_test_scenario_field(get_test_scenario_field(issue))


if __name__ == '__main__':
    main(get_branch_number())
