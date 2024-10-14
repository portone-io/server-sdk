from __future__ import annotations
from typing import Any, Literal, Optional
from dataclasses import dataclass, field
from portone_server_sdk._generated.common.bank import Bank, _deserialize_bank, _serialize_bank

@dataclass
class BillingKeyPaymentMethodTransfer:
    """계좌이체 정보
    """
    type: Literal["BillingKeyPaymentMethodTransfer"] = field(repr=False)
    bank: Optional[Bank]
    """표준 은행 코드
    """
    account_number: Optional[str]
    """계좌번호
    """


def _serialize_billing_key_payment_method_transfer(obj: BillingKeyPaymentMethodTransfer) -> Any:
    entity = {}
    entity["type"] = "BillingKeyPaymentMethodTransfer"
    if obj.bank is not None:
        entity["bank"] = _serialize_bank(obj.bank)
    if obj.account_number is not None:
        entity["accountNumber"] = obj.account_number
    return entity


def _deserialize_billing_key_payment_method_transfer(obj: Any) -> BillingKeyPaymentMethodTransfer:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "type" not in obj:
        raise KeyError(f"'type' is not in {obj}")
    type = obj["type"]
    if type != "BillingKeyPaymentMethodTransfer":
        raise ValueError(f"{repr(type)} is not 'BillingKeyPaymentMethodTransfer'")
    if "bank" in obj:
        bank = obj["bank"]
        bank = _deserialize_bank(bank)
    else:
        bank = None
    if "accountNumber" in obj:
        account_number = obj["accountNumber"]
        if not isinstance(account_number, str):
            raise ValueError(f"{repr(account_number)} is not str")
    else:
        account_number = None
    return BillingKeyPaymentMethodTransfer(type, bank, account_number)
