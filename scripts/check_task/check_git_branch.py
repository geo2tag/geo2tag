#!/usr/bin/env python
# -*- coding: utf-8 -*-
import subprocess
from find_unsuccessfull_build import get_branch_number

SCRIPT = 'git branch -a | grep '


def check_git_branch(branch):
    p = subprocess.Popen(SCRIPT + branch, shell=True, stdout=subprocess.PIPE)
    out = p.stdout.read() 
    result = out.split()
    if result == []:
        print "This branch doesn't exist"
    else:
        print 'This branch exists'

if __name__ == '__main__':
    check_git_branch(get_branch_number())
