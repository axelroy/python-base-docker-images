FROM hbpmip/python-base

MAINTAINER royaxe@gmail.com

LABEL eu.humanbrainproject.category=Python
COPY scripts/main.py /
COPY scripts/docker-entrypoint.sh /

ENV TINI_VERSION v0.14.0
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini /tini
RUN chmod +x /tini

ENTRYPOINT ["/tini", "-s", "-v" , "--", "/docker-entrypoint.sh"]
