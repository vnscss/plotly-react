#!/bin/bash

source ./venv/bin/activate
python3 ./api/manage.py runserver 127.0.0.1:1337

echo "Django na porta 1337"
