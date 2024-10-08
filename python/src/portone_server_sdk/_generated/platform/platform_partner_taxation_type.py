from __future__ import annotations
from typing import Any, Literal, Optional

PlatformPartnerTaxationType = Literal["NORMAL", "SIMPLE_TAX_INVOICE_ISSUER", "SIMPLE", "TAX_FREE"]
"""플랫폼 파트너 과세 유형
"""


def _serialize_platform_partner_taxation_type(obj: PlatformPartnerTaxationType) -> Any:
    return obj


def _deserialize_platform_partner_taxation_type(obj: Any) -> PlatformPartnerTaxationType:
    if obj not in ["NORMAL", "SIMPLE_TAX_INVOICE_ISSUER", "SIMPLE", "TAX_FREE"]:
        raise ValueError(f"{repr(obj)} is not PlatformPartnerTaxationType")
    return obj
