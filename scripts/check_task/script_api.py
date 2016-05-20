from jenkins_api import get_jenkins_build_result
import argparse

PROPSFILE = 'propsfile'
MODE_AW = 'aw'
ARG_BRANCH = '--branch'


def write_env_var(variable, value):
    f = open(PROPSFILE, MODE_AW)
    f.write(variable + '=' + value + '\n')
    f.close()


def get_branch_number():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        ARG_BRANCH,
        required=True)
    args = parser.parse_args()
    return args.branch


def get_comment(test_scenario_field=True, conflict=False, pullrequest=True,
                success_build=True, build_number=0):
    result = 'Test failed. \n'
    if not test_scenario_field:
        result += 'test scenario is missing\n'
    if conflict:
        result += 'conflicts exist at branch\n'
    if not pullrequest:
        result += 'pullrequest is missing\n'
    if not success_build:
        result += 'auto tests failed, link '
        result += 'http://' + get_jenkins_build_result(build_number)
    return result
