FROM continuumio/miniconda3:23.10.0-1

WORKDIR /mlflow
COPY requirements.txt requirements.txt
COPY run.sh run.sh

# set time zone
ENV TZ America/Los_Angeles
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN chmod +x run.sh
RUN pip install -r requirements.txt

COPY ndp_mlflow_auth-0.0.2-py3-none-any.whl ndp_mlflow_auth-0.0.2-py3-none-any.whl
RUN pip install ndp_mlflow_auth-0.0.2-py3-none-any.whl

ENTRYPOINT ["./run.sh"]