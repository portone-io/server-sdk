from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field
from ..common.date_range import DateRange, _deserialize_date_range, _serialize_date_range
from ..reconciliation.payment_reconciliation_transaction_summary_filter_input import PaymentReconciliationTransactionSummaryFilterInput, _deserialize_payment_reconciliation_transaction_summary_filter_input, _serialize_payment_reconciliation_transaction_summary_filter_input

@dataclass
class GetPaymentReconciliationTransactionVatReportBody:
    date_range: DateRange
    """거래일 범위
    """
    filter: Optional[PaymentReconciliationTransactionSummaryFilterInput] = field(default=None)


def _serialize_get_payment_reconciliation_transaction_vat_report_body(obj: GetPaymentReconciliationTransactionVatReportBody) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["dateRange"] = _serialize_date_range(obj.date_range)
    if obj.filter is not None:
        entity["filter"] = _serialize_payment_reconciliation_transaction_summary_filter_input(obj.filter)
    return entity


def _deserialize_get_payment_reconciliation_transaction_vat_report_body(obj: Any) -> GetPaymentReconciliationTransactionVatReportBody:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "dateRange" not in obj:
        raise KeyError(f"'dateRange' is not in {obj}")
    date_range = obj["dateRange"]
    date_range = _deserialize_date_range(date_range)
    if "filter" in obj:
        filter = obj["filter"]
        filter = _deserialize_payment_reconciliation_transaction_summary_filter_input(filter)
    else:
        filter = None
    return GetPaymentReconciliationTransactionVatReportBody(date_range, filter)
