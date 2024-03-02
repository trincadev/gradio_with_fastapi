# Run the app

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
