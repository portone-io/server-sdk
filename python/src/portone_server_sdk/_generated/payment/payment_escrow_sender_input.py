from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field
from ..common.separated_address_input import SeparatedAddressInput, _deserialize_separated_address_input, _serialize_separated_address_input

@dataclass
class PaymentEscrowSenderInput:
    """에스크로 발송자 정보
    """
    name: Optional[str] = field(default=None)
    """이름
    """
    phone_number: Optional[str] = field(default=None)
    """전화번호
    """
    zipcode: Optional[str] = field(default=None)
    """우편번호
    """
    relationship: Optional[str] = field(default=None)
    """수취인과의 관계
    """
    address: Optional[SeparatedAddressInput] = field(default=None)
    """주소
    """


def _serialize_payment_escrow_sender_input(obj: PaymentEscrowSenderInput) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    if obj.name is not None:
        entity["name"] = obj.name
    if obj.phone_number is not None:
        entity["phoneNumber"] = obj.phone_number
    if obj.zipcode is not None:
        entity["zipcode"] = obj.zipcode
    if obj.relationship is not None:
        entity["relationship"] = obj.relationship
    if obj.address is not None:
        entity["address"] = _serialize_separated_address_input(obj.address)
    return entity


def _deserialize_payment_escrow_sender_input(obj: Any) -> PaymentEscrowSenderInput:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "name" in obj:
        name = obj["name"]
        if not isinstance(name, str):
            raise ValueError(f"{repr(name)} is not str")
    else:
        name = None
    if "phoneNumber" in obj:
        phone_number = obj["phoneNumber"]
        if not isinstance(phone_number, str):
            raise ValueError(f"{repr(phone_number)} is not str")
    else:
        phone_number = None
    if "zipcode" in obj:
        zipcode = obj["zipcode"]
        if not isinstance(zipcode, str):
            raise ValueError(f"{repr(zipcode)} is not str")
    else:
        zipcode = None
    if "relationship" in obj:
        relationship = obj["relationship"]
        if not isinstance(relationship, str):
            raise ValueError(f"{repr(relationship)} is not str")
    else:
        relationship = None
    if "address" in obj:
        address = obj["address"]
        address = _deserialize_separated_address_input(address)
    else:
        address = None
    return PaymentEscrowSenderInput(name, phone_number, zipcode, relationship, address)
