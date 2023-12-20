FROM continuumio/miniconda3:23.10.0-1

WORKDIR /mlflow
COPY requirements.txt requirements.txt
COPY run.sh run.sh
COPY ndp_mlflow_auth-0.0.1-py3-none-any.whl ndp_mlflow_auth-0.0.1-py3-none-any.whl

RUN chmod +x run.sh
RUN pip install -r requirements.txt
RUN pip install ndp_mlflow_auth-0.0.1-py3-none-any.whl

ENTRYPOINT ["./run.sh"]