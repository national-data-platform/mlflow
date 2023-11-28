# MLFLOW

## Docker
The first part is to build and run the Docker containers via Docker-compose:

Build containers (detached mode):
```
docker compose up --build -d
```

Build containers:
```
docker compose up --build
```

Cleanup:
```
docker compose down --volume
```

## Tests
Simple NLP spacy training workflow is provided under [tests](tests)

```
cd tests
pip3 install -r requirements.txt
python3 mlflow_test.py
```

Next check the [MLFlow UI](http://localhost:5000) to see the trainning session being logged under `NER Model - test experiment`. One can also check [MinIO](http://localhost:9000) for the artifacts being stored in the `mlflow` bucket.