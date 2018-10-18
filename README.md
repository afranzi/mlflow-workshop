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
    --port 5000
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

> ⚠️**NOTE** Since clients needs to have access to the final path, it would be better to use a remote store, since we would need to have direct access to the fileStore directory.

# Run trainings
Since we have our MLflow Tracking docker exposed at 5000, we can log executions by setting the env variable `MLFLOW_TRACKING_URI`. 
```
MLFLOW_TRACKING_URI=http://localhost:5000 python example.py
```

# Serving models
***Ref:** [Saving and serving models](https://mlflow.org/docs/latest/quickstart.html#saving-and-serving-models)*

```
MLFLOW_TRACKING_URI=http://0.0.0.0:5000 mlflow sklearn serve \
    --port 5005 \
    -r 3e86bf0f27a347c59f0735aa92510a69 \
    -m model
```

> i.e: Query Wine Quality model prediction 
```
curl -X POST -H "Content-Type:application/json" \
    --data '[{"fixed acidity": 3.42, "volatile acidity": 1.66, "citric acid": 0.48, "residual sugar": 4.2, "chlorides": 0.229, "free sulfur dioxide": 39, "total sulfur dioxide": 55, "density": 1.98, "pH": 5.33, "sulphates": 4.39, "alcohol": 20.8}]' http://127.0.0.1:5005/invocations
```

# Run model from Spark

> pyspark
```
import mlflow.pyfunc
wine_udf = mlflow.pyfunc.spark_udf(spark, '/tmp/mlflow/artifacts/0/b0dfd62600ac4289a7b1bc058c528aad/artifacts/model/')
df = spark.read.format("csv").option("header", "true").option('delimiter', ';').load('/Users/yc00096/Projects/mlflow-workshop/examples/wine_quality/data/winequality-red.csv')
df.withColumn("prediction", wine_udf('fixed acidity','volatile acidity','citric acid','residual sugar','chlorides','free sulfur dioxide','total sulfur dioxide','density','pH','sulphates','alcohol')).show(10, False)
```


# Jupyter

```
export SPARK_HOME=~/spark
export PYSPARK_DRIVER_PYTHON=jupyter
export PYSPARK_DRIVER_PYTHON_OPTS='notebook  --notebook-dir=/Users/yc00096/Projects/notebooks'
```



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