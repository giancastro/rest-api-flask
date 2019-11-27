FROM postgres:9.6.16

ENV POSTGRES_USER admin
ENV POSTGRES_PASSWORD admin
ENV POSTGRES_DB api

COPY default_data.csv /docker-entrypoint-initdb.d/default_data.csv

ADD init.sql /docker-entrypoint-initdb.d/