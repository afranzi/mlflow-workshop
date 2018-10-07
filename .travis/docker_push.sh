#!/bin/bash
echo "$DOCKER_PASSWORD" | docker login -u "$DOCKER_USERNAME" --password-stdin

docker build --no-cache -t afranzi/mlflow-tracking:${MLFLOW_VERSION} ./docker

docker tag mlflow-tracking:${MLFLOW_VERSION} afranzi/mlflow-tracking:${MLFLOW_VERSION}

docker push afranzi/mlflow-tracking:${MLFLOW_VERSION}