# -*- coding: utf-8 -*-
import typing

import model as api_model

from app import app
from gate_wrapper import spot, model as gate_model, create_instanse


@app.post("/spot/currency_pair", tags=["Spot"])
async def currency_pair(
    data: api_model.SecurityData, currency_pair: str
) -> gate_model.CurrencyPair:

    return await create_instanse(spot.Spot, data.key, data.secret).currency_pair(
        currency_pair, async_req=True
    )


@app.post("/spot/cancel_orders", tags=["Spot"])
async def cancel_orders(
    data: api_model.SecurityData, currency_pair: str
) -> typing.List[gate_model.Order]:

    return await create_instanse(spot.Spot, data.key, data.secret).cancel_orders(
        currency_pair=currency_pair, async_req=True
    )


@app.post("/spot/orders", tags=["Spot"])
async def orders(
    data: api_model.SecurityData,
    currency_pair: str,
    status: typing.Literal["open", "finished"],
) -> typing.List[gate_model.Order]:

    return await create_instanse(spot.Spot, data.key, data.secret).list_orders(
        currency_pair, status, async_req=True
    )


@app.post("/spot/currency_pairs", tags=["Spot"])
async def currency_pairs(
    data: api_model.SecurityData,
) -> typing.List[gate_model.CurrencyPair]:

    return await create_instanse(spot.Spot, data.key, data.secret).list_currency_pairs(
        async_req=True
    )


@app.post("/spot/spot_accounts", tags=["Spot"])
async def spot_accounts(
    data: api_model.SecurityData, currency: str = None
) -> typing.List[gate_model.Account]:

    return await create_instanse(spot.Spot, data.key, data.secret).list_spot_accounts(
        currency=currency, async_req=True
    )


@app.post("/spot/spot_account_book", tags=["Spot"])
async def spot_account_book(
    data: api_model.SecurityData, currency: str = None
) -> typing.List[gate_model.AccountBook]:

    return await create_instanse(
        spot.Spot, data.key, data.secret
    ).list_spot_account_book(currency=currency, async_req=True)


@app.post("/spot/trades", tags=["Spot"])
async def trades(
    data: api_model.SecurityData, currency_pair: str
) -> typing.List[gate_model.Trade]:

    return await create_instanse(spot.Spot, data.key, data.secret).list_trades(
        currency_pair, async_req=True
    )


@app.post("/spot/order_book", tags=["Spot"])
async def order_book(
    data: api_model.SecurityData, currency_pair: str
) -> spot.OrderBook:

    return await create_instanse(spot.Spot, data.key, data.secret).order_book(
        currency_pair, async_req=True
    )


@app.post("/spot/all_open_orders", tags=["Spot"])
async def all_open_orders(
    data: api_model.SecurityData,
) -> typing.List[gate_model.OpenOrders]:

    return await create_instanse(spot.Spot, data.key, data.secret).list_all_open_orders(
        async_req=True
    )


@app.post("/spot/candlesticks", tags=["Spot"])
async def candlesticks(
    data: api_model.SecurityData, currency_pair: str
) -> typing.List[gate_model.Candlestick]:

    return await create_instanse(spot.Spot, data.key, data.secret).list_candlesticks(
        currency_pair, async_req=True
    )
