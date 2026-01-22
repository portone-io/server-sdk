from __future__ import annotations
from typing import Any, Literal, Optional, Union

ReconciliationPgProvider = Union[Literal["KAKAOPAY", "NICEPAY", "NAVERPAY", "UPLUS", "TOSSPAYMENTS", "TOSSPAY", "PAYCO", "KCP", "DANAL", "EXIMBAY", "INICIS", "HECTO", "KSNET", "KPN", "HYPHEN", "PAYPAL", "HECTO_EASY", "MOBILIANS", "PAYLETTER_GLOBAL"], str]


def _serialize_reconciliation_pg_provider(obj: ReconciliationPgProvider) -> Any:
    if isinstance(obj, dict):
        return obj
    return obj


def _deserialize_reconciliation_pg_provider(obj: Any) -> ReconciliationPgProvider:
    return obj
