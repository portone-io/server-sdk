from __future__ import annotations
from typing import Any, Literal, Optional, Union

PlatformCancellableAmountType = Union[Literal["SUPPLY_WITH_VAT", "TAX_FREE"], str]
"""금액 타입
"""


def _serialize_platform_cancellable_amount_type(obj: PlatformCancellableAmountType) -> Any:
    if isinstance(obj, dict):
        return obj
    return obj


def _deserialize_platform_cancellable_amount_type(obj: Any) -> PlatformCancellableAmountType:
    return obj
