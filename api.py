from typing import Union
from fastapi import FastAPI, Header
from pydantic import BaseModel

import ai
import jwt_service

app = FastAPI()

class Item(BaseModel):
    name: str


@app.get("/recommend")
def read_item(authorization: Union[str, None] = Header(default=None)):
    user_id = jwt_service.get_id_from_jwt(authorization)
    result = ai.recomm_items(user_id)
    return result


@app.post("/recommend")
async def create_item_rating(item:Item, authorization: Union[str, None] = Header(default=None)):
    user_id = jwt_service.get_id_from_jwt(authorization)
    print(item.name, user_id)





    # 필요한 의존성
    # pip install fastapi
    # pip install "uvicorn[standard]"

    # 실행 명령어
    # uvicorn api:app --reload

    # API 명세서 
    # http://127.0.0.1:8000/docs

    # http://127.0.0.1:8000/redoc