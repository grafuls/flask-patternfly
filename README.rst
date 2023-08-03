======================
Flask PatternFly
======================

* Free software: GPLv3

Usage
-----

Here is an example::

  from flask_patternfly import Patternfly

  [...]

  Patternfly(app)

Sample app
----------

Here is how to run it on a virtual environment::

    cd flask-patternfly
    virtualenv venv
    source venv/bin/activate
    pip install -r requirements.txt
    python setup.py install
    PYTHONPATH=$PYTHONPATH:/flask_patternfly/ flask --app=sample_app run --port=5001


Navigate to http://127.0.0.1:5001/