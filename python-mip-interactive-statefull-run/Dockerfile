FROM hbpmip/python-base

MAINTAINER royaxe@gmail.com

LABEL eu.humanbrainproject.category=Python

ENV IN_JDBC_URL="jdbc:postgresql://"${HOST}":5432/postgres"
ENV IN_JDBC_USER="postgres"
ENV IN_JDBC_PASSWORD="test"

ENV OUT_JDBC_URL="jdbc:postgresql://"${HOST}":5432/postgres"
ENV OUT_JDBC_USER="postgres"
ENV OUT_JDBC_PASSWORD="test"

ENV PARAM_meta="{}"

RUN mkdir /docker-volume

RUN conda install -y psycopg2
RUN conda update psycopg2

COPY scripts/main.py /
COPY scripts/docker-entrypoint.sh /
COPY scripts/database_connector/database_connector.py /

ENTRYPOINT ["/docker-entrypoint.sh"]
