### Для создания коллекции, добавления аккаунтов к коллекции, добавления разрешений, запустите скрипт
```shell
svip create
```
или, полным путём
```shell
./env/bin/svip create
```

### Для удаления коллекции
```shell
svip delete
```
или, полным путём
```shell
./env/bin/svip delete
```

Название коллекции (**COLLECTION_NAME**) задаётся в [development.ini](./../../development.ini)

Хост СВИП, пользователь (владелец коллекции), от которого будут создаваться данные в СВИП, указаны в [development.ini](./../../development.ini)
```shell
MKS_USER = mks
MKS_PASSWORD = iEfG02AE
```

Список пользователей, которые будут добавлены в коллекцию без права на редактирование, указаны в файле [accounts.json](initial_data/accounts.json)  

Разрешения указаны в файлу [permissions.json](initial_data/permissions.json)

Связь между пользователями и разрешениями указана в файле [account_permissions.json](initial_data/account_permissions.json)
