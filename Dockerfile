ARG AIRFLOW_VERSION=3.1.6

FROM apache/airflow:${AIRFLOW_VERSION}

USER root

# Dependências do sistema (use apenas o necessário)
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
       vim \
    && apt-get autoremove -yqq --purge \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Instalar dependências Python
COPY requirements.txt /requirements.txt
RUN pip install --no-cache-dir -r /requirements.txt

# Copiar DAGs e plugins
COPY dags /opt/airflow/dags
COPY plugins /opt/airflow/plugins

USER airflow

ENV AIRFLOW__CORE__LOAD_EXAMPLES=False

