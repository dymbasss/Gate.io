# -*- coding: utf-8 -*-
import logging
import os
import fastapi
import uvicorn
import multiprocessing
from config import ProductionConfig


if "log" not in os.listdir():
    os.mkdir(os.path.join(os.getcwd(), "log"))

logging.basicConfig(
    level=logging.DEBUG,
    filename=f"./log/gate_rest_api.log",
    filemode="a",
    format='[%(asctime)s] (%(filename)s:%(lineno)d %(threadName)s) %(levelname)s - %(name)s: "%(message)s"',
)

app_conf = ProductionConfig()

app = fastapi.FastAPI(**app_conf.api_metadata, debug=app_conf.DEBUG)

from exceptions import *
from views import *

if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", 
                port=int(os.environ.get("PORT", 3500)), 
                workers=multiprocessing.cpu_count())