from find_unsuccessfull_build import reopened_task, get_branch_number
import subprocess

SCRIPT = 'git fetch -a && git merge origin/master'
PIPE = subprocess.PIPE
ERROR_1 = 'Automatic merge failed'
ERROR_2 = 'fatal: Exiting because of an unresolved conflict'


def check_git_conflict(branch):
    result = subprocess.Popen(SCRIPT, shell=True, stdin=PIPE, stdout=PIPE)
    str_result = result.stdout.read()
    if str_result.find(ERROR_1) == -1 or str_result.find(ERROR_2) == -1:
        reopened_task(branch)

if __name__ == '__main__':
    check_git_conflict(get_branch_number())
