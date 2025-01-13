from __future__ import annotations
from typing import Any, Literal, Optional, Union

PlatformTaxationType = Union[Literal["NORMAL", "SIMPLE_TAX_INVOICE_ISSUER", "SIMPLE", "TAX_FREE", "ASSIGNED_ID_NUMBER", "SPECIAL"], str]
"""플랫폼 과세 유형
"""


def _serialize_platform_taxation_type(obj: PlatformTaxationType) -> Any:
    if isinstance(obj, dict):
        return obj
    return obj


def _deserialize_platform_taxation_type(obj: Any) -> PlatformTaxationType:
    return obj
