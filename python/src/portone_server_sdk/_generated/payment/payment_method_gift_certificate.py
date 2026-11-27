from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field
from ..payment.payment_method_gift_certificate_type import PaymentMethodGiftCertificateType, _deserialize_payment_method_gift_certificate_type, _serialize_payment_method_gift_certificate_type

@dataclass
class PaymentMethodGiftCertificate:
    """상품권 상세 정보
    """
    approval_number: str
    """상품권 승인 번호
    """
    gift_certificate_type: Optional[PaymentMethodGiftCertificateType] = field(default=None)
    """상품권 종류
    """


def _serialize_payment_method_gift_certificate(obj: PaymentMethodGiftCertificate) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["type"] = "PaymentMethodGiftCertificate"
    entity["approvalNumber"] = obj.approval_number
    if obj.gift_certificate_type is not None:
        entity["giftCertificateType"] = _serialize_payment_method_gift_certificate_type(obj.gift_certificate_type)
    return entity


def _deserialize_payment_method_gift_certificate(obj: Any) -> PaymentMethodGiftCertificate:
    if not isinstance(obj, dict):
        raise ValueError("Expected dict for obj")
    if "type" not in obj:
        raise KeyError("Missing required field 'type'")
    type = obj["type"]
    if type != "PaymentMethodGiftCertificate":
        raise ValueError("Expected 'PaymentMethodGiftCertificate' for type")
    if "approvalNumber" not in obj:
        raise KeyError("Missing required field 'approvalNumber'")
    approval_number = obj["approvalNumber"]
    if not isinstance(approval_number, str):
        raise ValueError("Expected str for approval_number")
    if "giftCertificateType" in obj:
        gift_certificate_type = obj["giftCertificateType"]
        gift_certificate_type = _deserialize_payment_method_gift_certificate_type(gift_certificate_type)
    else:
        gift_certificate_type = None
    return PaymentMethodGiftCertificate(approval_number, gift_certificate_type)
