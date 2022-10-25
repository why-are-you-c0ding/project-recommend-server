from typing import Union
from fastapi import FastAPI, Header
from pydantic import BaseModel
from starlette.middleware.cors import CORSMiddleware

import ai
import jwt_service

origins = [
    "http://localhost:3090",
]

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Item(BaseModel):
    item_id: int
    rating: float


@app.get("/recommend")
def read_item(authorization: Union[str, None] = Header(default=None)):
    user_id = jwt_service.get_id_from_jwt(authorization)
    result = ai.recomm_items(user_id)
    return result


@app.post("/recommend")
async def create_item_rating(item:Item, authorization: Union[str, None] = Header(default=None)):
    token = jwt_service.get_id_from_jwt(authorization)
    ai.track_user_behavior(item.rating, item.item_id, token)
    return {"message" : "요청을 성공했습니다."}





    # 필요한 의존성
    # pip install fastapi
    # pip install "uvicorn[standard]"

    # 실행 명령어
    # uvicorn api:app --reload

    # API 명세서 
    # http://127.0.0.1:8000/docs

    # http://127.0.0.1:8000/redoc