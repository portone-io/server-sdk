from __future__ import annotations
from typing import Any, Literal, Optional, Union

PgCompany = Union[Literal["INICIS", "NICE", "KCP", "DANAL", "TOSSPAYMENTS", "MOBILIANS", "KICC", "SMARTRO", "DAOU", "BLUEWALNUT", "PAYPAL", "ALIPAY", "EXIMBAY", "PAYMENTWALL", "SETTLE", "GALAXIA", "NAVERPAY", "KAKAOPAY", "SMILEPAY", "KAKAO", "TOSSPAY", "CHAI", "PAYCO", "PAYPLE", "SYRUP", "KSNET", "WELCOME", "JTNET", "KPN", "HYPHEN"], str]
"""PG사
"""


def _serialize_pg_company(obj: PgCompany) -> Any:
    if isinstance(obj, dict):
        return obj
    return obj


def _deserialize_pg_company(obj: Any) -> PgCompany:
    return obj
