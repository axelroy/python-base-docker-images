FROM hbpmip/python-base

MAINTAINER royaxe@gmail.com

LABEL eu.humanbrainproject.category=Python

RUN mkdir /docker-volume

RUN conda install -y psycopg2
RUN conda update psycopg2

COPY scripts/main.py /
COPY scripts/docker-entrypoint.sh /
COPY scripts/database_connector/database_connector.py /

ENV TINI_VERSION v0.14.0
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini /tini
RUN chmod +x /tini

ENTRYPOINT ["/tini", "-s", "-v" , "--", "/docker-entrypoint.sh"]
