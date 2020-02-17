import mlflow
mlflow.set_tracking_uri("ML_TRACKING_URI")
mlflow.create_experiment("MLFLOW_EXPERIMENT_NAME", artifact_location=None)
mlflow.start_run()
mlflow.log_param("my", "param")
mlflow.log_metric("score", 100)
mlflow.end_run()
