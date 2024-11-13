from __future__ import annotations
from typing import Any, Literal, Optional, Union

PlatformPartnerTaxationType = Union[Literal["NORMAL", "SIMPLE_TAX_INVOICE_ISSUER", "SIMPLE", "TAX_FREE"], str]
"""플랫폼 파트너 과세 유형
"""


def _serialize_platform_partner_taxation_type(obj: PlatformPartnerTaxationType) -> Any:
    if isinstance(obj, dict):
        return obj
    return obj


def _deserialize_platform_partner_taxation_type(obj: Any) -> PlatformPartnerTaxationType:
    return obj
