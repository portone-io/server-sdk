from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field
from ..payment.payment_transaction import PaymentTransaction, _deserialize_payment_transaction, _serialize_payment_transaction

@dataclass
class GetPaymentTransactionsResponse:
    """결제 시도 내역 조회 응답 정보
    """
    items: list[PaymentTransaction]
    """결제 시도 내역
    """


def _serialize_get_payment_transactions_response(obj: GetPaymentTransactionsResponse) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["items"] = list(map(_serialize_payment_transaction, obj.items))
    return entity


def _deserialize_get_payment_transactions_response(obj: Any) -> GetPaymentTransactionsResponse:
    if not isinstance(obj, dict):
        raise ValueError("Expected dict for obj")
    if "items" not in obj:
        raise KeyError("Missing required field 'items'")
    items = obj["items"]
    if not isinstance(items, list):
        raise ValueError("Expected list for items")
    for i, item in enumerate(items):
        item = _deserialize_payment_transaction(item)
        items[i] = item
    return GetPaymentTransactionsResponse(items)
