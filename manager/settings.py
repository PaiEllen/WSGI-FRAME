#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONF = os.path.join(BASE_DIR, 'conf')

PY_MYSQL_CONN_DICT = {
    "host": 'host',
    "port": 3306,
    "user": 'username',
    "passwd": 'password',
    "db": 'databasename',
    "charset": 'utf8'
}