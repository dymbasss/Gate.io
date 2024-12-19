import os
import pytest
import gate_api

from ..spot import Spot
from ..wallet import Wallet

__all__ = [
    "instance_spot",
    "instance_wallet",
]


# Your credentials
GATE_CONFIGURATION = {
    "host": os.environ.get("GATE_HOST", "https://api.gateio.ws/api/v4"),
    "key": os.environ.get("GATE_KEY", ""),
    "secret": os.environ.get(
        "GATE_SECRET",
        "",
    ),
}

api_client = gate_api.ApiClient(gate_api.Configuration(**GATE_CONFIGURATION))


@pytest.fixture
def instance_spot():
    spot = Spot(api_client)
    yield spot



@pytest.fixture
def instance_wallet():

    wallet = Wallet(api_client)
    yield wallet