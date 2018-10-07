# MLflow workshop
First steps to interact with [MLflow](mlflow.org).

The idea aims to discover how MLflow works and which benefits could provide to our Data Scientists.

[![Build Status](https://travis-ci.com/afranzi/mlflow-workshop.svg?branch=master)](https://travis-ci.com/afranzi/mlflow-workshop)

# Steps
## Environment setup
Create a **virtual env** with Python3 to have a clean setup for our projects with all the required libraries listed in the **requirements.txt**

```:python
virtualenv -p python3 venv
source venv/bin/activate
pip install -r requirements.txt
```




# Tracking API
***Docs:** [MLflow // docs // Tracking](https://mlflow.org/docs/latest/tracking.html)*

> Launch Tracking UI (*http://localhost:5000*)
```
mlflow ui
```

```
mlflow server \
    --file-store /tmp/mlflow/fileStore \
    --default-artifact-root /tmp/mlflow/artifacts/ \
    --host localhost
```

> Launch MLFlow Tracking Docker
```
docker run -d -p 5000:5000 \
    --name mlflow-tracking afranzi/mlflow-tracking:0.7.0
```

By default it will store the artifacts and files inside ***/opt/mlflow***. 
It's possible to define the following variables:
* MLFLOW_HOME (`/opt/mlflow`)
* MLFLOW_VERSION (`0.7.0`)
* SERVER_PORT (`5000`)
* SERVER_HOST (`0.0.0.0`)
* FILE_STORE (`${MLFLOW_HOME}/fileStore`)
* ARTIFACT_STORE (`${MLFLOW_HOME}/artifactStore`)

# Notes

## Docker management
***Ref:** [Remove docker images and containers](https://tecadmin.net/remove-docker-images-and-containers/).*

> List all images
```
docker images
``` 

> Remove intermediate images
```
docker rmi $(docker images -qa -f 'dangling=true')
```

> List all containers
```
docker ps -a
```

> Stop all containers
```
docker stop $(docker ps -a -q)
```

> Remove all containers
```
docker rm $(docker ps -a -q)
```


# Links Of Interest
* [Docs // MLflow Tracking](https://mlflow.org/docs/latest/tracking.html)
* [Docs // Supported Artifact Stores](https://mlflow.org/docs/latest/tracking.html#supported-artifact-stores)
* **Base Docker** with Machine Learning libraries to build the MLflow image - *[frolvlad/alpine-python-machinelearning](https://hub.docker.com/r/frolvlad/alpine-python-machinelearning/)*