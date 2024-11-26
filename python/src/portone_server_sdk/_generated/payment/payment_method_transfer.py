from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field
from ..common.bank import Bank, _deserialize_bank, _serialize_bank

@dataclass
class PaymentMethodTransfer:
    """계좌 이체 상세 정보
    """
    bank: Optional[Bank] = field(default=None)
    """표준 은행 코드
    """


def _serialize_payment_method_transfer(obj: PaymentMethodTransfer) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["type"] = "PaymentMethodTransfer"
    if obj.bank is not None:
        entity["bank"] = _serialize_bank(obj.bank)
    return entity


def _deserialize_payment_method_transfer(obj: Any) -> PaymentMethodTransfer:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "type" not in obj:
        raise KeyError(f"'type' is not in {obj}")
    type = obj["type"]
    if type != "PaymentMethodTransfer":
        raise ValueError(f"{repr(type)} is not 'PaymentMethodTransfer'")
    if "bank" in obj:
        bank = obj["bank"]
        bank = _deserialize_bank(bank)
    else:
        bank = None
    return PaymentMethodTransfer(bank)
