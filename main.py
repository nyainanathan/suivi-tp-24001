import _pydatetime
import base64
import math
import os
import json
from _pydatetime import datetime

from fastapi.openapi.utils import status_code_ranges
from pydantic_core.core_schema import DatetimeSchema
from starlette.requests import Request
from starlette.responses import Response, JSONResponse
from pydantic import BaseModel
from typing import List

from fastapi import FastAPI
app = FastAPI()

@app.get("/ping")
def ping():
    return Response(content="pong", status_code=200, media_type="text/plain")

@app.get("/users")
def get_users(Page: int , Size: int):
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    USERS_FILE = os.path.join(BASE_DIR, "users.json")

    with open(USERS_FILE, "r", encoding="utf-8") as file:
        users = json.load(file)

    available_pages = math.ceil(len(users) / Size)

    if(Page > available_pages) :
        return JSONResponse(content={"error": "Bad types for provided query parameters"}, status_code=400)

    required_users = []
    start_index = Size * (Page - 1)
    end_index = min(start_index + Size, len(users))

    for i in range(start_index, end_index):
        required_users.append(users[i])

    return JSONResponse(content=required_users, status_code=200)