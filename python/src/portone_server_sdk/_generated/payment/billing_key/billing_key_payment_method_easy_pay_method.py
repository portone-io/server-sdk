from __future__ import annotations
from typing import Any, Optional, Union
from ...payment.billing_key.billing_key_payment_method_card import BillingKeyPaymentMethodCard, _deserialize_billing_key_payment_method_card, _serialize_billing_key_payment_method_card
from ...payment.billing_key.billing_key_payment_method_easy_pay_charge import BillingKeyPaymentMethodEasyPayCharge, _deserialize_billing_key_payment_method_easy_pay_charge, _serialize_billing_key_payment_method_easy_pay_charge
from ...payment.billing_key.billing_key_payment_method_transfer import BillingKeyPaymentMethodTransfer, _deserialize_billing_key_payment_method_transfer, _serialize_billing_key_payment_method_transfer

BillingKeyPaymentMethodEasyPayMethod = Union[BillingKeyPaymentMethodCard, BillingKeyPaymentMethodEasyPayCharge, BillingKeyPaymentMethodTransfer, dict]
"""간편 결제 수단
"""


def _serialize_billing_key_payment_method_easy_pay_method(obj: BillingKeyPaymentMethodEasyPayMethod) -> Any:
    if isinstance(obj, dict):
        return obj
    if isinstance(obj, BillingKeyPaymentMethodCard):
        return _serialize_billing_key_payment_method_card(obj)
    if isinstance(obj, BillingKeyPaymentMethodEasyPayCharge):
        return _serialize_billing_key_payment_method_easy_pay_charge(obj)
    if isinstance(obj, BillingKeyPaymentMethodTransfer):
        return _serialize_billing_key_payment_method_transfer(obj)


def _deserialize_billing_key_payment_method_easy_pay_method(obj: Any) -> BillingKeyPaymentMethodEasyPayMethod:
    try:
        return _deserialize_billing_key_payment_method_card(obj)
    except Exception:
        pass
    try:
        return _deserialize_billing_key_payment_method_easy_pay_charge(obj)
    except Exception:
        pass
    try:
        return _deserialize_billing_key_payment_method_transfer(obj)
    except Exception:
        pass
    raise ValueError(f"{repr(obj)} is not BillingKeyPaymentMethodEasyPayMethod")
