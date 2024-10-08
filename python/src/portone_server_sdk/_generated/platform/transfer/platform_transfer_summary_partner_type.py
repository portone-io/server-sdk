from __future__ import annotations
from typing import Any, Literal, Optional

PlatformTransferSummaryPartnerType = Literal["BUSINESS", "WHT_PAYER", "NON_WHT_PAYER"]
"""파트너 유형
"""


def _serialize_platform_transfer_summary_partner_type(obj: PlatformTransferSummaryPartnerType) -> Any:
    return obj


def _deserialize_platform_transfer_summary_partner_type(obj: Any) -> PlatformTransferSummaryPartnerType:
    if obj not in ["BUSINESS", "WHT_PAYER", "NON_WHT_PAYER"]:
        raise ValueError(f"{repr(obj)} is not PlatformTransferSummaryPartnerType")
    return obj
