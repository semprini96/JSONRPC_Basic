# JSONRPC_Basic
Very simple JSON-RPC Server and Client in Python

# Getting started
```
git clone https://github.com/semprini96/JSONRPC_Basic.git
```

This project uses [Pipenv](https://pipenv.pypa.io/en/latest/). Install it first:
```
pip install pipenv
```

# Project files
* ***server.py*** - Server process, uses `jsonrpcserver`
* ***client.py*** - Command line client process, uses `jsonrpcclient`
* ***qt_app.py*** - Very simple Qt-based client GUI made with PyQt5
* ***qt_client.ui***, ***qt_client.py*** - UI file made in Qt Designer and corresponding *.py file made by `pyuic5`
* ***json_utils.py*** - functions for Numpy <--> JSON conversion