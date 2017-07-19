FROM hbpmip/python-base

MAINTAINER royaxe@gmail.com

LABEL eu.humanbrainproject.category=Python

RUN mkdir /docker-volume

ENV COMPUTE_IN=/data/in \
    COMPUTE_OUT=/data/out

RUN conda install -y psycopg2
RUN conda update psycopg2

RUN pip install TPOT

COPY scripts/main.py /
COPY scripts/docker-entrypoint.sh /
COPY scripts/database_connector/database_connector.py /

ENTRYPOINT ["/docker-entrypoint.sh"]
