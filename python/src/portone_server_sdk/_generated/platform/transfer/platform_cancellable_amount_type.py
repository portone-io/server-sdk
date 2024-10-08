from __future__ import annotations
from typing import Any, Literal, Optional

PlatformCancellableAmountType = Literal["SUPPLY_WITH_VAT", "TAX_FREE"]
"""금액 타입
"""


def _serialize_platform_cancellable_amount_type(obj: PlatformCancellableAmountType) -> Any:
    return obj


def _deserialize_platform_cancellable_amount_type(obj: Any) -> PlatformCancellableAmountType:
    if obj not in ["SUPPLY_WITH_VAT", "TAX_FREE"]:
        raise ValueError(f"{repr(obj)} is not PlatformCancellableAmountType")
    return obj
