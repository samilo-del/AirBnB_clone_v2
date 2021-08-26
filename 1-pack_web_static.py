#!/usr/bin/python3
""" function do_pack. """

from datetime import datetime
import os
from fabric.api import local


def do_pack():
    """ ... """
    try:
        form = datetime.now().strftime("%Y%m%d%H%M%S")
        if not os.path.exists("versions"):
            os.mkdir("versions")

        f1le = "versions/web_static_{}.tgz".format(form)
        local("tar -cvzf {} web_static".format(f1le))
        return f1le
    except:
        return(None)
