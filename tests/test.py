#!/usr/bin/env python
# -*- coding: utf-8 -*-
import eventlet
from eventlet import wsgi
from paste.deploy import loadapp
import routes
import routes.middleware as middleware
import webob.dec
import webob.exc

from manager.settings import CONF


class TestController(object):

    def index(self, req):
        return 'GET'

    def create(self, req):
        return 'POST'

    def delete(self, req):
        return 'DELETE'

    def update(self, req):
        return 'PUT'


class Resource(object):
    def __init__(self, controller):
        self.controller = controller()

    @webob.dec.wsgify
    def __call__(self, req):
        match = req.environ['wsgiorg.routing_args'][1]
        action = match['action']
        if hasattr(self.controller, action):
            method = getattr(self.controller, action)
            return method(req)
        return webob.exc.HTTPNotFound()


class TestApplication(object):
    def __init__(self):
        self.mapper = routes.Mapper()
        self.mapper.resource('test', 'tests', controller=Resource(TestController))
        self.router = middleware.RoutesMiddleware(self.dispatch, self.mapper)

    @webob.dec.wsgify
    def __call__(self, req):
        return self.router

    @classmethod
    def factory(cls, global_conf, **local_conf):
        return cls()

    @staticmethod
    @webob.dec.wsgify
    def dispatch(req):
        match = req.environ['wsgiorg.routing_args'][1]
        return match['controller'] if match else webob.exc.HTTPNotFound()


if '__main__' == __name__:
    application = loadapp('config:%s/config.ini' % (CONF))
    server = eventlet.spawn(wsgi.server,
                            eventlet.listen(('0.0.0.0', 8080)), application)
    server.wait()
