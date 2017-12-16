# 3mw
3mw

# Installation:
## Create Virtual Environment (Python3)
    mkvirtualenv -p $(which python3) 3mw
## Install Requirements
    pip install -r requirements.txt
## Run Migrations
    ./manage.py migrate
## Load initial fixtures
    ./manage.py loaddata sites/fixtures/initial.json
# Testing
    ./manage.py test
# Running App
    ./manage.py runserver
    
# Using Makefile
You can also use the Makefile for automated installation.
## Setup
    make setup
## Run
    make run