Настройки подключения к БД лежат в файле [development.ini](../development.ini)

Чтобы создать миграцию нужно запустить команду
```shell
alembic -c mks_backend/alembic.ini revision --autogenerate -m "Your migration name"
```
Чтобы накатить миграцию нужно запустить команду
```shell
alembic -c mks_backend/alembic.ini upgrade head
```

Если получили ошибку вида:
```shell
ERROR [alembic.util.messaging] Multiple heads are present; please specify the head revision on which the new revision should be based, or perform a merge.
  FAILED: Multiple heads are present; please specify the head revision on which the new revision should be based, or perform a merge.
```
Создаём миграцию-merge нескольких ревизий
```shell
alembic merge heads -m "merge_migration"
```
Накатываем заново
