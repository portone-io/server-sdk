from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class WebhookTransactionDataVirtualAccountIssued:
    """가상계좌가 발급되었을 때 이벤트의 실제 세부 내용입니다.
    """
    payment_id: str
    """고객사에서 채번한 결제 건의 고유 주문 번호입니다.
    """
    store_id: str
    """웹훅을 트리거한 상점의 아이디입니다.
    """
    transaction_id: str
    """포트원에서 채번한 고유 거래 번호입니다. 한 결제 건에 여러 시도가 있을 경우 `transactionId` 가 달라질 수 있습니다.
    """


def _deserialize_webhook_transaction_data_virtual_account_issued(obj: Any) -> WebhookTransactionDataVirtualAccountIssued:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "paymentId" not in obj:
        raise KeyError(f"'paymentId' is not in {obj}")
    payment_id = obj["paymentId"]
    if not isinstance(payment_id, str):
        raise ValueError(f"{repr(payment_id)} is not str")
    if "storeId" not in obj:
        raise KeyError(f"'storeId' is not in {obj}")
    store_id = obj["storeId"]
    if not isinstance(store_id, str):
        raise ValueError(f"{repr(store_id)} is not str")
    if "transactionId" not in obj:
        raise KeyError(f"'transactionId' is not in {obj}")
    transaction_id = obj["transactionId"]
    if not isinstance(transaction_id, str):
        raise ValueError(f"{repr(transaction_id)} is not str")
    return WebhookTransactionDataVirtualAccountIssued(payment_id, store_id, transaction_id)
