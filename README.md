# 3mw
3mw

# Installation:
## Create Virtual Environment (Python3)
    mkvirtualenv -p $(which python3) 3mw
## Install Requirements
    pip install -r requirements.txt
## Run Migrations
    ./manage.py migrate
# Testing
    ./manage.py test
# Running App
    ./manage.py runserver