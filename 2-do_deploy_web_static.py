#!/usr/bin/python3
"""point 2"""


from datetime import datetime
import os
from fabric.api import run, put, env


env.hosts = ["34.139.181.5", "3.87.76.93"]


def do_deploy(archive_path):
    """ point2 """

    if not os.path.exists(archive_path):
        return False

    file_ = archive_path.split('.')[0].split('/')[1]
    directory = "/data/web_static/releases/"

    complete = directory + file_

    try:

        put(archive_path, '/tmp')
        run('mkdir -p {}'.format(complete))
        run('tar -xzf /tmp/{}.tgz -C {}'.format(file_, complete))
        run('rm -f /tmp/{}.tgz'.format(file_))
        run('mv {}/web_static/* {}/'.format(complete, complete))
        run('rm -rf {}/web_static'.format(complete))
        run('rm -rf /data/web_static/current')
        run('ln -s {} /data/web_static/current'.format(complete))

        return True

    except:
        return False
