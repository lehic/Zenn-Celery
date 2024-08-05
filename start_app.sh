#!/bin/bash


python fetch_secrets.py

celery --app tasks flower --loglevel=info --basic-auth=intoadmin:weareinto123!!@ --port=30005
