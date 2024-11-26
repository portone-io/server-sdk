from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field
from ...payment.billing_key.billing_key_payment_method import BillingKeyPaymentMethod, _deserialize_billing_key_payment_method, _serialize_billing_key_payment_method
from ...common.selected_channel import SelectedChannel, _deserialize_selected_channel, _serialize_selected_channel

@dataclass
class IssuedPgBillingKeyIssueResponse:
    """빌링키 발급 성공 채널 응답
    """
    channel: SelectedChannel
    """채널

    빌링키 발급을 시도한 채널입니다.
    """
    pg_tx_id: Optional[str] = field(default=None)
    """PG사 거래 아이디
    """
    method: Optional[BillingKeyPaymentMethod] = field(default=None)
    """빌링키 결제수단 상세 정보

    채널에 대응되는 PG사에서 응답한 빌링키 발급 수단 정보입니다.
    """


def _serialize_issued_pg_billing_key_issue_response(obj: IssuedPgBillingKeyIssueResponse) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["type"] = "ISSUED"
    entity["channel"] = _serialize_selected_channel(obj.channel)
    if obj.pg_tx_id is not None:
        entity["pgTxId"] = obj.pg_tx_id
    if obj.method is not None:
        entity["method"] = _serialize_billing_key_payment_method(obj.method)
    return entity


def _deserialize_issued_pg_billing_key_issue_response(obj: Any) -> IssuedPgBillingKeyIssueResponse:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "type" not in obj:
        raise KeyError(f"'type' is not in {obj}")
    type = obj["type"]
    if type != "ISSUED":
        raise ValueError(f"{repr(type)} is not 'ISSUED'")
    if "channel" not in obj:
        raise KeyError(f"'channel' is not in {obj}")
    channel = obj["channel"]
    channel = _deserialize_selected_channel(channel)
    if "pgTxId" in obj:
        pg_tx_id = obj["pgTxId"]
        if not isinstance(pg_tx_id, str):
            raise ValueError(f"{repr(pg_tx_id)} is not str")
    else:
        pg_tx_id = None
    if "method" in obj:
        method = obj["method"]
        method = _deserialize_billing_key_payment_method(method)
    else:
        method = None
    return IssuedPgBillingKeyIssueResponse(channel, pg_tx_id, method)
