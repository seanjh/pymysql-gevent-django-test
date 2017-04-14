#!/usr/bin/env python
from gevent import monkey
monkey.patch_all()

import os
import sys


def handle_pymysql():
    try:
        i = sys.argv.index('pymysql')
    except ValueError:
        return

    import pymysql
    pymysql.install_as_MySQLdb()
    sys.argv.pop(i)
    print("DEBUG: enabled pymysql")


if __name__ == "__main__":
    handle_pymysql()

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dgtest.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
