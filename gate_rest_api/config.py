# -*- coding: utf-8 -*-
import os
import json
import secrets
from pydantic import BaseModel


class ProductionConfig(BaseModel):
    DB_URL: str = ""
    SECRET_KEY: str = os.environ.get("SECRET_KEY") or secrets.token_hex(256)
    DEBUG: bool = True
    RABBITMQ: dict = {
        "in_exchange": "e.smtp",
        "TTL": 300 * 1000,
        "url": f"amqp://{os.environ.get('RABBITMQ_USER','guest')}:"
        + f"{os.environ.get('RABBITMQ_PASS','guest')}@"
        + f"{os.environ.get('RABBITMQ_HOST', '')}",
    }
    # "url": "amqp://guest:guest@172.100.100.100"}
    api_metadata: str = json.loads(
        open("./data/api_metadata.json", "r", encoding="utf-8").read()
    )
