#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging
import routes
import webob
import webob.dec
import webob.exc
import routes.middleware as middleware

from app.utils.common import import_object
from manager.urls import url_list
from manager.wsgi import Resource
from backend.middleware.base import Request

LOG = logging.getLogger(__name__)


class Router(object):
    def __init__(self):
        self.mapper = routes.Mapper()
        for url_item in url_list:
            self.mapper.resource('%s' % (url_item[0]), '%s' % (url_item[1]),
                                 controller=Resource(import_object(url_item[2])))
        self._router = routes.middleware.RoutesMiddleware(self._dispatch,
                                                          self.mapper)

    @webob.dec.wsgify(RequestClass=Request)
    def __call__(self, req):
        return self._router

    @classmethod
    def factory(cls, global_conf, **local_conf):
        return cls()

    @staticmethod
    @webob.dec.wsgify(RequestClass=Request)
    def _dispatch(req):
        match = req.environ['wsgiorg.routing_args'][1]
        if not match:
            return webob.exc.HTTPNotFound()
        app = match['controller']
        return app
