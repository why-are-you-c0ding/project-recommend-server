from typing import Union

from fastapi import FastAPI, Header

import ai
import jwt_service

app = FastAPI()


@app.get("/")
def read_root(authorization: Union[str, None] = Header(default=None)):
    jwt_service.get_id_from_jwt(authorization)
    return {"Hello": "World"}


@app.get("/recommend")
def read_item():
    result = ai.recomm_items()
    return result



    # 필요한 의존성
    # pip install fastapi
    # pip install "uvicorn[standard]"

    # 실행 명령어
    # uvicorn main:app --reload

    # API 명세서 
    # http://127.0.0.1:8000/docs

    # http://127.0.0.1:8000/redoc