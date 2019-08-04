# -*- coding: utf-8 -*-
from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)

from os.path import dirname, join
import sys

# manually inject libs
current_path = dirname(__file__)
sys.path.extend(
    (join(current_path, "../libs/compiled.zip"),)
)

from requests_toolbelt.adapters import appengine

appengine.monkeypatch(validate_certificate=False)

import urllib3

urllib3.disable_warnings()
