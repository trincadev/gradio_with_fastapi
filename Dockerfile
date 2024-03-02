FROM python:3.11-bookworm AS builder_global

ARG PACKAGE_NAME="app_gradio_fastapi"
ARG ROOT_DIR="/code"
WORKDIR ${ROOT_DIR}
RUN chmod 770 -R ${ROOT_DIR}/

COPY ./requirements.txt ${ROOT_DIR}/requirements.txt

RUN pip install pip --upgrade
RUN python -m venv venv
RUN . ${ROOT_DIR}/venv/bin/activate && pip install --no-cache-dir -r ${ROOT_DIR}/requirements.txt

COPY ./scripts ${ROOT_DIR}/scripts
COPY ./${PACKAGE_NAME} ${ROOT_DIR}/${PACKAGE_NAME}

RUN chmod +x ${ROOT_DIR}/scripts/entrypoint.sh

EXPOSE 7860

CMD ["/code/scripts/entrypoint.sh"]
# CMD ["uvicorn", "wrappers.main:app", "--host", "0.0.0.0", "--port", "7860"]
