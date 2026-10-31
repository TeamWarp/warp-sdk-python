---
name: warp-python-sdk
description: "Python SDK for warp API. Use when writing Python code that calls warp API with the warp-hr package: installing it, constructing and authenticating the client, and calling API operations."
---

# warp Python SDK

Generated Python client for warp API, published as `warp-hr`. Use the generated client instead of hand-writing HTTP requests.

## Install

```sh
pip install warp-hr
```

## Client setup and authentication

```python
import os

from warp_hr import Warp

client = Warp(
    api_key=os.environ.get("WARP_API_KEY"),
)
```

Provide credentials using the options below. Environment variables are read automatically when the target runtime supports them:

- `api_key` (env: `WARP_API_KEY`) — Credential for the apiKey scheme.

## Calling operations

```python
import os

from warp_hr import Warp

client = Warp(
    api_key=os.environ.get("WARP_API_KEY"),
)

health_plan = client.benefits.health_plans.list(
    limit="limit",
    statuses=["active"],
)

print(health_plan)
```

Method names, parameter shapes, and response types are generated from the API description — do not guess them. Look up the exact call signature in [api.md](./api.md) before writing a call.

## Error handling

Non-success responses throw generated API errors. Error objects expose status, headers, response body, and request metadata where the target runtime supports it.

```python
from warp_hr import APIStatusError

try:
    health_plan = client.benefits.health_plans.list(
        limit="limit",
        statuses=["active"],
    )
except APIStatusError as err:
    print(err.status_code, err.message)
    raise
```

## Requirements

- Python 3.9 or newer

## Reference files

- [README.md](./README.md) — full feature tour: client options, retries and timeouts, webhooks, logging.
- [api.md](./api.md) — complete catalogue of every operation with request and response types.
