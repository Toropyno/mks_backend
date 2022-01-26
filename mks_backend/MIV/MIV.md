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
<details>
<summary>Вручную</summary>

```shell
# Реестр ИСП
miv send mks@int.aorti.tech mks_backend/MIV/parsing/constructions/sakura_isp.xml
```
</details>

<details>
<summary>Через EXTR DOCS</summary>

1. Заполнить переменную EXTR_DOCS_MIV_SENDER в [development.ini](./../../development.ini)
2. Воспользоваться графическим интерфейсом EXTR DOCS и отправить документ [sakura_isp.xml](./parsing/constructions/sakura_isp.xml)
</details>
