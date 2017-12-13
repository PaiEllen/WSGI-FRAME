#!/usr/bin/env python
# -*- coding: utf-8 -*-


class IPBlacklistMiddleware(object):
    def __init__(self, application):
        self.application = application

    def __call__(self, environ, start_response):
        ip_addr = environ.get('HTTP_HOST').split(':')[0]
        if ip_addr not in ('127.0.0.1'):
            start_response('403 Forbidden', [('Content-Type', 'text/plain')])
            return ['Forbidden']

        return self.application(environ, start_response)

    @classmethod
    def factory(cls, global_conf, **local_conf):
        def _factory(application):
            return cls(application)

        return _factory
