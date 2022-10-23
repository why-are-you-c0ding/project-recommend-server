from typing import Union

from fastapi import FastAPI, Header

import ai
import jwt_service

app = FastAPI()


@app.get("/recommend")
def read_item(authorization: Union[str, None] = Header(default=None)):
    id = jwt_service.get_id_from_jwt(authorization)
    result = ai.recomm_items()
    return result



    # 필요한 의존성
    # pip install fastapi
    # pip install "uvicorn[standard]"

    # 실행 명령어
    # uvicorn api:app --reload

    # API 명세서 
    # http://127.0.0.1:8000/docs

    # http://127.0.0.1:8000/redoc