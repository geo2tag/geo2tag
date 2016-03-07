from find_unsuccessfull_build_in_jenkins import \
    find_unsuccessfull_build_for_branch
from check_test_scenario_field import check_test_scenario_field
from check_pullrequest import check_pullrequest
from check_git_conflict import check_git_conflict
from check_git_branch import check_git_branch
from jira_api import get_jira_server, get_jira_issue, reopen_issue
import argparse

ARG_BRANCH = '--branch'


def check_issue(branch):
    jira = get_jira_server()
    issue = get_jira_issue(jira, branch)
    test_scenario_field = check_test_scenario_field(issue)
    if check_git_branch(branch) == True:
        conflict = check_git_conflict(branch)
        pullrequest = check_pullrequest(branch)
        success_build = find_unsuccessfull_build_for_branch(branch)
        if not conflict and pullrequest and success_build and \
                test_scenario_field:
            print 'This issue', branch, 'is successfully completed'
        else:
            print 'This issue', branch, 'is unsuccessfully completed'
            reopen_issue(
                jira,
                issue,
                branch,
                get_comment(
                    test_scenario_field,
                    conflict,
                    pullrequest,
                    success_build))
    else:
        if test_scenario_field:
            print 'This issue', branch, 'is successfully completed'
        else:
            print 'This issue', branch, 'is unsuccessfully completed'
            reopen_issue(jira, issue, branch, get_comment(False))


def get_branch_number():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        ARG_BRANCH,
        required=True)
    args = parser.parse_args()
    return args.branch


def get_comment(test_scenario_field=True, conflict=False, pullrequest=True,
                success_build=False):
    result = 'Autotest fail. "True" means existence. \n'
    result += 'testscenario ' + test_scenario_field + ' conflict ' + \
        conflict, ' pullrequest ' + pullrequest + ' success_build ' + \
        success_build
    return result


if __name__ == '__main__':
    check_issue(get_branch_number())
