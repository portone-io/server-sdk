from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field
from portone_server_sdk._generated.common.bank import Bank, _deserialize_bank, _serialize_bank

@dataclass
class CancelPaymentBodyRefundAccount:
    """고객 정보 입력 형식
    """
    bank: Bank
    """은행
    """
    number: str
    """계좌번호
    """
    holder_name: str
    """예금주
    """
    holder_phone_number: Optional[str]
    """예금주 연락처 - 스마트로 가상계좌 결제인 경우에 필요합니다.
    """


def _serialize_cancel_payment_body_refund_account(obj: CancelPaymentBodyRefundAccount) -> Any:
    entity = {}
    entity["bank"] = _serialize_bank(obj.bank)
    entity["number"] = obj.number
    entity["holderName"] = obj.holder_name
    if obj.holder_phone_number is not None:
        entity["holderPhoneNumber"] = obj.holder_phone_number
    return entity


def _deserialize_cancel_payment_body_refund_account(obj: Any) -> CancelPaymentBodyRefundAccount:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "bank" not in obj:
        raise KeyError(f"'bank' is not in {obj}")
    bank = obj["bank"]
    bank = _deserialize_bank(bank)
    if "number" not in obj:
        raise KeyError(f"'number' is not in {obj}")
    number = obj["number"]
    if not isinstance(number, str):
        raise ValueError(f"{repr(number)} is not str")
    if "holderName" not in obj:
        raise KeyError(f"'holderName' is not in {obj}")
    holder_name = obj["holderName"]
    if not isinstance(holder_name, str):
        raise ValueError(f"{repr(holder_name)} is not str")
    if "holderPhoneNumber" in obj:
        holder_phone_number = obj["holderPhoneNumber"]
        if not isinstance(holder_phone_number, str):
            raise ValueError(f"{repr(holder_phone_number)} is not str")
    else:
        holder_phone_number = None
    return CancelPaymentBodyRefundAccount(bank, number, holder_name, holder_phone_number)
