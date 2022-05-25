# это БАЗА, для контейнера
FROM python:3.5

RUN apt update
RUN apt upgrade -y

ADD . /opt/mks/backend
WORKDIR /opt/mks/backend

RUN pip install -U pip setuptools wheel
RUN pip install -e .[dev]

# меняем настройки подключения к БД
RUN sed -i 's/DATABASE_HOST = localhost/DATABASE_HOST = db/g' development.ini

RUN wget https://raw.githubusercontent.com/vishnubob/wait-for-it/master/wait-for-it.sh
RUN chmod 777 ./wait-for-it.sh
RUN chmod 777 ./docker-entrypoint.sh

# expose port
EXPOSE 6543

CMD ["./wait-for-it.sh", "db:5432", "--", "./docker-entrypoint.sh"]
