import subprocess

CHECKOUT_SCRIPT = 'git checkout '
PULL_SCRIPT = '&& git pull origin '
MERGE_SCRIPT = '&& git fetch -a && git merge origin/master'
PIPE = subprocess.PIPE
ERROR_1 = 'Automatic merge failed'
ERROR_2 = 'fatal: Exiting because of an unresolved conflict'


def check_git_conflict(branch):
    result = subprocess.Popen(
        CHECKOUT_SCRIPT +
        branch +
        PULL_SCRIPT + 
        branch +
        MERGE_SCRIPT,
        shell=True,
        stdin=PIPE,
        stdout=PIPE)
    str_result = result.stdout.read()
    print str_result
    if str_result.find(ERROR_1) != -1 or str_result.find(ERROR_2) != -1:
        return True
    else:
        return False
