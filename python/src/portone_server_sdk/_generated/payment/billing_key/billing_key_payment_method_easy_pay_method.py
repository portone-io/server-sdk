from __future__ import annotations
from typing import Any, Optional, Union
from portone_server_sdk._generated.payment.billing_key.billing_key_payment_method_card import BillingKeyPaymentMethodCard, _deserialize_billing_key_payment_method_card, _serialize_billing_key_payment_method_card
from portone_server_sdk._generated.payment.billing_key.billing_key_payment_method_easy_pay_charge import BillingKeyPaymentMethodEasyPayCharge, _deserialize_billing_key_payment_method_easy_pay_charge, _serialize_billing_key_payment_method_easy_pay_charge
from portone_server_sdk._generated.payment.billing_key.billing_key_payment_method_transfer import BillingKeyPaymentMethodTransfer, _deserialize_billing_key_payment_method_transfer, _serialize_billing_key_payment_method_transfer

BillingKeyPaymentMethodEasyPayMethod = Union[BillingKeyPaymentMethodCard, BillingKeyPaymentMethodEasyPayCharge, BillingKeyPaymentMethodTransfer]
"""간편 결제 수단
"""


def _serialize_billing_key_payment_method_easy_pay_method(obj: BillingKeyPaymentMethodEasyPayMethod) -> Any:
    if obj.type == "BillingKeyPaymentMethodCard":
        return _serialize_billing_key_payment_method_card(obj)
    if obj.type == "BillingKeyPaymentMethodEasyPayCharge":
        return _serialize_billing_key_payment_method_easy_pay_charge(obj)
    if obj.type == "BillingKeyPaymentMethodTransfer":
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
