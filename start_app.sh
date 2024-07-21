#!/bin/bash


python fetch_secrets.py

celery flower --app tasks --loglevel info --basic-auth=intoadmin:weareinto123!!@ --port=30005