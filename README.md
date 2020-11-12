# ПАК ЦУПД 83т4.5 "Мониторинг капитального строительства"

- ##### [Функциональные требования](https://confluence.rd.aorti.ru/pages/viewpage.action?pageId=34288411)
- ##### [Техническое проектирование](https://gitlab.rd.aorti.ru/ntc-sria/nio1/analytics2/-/tree/master/%D0%A6%D0%A3%D0%9F%D0%94/%D0%9C%D0%9A%D0%A1/%D0%A2%D0%9F%20%D0%BD%D0%B0%20%D1%80%D0%B0%D0%B7%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D0%BA%D1%83%20%D0%9F%D0%98)

--------------------------------------------------------------------------------
## Локальное развертывание проекта:
### Настройка окружения
```sh
sudo apt update && apt -y upgrade
sudo apt install -y python3-pip python3-venv

python3 -m venv env
source env/bin/activate

pip install --upgrade pip setuptools
python setup.py install
pip install -e ".[dev]" 
``` 

### Установка PostgreSQL 
```sh
sudo apt install postgresql
sudo -u postgres psql

CREATE DATABASE mks_db;
\password postgres
``` 
#### Инициализация БД
```sh
initialize_mks_db development.ini
```
#### Запуск севрвера
```sh
pserve development.ini --reload
```
