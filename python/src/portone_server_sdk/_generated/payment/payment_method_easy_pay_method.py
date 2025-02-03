from __future__ import annotations
from typing import Any, Optional, Union
from ..payment.payment_method_card import PaymentMethodCard, _deserialize_payment_method_card, _serialize_payment_method_card
from ..payment.payment_method_easy_pay_method_charge import PaymentMethodEasyPayMethodCharge, _deserialize_payment_method_easy_pay_method_charge, _serialize_payment_method_easy_pay_method_charge
from ..payment.payment_method_transfer import PaymentMethodTransfer, _deserialize_payment_method_transfer, _serialize_payment_method_transfer

PaymentMethodEasyPayMethod = Union[PaymentMethodCard, PaymentMethodEasyPayMethodCharge, PaymentMethodTransfer, dict]
"""간편 결제 수단
"""


def _serialize_payment_method_easy_pay_method(obj: PaymentMethodEasyPayMethod) -> Any:
    if isinstance(obj, dict):
        return obj
    if isinstance(obj, PaymentMethodCard):
        return _serialize_payment_method_card(obj)
    if isinstance(obj, PaymentMethodEasyPayMethodCharge):
        return _serialize_payment_method_easy_pay_method_charge(obj)
    if isinstance(obj, PaymentMethodTransfer):
        return _serialize_payment_method_transfer(obj)


def _deserialize_payment_method_easy_pay_method(obj: Any) -> PaymentMethodEasyPayMethod:
    try:
        return _deserialize_payment_method_card(obj)
    except Exception:
        pass
    try:
        return _deserialize_payment_method_easy_pay_method_charge(obj)
    except Exception:
        pass
    try:
        return _deserialize_payment_method_transfer(obj)
    except Exception:
        pass
    raise ValueError(f"{repr(obj)} is not PaymentMethodEasyPayMethod")
