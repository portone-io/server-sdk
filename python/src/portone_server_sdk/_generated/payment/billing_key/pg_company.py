from __future__ import annotations
from typing import Any, Literal, Optional

PgCompany = Literal["INICIS", "NICE", "KCP", "DANAL", "TOSSPAYMENTS", "MOBILIANS", "KICC", "SMARTRO", "DAOU", "BLUEWALNUT", "PAYPAL", "ALIPAY", "EXIMBAY", "PAYMENTWALL", "SETTLE", "GALAXIA", "NAVERPAY", "KAKAOPAY", "SMILEPAY", "KAKAO", "TOSSPAY", "CHAI", "PAYCO", "PAYPLE", "SYRUP", "KSNET", "WELCOME", "JTNET", "KPN", "HYPHEN"]
"""PG사
"""


def _serialize_pg_company(obj: PgCompany) -> Any:
    return obj


def _deserialize_pg_company(obj: Any) -> PgCompany:
    if obj not in ["INICIS", "NICE", "KCP", "DANAL", "TOSSPAYMENTS", "MOBILIANS", "KICC", "SMARTRO", "DAOU", "BLUEWALNUT", "PAYPAL", "ALIPAY", "EXIMBAY", "PAYMENTWALL", "SETTLE", "GALAXIA", "NAVERPAY", "KAKAOPAY", "SMILEPAY", "KAKAO", "TOSSPAY", "CHAI", "PAYCO", "PAYPLE", "SYRUP", "KSNET", "WELCOME", "JTNET", "KPN", "HYPHEN"]:
        raise ValueError(f"{repr(obj)} is not PgCompany")
    return obj
