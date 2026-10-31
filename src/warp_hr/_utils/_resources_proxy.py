from __future__ import annotations

from typing import Any
from typing_extensions import override

from ._proxy import LazyProxy


class ResourcesProxy(LazyProxy[Any]):
    """A proxy for the `warp_hr.resources` module.

    This is used so that we can lazily import `warp_hr.resources` only when
    needed *and* so that users can just import `warp_hr` and reference `warp_hr.resources`
    """

    @override
    def __load__(self) -> Any:
        import importlib

        mod = importlib.import_module("warp_hr.resources")
        return mod


resources = ResourcesProxy().__as_proxied__()
