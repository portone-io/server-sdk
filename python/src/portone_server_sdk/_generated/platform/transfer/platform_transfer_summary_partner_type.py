from __future__ import annotations
from typing import Any, Literal, Optional, Union

PlatformTransferSummaryPartnerType = Union[Literal["BUSINESS", "WHT_PAYER", "NON_WHT_PAYER"], str]
"""파트너 유형
"""


def _serialize_platform_transfer_summary_partner_type(obj: PlatformTransferSummaryPartnerType) -> Any:
    if isinstance(obj, dict):
        return obj
    return obj


def _deserialize_platform_transfer_summary_partner_type(obj: Any) -> PlatformTransferSummaryPartnerType:
    return obj
