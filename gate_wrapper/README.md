This packet is the facate pattern for integration with the service <a href="https://www.gate.io/docs/developers/apiv4/">gate.io API</a>.

Info about module:

* **model.py** - pydantic model of the all data is received from <a href="https://www.gate.io/docs/developers/apiv4/">gate.io API</a>
* **parse.py** - types of parsers serializing data from <a href="https://www.gate.io/docs/developers/apiv4/">gate.io API</a> methods. It was implemented according to the pattern factory method.
* **wallet.py / spot.py** - facate pattern in which methods are presented as wapper methods under methods package gate_api.
* **./tests** - integration testing

**Right now this packge doesn't cover all methods of the <a href="https://www.gate.io/docs/developers/apiv4/">gate.io API</a>.**
