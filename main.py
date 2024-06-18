import logging
import os

from link_shortener import LinkShortener
from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse

from logging.handlers import SocketHandler
from logstash_formatter import LogstashFormatterV1

LOGSTASH_HOST = os.getenv("LOGSTASH_HOST")
LOGSTASH_PORT = int(os.getenv("LOGSTASH_PORT"))

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

logstash_handler = SocketHandler(LOGSTASH_HOST, LOGSTASH_PORT)
logstash_handler.setFormatter(LogstashFormatterV1)
logger.addHandler(logstash_handler)

app = FastAPI()

@app.get("/health_check")
def health_check(r: Request):
    return "healthy"

