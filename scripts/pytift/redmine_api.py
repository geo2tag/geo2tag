from redmine import Redmine
from get_args_pytift import get_branch_number

USER = 'pytift.test.bot'
PASSWORD = 'pytift.test.bot'
COMPANY = 'https://dev.osll.ru'
TEST_COMMENT = 'test comment'
REOPENED = 14
DONE = 3


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


# for tests
def main(branch):
    redmine = get_redmine_server()
    issue = get_redmine_issue(redmine, branch)
    transition_issue(issue, DONE)
    if is_issue_resolved(issue):
        transition_issue(issue, REOPENED)
    comment = TEST_COMMENT
    add_comment(issue, comment)


if __name__ == '__main__':
    main(get_branch_number())
