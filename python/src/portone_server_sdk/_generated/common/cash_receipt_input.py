from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field
from ..common.cash_receipt_input_type import CashReceiptInputType, _deserialize_cash_receipt_input_type, _serialize_cash_receipt_input_type

@dataclass
class CashReceiptInput:
    """현금영수증 입력 정보
    """
    type: CashReceiptInputType
    """현금영수증 유형
    """
    customer_identity_number: Optional[str] = field(default=None)
    """사용자 식별 번호

    미발행 유형 선택 시 입력하지 않습니다.
    """


def _serialize_cash_receipt_input(obj: CashReceiptInput) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["type"] = _serialize_cash_receipt_input_type(obj.type)
    if obj.customer_identity_number is not None:
        entity["customerIdentityNumber"] = obj.customer_identity_number
    return entity


def _deserialize_cash_receipt_input(obj: Any) -> CashReceiptInput:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "type" not in obj:
        raise KeyError(f"'type' is not in {obj}")
    type = obj["type"]
    type = _deserialize_cash_receipt_input_type(type)
    if "customerIdentityNumber" in obj:
        customer_identity_number = obj["customerIdentityNumber"]
        if not isinstance(customer_identity_number, str):
            raise ValueError(f"{repr(customer_identity_number)} is not str")
    else:
        customer_identity_number = None
    return CashReceiptInput(type, customer_identity_number)
