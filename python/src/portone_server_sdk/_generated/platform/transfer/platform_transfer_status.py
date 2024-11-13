from __future__ import annotations
from typing import Any, Literal, Optional, Union

PlatformTransferStatus = Union[Literal["SCHEDULED", "IN_PROCESS", "SETTLED", "IN_PAYOUT", "PAID_OUT"], str]
"""정산 상태
"""


def _serialize_platform_transfer_status(obj: PlatformTransferStatus) -> Any:
    if isinstance(obj, dict):
        return obj
    return obj


def _deserialize_platform_transfer_status(obj: Any) -> PlatformTransferStatus:
    return obj
