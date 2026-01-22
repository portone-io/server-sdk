from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field
from ..reconciliation.reconciliation_pg_specifier import ReconciliationPgSpecifier, _deserialize_reconciliation_pg_specifier, _serialize_reconciliation_pg_specifier

@dataclass
class PaymentReconciliationSettlementSummaryFilterInput:
    """거래대사 정산 요약 내역 필터
    """
    pg_specifiers: Optional[list[ReconciliationPgSpecifier]] = field(default=None)
    """PG사 가맹점 식별자 필터
    """
    store_ids: Optional[list[str]] = field(default=None)
    """하위 상점 아이디 필터
    """


def _serialize_payment_reconciliation_settlement_summary_filter_input(obj: PaymentReconciliationSettlementSummaryFilterInput) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    if obj.pg_specifiers is not None:
        entity["pgSpecifiers"] = list(map(_serialize_reconciliation_pg_specifier, obj.pg_specifiers))
    if obj.store_ids is not None:
        entity["storeIds"] = obj.store_ids
    return entity


def _deserialize_payment_reconciliation_settlement_summary_filter_input(obj: Any) -> PaymentReconciliationSettlementSummaryFilterInput:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "pgSpecifiers" in obj:
        pg_specifiers = obj["pgSpecifiers"]
        if not isinstance(pg_specifiers, list):
            raise ValueError(f"{repr(pg_specifiers)} is not list")
        for i, item in enumerate(pg_specifiers):
            item = _deserialize_reconciliation_pg_specifier(item)
            pg_specifiers[i] = item
    else:
        pg_specifiers = None
    if "storeIds" in obj:
        store_ids = obj["storeIds"]
        if not isinstance(store_ids, list):
            raise ValueError(f"{repr(store_ids)} is not list")
        for i, item in enumerate(store_ids):
            if not isinstance(item, str):
                raise ValueError(f"{repr(item)} is not str")
    else:
        store_ids = None
    return PaymentReconciliationSettlementSummaryFilterInput(pg_specifiers, store_ids)
