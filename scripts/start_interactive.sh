#!/bin/bash
source venv/bin/activate
export LC_ALL='en_US.UTF-8'

export PYTHONPATH=.:$PYTHONPATH
export PYTHONPATH=./src:$PYTHONPATH

export PYTHONWARNINGS=ignore::yaml.YAMLLoadWarning

python ./scripts/manage.py runserver 0.0.0.0:8000
