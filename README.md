--------------------------------------------------------------------------------

-   быстрый запуск (когда есть все настройки)
    
    source env/bin/activate
    
    initialize_mks_backend_db development.ini
    
    pserve development.ini --reload
    
--------------------------------------------------------------------------------

Activation on Linux:
--------------------------------------------------------------------------------

    cd mfo_backend/

    sudo apt update && apt -y upgrade

    sudo apt install -y python3-pip python3-venv

    python3 -m venv env

    source env/bin/activate

    pip install --upgrade setuptools
    
    pip install -e ".[dev]" 
    
--------------------------------------------------------------------------------

 -  создание таблиц в БД

    initialize_app_db development.ini
    
--------------------------------------------------------------------------------

 -  запуск

    pserve development.ini --reload

--------------------------------------------------------------------------------

PostgreSQL installation 
--------------------------------------------------------------------------------

-   You need to create a database if it is not

    sudo apt install postgresql

    sudo -u postgres psql

    CREATE DATABASE mks_backend;

    \password postgres
    
--------------------------------------------------------------------------------

- Upgrade packaging tools.
    env/bin/pip install --upgrade pip setuptools

- Install the project in editable mode with its testing requirements.
    env/bin/pip install -e ".[testing]"
