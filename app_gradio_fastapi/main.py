from fastapi import FastAPI
import gradio as gr

from app_gradio_fastapi import routes


def request_formatter(text: str) -> str:
    return f"transformed {text}."


CUSTOM_GRADIO_PATH = "/"
app = FastAPI(title="logging_app", version="1.0")
app.include_router(routes.router)
io = gr.Interface(
    request_formatter,
    inputs=[
        gr.Textbox(lines=1, placeholder=None, label="Text input"),
    ],
    outputs=[
        gr.Textbox(lines=1, placeholder=None, label="Text Output"),
    ],
)
app = gr.mount_gradio_app(app, io, path=CUSTOM_GRADIO_PATH)
