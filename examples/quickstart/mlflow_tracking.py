import os
from random import random, randint

from mlflow import log_metric, log_param, log_artifacts
import mlflow

if __name__ == "__main__":
    print("Running mlflow_tracking.py")

    log_param("param1", randint(0, 100))
    remote_server_uri = "http://10.77.36.45:5000" # set to your server URI
    mlflow.set_tracking_uri(remote_server_uri)

    log_metric("foo", 1)
    log_metric("foo", 2)
    log_metric("foo", 3)
    print(os.getenv('MLFLOW_EXPERIMENT_NAME'))
    mlflow.set_experiment(os.getenv('MLFLOW_EXPERIMENT_NAME'))
    #mlflow.set_experiment("regression_module")

    if not os.path.exists("outputs"):
        os.makedirs("outputs")
    with open("outputs/test.txt", "w") as f:
        f.write("hello world!")

    log_artifacts("outputs")
