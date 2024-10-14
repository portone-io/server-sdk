from __future__ import annotations
from typing import Any, Literal, Optional

EasyPayProvider = Literal["SAMSUNGPAY", "KAKAOPAY", "NAVERPAY", "PAYCO", "SSGPAY", "CHAI", "LPAY", "KPAY", "TOSSPAY", "LGPAY", "PINPAY", "APPLEPAY", "SKPAY", "TOSS_BRANDPAY", "KB_APP", "ALIPAY", "HYPHEN", "TMONEY"]
"""간편 결제사
"""


def _serialize_easy_pay_provider(obj: EasyPayProvider) -> Any:
    return obj


def _deserialize_easy_pay_provider(obj: Any) -> EasyPayProvider:
    if obj not in ["SAMSUNGPAY", "KAKAOPAY", "NAVERPAY", "PAYCO", "SSGPAY", "CHAI", "LPAY", "KPAY", "TOSSPAY", "LGPAY", "PINPAY", "APPLEPAY", "SKPAY", "TOSS_BRANDPAY", "KB_APP", "ALIPAY", "HYPHEN", "TMONEY"]:
        raise ValueError(f"{repr(obj)} is not EasyPayProvider")
    return obj
