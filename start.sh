#!/bin/sh

pip install -e .
export FLASK_APP=tinyhands
export FLASK_DEBUG=true
flask run
