#!/usr/bin/env bash

WORKDIR="/code"

cd ${WORKDIR} || exit
pwd
source ${WORKDIR}/venv/bin/activate

which python
python --version
which pip
pip --version

free -m
pip list
ls -l
echo "uvicorn"
ls -l ${WORKDIR}/venv/bin/uvicorn

# python ${WORKDIR}/app.py --version='xinlai/LISA-13B-llama2-v1-explanatory' --precision='fp16' --load_in_4bit
echo "${WORKDIR}/venv/bin/uvicorn app_gradio_fastapi.main:app --host 0.0.0.0 --port 7860"
${WORKDIR}/venv/bin/uvicorn app_gradio_fastapi.main:app --host 0.0.0.0 --port 7860

exit 0
