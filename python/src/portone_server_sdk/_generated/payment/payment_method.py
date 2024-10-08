from __future__ import annotations
from typing import Any, Optional, Union
from portone_server_sdk._generated.payment.payment_method_card import PaymentMethodCard, _deserialize_payment_method_card, _serialize_payment_method_card
from portone_server_sdk._generated.payment.payment_method_easy_pay import PaymentMethodEasyPay, _deserialize_payment_method_easy_pay, _serialize_payment_method_easy_pay
from portone_server_sdk._generated.payment.payment_method_gift_certificate import PaymentMethodGiftCertificate, _deserialize_payment_method_gift_certificate, _serialize_payment_method_gift_certificate
from portone_server_sdk._generated.payment.payment_method_mobile import PaymentMethodMobile, _deserialize_payment_method_mobile, _serialize_payment_method_mobile
from portone_server_sdk._generated.payment.payment_method_transfer import PaymentMethodTransfer, _deserialize_payment_method_transfer, _serialize_payment_method_transfer
from portone_server_sdk._generated.payment.payment_method_virtual_account import PaymentMethodVirtualAccount, _deserialize_payment_method_virtual_account, _serialize_payment_method_virtual_account

PaymentMethod = Union[PaymentMethodCard, PaymentMethodEasyPay, PaymentMethodGiftCertificate, PaymentMethodMobile, PaymentMethodTransfer, PaymentMethodVirtualAccount]
"""결제수단 정보
"""


def _serialize_payment_method(obj: PaymentMethod) -> Any:
    if obj.type == "PaymentMethodCard":
        return _serialize_payment_method_card(obj)
    if obj.type == "PaymentMethodEasyPay":
        return _serialize_payment_method_easy_pay(obj)
    if obj.type == "PaymentMethodGiftCertificate":
        return _serialize_payment_method_gift_certificate(obj)
    if obj.type == "PaymentMethodMobile":
        return _serialize_payment_method_mobile(obj)
    if obj.type == "PaymentMethodTransfer":
        return _serialize_payment_method_transfer(obj)
    if obj.type == "PaymentMethodVirtualAccount":
        return _serialize_payment_method_virtual_account(obj)


def _deserialize_payment_method(obj: Any) -> PaymentMethod:
    try:
        return _deserialize_payment_method_card(obj)
    except Exception:
        pass
    try:
        return _deserialize_payment_method_easy_pay(obj)
    except Exception:
        pass
    try:
        return _deserialize_payment_method_gift_certificate(obj)
    except Exception:
        pass
    try:
        return _deserialize_payment_method_mobile(obj)
    except Exception:
        pass
    try:
        return _deserialize_payment_method_transfer(obj)
    except Exception:
        pass
    try:
        return _deserialize_payment_method_virtual_account(obj)
    except Exception:
        pass
    raise ValueError(f"{repr(obj)} is not PaymentMethod")
