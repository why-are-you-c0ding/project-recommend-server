from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}



    # 필요한 의존성
    # pip install fastapi
    # pip install "uvicorn[standard]"

    # 실행 명령어
    # uvicorn main:app --reload

    # API 명세서 
    # http://127.0.0.1:8000/docs

    # http://127.0.0.1:8000/redoc