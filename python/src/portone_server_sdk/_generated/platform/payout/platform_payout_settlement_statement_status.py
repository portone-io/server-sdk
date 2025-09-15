from __future__ import annotations
from typing import Any, Literal, Optional, Union

PlatformPayoutSettlementStatementStatus = Union[Literal["UNSENT", "SENT", "SEND_FAILED", "SEND_PREPARED"], str]
"""정산 내역서 발송 상태
"""


def _serialize_platform_payout_settlement_statement_status(obj: PlatformPayoutSettlementStatementStatus) -> Any:
    if isinstance(obj, dict):
        return obj
    return obj


def _deserialize_platform_payout_settlement_statement_status(obj: Any) -> PlatformPayoutSettlementStatementStatus:
    return obj
