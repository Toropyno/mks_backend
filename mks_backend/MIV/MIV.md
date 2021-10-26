### Регистрация в МИВ
```shell
miv register
```
или, полным путём
```shell
./env/bin/miv register
```
Данные для регистрации заданы в [development.ini](./../../development.ini) (MIV_*)


### Отправка сообщения
```shell
miv send <получатель> <путь/к/файлу>
```
или, полным путём
```shell
./env/bin/miv send <получатель> <путь/к/файлу>
```

### Симуляция отправки/получения файла из САКУРы через МИВ
```shell
# Реестр ИСП
miv send mks@int.aorti.tech mks_backend/MIV/parsing/constructions/sakura_isp.xml
```

