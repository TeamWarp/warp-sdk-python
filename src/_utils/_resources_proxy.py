from __future__ import annotations

from typing import Any
from typing_extensions import override

from ._proxy import LazyProxy


class ResourcesProxy(LazyProxy[Any]):
    """A proxy for the `warp.resources` module.

    This is used so that we can lazily import `warp.resources` only when
    needed *and* so that users can just import `warp` and reference `warp.resources`
    """

    @override
    def __load__(self) -> Any:
        import importlib

        mod = importlib.import_module("warp.resources")
        return mod


resources = ResourcesProxy().__as_proxied__()
