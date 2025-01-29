# -*- coding: utf-8 -*-
import os
import gate_api

from . import spot
from . import wallet

def create_instanse(_type: wallet.Wallet | spot.Spot, key: str, secret: str, host="https://api.gateio.ws/api/v4") -> wallet.Wallet | spot.Spot:

    GATE_CONFIGURATION: dict[str, str] = {
        "host": os.environ.get("GATE_HOST", host),
        "key": os.environ.get("GATE_KEY", key),
        "secret": os.environ.get(
            "GATE_SECRET",
            secret,
        ),
    }
    gate_api_client = gate_api.ApiClient(
        gate_api.Configuration(**GATE_CONFIGURATION))
    return _type(gate_api_client)