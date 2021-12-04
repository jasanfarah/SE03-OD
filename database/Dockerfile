FROM mysql

ENV MYSQL_ALLOW_EMPTY_PASSWORD yes
ENV MYSQL_ROOT_PASSWORD=1234
COPY init.sql /docker-entrypoint-initdb.d/

