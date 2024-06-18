import logging
import os

import requests
import ollama

from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse

from logging.handlers import SocketHandler
from logstash_formatter import LogstashFormatterV1
from pymongo.mongo_client import MongoClient


# Create a new client and connect to the server
client = MongoClient("your mongo url ")
db = client["menu-app"]
collection = db['menu']

app = FastAPI()

@app.get("/health_check")
def health_check(r: Request):
    return "healthy"




@app.get("/recommend")
def recommend():
    criteria = collection.find({})
    menu_items = list(criteria)
    prompt = f"I am a vegiterian what can I eat under $200 (choose 1) this is the menu: {str(menu_items)} thanks"
    

    response = ollama.chat(model='llama3', messages=[
        {
            'role': 'user',
            'content': prompt,
        },
    ])

    return {
        "message": response['message']['content']
    }


