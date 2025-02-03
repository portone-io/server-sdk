from __future__ import annotations
from typing import Any, Optional, Union
from ...platform.transfer.platform_payment_method_card import PlatformPaymentMethodCard, _deserialize_platform_payment_method_card, _serialize_platform_payment_method_card
from ...platform.transfer.platform_payment_method_easy_pay import PlatformPaymentMethodEasyPay, _deserialize_platform_payment_method_easy_pay, _serialize_platform_payment_method_easy_pay
from ...platform.transfer.platform_payment_method_gift_certificate import PlatformPaymentMethodGiftCertificate, _deserialize_platform_payment_method_gift_certificate, _serialize_platform_payment_method_gift_certificate
from ...platform.transfer.platform_payment_method_mobile import PlatformPaymentMethodMobile, _deserialize_platform_payment_method_mobile, _serialize_platform_payment_method_mobile
from ...platform.transfer.platform_payment_method_transfer import PlatformPaymentMethodTransfer, _deserialize_platform_payment_method_transfer, _serialize_platform_payment_method_transfer
from ...platform.transfer.platform_payment_method_virtual_account import PlatformPaymentMethodVirtualAccount, _deserialize_platform_payment_method_virtual_account, _serialize_platform_payment_method_virtual_account

PlatformPaymentMethod = Union[PlatformPaymentMethodCard, PlatformPaymentMethodEasyPay, PlatformPaymentMethodGiftCertificate, PlatformPaymentMethodMobile, PlatformPaymentMethodTransfer, PlatformPaymentMethodVirtualAccount, dict]
"""결제 수단
"""


def _serialize_platform_payment_method(obj: PlatformPaymentMethod) -> Any:
    if isinstance(obj, dict):
        return obj
    if isinstance(obj, PlatformPaymentMethodCard):
        return _serialize_platform_payment_method_card(obj)
    if isinstance(obj, PlatformPaymentMethodEasyPay):
        return _serialize_platform_payment_method_easy_pay(obj)
    if isinstance(obj, PlatformPaymentMethodGiftCertificate):
        return _serialize_platform_payment_method_gift_certificate(obj)
    if isinstance(obj, PlatformPaymentMethodMobile):
        return _serialize_platform_payment_method_mobile(obj)
    if isinstance(obj, PlatformPaymentMethodTransfer):
        return _serialize_platform_payment_method_transfer(obj)
    if isinstance(obj, PlatformPaymentMethodVirtualAccount):
        return _serialize_platform_payment_method_virtual_account(obj)


def _deserialize_platform_payment_method(obj: Any) -> PlatformPaymentMethod:
    try:
        return _deserialize_platform_payment_method_card(obj)
    except Exception:
        pass
    try:
        return _deserialize_platform_payment_method_easy_pay(obj)
    except Exception:
        pass
    try:
        return _deserialize_platform_payment_method_gift_certificate(obj)
    except Exception:
        pass
    try:
        return _deserialize_platform_payment_method_mobile(obj)
    except Exception:
        pass
    try:
        return _deserialize_platform_payment_method_transfer(obj)
    except Exception:
        pass
    try:
        return _deserialize_platform_payment_method_virtual_account(obj)
    except Exception:
        pass
    raise ValueError(f"{repr(obj)} is not PlatformPaymentMethod")
