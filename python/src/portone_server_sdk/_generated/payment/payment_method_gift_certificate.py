from __future__ import annotations
from typing import Any, Literal, Optional
from dataclasses import dataclass, field
from portone_server_sdk._generated.payment.payment_method_gift_certificate_type import PaymentMethodGiftCertificateType, _deserialize_payment_method_gift_certificate_type, _serialize_payment_method_gift_certificate_type

@dataclass
class PaymentMethodGiftCertificate:
    """상품권 상세 정보
    """
    type: Literal["PaymentMethodGiftCertificate"] = field(repr=False)
    approval_number: str
    """상품권 승인 번호
    """
    gift_certificate_type: Optional[PaymentMethodGiftCertificateType]
    """상품권 종류
    """


def _serialize_payment_method_gift_certificate(obj: PaymentMethodGiftCertificate) -> Any:
    entity = {}
    entity["type"] = obj.type
    entity["approvalNumber"] = obj.approval_number
    if obj.gift_certificate_type is not None:
        entity["giftCertificateType"] = _serialize_payment_method_gift_certificate_type(obj.gift_certificate_type)
    return entity


def _deserialize_payment_method_gift_certificate(obj: Any) -> PaymentMethodGiftCertificate:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "type" not in obj:
        raise KeyError(f"'type' is not in {obj}")
    type = obj["type"]
    if type != "PaymentMethodGiftCertificate":
        raise ValueError(f"{repr(type)} is not 'PaymentMethodGiftCertificate'")
    if "approvalNumber" not in obj:
        raise KeyError(f"'approvalNumber' is not in {obj}")
    approval_number = obj["approvalNumber"]
    if not isinstance(approval_number, str):
        raise ValueError(f"{repr(approval_number)} is not str")
    if "giftCertificateType" in obj:
        gift_certificate_type = obj["giftCertificateType"]
        gift_certificate_type = _deserialize_payment_method_gift_certificate_type(gift_certificate_type)
    else:
        gift_certificate_type = None
    return PaymentMethodGiftCertificate(type, approval_number, gift_certificate_type)