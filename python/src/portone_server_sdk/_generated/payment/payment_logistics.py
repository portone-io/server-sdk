from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field
from portone_server_sdk._generated.payment.payment_logistics_company import PaymentLogisticsCompany, _deserialize_payment_logistics_company, _serialize_payment_logistics_company
from portone_server_sdk._generated.common.separated_address_input import SeparatedAddressInput, _deserialize_separated_address_input, _serialize_separated_address_input

@dataclass
class PaymentLogistics:
    """배송정보
    """
    company: PaymentLogisticsCompany
    """물류회사
    """
    invoice_number: str
    """송장번호
    """
    sent_at: str
    """발송시점
    (RFC 3339 date-time)
    """
    received_at: Optional[str]
    """수령시점
    (RFC 3339 date-time)
    """
    address: Optional[SeparatedAddressInput]
    """주소
    """


def _serialize_payment_logistics(obj: PaymentLogistics) -> Any:
    entity = {}
    entity["company"] = _serialize_payment_logistics_company(obj.company)
    entity["invoiceNumber"] = obj.invoice_number
    entity["sentAt"] = obj.sent_at
    if obj.received_at is not None:
        entity["receivedAt"] = obj.received_at
    if obj.address is not None:
        entity["address"] = _serialize_separated_address_input(obj.address)
    return entity


def _deserialize_payment_logistics(obj: Any) -> PaymentLogistics:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "company" not in obj:
        raise KeyError(f"'company' is not in {obj}")
    company = obj["company"]
    company = _deserialize_payment_logistics_company(company)
    if "invoiceNumber" not in obj:
        raise KeyError(f"'invoiceNumber' is not in {obj}")
    invoice_number = obj["invoiceNumber"]
    if not isinstance(invoice_number, str):
        raise ValueError(f"{repr(invoice_number)} is not str")
    if "sentAt" not in obj:
        raise KeyError(f"'sentAt' is not in {obj}")
    sent_at = obj["sentAt"]
    if not isinstance(sent_at, str):
        raise ValueError(f"{repr(sent_at)} is not str")
    if "receivedAt" in obj:
        received_at = obj["receivedAt"]
        if not isinstance(received_at, str):
            raise ValueError(f"{repr(received_at)} is not str")
    else:
        received_at = None
    if "address" in obj:
        address = obj["address"]
        address = _deserialize_separated_address_input(address)
    else:
        address = None
    return PaymentLogistics(company, invoice_number, sent_at, received_at, address)
