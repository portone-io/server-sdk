from __future__ import annotations
from typing import Any, Literal, Optional
from dataclasses import dataclass, field
from portone_server_sdk._generated.common.bank import Bank, _deserialize_bank, _serialize_bank

@dataclass
class PaymentMethodEasyPayMethodCharge:
    """충전식 포인트 결제 정보
    """
    type: Literal["PaymentMethodEasyPayMethodCharge"] = field(repr=False)
    bank: Optional[Bank]
    """표준 은행 코드
    """


def _serialize_payment_method_easy_pay_method_charge(obj: PaymentMethodEasyPayMethodCharge) -> Any:
    entity = {}
    entity["type"] = "PaymentMethodEasyPayMethodCharge"
    if obj.bank is not None:
        entity["bank"] = _serialize_bank(obj.bank)
    return entity


def _deserialize_payment_method_easy_pay_method_charge(obj: Any) -> PaymentMethodEasyPayMethodCharge:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "type" not in obj:
        raise KeyError(f"'type' is not in {obj}")
    type = obj["type"]
    if type != "PaymentMethodEasyPayMethodCharge":
        raise ValueError(f"{repr(type)} is not 'PaymentMethodEasyPayMethodCharge'")
    if "bank" in obj:
        bank = obj["bank"]
        bank = _deserialize_bank(bank)
    else:
        bank = None
    return PaymentMethodEasyPayMethodCharge(type, bank)
