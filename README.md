---
title: Gradio With Fastapi
emoji: 🌖
colorFrom: yellow
colorTo: purple
sdk: docker
pinned: false
license: mit
---

# Gradio plus FastAPI with UUID logging sessions
## Run the app in a virtual environment

1. create and activate a virtual environment
2. install the dependencies
3. execute the uvicorn webserver

```bash
# create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate
# install the project dependencies
python -m pip install pip --upgrade
python -m pip install -r requirements.txt
# execute the uvicorn webserver
uvicorn app_gradio_fastapi.main:app --host 0.0.0.0 --port 7860 --reload
```

## Run the app within a docker container

Build the docker image and run the container:

```bash
docker build . --tag app_gradio_fastapi --progress=plain
docker run -d --name app_gradio_fastapi -p 7860:7860 app_gradio_fastapi; docker logs -f app_gradio_fastapi
```

To stop all the container and remove all the docker images:


```bash
docker stop $(docker ps -a -q); docker rm $(docker ps -a -q)
docker rmi $(docker images -q) -f
```
