#!/usr/bin/python3
"""
Deploying function
"""
from fabric.api import *


env.hosts = ['107.22.142.168', '54.157.140.107']
env.user = "ubuntu"


def do_clean(number=0):
    """
    Cleaning function
    """

    number = int(number)

    if number == 0:
        number = 2
    else:
        number += 1

    local('cd versions ; ls -t | tail -n +{} | xargs rm -rf'.format(number))
    path = '/data/web_static/releases'
    run('cd {} ; ls -t | tail -n +{} | xargs rm -rf'.format(path, number))
