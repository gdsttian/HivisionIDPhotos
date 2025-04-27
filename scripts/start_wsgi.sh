#!/bin/bash
source venv/bin/activate
export LC_ALL='en_US.UTF-8'

export PYTHONPATH=.:$PYTHONPATH
export PYTHONPATH=./src:$PYTHONPATH

export UWSGI_BUFFER_SIZE=65535
export UWSGI_DIE_ON_TERM=1
export UWSGI_MAX_REQUESTS=1000000
export UWSGI_MAX_REQUESTS_DELTA=50
export UWSGI_NEED_APP=True
export UWSGI_WORKERS=2
export DJANGO_DEBUG="False"
export DJANGO_ALLOWED_HOSTS="['*']"

export PYTHONWARNINGS=ignore::yaml.YAMLLoadWarning

uwsgi --master \
 --http-socket 0.0.0.0:8000 \
 --module project.wsgi \
 --logformat "INFO %(ctime) %(status) %(method) %(msecs)ms %(addr) %(uri)" \
 --static-map /static=./var/data/static
