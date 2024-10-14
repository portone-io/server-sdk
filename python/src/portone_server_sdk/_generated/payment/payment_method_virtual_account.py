from __future__ import annotations
from typing import Any, Literal, Optional
from dataclasses import dataclass, field
from portone_server_sdk._generated.common.bank import Bank, _deserialize_bank, _serialize_bank
from portone_server_sdk._generated.payment.payment_method_virtual_account_refund_status import PaymentMethodVirtualAccountRefundStatus, _deserialize_payment_method_virtual_account_refund_status, _serialize_payment_method_virtual_account_refund_status
from portone_server_sdk._generated.payment.payment_method_virtual_account_type import PaymentMethodVirtualAccountType, _deserialize_payment_method_virtual_account_type, _serialize_payment_method_virtual_account_type

@dataclass
class PaymentMethodVirtualAccount:
    """가상계좌 상세 정보
    """
    type: Literal["PaymentMethodVirtualAccount"] = field(repr=False)
    account_number: str
    """계좌번호
    """
    bank: Optional[Bank]
    """표준 은행 코드
    """
    account_type: Optional[PaymentMethodVirtualAccountType]
    """계좌 유형
    """
    remittee_name: Optional[str]
    """계좌주
    """
    remitter_name: Optional[str]
    """송금인(입금자)
    """
    expired_at: Optional[str]
    """입금만료시점
    (RFC 3339 date-time)
    """
    issued_at: Optional[str]
    """계좌발급시점
    (RFC 3339 date-time)
    """
    refund_status: Optional[PaymentMethodVirtualAccountRefundStatus]
    """가상계좌 결제가 환불 단계일 때의 환불 상태
    """


def _serialize_payment_method_virtual_account(obj: PaymentMethodVirtualAccount) -> Any:
    entity = {}
    entity["type"] = "PaymentMethodVirtualAccount"
    entity["accountNumber"] = obj.account_number
    if obj.bank is not None:
        entity["bank"] = _serialize_bank(obj.bank)
    if obj.account_type is not None:
        entity["accountType"] = _serialize_payment_method_virtual_account_type(obj.account_type)
    if obj.remittee_name is not None:
        entity["remitteeName"] = obj.remittee_name
    if obj.remitter_name is not None:
        entity["remitterName"] = obj.remitter_name
    if obj.expired_at is not None:
        entity["expiredAt"] = obj.expired_at
    if obj.issued_at is not None:
        entity["issuedAt"] = obj.issued_at
    if obj.refund_status is not None:
        entity["refundStatus"] = _serialize_payment_method_virtual_account_refund_status(obj.refund_status)
    return entity


def _deserialize_payment_method_virtual_account(obj: Any) -> PaymentMethodVirtualAccount:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "type" not in obj:
        raise KeyError(f"'type' is not in {obj}")
    type = obj["type"]
    if type != "PaymentMethodVirtualAccount":
        raise ValueError(f"{repr(type)} is not 'PaymentMethodVirtualAccount'")
    if "accountNumber" not in obj:
        raise KeyError(f"'accountNumber' is not in {obj}")
    account_number = obj["accountNumber"]
    if not isinstance(account_number, str):
        raise ValueError(f"{repr(account_number)} is not str")
    if "bank" in obj:
        bank = obj["bank"]
        bank = _deserialize_bank(bank)
    else:
        bank = None
    if "accountType" in obj:
        account_type = obj["accountType"]
        account_type = _deserialize_payment_method_virtual_account_type(account_type)
    else:
        account_type = None
    if "remitteeName" in obj:
        remittee_name = obj["remitteeName"]
        if not isinstance(remittee_name, str):
            raise ValueError(f"{repr(remittee_name)} is not str")
    else:
        remittee_name = None
    if "remitterName" in obj:
        remitter_name = obj["remitterName"]
        if not isinstance(remitter_name, str):
            raise ValueError(f"{repr(remitter_name)} is not str")
    else:
        remitter_name = None
    if "expiredAt" in obj:
        expired_at = obj["expiredAt"]
        if not isinstance(expired_at, str):
            raise ValueError(f"{repr(expired_at)} is not str")
    else:
        expired_at = None
    if "issuedAt" in obj:
        issued_at = obj["issuedAt"]
        if not isinstance(issued_at, str):
            raise ValueError(f"{repr(issued_at)} is not str")
    else:
        issued_at = None
    if "refundStatus" in obj:
        refund_status = obj["refundStatus"]
        refund_status = _deserialize_payment_method_virtual_account_refund_status(refund_status)
    else:
        refund_status = None
    return PaymentMethodVirtualAccount(type, account_number, bank, account_type, remittee_name, remitter_name, expired_at, issued_at, refund_status)
