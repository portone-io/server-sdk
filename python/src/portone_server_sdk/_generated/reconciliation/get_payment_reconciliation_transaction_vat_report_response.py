from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field
from ..reconciliation.payment_reconciliation_vat_report_item import PaymentReconciliationVatReportItem, _deserialize_payment_reconciliation_vat_report_item, _serialize_payment_reconciliation_vat_report_item
from ..reconciliation.payment_reconciliation_vat_report_summary import PaymentReconciliationVatReportSummary, _deserialize_payment_reconciliation_vat_report_summary, _serialize_payment_reconciliation_vat_report_summary
from ..reconciliation.reconciliation_pg_specifier import ReconciliationPgSpecifier, _deserialize_reconciliation_pg_specifier, _serialize_reconciliation_pg_specifier

@dataclass
class GetPaymentReconciliationTransactionVatReportResponse:
    summary: PaymentReconciliationVatReportSummary
    """부가세 내역 요약
    """
    items: Optional[list[PaymentReconciliationVatReportItem]] = field(default=None)
    """부가세 내역 항목 리스트
    """
    pg_specifiers: Optional[list[ReconciliationPgSpecifier]] = field(default=None)
    """PG사 식별자 리스트
    """


def _serialize_get_payment_reconciliation_transaction_vat_report_response(obj: GetPaymentReconciliationTransactionVatReportResponse) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["summary"] = _serialize_payment_reconciliation_vat_report_summary(obj.summary)
    if obj.items is not None:
        entity["items"] = list(map(_serialize_payment_reconciliation_vat_report_item, obj.items))
    if obj.pg_specifiers is not None:
        entity["pgSpecifiers"] = list(map(_serialize_reconciliation_pg_specifier, obj.pg_specifiers))
    return entity


def _deserialize_get_payment_reconciliation_transaction_vat_report_response(obj: Any) -> GetPaymentReconciliationTransactionVatReportResponse:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "summary" not in obj:
        raise KeyError(f"'summary' is not in {obj}")
    summary = obj["summary"]
    summary = _deserialize_payment_reconciliation_vat_report_summary(summary)
    if "items" in obj:
        items = obj["items"]
        if not isinstance(items, list):
            raise ValueError(f"{repr(items)} is not list")
        for i, item in enumerate(items):
            item = _deserialize_payment_reconciliation_vat_report_item(item)
            items[i] = item
    else:
        items = None
    if "pgSpecifiers" in obj:
        pg_specifiers = obj["pgSpecifiers"]
        if not isinstance(pg_specifiers, list):
            raise ValueError(f"{repr(pg_specifiers)} is not list")
        for i, item in enumerate(pg_specifiers):
            item = _deserialize_reconciliation_pg_specifier(item)
            pg_specifiers[i] = item
    else:
        pg_specifiers = None
    return GetPaymentReconciliationTransactionVatReportResponse(summary, items, pg_specifiers)
