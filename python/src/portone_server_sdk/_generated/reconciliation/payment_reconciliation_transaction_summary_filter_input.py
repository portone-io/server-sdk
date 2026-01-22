from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field
from ..reconciliation.payment_reconciliation_status import PaymentReconciliationStatus, _deserialize_payment_reconciliation_status, _serialize_payment_reconciliation_status
from ..reconciliation.reconciliation_pg_specifier import ReconciliationPgSpecifier, _deserialize_reconciliation_pg_specifier, _serialize_reconciliation_pg_specifier

@dataclass
class PaymentReconciliationTransactionSummaryFilterInput:
    """거래대사 거래내역 필터
    """
    reconciliation_statuses: Optional[list[PaymentReconciliationStatus]] = field(default=None)
    """대사 상태 필터
    """
    pg_specifiers: Optional[list[ReconciliationPgSpecifier]] = field(default=None)
    """대사용 PG사 가맹점 식별자 필터
    """
    store_ids: Optional[list[str]] = field(default=None)
    """하위 상점 아이디 필터
    """


def _serialize_payment_reconciliation_transaction_summary_filter_input(obj: PaymentReconciliationTransactionSummaryFilterInput) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    if obj.reconciliation_statuses is not None:
        entity["reconciliationStatuses"] = list(map(_serialize_payment_reconciliation_status, obj.reconciliation_statuses))
    if obj.pg_specifiers is not None:
        entity["pgSpecifiers"] = list(map(_serialize_reconciliation_pg_specifier, obj.pg_specifiers))
    if obj.store_ids is not None:
        entity["storeIds"] = obj.store_ids
    return entity


def _deserialize_payment_reconciliation_transaction_summary_filter_input(obj: Any) -> PaymentReconciliationTransactionSummaryFilterInput:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "reconciliationStatuses" in obj:
        reconciliation_statuses = obj["reconciliationStatuses"]
        if not isinstance(reconciliation_statuses, list):
            raise ValueError(f"{repr(reconciliation_statuses)} is not list")
        for i, item in enumerate(reconciliation_statuses):
            item = _deserialize_payment_reconciliation_status(item)
            reconciliation_statuses[i] = item
    else:
        reconciliation_statuses = None
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
    return PaymentReconciliationTransactionSummaryFilterInput(reconciliation_statuses, pg_specifiers, store_ids)
