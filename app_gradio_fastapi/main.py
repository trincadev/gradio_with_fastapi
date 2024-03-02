import gradio as gr
from fastapi import FastAPI

from app_gradio_fastapi import routes
from app_gradio_fastapi.helpers.formatters import request_formatter
from app_gradio_fastapi.helpers.session_logger import change_logging


change_logging()

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
