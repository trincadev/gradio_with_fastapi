import logging
from fastapi import HTTPException

from app_gradio_fastapi.helpers import session_logger


def divide(a: int, b: int) -> float:
    logging.info(f"a:{a}, b:{b}.")
    result = a / b
    logging.info(f"result:{result}.")
    return result


@session_logger.set_uuid_logging
def request_formatter(text: str) -> dict:
    logging.info("start request...")
    try:
        logging.info(f"input text we need to treat as an integer: {text}.")
        b = int(text)
        transformed_text = f"input after integer cast: {b}."
        try:
            result_division = divide(100, b)
            logging.info(f"some_function, result_division:{result_division}.")
            return {"text": transformed_text, "result": result_division}
        except ZeroDivisionError as zde:
            logging.info(f"exception:{zde}.")
            raise HTTPException(status_code=500, detail="Internal server error")
    except ValueError as ve:
        logging.info(f"exception:{ve}.")
        raise HTTPException(status_code=500, detail="Internal server error")
