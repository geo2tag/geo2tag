from github import Github
from script_api import get_branch_number

GITHUB_USERNAME = 'TestUserGeomongoGithub'
PASSWORD = 'ND3GyNHCpxweSqC2'
OPEN = 'open'
REPO = 'pytift_experimental'


def get_github_instance():
    github = Github(GITHUB_USERNAME, PASSWORD)
    return github


def main(branch):
    ghs = get_github_instance()
    list_repo = ghs.get_user().get_repos()
    for repo in list_repo:
        if repo.name == REPO:
            right_repo = repo
            break
    list_pulls = right_repo.get_pulls(OPEN)
    for pullrequest in list_pulls:
        if pullrequest.title == branch:
            print 'pullrequest exists'
            return True
    print 'pullrequest is missed'
    return False


if __name__ == '__main__':
    main(get_branch_number())
