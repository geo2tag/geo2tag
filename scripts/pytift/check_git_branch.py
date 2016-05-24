#!/usr/bin/env python
# -*- coding: utf-8 -*-
import subprocess

SCRIPT = 'git branch -a | grep '


def check_git_branch(branch):
    p = subprocess.Popen(SCRIPT + branch, shell=True, stdout=subprocess.PIPE)
    out = p.stdout.read()
    result = out.split()
    if result == []:
        print "This branch doesn't exist"
        return False
    else:
        print 'This branch exists'
        return True
