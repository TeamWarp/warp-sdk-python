# Warp

This library provides convenient access to the Warp REST API from Python.

The REST API documentation can be found on [docs.warp.co](https://docs.warp.co). The full API of this library can be found in [api.md](./api.md).

<br />

## Contents

- [Installation](#installation)
- [Usage](#usage)
- [API Reference](./api.md)
- [Async](#async)
- [Authentication](#authentication)
- [Errors](#errors)
- [Client Options](#client-options)
- [Retries and Timeouts](#retries-and-timeouts)
- [Webhooks](#webhooks)
- [Helpers](#helpers)
- [Logging](#logging)
- [Requirements](#requirements)

<br />

## Installation

```sh
pip install warp-hr
```

<br />

## Usage

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

The examples in the following sections assume a `client` configured as shown above.

See the [API reference](./api.md) for every available operation.

<br />

## Async

Every client has an `Async` counterpart (`AsyncWarp`) exposing the same resource tree with `await`.

```python
import asyncio

from warp_hr import AsyncWarp


async def main() -> None:
    client = AsyncWarp()
    health_plan = await client.benefits.health_plans.list(
        limit="limit",
        statuses=["active"],
    )


asyncio.run(main())
```

<br />

## Authentication

Pass credentials to the generated client constructor. Environment variables are read automatically when supported by the target runtime.

| Option | Type | Default | Description |
| --- | --- | --- | --- |
| `api_key` | `str \| None` | - | Credential for the apiKey scheme. Defaults to WARP_API_KEY. |

Declared schemes:

- `apiKey` API key in header `x-api-key`

<br />

## Errors

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

Documented error statuses: `400`, `401`, `403`, `404`, `409`, `422`, `429`, `500`.

<br />

## Client Options

Configure the generated client by setting any of these options when you create it.

```python
from warp_hr import Warp

client = Warp(
    timeout=60.0,
    max_retries=2,
)
```

| Option | Type | Default | Description |
| --- | --- | --- | --- |
| `api_key` | `str \| None` | `os.environ.get("WARP_API_KEY")` | Credential for the apiKey scheme. |
| `base_url` | `str \| httpx.URL \| None` | - | Override the default API base URL. |
| `timeout` | `float \| Timeout \| None` | `60.0` | Maximum time in seconds to wait for a response before aborting a request. |
| `max_retries` | `int` | `2` | Number of retries for temporary failures. |
| `default_headers` | `Mapping[str, str] \| None` | - | Headers sent with every request. |
| `default_query` | `Mapping[str, object] \| None` | - | Query parameters sent with every request. |

<br />

## Retries and Timeouts

Generated clients support request timeouts and retry temporary failures such as network errors, 408, 409, 429, and 5xx responses. Retry delays honor `Retry-After` headers when present. Tune the retry and timeout client options shown above, or override them per request.

<br />

## Webhooks

The webhook helper verifies the signature of each delivery your server receives, then decodes its body into a typed event. Pass it the request body exactly as it arrived, before any JSON parsing, together with the request headers: the signature covers the raw body, so one that was parsed and re-serialized fails verification. A delivery whose signature does not verify is rejected before it is decoded.

```python
# `payload` is the raw request body; `headers` holds the request headers.
event = client.webhooks.unwrap(payload, headers=headers)
```

The signing secret comes from the client's `webhook_secret` option, which defaults to the `WARP_WEBHOOK_SECRET` environment variable. Pass `key` to use a different secret for one call.

The same resource also has:

- `client.webhooks.verify_signature(payload, headers)` checks a delivery's signature, and fails when it does not verify.
- `client.webhooks.parse_unsafe(payload)` decodes a body into a typed event without checking its signature. Use it only for a body verified elsewhere, or in tests.

<br />

## Helpers

- Use `client.with_raw_response.<resource>.<method>(...)` to access the raw `httpx.Response` and parse it yourself.
- Use `client.with_streaming_response.<resource>.<method>(...)` to stream a response body without buffering it.

<br />

## Logging

- Set the `WARP_LOG` environment variable to `info` or `debug` to enable HTTP logging.
- Logs are emitted through the standard `logging` module under the `warp_hr` logger.

<br />

## Requirements

- Python 3.9 or newer

Powered by Scalar.
