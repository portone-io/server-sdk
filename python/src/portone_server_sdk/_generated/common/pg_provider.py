from __future__ import annotations
from typing import Any, Literal, Optional

PgProvider = Literal["HTML5_INICIS", "PAYPAL", "PAYPAL_V2", "INICIS", "DANAL", "NICE", "DANAL_TPAY", "JTNET", "UPLUS", "NAVERPAY", "KAKAO", "SETTLE", "KCP", "MOBILIANS", "KAKAOPAY", "NAVERCO", "SYRUP", "KICC", "EXIMBAY", "SMILEPAY", "PAYCO", "KCP_BILLING", "ALIPAY", "PAYPLE", "CHAI", "BLUEWALNUT", "SMARTRO", "SMARTRO_V2", "PAYMENTWALL", "TOSSPAYMENTS", "KCP_QUICK", "DAOU", "GALAXIA", "TOSSPAY", "KCP_DIRECT", "SETTLE_ACC", "SETTLE_FIRM", "INICIS_UNIFIED", "KSNET", "PINPAY", "NICE_V2", "TOSS_BRANDPAY", "WELCOME", "TOSSPAY_V2", "INICIS_V2", "KPN", "KCP_V2", "HYPHEN"]
"""PG사 결제 모듈
"""


def _serialize_pg_provider(obj: PgProvider) -> Any:
    return obj


def _deserialize_pg_provider(obj: Any) -> PgProvider:
    if obj not in ["HTML5_INICIS", "PAYPAL", "PAYPAL_V2", "INICIS", "DANAL", "NICE", "DANAL_TPAY", "JTNET", "UPLUS", "NAVERPAY", "KAKAO", "SETTLE", "KCP", "MOBILIANS", "KAKAOPAY", "NAVERCO", "SYRUP", "KICC", "EXIMBAY", "SMILEPAY", "PAYCO", "KCP_BILLING", "ALIPAY", "PAYPLE", "CHAI", "BLUEWALNUT", "SMARTRO", "SMARTRO_V2", "PAYMENTWALL", "TOSSPAYMENTS", "KCP_QUICK", "DAOU", "GALAXIA", "TOSSPAY", "KCP_DIRECT", "SETTLE_ACC", "SETTLE_FIRM", "INICIS_UNIFIED", "KSNET", "PINPAY", "NICE_V2", "TOSS_BRANDPAY", "WELCOME", "TOSSPAY_V2", "INICIS_V2", "KPN", "KCP_V2", "HYPHEN"]:
        raise ValueError(f"{repr(obj)} is not PgProvider")
    return obj
