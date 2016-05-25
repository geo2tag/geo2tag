from redmine import Redmine
from get_args_pytift import get_branch_number

USER = 'pytift.test.bot'
PASSWORD = 'pytift.test.bot'
COMPANY = 'https://dev.osll.ru'
TEST_COMMENT = 'test comment'


def get_redmine_server():
    redmine = Redmine(COMPANY, username=USER, password=PASSWORD)
    return redmine


def get_redmine_issue(redmine, branch):
    issue = redmine.issue.get(branch)
    return issue


def add_comment(issue, comment):
    issue.notes = comment
    issue.save()


def main(branch):
    redmine = get_redmine_server()
    issue = get_redmine_issue(redmine, branch)
    comment = TEST_COMMENT
    add_comment(issue, comment)


if __name__ == '__main__':
    main(get_branch_number())
