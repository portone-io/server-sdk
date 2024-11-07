from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class WebhookTransactionRequestCancelledData:
    payment_id: str
    """고객사에서 채번한 결제 건의 고유 주문 번호입니다.
    """
    transaction_id: str
    """포트원에서 채번한 고유 거래 번호입니다. 한 결제 건에 여러 시도가 있을 경우 `transactionId` 가 달라질 수 있습니다.
    """
    cancellation_id: str
    """포트원에서 채번한 결제건의 취소 고유 번호입니다. `type` 이 `Transaction.PartialCancelled` 혹은 `Transaction.Cancelled` 일 때 존재합니다.
    """


def _serialize_webhook_transaction_request_cancelled_data(obj: WebhookTransactionRequestCancelledData) -> Any:
    entity = {}
    entity["paymentId"] = obj.payment_id
    entity["transactionId"] = obj.transaction_id
    entity["cancellationId"] = obj.cancellation_id
    return entity


def _deserialize_webhook_transaction_request_cancelled_data(obj: Any) -> WebhookTransactionRequestCancelledData:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "paymentId" not in obj:
        raise KeyError(f"'paymentId' is not in {obj}")
    payment_id = obj["paymentId"]
    if not isinstance(payment_id, str):
        raise ValueError(f"{repr(payment_id)} is not str")
    if "transactionId" not in obj:
        raise KeyError(f"'transactionId' is not in {obj}")
    transaction_id = obj["transactionId"]
    if not isinstance(transaction_id, str):
        raise ValueError(f"{repr(transaction_id)} is not str")
    if "cancellationId" not in obj:
        raise KeyError(f"'cancellationId' is not in {obj}")
    cancellation_id = obj["cancellationId"]
    if not isinstance(cancellation_id, str):
        raise ValueError(f"{repr(cancellation_id)} is not str")
    return WebhookTransactionRequestCancelledData(payment_id, transaction_id, cancellation_id)
