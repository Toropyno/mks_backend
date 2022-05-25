#!/bin/bash

alembic upgrade heads

fill_db

pserve development.ini
