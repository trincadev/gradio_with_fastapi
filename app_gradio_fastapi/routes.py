import json
import logging

from fastapi import APIRouter


router = APIRouter()


@router.get("/health")
def health():
    try:
        logging.info("health check")
        return json.dumps({"msg": "ok"})
    except Exception as e:
        logging.error(f"exception:{e}.")
        return json.dumps({"msg": "request failed"})
