from github import Github
from main import get_branch_number

GITHUB_USERNAME = 'TestUserGeomongoGithub'
PASSWORD = 'ND3GyNHCpxweSqC2'
OPEN = 'open'


def get_github_server():
    github = Github(GITHUB_USERNAME, PASSWORD)
    return github


def main(branch):
    ghs = get_github_server()
    repo = g.get_user().get_repos()[0]
    list_pulls = repo.get_pulls(OPEN)
    for pullrequest in list_pulls:
        if pullrequest.title == branch:
            return True
    else:
         return False


if __name__ == '__main__':
    main(get_branch_number())
