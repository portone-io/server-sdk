from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field
from portone_server_sdk._generated.common.separated_address_input import SeparatedAddressInput, _deserialize_separated_address_input, _serialize_separated_address_input

@dataclass
class PaymentEscrowReceiverInput:
    """에스크로 수취인 정보
    """
    name: Optional[str]
    """이름
    """
    phone_number: Optional[str]
    """전화번호
    """
    zipcode: Optional[str]
    """우편번호
    """
    address: Optional[SeparatedAddressInput]
    """주소
    """


def _serialize_payment_escrow_receiver_input(obj: PaymentEscrowReceiverInput) -> Any:
    entity = {}
    if obj.name is not None:
        entity["name"] = obj.name
    if obj.phone_number is not None:
        entity["phoneNumber"] = obj.phone_number
    if obj.zipcode is not None:
        entity["zipcode"] = obj.zipcode
    if obj.address is not None:
        entity["address"] = _serialize_separated_address_input(obj.address)
    return entity


def _deserialize_payment_escrow_receiver_input(obj: Any) -> PaymentEscrowReceiverInput:
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
    if "address" in obj:
        address = obj["address"]
        address = _deserialize_separated_address_input(address)
    else:
        address = None
    return PaymentEscrowReceiverInput(name, phone_number, zipcode, address)
