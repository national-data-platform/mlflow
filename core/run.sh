#!/bin/sh
MLFLOW_FILE_STORE=postgresql://${POSTGRES_USER}:${POSTGRES_PASSWORD}@db:5432/${POSTGRES_DB}
MLFLOW_ARTIFACT_STORE=s3://${AWS_BUCKET_NAME}

mlflow server \
    --host 0.0.0.0 \
    --port ${MLFLOW_PORT} \
    --backend-store-uri ${MLFLOW_FILE_STORE} \
    --default-artifact-root ${MLFLOW_ARTIFACT_STORE}