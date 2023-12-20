FROM continuumio/miniconda3:23.10.0-1

WORKDIR /mlflow
COPY requirements.txt requirements.txt
COPY run.sh run.sh

RUN chmod +x run.sh
RUN pip install -r requirements.txt

ENTRYPOINT ["./run.sh"]