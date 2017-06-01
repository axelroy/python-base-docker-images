FROM hbpmip/python-base

MAINTAINER royaxe@gmail.com

LABEL eu.humanbrainproject.category=Python
COPY scripts/main.py /

COPY scripts/docker-entrypoint.sh /

ENTRYPOINT ["/docker-entrypoint.sh"]
