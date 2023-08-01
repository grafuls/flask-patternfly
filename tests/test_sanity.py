def test_can_import_package():
    import flask_patternfly


def test_can_initialize_app_and_extesion():
    from flask import Flask
    from flask_patternfly import Patternfly

    app = Flask(__name__)
    Patternfly(app)
