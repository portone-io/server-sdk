from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field
from portone_server_sdk._generated.common.cash_receipt_input_type import CashReceiptInputType, _deserialize_cash_receipt_input_type, _serialize_cash_receipt_input_type

@dataclass
class InstantPaymentMethodInputVirtualAccountCashReceiptInfo:
    """가상계좌 결제 시 현금영수증 정보
    """
    type: CashReceiptInputType
    """현금영수증 유형
    """
    customer_identity_number: str
    """사용자 식별 번호
    """


def _serialize_instant_payment_method_input_virtual_account_cash_receipt_info(obj: InstantPaymentMethodInputVirtualAccountCashReceiptInfo) -> Any:
    entity = {}
    entity["type"] = _serialize_cash_receipt_input_type(obj.type)
    entity["customerIdentityNumber"] = obj.customer_identity_number
    return entity


def _deserialize_instant_payment_method_input_virtual_account_cash_receipt_info(obj: Any) -> InstantPaymentMethodInputVirtualAccountCashReceiptInfo:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "type" not in obj:
        raise KeyError(f"'type' is not in {obj}")
    type = obj["type"]
    type = _deserialize_cash_receipt_input_type(type)
    if "customerIdentityNumber" not in obj:
        raise KeyError(f"'customerIdentityNumber' is not in {obj}")
    customer_identity_number = obj["customerIdentityNumber"]
    if not isinstance(customer_identity_number, str):
        raise ValueError(f"{repr(customer_identity_number)} is not str")
    return InstantPaymentMethodInputVirtualAccountCashReceiptInfo(type, customer_identity_number)
