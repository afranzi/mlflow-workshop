# MLflow workshop
First steps to interact with [MLflow](mlflow.org).

The idea aims to discover how MLflow works and which benefits could provide to our Data Scientists.

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