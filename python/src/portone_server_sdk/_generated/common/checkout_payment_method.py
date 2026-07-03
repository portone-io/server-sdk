from __future__ import annotations
from typing import Any, Literal, Optional, Union

CheckoutPaymentMethod = Union[Literal["CARD_KR", "N_PAY", "KAKAO_PAY", "TOSS_PAY", "CARD_INTERNATIONAL", "PAY_PAL", "UNION_PAY", "ALIPAY_CN", "ALIPAY_HK", "TRUE_MONEY", "DANA", "TOUCH_N_GO", "G_CASH", "WE_CHAT_PAY", "KLARNA", "E_CONTEXT", "GRAB_PAY_MY", "GRAB_PAY_SG", "SHOPEE_PAY_TH", "PAY_PAY", "BPI", "RABBIT_LINE_PAY", "CONVENIENCE_STORE_JP", "AMAZON_PAY", "RAKUTEN_PAY", "D_BARAI", "AU_PAY", "MERPAY"], str]
"""결제 수단
"""


def _serialize_checkout_payment_method(obj: CheckoutPaymentMethod) -> Any:
    if isinstance(obj, dict):
        return obj
    return obj


def _deserialize_checkout_payment_method(obj: Any) -> CheckoutPaymentMethod:
    return obj
