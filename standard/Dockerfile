FROM opensearchproject/opensearch:2.11.1

USER root
RUN set -x && \
    rm /usr/share/opensearch/config/jvm.options
COPY jvm.options /usr/share/opensearch/config/jvm.options
RUN set -x && \
    chown opensearch:opensearch /usr/share/opensearch/config/jvm.options

USER opensearch
