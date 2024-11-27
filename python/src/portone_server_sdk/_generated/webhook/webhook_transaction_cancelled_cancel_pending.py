from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field
from .webhook_transaction_cancelled_data_cancel_pending import WebhookTransactionCancelledDataCancelPending, _deserialize_webhook_transaction_cancelled_data_cancel_pending

@dataclass
class WebhookTransactionCancelledCancelPending:
    """(결제 취소가 비동기로 수행되는 경우) 결제 취소를 요청했을 때
    """
    timestamp: str
    """해당 웹훅을 트리거한 이벤트의 발생 시각(RFC 3339 형식)입니다. 고객사 서버가 웹훅을 수신하는 데 실패하여 재시도가 일어나도 이 값은 동일하게 유지됩니다.
    (RFC 3339 date-time)
    """
    data: WebhookTransactionCancelledDataCancelPending
    """(결제 취소가 비동기로 수행되는 경우) 결제 취소를 요청했을 때 이벤트의 실제 세부 내용입니다.
    """


def _deserialize_webhook_transaction_cancelled_cancel_pending(obj: Any) -> WebhookTransactionCancelledCancelPending:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "type" not in obj:
        raise KeyError(f"'type' is not in {obj}")
    type = obj["type"]
    if type != "Transaction.CancelPending":
        raise ValueError(f"{repr(type)} is not 'Transaction.CancelPending'")
    if "timestamp" not in obj:
        raise KeyError(f"'timestamp' is not in {obj}")
    timestamp = obj["timestamp"]
    if not isinstance(timestamp, str):
        raise ValueError(f"{repr(timestamp)} is not str")
    if "data" not in obj:
        raise KeyError(f"'data' is not in {obj}")
    data = obj["data"]
    data = _deserialize_webhook_transaction_cancelled_data_cancel_pending(data)
    return WebhookTransactionCancelledCancelPending(timestamp, data)
