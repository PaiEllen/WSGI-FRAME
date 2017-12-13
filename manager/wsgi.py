#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

import webob.dec
import webob.exc
from paste import deploy

from manager.settings import CONF


class Loader(object):
    def __init__(self, config_path=None):
        self.config_path = None

        config_path = config_path or CONF
        if not os.path.isabs(config_path):
            self.config_path = CONF.find_file(config_path)
        elif os.path.exists(config_path):
            self.config_path = config_path

        if not self.config_path:
            raise Exception("Could not find config at %(path)s")

    def load_app(self, name):

        try:
            return deploy.loadapp("config:%s" % self.config_path, name=name)
        except LookupError:
            raise Exception("Could not load paste app '%(name)s' from %(path)s")


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
