from __future__ import annotations
from typing import Any, Literal, Optional

PlatformPayoutMethod = Literal["DIRECT", "AGENCY"]


def _serialize_platform_payout_method(obj: PlatformPayoutMethod) -> Any:
    return obj


def _deserialize_platform_payout_method(obj: Any) -> PlatformPayoutMethod:
    if obj not in ["DIRECT", "AGENCY"]:
        raise ValueError(f"{repr(obj)} is not PlatformPayoutMethod")
    return obj
