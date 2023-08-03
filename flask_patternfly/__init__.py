#!/usr/bin/env python
# coding=utf8

from flask import Blueprint


class Patternfly:
    """
    Doc string.
    Explain your extension in detail here.
    """

    def __init__(self, app=None):
        if app is not None:
            self.init_app(app)

    def init_app(self, app):

        blueprint = Blueprint(
            'patternfly',
            __name__,
            template_folder='templates',
            static_folder='static',
            static_url_path=app.static_url_path + '/patternfly',
        )
        app.register_blueprint(blueprint)
