sudo -u postgres psql
CREATE DATABASE mks_backend;

source env/bin/activate
initialize_mks_backend_db development.ini
pserve development.ini --reload