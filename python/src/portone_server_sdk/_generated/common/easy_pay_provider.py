from __future__ import annotations
from typing import Any, Literal, Optional, Union

EasyPayProvider = Union[Literal["SAMSUNGPAY", "KAKAOPAY", "NAVERPAY", "PAYCO", "SSGPAY", "CHAI", "LPAY", "KPAY", "TOSSPAY", "LGPAY", "PINPAY", "APPLEPAY", "SKPAY", "TOSS_BRANDPAY", "KB_APP", "ALIPAY", "HYPHEN", "TMONEY", "PAYPAL", "SMILEPAY", "MIR", "WECHAT", "LINEPAY", "KLARNA", "GRABPAY", "SHOPEEPAY", "JKOPAY", "PAYPAY"], str]
"""간편 결제사
"""


def _serialize_easy_pay_provider(obj: EasyPayProvider) -> Any:
    if isinstance(obj, dict):
        return obj
    return obj


def _deserialize_easy_pay_provider(obj: Any) -> EasyPayProvider:
    return obj
