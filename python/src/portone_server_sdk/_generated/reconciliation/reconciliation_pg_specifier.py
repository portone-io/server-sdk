from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field
from ..reconciliation.reconciliation_pg_provider import ReconciliationPgProvider, _deserialize_reconciliation_pg_provider, _serialize_reconciliation_pg_provider

@dataclass
class ReconciliationPgSpecifier:
    """대사용 PG사 가맹점 식별자
    """
    pg_merchant_id: str
    """PG사 가맹점 식별 아이디
    """
    pg_provider: ReconciliationPgProvider
    """PG사
    """


def _serialize_reconciliation_pg_specifier(obj: ReconciliationPgSpecifier) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["pgMerchantId"] = obj.pg_merchant_id
    entity["pgProvider"] = _serialize_reconciliation_pg_provider(obj.pg_provider)
    return entity


def _deserialize_reconciliation_pg_specifier(obj: Any) -> ReconciliationPgSpecifier:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "pgMerchantId" not in obj:
        raise KeyError(f"'pgMerchantId' is not in {obj}")
    pg_merchant_id = obj["pgMerchantId"]
    if not isinstance(pg_merchant_id, str):
        raise ValueError(f"{repr(pg_merchant_id)} is not str")
    if "pgProvider" not in obj:
        raise KeyError(f"'pgProvider' is not in {obj}")
    pg_provider = obj["pgProvider"]
    pg_provider = _deserialize_reconciliation_pg_provider(pg_provider)
    return ReconciliationPgSpecifier(pg_merchant_id, pg_provider)
