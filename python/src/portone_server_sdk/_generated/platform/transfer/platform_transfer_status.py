from __future__ import annotations
from typing import Any, Literal, Optional

PlatformTransferStatus = Literal["SCHEDULED", "IN_PROCESS", "SETTLED", "IN_PAYOUT", "PAID_OUT"]
"""정산 상태
"""


def _serialize_platform_transfer_status(obj: PlatformTransferStatus) -> Any:
    return obj


def _deserialize_platform_transfer_status(obj: Any) -> PlatformTransferStatus:
    if obj not in ["SCHEDULED", "IN_PROCESS", "SETTLED", "IN_PAYOUT", "PAID_OUT"]:
        raise ValueError(f"{repr(obj)} is not PlatformTransferStatus")
    return obj
