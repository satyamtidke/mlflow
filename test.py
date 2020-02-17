import mlflow
ML_TRACKING_URI="http://10.77.36.45:5000/"
MLFLOW_EXPERIMENT_NAME="mlflow_experiment_jnekins"
mlflow.set_tracking_uri(ML_TRACKING_URI)
mlflow.create_experiment(MLFLOW_EXPERIMENT_NAME, artifact_location=None)
mlflow.start_run()
mlflow.log_param("my", "param")
mlflow.log_metric("score", 100)
mlflow.end_run()
