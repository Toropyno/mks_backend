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
