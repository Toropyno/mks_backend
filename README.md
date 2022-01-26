[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)
[![Linter: flake8](https://img.shields.io/badge/linter-flake8-black)](https://flake8.pycqa.org/en/latest/index.html#)

# ПАК ЦУПД 83т4.5 "Мониторинг капитального строительства"

- ##### [Функциональные требования](https://confluence.rd.aorti.ru/pages/viewpage.action?pageId=34288411)
- ##### [Техническое проектирование](https://gitlab.rd.aorti.ru/ntc-sria/nio1/analytics2/-/tree/master/%D0%A6%D0%A3%D0%9F%D0%94/%D0%9C%D0%9A%D0%A1/%D0%A2%D0%9F%20%D0%BD%D0%B0%20%D1%80%D0%B0%D0%B7%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D0%BA%D1%83%20%D0%9F%D0%98)

--------------------------------------------------------------------------------
### Необходимые apt-пакеты
[ansible/group_vars/apt_packages.yml](ansible/group_vars/apt_packages.yml)

### Общий конфигурационный файл
Все специфичные переменные для проекта задаются в [development.ini](development.ini)

Чтобы использовать другой конфиг, необходимо изменить путь к нему:
- В [.wsgi-прослойке](pyramid.wsgi)
- В [настройках приложения](mks_backend/settings.py)

--------------------------------------------------------------------------------
<details>
<summary>Локальное разворачивание</summary>

### Настройка локального окружения
```sh
python3 -m venv env
source env/bin/activate
pip install -e ".[dev]" -i http://art.rd.aorti.ru/repository/pypi-proxy/simple/ --trusted-host art.rd.aorti.ru
``` 

### Настройка локального PostgreSQL 
```sh
CREATE DATABASE mks;
\password postgres
```

#### Накатывание миграций на БД
```sh
alembic upgrade heads || env/bin/alembic upgrade heads
```
#### Наполнение БД
```sh
fill_db development.ini
```

#### Запуск
```sh
pserve development.ini
```
</details>

--------------------------------------------------------------------------------

<details>
<summary>Разворачивание на удалённых серверах через ansible</summary>

1. Создайте и скопируйте ключ пару ssh-ключей на целевой хост [(пример)](http://www.linuxproblem.org/art_9.html)
2. Для деплоя запустите в терминале
   ```shell
   # установить сам ansible
   pip install -e ".[deploy]" -i http://art.rd.aorti.ru/repository/pypi-proxy/simple/ --trusted-host art.rd.aorti.ru
   
   # деплой на стенды
   ansible-playbook ansible/install_to_stands.yml -i ansible/hosts
   ```
   Но вообще, здесь настроено CI/CD, так что dev ветку таким образом точно заливать не нужно
</details>

--------------------------------------------------------------------------------

Если при любой ошибке система выдаёт **Ошибка с БД**,
значит, БД на сервере генерирует ошибки на русском языке.
Следует изменить текст ошибки, чтобы модуль обработки её поймал:
<details>
<p>

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
</p>
</details>

--------------------------------------------------------------------------------

### СВИП
[СВИП README](mks_backend/SVIP/README.md)


### МИВ
[МИВ README](mks_backend/MIV/MIV.md)

### САКУРА (ЧЕРЕЗ EXTR DOCS)
[МИВ README](mks_backend/MIV/MIV.md)
