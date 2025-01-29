# coding: utf-8
import aio_pika
import json

import model as api_model

from app import app, app_conf


def check_type(data):

    if isinstance(data, api_model.SMTPBody):
        data = data.model_dump()
    elif isinstance(data, str):
        return data.encode("utf-8")

    return json.dumps(data).encode("utf-8")


async def publish(in_exchange: str, data: api_model.SMTPBody | str) -> None:

    connection = await aio_pika.connect_robust(
        app_conf.RABBITMQ["url"],
    )

    async with connection:

        routing_key = in_exchange

        channel = await connection.channel()

        exchange = await channel.declare_exchange(
            routing_key, type=aio_pika.exchange.ExchangeType.FANOUT
        )

        await exchange.publish(
            aio_pika.Message(body=check_type(data)),
            routing_key=routing_key,
        )


@app.post("/smtp/send", tags=["Smtp"])
async def send(data: api_model.SMTPBody) -> api_model.Response:

    try:

        await publish(app_conf.RABBITMQ["in_exchange"], data)
        return api_model.Response(status="Success")

    except aio_pika.exceptions.AMQPError as err:
        return api_model.Response(status="NotSuccess", error=str(err))


# @app.post("/smtp/send_file", tags=["Smtp"])
# async def send(data: api_model.SMTPBodyWithFile) -> api_model.Response:

#     try:

#         await publish(app_conf.RABBITMQ["in_exchange"], data)
#         return api_model.Response(status="Success")

#     except aio_pika.exceptions.AMQPError as err:
#         return api_model.Response(status="NotSuccess", error=str(err))
