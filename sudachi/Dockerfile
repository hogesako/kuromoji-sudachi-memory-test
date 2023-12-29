FROM eclipse-temurin:11-jdk AS sudachi-build

RUN set -x && apt update && apt install -y git wget unzip && apt clean

RUN set -x && \ 
    wget http://sudachi.s3-website-ap-northeast-1.amazonaws.com/sudachidict/sudachi-dictionary-20230927-core.zip -P /tmp && \
    unzip /tmp/sudachi-dictionary-20230927-core.zip -d /tmp

RUN set -x && \ 
    git clone https://github.com/WorksApplications/elasticsearch-sudachi.git && \
    cd elasticsearch-sudachi && \
    git checkout refs/tags/v3.1.0

RUN set -x && \ 
    cd /elasticsearch-sudachi && \
    ./gradlew -PengineVersion=os:2.11.1 build distZip -x test && \
    ls -l build/distributions

FROM opensearchproject/opensearch:2.11.1

USER root

RUN set -x && \
    mkdir -p /usr/share/opensearch/config/sudachi/ && \
    chown opensearch:opensearch /usr/share/opensearch/config/sudachi/
USER opensearch


COPY --from=sudachi-build /tmp/sudachi-dictionary-20230927/system_core.dic /usr/share/opensearch/config/sudachi/
COPY --from=sudachi-build /elasticsearch-sudachi/build/distributions/opensearch-2.11.1-analysis-sudachi-3.1.0.zip /usr/share/opensearch/config/
RUN set -x && \
    opensearch-plugin install file:///usr/share/opensearch/config/opensearch-2.11.1-analysis-sudachi-3.1.0.zip && \
    rm /usr/share/opensearch/config/opensearch-2.11.1-analysis-sudachi-3.1.0.zip