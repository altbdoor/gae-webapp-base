# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function, unicode_literals

from base import Base


class Example(Base):
    def get_hello_world(self):
        # the write_json method is inherited from Base
        self.write_json('hello world')
