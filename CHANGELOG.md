### 21.09.2021
-  **GLOBAL**. Изменена архитектуру проекта с горизонтального разделения, на вертикальное, чтобы все проекты были одинаковыми по архитектуре. 
    <details>
    
    ```
    Было:
    
    controllers
        ├── entity_1_controller
        ├── entity_2_controller
        └── entity_3_controller
         
    services
        ├── entity_1_service
        ├── entity_2_service
        └── entity_3_service
    ...
    
    Стало:
    
    entities:
        ├── entity_1
        |        ├── controller
        |        ├── service
        |        └── serializer
        ├── entity_2
        |        ├── controller
        |        ├── service
        |        └── serializer
        └── entity_3
                 ├── controller
                 ├── service
                 └── serializer
    ```
    
    </details> 
  

-  **GLOBAL**. Изменён механизм обновления БД со старого и тупого `drop database...create database` на миграции alembic  


- Переделал fill_db чтобы его можно было запускать по несколько раз и не получать ошибку вида "ALREADY EXISTS". Это будет необходимо для CI/CD при каждом деплое.

### 22.09.2021
-  **GLOBAL**. Внедрил [ansible](ansible)

### 11.10.2021
- Переделал `fill_db` в контексте категории-подкатегории ИСП. [Задача в JIRA](https://jira.rd.aorti.ru/browse/MKSBRYANS-334)

### 12.10.2021
- Добавил словарь категории критичных объектов 
- Добавил поле категория критичного объекта в проекты ИСП

### 25.10.2021
- Добавил фаилы поездок руководства
- Добавил поле фильтрации "наличие фаила" в поездки руководства

### 26.10.2021
- Добавлен скрипт для выгрузки Реестра ИСП из САКУРА (крайне сырая реализация, требуется доработка)

### 27.10.2021
- **GLOBAL**. Реализована сквозная аутентификация в БД, через REMOTE_USER и GSSAPI  
  Подробнее описано в [ansible-playbook/tasks/04_postgresql.yml](ansible/tasks/04_postgresql.yml)

### 23.12.2021
- Реализована фильтрация дерева организаций по ФИО должностных лиц и по краткому и полному наименованию организации

### 11.01.2022
- Общий рефакторинг
- id заменены на id_, чтобы не спутать с built-in id
- Создан общий сериализатор BaseSerializer
- Убраны необязательные relationships в моделях
- Убраны ограничения на расширения файлов
- Добавлены ограничения на расширения фото-файлов

### 27.01.2022
- Проведена интеграция с СОВой, теперь обрабатываем входящее сообщение от САКУРЫ обернутое в служебную информацию от EXTR DOC

### 02.02.2022
- Добавлена обработка Сведений о государственных контрактов и Сроков окончания работ по контракту

### 16.02.2022
- Реализована сущность Предметы судебных споров
- Реализована сущность Документы по судебным спорам
