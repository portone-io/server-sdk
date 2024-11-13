from __future__ import annotations
from typing import Any, Literal, Optional, Union

PlatformPayoutMethod = Union[Literal["DIRECT", "AGENCY"], str]


def _serialize_platform_payout_method(obj: PlatformPayoutMethod) -> Any:
    if isinstance(obj, dict):
        return obj
    return obj


def _deserialize_platform_payout_method(obj: Any) -> PlatformPayoutMethod:
    return obj
