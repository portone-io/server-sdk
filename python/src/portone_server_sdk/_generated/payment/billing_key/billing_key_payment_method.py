from __future__ import annotations
from typing import Any, Optional, Union
from ...payment.billing_key.billing_key_payment_method_card import BillingKeyPaymentMethodCard, _deserialize_billing_key_payment_method_card, _serialize_billing_key_payment_method_card
from ...payment.billing_key.billing_key_payment_method_easy_pay import BillingKeyPaymentMethodEasyPay, _deserialize_billing_key_payment_method_easy_pay, _serialize_billing_key_payment_method_easy_pay
from ...payment.billing_key.billing_key_payment_method_mobile import BillingKeyPaymentMethodMobile, _deserialize_billing_key_payment_method_mobile, _serialize_billing_key_payment_method_mobile
from ...payment.billing_key.billing_key_payment_method_paypal import BillingKeyPaymentMethodPaypal, _deserialize_billing_key_payment_method_paypal, _serialize_billing_key_payment_method_paypal
from ...payment.billing_key.billing_key_payment_method_transfer import BillingKeyPaymentMethodTransfer, _deserialize_billing_key_payment_method_transfer, _serialize_billing_key_payment_method_transfer

BillingKeyPaymentMethod = Union[BillingKeyPaymentMethodCard, BillingKeyPaymentMethodEasyPay, BillingKeyPaymentMethodMobile, BillingKeyPaymentMethodPaypal, BillingKeyPaymentMethodTransfer, dict]
"""빌링키 발급 수단 정보
"""


def _serialize_billing_key_payment_method(obj: BillingKeyPaymentMethod) -> Any:
    if isinstance(obj, dict):
        return obj
    if isinstance(obj, BillingKeyPaymentMethodCard):
        return _serialize_billing_key_payment_method_card(obj)
    if isinstance(obj, BillingKeyPaymentMethodEasyPay):
        return _serialize_billing_key_payment_method_easy_pay(obj)
    if isinstance(obj, BillingKeyPaymentMethodMobile):
        return _serialize_billing_key_payment_method_mobile(obj)
    if isinstance(obj, BillingKeyPaymentMethodPaypal):
        return _serialize_billing_key_payment_method_paypal(obj)
    if isinstance(obj, BillingKeyPaymentMethodTransfer):
        return _serialize_billing_key_payment_method_transfer(obj)


def _deserialize_billing_key_payment_method(obj: Any) -> BillingKeyPaymentMethod:
    try:
        return _deserialize_billing_key_payment_method_card(obj)
    except Exception:
        pass
    try:
        return _deserialize_billing_key_payment_method_easy_pay(obj)
    except Exception:
        pass
    try:
        return _deserialize_billing_key_payment_method_mobile(obj)
    except Exception:
        pass
    try:
        return _deserialize_billing_key_payment_method_paypal(obj)
    except Exception:
        pass
    try:
        return _deserialize_billing_key_payment_method_transfer(obj)
    except Exception:
        pass
    raise ValueError(f"{repr(obj)} is not BillingKeyPaymentMethod")
