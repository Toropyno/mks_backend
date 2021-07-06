# ПАК ЦУПД 83т4.5 "Мониторинг капитального строительства"

- ##### [Функциональные требования](https://confluence.rd.aorti.ru/pages/viewpage.action?pageId=34288411)
- ##### [Техническое проектирование](https://gitlab.rd.aorti.ru/ntc-sria/nio1/analytics2/-/tree/master/%D0%A6%D0%A3%D0%9F%D0%94/%D0%9C%D0%9A%D0%A1/%D0%A2%D0%9F%20%D0%BD%D0%B0%20%D1%80%D0%B0%D0%B7%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D0%BA%D1%83%20%D0%9F%D0%98)

--------------------------------------------------------------------------------
## Развёртывание проекта:
### Настройка окружения (для всех последующих команд)
```sh
sudo apt update && apt -y upgrade
sudo apt install -y python3-pip python3-venv

python3 -m venv env
source env/bin/activate

pip install --upgrade pip setuptools
python setup.py install
pip install -e ".[dev]" -i http://art.rd.aorti.ru/repository/pypi-proxy/simple/ --trusted-host art.rd.aorti.ru
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

#### Наполнение БД
```sh
fill_db development.ini
```
###

### Если при любой ошибке система выдаёт "Ошибка с БД",
### значит, БД на сервере генерирует ошибки на русском языке.
### Следует изменить текст ошибки, чтобы модуль обработки её поймал
```sh
nano /etc/locale.gen  # запускаем на редактирование
```
Меняем строчку (поиск ctrl+W)
```sh
# en_US.UTF-8 UTF-8
```
на
```sh
en_US.UTF-8 UTF-8
```
Генерируем локали
```sh
sudo locale-gen
```
Редактируем конфиг Postgresql
```
nano /etc/postgresql/9.6/main/postgresql.conf
```
Меняем строчку
```sh
lc_messages = 'ru_RU.UTF-8'
```
на
```sh
lc_messages = 'en_US.UTF-8'
```
Перезапускаем БД
```sh
sudo service postgresql restart
```
