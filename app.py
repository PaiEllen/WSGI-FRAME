#!/usr/bin/env python
# -*- coding: utf-8 -*-
import eventlet
from eventlet import wsgi
from paste.deploy import loadapp

from manager.settings import CONF

if '__main__' == __name__:
    application = loadapp('config:%s/config.ini' % CONF)
    server = eventlet.spawn(wsgi.server,
                            eventlet.listen(('127.0.0.1', 8080)), application)
    server.wait()
