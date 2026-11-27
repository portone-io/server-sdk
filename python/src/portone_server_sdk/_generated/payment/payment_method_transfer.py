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
    account_number: Optional[str] = field(default=None)
    """계좌번호
    """


def _serialize_payment_method_transfer(obj: PaymentMethodTransfer) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["type"] = "PaymentMethodTransfer"
    if obj.bank is not None:
        entity["bank"] = _serialize_bank(obj.bank)
    if obj.account_number is not None:
        entity["accountNumber"] = obj.account_number
    return entity


def _deserialize_payment_method_transfer(obj: Any) -> PaymentMethodTransfer:
    if not isinstance(obj, dict):
        raise ValueError("Expected dict for obj")
    if "type" not in obj:
        raise KeyError("Missing required field 'type'")
    type = obj["type"]
    if type != "PaymentMethodTransfer":
        raise ValueError("Expected 'PaymentMethodTransfer' for type")
    if "bank" in obj:
        bank = obj["bank"]
        bank = _deserialize_bank(bank)
    else:
        bank = None
    if "accountNumber" in obj:
        account_number = obj["accountNumber"]
        if not isinstance(account_number, str):
            raise ValueError("Expected str for account_number")
    else:
        account_number = None
    return PaymentMethodTransfer(bank, account_number)
