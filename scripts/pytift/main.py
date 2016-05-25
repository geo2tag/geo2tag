from find_unsuccessfull_build_in_jenkins import \
    find_unsuccessfull_build_for_branch
from check_test_scenario_field import check_test_scenario_field
from check_pullrequest import check_pullrequest
from check_git_conflict import check_git_conflict
from check_git_branch import check_git_branch
from jira_api import get_jira_server, get_jira_issue, reopen_issue, \
    add_comment
from pytift_result_api import get_comment, write_env_var
from get_args_pytift import get_branch_number


FAIL_REASON = "FAIL_REASON"
SUCCESS_MSG = "SUCCESS"


def check_issue(branch):
    jira = get_jira_server()
    issue = get_jira_issue(jira, branch)
    if str(issue.fields.status) == 'Resolved':
        test_scenario_field = check_test_scenario_field(issue)
        if check_git_branch(branch) == True:
            conflict = check_git_conflict(branch)
            pullrequest = check_pullrequest(branch)
            success_build, build_number = find_unsuccessfull_build_for_branch(
                branch)
            if not conflict and pullrequest and success_build and \
                    test_scenario_field:
                print 'This issue', branch, 'is successfully completed'
                comment = 'Test success'
                add_comment(jira, branch, comment)
                write_env_var(FAIL_REASON, SUCCESS_MSG)
            else:
                print 'This issue', branch, 'is unsuccessfully completed'
                comment = get_comment(
                    test_scenario_field,
                    conflict,
                    pullrequest,
                    success_build,
                    build_number)
                reopen_issue(
                    jira,
                    issue,
                    branch,
                    comment)
                write_env_var(FAIL_REASON, comment)
        else:
            if test_scenario_field:
                print 'This issue', branch, 'is successfully completed'
                comment = 'Test success'
                add_comment(jira, branch, comment)
                write_env_var(FAIL_REASON, SUCCESS_MSG)
            else:
                print 'This issue', branch, 'is unsuccessfully completed'
                comment = get_comment(False)
                reopen_issue(jira, issue, branch, comment)
                write_env_var(FAIL_REASON, comment)
    else:
        write_env_var(FAIL_REASON, SUCCESS_MSG)


if __name__ == '__main__':
    check_issue(get_branch_number())
