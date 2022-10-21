from typing import Union

from fastapi import FastAPI

import ai

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/recommend")
def read_item():
    result = ai.recomm_items()
    return {"result": result}



    # 필요한 의존성
    # pip install fastapi
    # pip install "uvicorn[standard]"

    # 실행 명령어
    # uvicorn main:app --reload

    # API 명세서 
    # http://127.0.0.1:8000/docs

    # http://127.0.0.1:8000/redoc