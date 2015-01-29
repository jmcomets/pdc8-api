API catalog of the trees in Tête d'Or (Lyon)
============================================

# Commands

There is a `manage.py` script for development purposes only, the
`distmanage.py` script will use Heroku credentials (assuming the config
environment vars are set in your and therefore will **operate on the production
database**.

Both scripts work the same way. Run them without arguments and you will get the
full list of commands available.

## Importing trees into the database

    ./manage.py import-trees

This import command reads a `arbres.csv` csv export (at the root of the
project) and updates the database.

## Importing trees coordinates into the database

    ./manage.py import-gps

This import command reads a `gps.csv` csv export (at the root of the
project) and updates the database.

## Running the local development webserver

    ./manage.py runserver

# Dependencies

- Python 3 (untested on Python 2)
- Django 1.7+
- Django REST Framework 3+

If you have [pip](https://pip.pypa.io/) installed, use `pip install -r requirements.txt` to install directly the dependencies

# Deployment

Check out the [Heroku guide for deploying Heroku apps](https://devcenter.heroku.com/articles/getting-started-with-django).
