import _pydatetime
import base64
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