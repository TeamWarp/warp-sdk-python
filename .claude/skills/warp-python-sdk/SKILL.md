---
name: warp-python-sdk
description: "Python SDK for Warp API. Use when writing Python code that calls Warp API with the warp package: installing it, constructing and authenticating the client, and calling API operations."
---

# Warp Python SDK

Generated Python client for Warp API, published as `warp`. Use the generated client instead of hand-writing HTTP requests.

## Install

```sh
pip install warp
```

## Client setup and authentication

```python
import os

from warp import Warp

client = Warp(
    api_key=os.environ.get("WARP_API_KEY"),
)
```

Provide credentials using the options below. Environment variables are read automatically when the target runtime supports them:

- `api_key` (env: `WARP_API_KEY`) — Credential for the apiKey scheme.

## Calling operations

```python
import os

from warp import Warp

client = Warp(
    api_key=os.environ.get("WARP_API_KEY"),
)

time_off = client.time_off.list_assignments()
print(time_off)
```

Method names, parameter shapes, and response types are generated from the API description — do not guess them. Look up the exact call signature in [api.md](../../../api.md) before writing a call.

## Error handling

Non-success responses throw generated API errors. Error objects expose status, headers, response body, and request metadata where the target runtime supports it.

```python
from warp import APIStatusError

try:
    time_off = client.time_off.list_assignments()
except APIStatusError as err:
    print(err.status_code, err.message)
    raise
```

## Requirements

- Python 3.8 or newer

## Reference files

- [README.md](../../../README.md) — full feature tour: client options, request options, retries and timeouts, logging.
- [api.md](../../../api.md) — complete catalogue of every operation with request and response types.
