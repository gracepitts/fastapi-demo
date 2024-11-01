#!/usr/bin/env py
# python3

from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import json
import os

app = FastAPI()

@app.get("/")  # zone apex
def zone_apex():
    return {"Hello": "Grace!"}

@app.get("/add/{a}/{b}")
def add(a: int, b: int):
    return {"sum": a + b}
@app.get("/square/{a}")
def square(a: int):
    return {"square": a * a}

@app.get("/multiply/{c}/{d}")
def multiply(c: int, d: int):
    return {"product": c * d}

@app.get("/subtract/{e}/{f}")
def subtract(c: int, d: int):
    return {"subtract": e - f}
