# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function, unicode_literals

from webapp2 import RequestHandler

import json


class Base(RequestHandler):
    def __init__(self, request, response):
        self.initialize(request, response)

    def write_json(self, data):
        # https://code.google.com/p/googleappengine/issues/detail?id=7116
        # self.response.headers[b'Access-Control-Allow-Origin'] = b'*'
        self.response.headers[b'Content-Type'] = b'application/json'
        self.response.out.write(json.dumps(data))
