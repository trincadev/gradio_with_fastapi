from fastapi import FastAPI
import gradio as gr

CUSTOM_PATH = "/"

app = FastAPI()


def request_formatter(text: str) -> str:
    return f"transformed {text}."


@app.get("/health")
def read_main():
    return {"message": "ok"}


io = gr.Interface(request_formatter, "textbox", "textbox")
app = gr.mount_gradio_app(app, io, path=CUSTOM_PATH)
