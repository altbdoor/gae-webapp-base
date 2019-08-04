# -*- coding: utf-8 -*-
from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)

import shim  # noqa
from flask import Flask, render_template

app = Flask(__name__)
app.config.update(DEBUG=False, TEMPLATES_AUTO_RELOAD=True)


@app.route("/", methods=("GET",))
def home():
    context = {
        "project": "gae-webapp-base",
        "license": "MIT",
    }
    return render_template("home.html", **context)


@app.errorhandler(404)
def page_not_found(error):
    return (render_template("404.html"), 404)
