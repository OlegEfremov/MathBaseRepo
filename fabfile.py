# For full fab documentation see:
# http://docs.fabfile.org/en/1.14/api/core/operations.html

from __future__ import with_statement

from datetime import datetime
import time
from fabric.api import *

import os

env.hosts = ['leobreslav@134.0.118.26:2392']

# Uncomment to ignore execution errors and continue executing
# See http://docs.fabfile.org/en/1.4.1/usage/execution.html#failure-handling
#
# env.warn_only = True


def start():
    run("sudo systemctl start gunicorn")

def stop():
    run("sudo systemctl stop gunicorn")

def restart():
    run("sudo systemctl restart gunicorn")

def status():
    run("sudo systemctl status gunicorn")

def deploy():
    # If any issues with ascii errors just add this commands
    # run('export LC_ALL=en_US.UTF-8')
    # run('export LANG=en_US.UTF-8')

    # Stop gunicorn
    stop()

    with cd('./LBBASE'):
        # get the latest version from master branch
        run('git pull origin master')

        # install requirements
        run('../venv/bin/pip3 install -r ./requirements.txt')

        # migrate data
        run('../venv/bin/python manage.py migrate')

        # collect static
        run('../venv/bin/python manage.py collectstatic')

    # Start gunicorn
    start()



def dump_local_db():
    time_str = datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d_%H%-M-%S')

    dump_filename = 'backup/db/dump_' + time_str + '.sql'

    local('mysqldump --databases lbbase_db > ' + dump_filename + ' -u leobreslav -p')

    return dump_filename


# Dump a prod db with a timestamp
# returns a filename of dump
def dump_prod_db():
    time_str = datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d_%H-%M-%S')

    dump_filename = 'dump_' + time_str + '.sql'

    run('mysqldump --databases lbbase_db > ' + dump_filename + ' -u leobreslav_mysql -p')

    return dump_filename


def replace_prod_db(dump_filename):
    run('mysql -u leobreslav_mysql -p lbbase_db < ' + dump_filename)


def replace_local_db(dump_filename):
    os.system('mysql -u leobreslav -p lbbase_db < ' + dump_filename)
    pass

# This method replaces remote db with local db!

def replace_prod_db_with_local_db():
    #dump local db
    dump_filename = dump_local_db()

    dump_filename_after_upload = 'local_' + dump_filename

    # copy file to server
    put(dump_filename, dump_filename_after_upload)

    # dump prod db
    dump_prod_db()

    # replace prod db with uploaded local db
    replace_prod_db(dump_filename_after_upload)



def replace_local_db_with_prod_db():
    #dump local db
    dump_local_db()

    # dump prod db
    dump_filename = dump_prod_db()

    dump_filename_after_download = 'backup/db/prod_' + dump_filename

    # copy file from server
    get(dump_filename, dump_filename_after_download)


    # replace prod db with uploaded local db
    replace_local_db(dump_filename_after_download)


def download_media():
    # copy file from server

    time_str = datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d_%H%-M-%S')

    path_to_media_prod = './LBBASE/LBBASE_v_0_40/media'
    path_to_media_local = 'backup/media/media_'+time_str
    get(path_to_media_prod, path_to_media_local)
