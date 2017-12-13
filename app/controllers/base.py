#!/usr/bin/env python
# -*- coding: utf-8 -*-
# CONTROLLER 逻辑处理接口


class TestController(object):

    def index(self, req):
        return 'GET'

    def create(self, req):
        return 'POST'

    def delete(self, req):
        return 'DELETE'

    def update(self, req):
        return 'PUT'
