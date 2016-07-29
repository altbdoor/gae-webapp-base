# -*- coding: utf-8 -*-

from os.path import dirname, join
import sys
import webapp2

# import the config
import config

# import apps and libs
current_path = dirname(__file__)

sys.path.extend((
    join(current_path, 'apps'),
    join(current_path, 'libs/compiled.zip'),
))

# format the routes
formatted_routes = []
for route in config.routes:
    path = '/api/{filename}/{method}'.format(
        filename=route[1].lower(),
        method=route[2].replace('_', '-')
    )

    handler = 'apps.{filename}.{_class}'.format(
        filename=route[1].lower(),
        _class=route[1]
    )

    formatted_routes.append(
        webapp2.Route(
            path,
            handler=handler,
            handler_method=route[2],
            methods=[route[0].upper()]
        )
    )

# run the app
app = webapp2.WSGIApplication(formatted_routes, debug=config.debug)
