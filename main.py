import collections
from collections import abc

# TODO remove collections trash
# TODO Consider moving to python 3.9 or 3.11

collections.Iterable = collections.abc.Iterable
collections.Mapping = collections.abc.Mapping
collections.MutableSet = collections.abc.MutableSet
collections.MutableMapping = collections.abc.MutableMapping
collections.Sequence = collections.abc.Sequence



from pymongo.mongo_client import MongoClient
url = "mongourl"

# Create a new client and connect to the server
client = MongoClient(uri)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)



# import logging
# import os

# from link_shortener import LinkShortener
# from fastapi import FastAPI, Request
# from fastapi.responses import RedirectResponse

# from logging.handlers import SocketHandler
# from logstash_formatter import LogstashFormatterV1

# LOGSTASH_HOST = os.getenv("LOGSTASH_HOST")
# LOGSTASH_PORT = int(os.getenv("LOGSTASH_PORT"))

# logging.basicConfig(level=logging.INFO)
# logger = logging.getLogger(__name__)

# logstash_handler = SocketHandler(LOGSTASH_HOST, LOGSTASH_PORT)
# logstash_handler.setFormatter(LogstashFormatterV1)
# logger.addHandler(logstash_handler)

# app = FastAPI()

# @app.get("/health_check")
# def health_check(r: Request):
#     return "healthy"

