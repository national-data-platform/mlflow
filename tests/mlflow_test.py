import random
import spacy
from spacy.util import minibatch, compounding
from spacy.training import Example
import mlflow.spacy
import mlflow
import os,sys

from dotenv import load_dotenv

load_dotenv()

# training data
TRAIN_DATA = [
    ("Who is Shaka Khan?", {"entities": [(7, 17, "PERSON")]}),
    ("I like London and Berlin.", {"entities": [(7, 13, "LOC"), (18, 24, "LOC")]}),
]

nlp = spacy.blank("en")
ner = nlp.add_pipe("ner", last=True)

# add labels
for _, annotations in TRAIN_DATA:
    for ent in annotations.get("entities"):
        ner.add_label(ent[2])

params = {"n_iter": 100, "drop": 0.5}

env_list = ["AWS_SECRET_ACCESS_KEY",
            "AWS_ACCESS_KEY_ID",
            "AWS_S3_BUCKET",
            "MLFLOW_TRACKING_URI",
            "MLFLOW_S3_ENDPOINT_URL",
            ]

for env in env_list:
    env_val = os.getenv(env)
    if env_val is None:
        sys.exit(f"Error: missing env var {env}")

experiment_name = "NER Model - test experiment"
experiment=mlflow.get_experiment_by_name(experiment_name)

if experiment is None:
    experiment = mlflow.create_experiment(experiment_name)
else:
    experiment = mlflow.set_experiment(experiment_name)

mlflow.log_params(params)
run_id=mlflow.active_run().info.run_id
artifact_path = mlflow.get_artifact_uri()

file = 'test_file.txt'
mlflow.log_artifact(file)
mlflow.log_artifact(__file__)

nlp.begin_training()
for itn in range(params["n_iter"]):
    random.shuffle(TRAIN_DATA)
    losses = {}
    batches = minibatch(TRAIN_DATA, size=compounding(4.0, 32.0, 1.001))
    example = []
    for batch in batches:
        texts, annotations = zip(*batch)
        for i in range(len(texts)):
            doc = nlp.make_doc(texts[i])
            example.append(Example.from_dict(doc, annotations[i]))
            nlp.update(
                example,
                drop=params["drop"],
                losses=losses,
            )
        mlflow.log_metrics(losses)

# Log the spaCy model using mlflow
mlflow.spacy.log_model(spacy_model=nlp,artifact_path='model')
model_uri = "runs:/{run_id}/{artifact_path}".format(run_id=run_id, artifact_path='model')
print('model_uri:',model_uri)
print("Model saved in run %s" % mlflow.active_run().info.run_uuid)
mlflow.end_run()