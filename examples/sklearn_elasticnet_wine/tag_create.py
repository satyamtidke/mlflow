from  mlflow.tracking import MlflowClient
import mlflow
import os
client = MlflowClient()
experiments = client.list_experiments() # returns a list of mlflow.entities.Experiment
remote_server_uri = "http://10.77.36.45:5050/" # set to your server URI
mlflow.set_tracking_uri(remote_server_uri)

run = client.create_run(experiments[0].experiment_id) # returns mlflow.entities.Run
client.log_param(run.info.run_id, "hello", "world")
client.set_terminated(run.info.run_id)
client.set_tag(run.info.run_id,"36","new module")
