from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class PaymentReconciliationVatReportSummary:
    total_supply_amount: int
    """총 공급가액
    (int64)
    """
    total_vat_amount: int
    """총 부가세 금액
    (int64)
    """
    total_tax_free_amount: int
    """총 면세 금액
    (int64)
    """
    total_amount: int
    """총 금액
    (int64)
    """


def _serialize_payment_reconciliation_vat_report_summary(obj: PaymentReconciliationVatReportSummary) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["totalSupplyAmount"] = obj.total_supply_amount
    entity["totalVatAmount"] = obj.total_vat_amount
    entity["totalTaxFreeAmount"] = obj.total_tax_free_amount
    entity["totalAmount"] = obj.total_amount
    return entity


def _deserialize_payment_reconciliation_vat_report_summary(obj: Any) -> PaymentReconciliationVatReportSummary:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "totalSupplyAmount" not in obj:
        raise KeyError(f"'totalSupplyAmount' is not in {obj}")
    total_supply_amount = obj["totalSupplyAmount"]
    if not isinstance(total_supply_amount, int):
        raise ValueError(f"{repr(total_supply_amount)} is not int")
    if "totalVatAmount" not in obj:
        raise KeyError(f"'totalVatAmount' is not in {obj}")
    total_vat_amount = obj["totalVatAmount"]
    if not isinstance(total_vat_amount, int):
        raise ValueError(f"{repr(total_vat_amount)} is not int")
    if "totalTaxFreeAmount" not in obj:
        raise KeyError(f"'totalTaxFreeAmount' is not in {obj}")
    total_tax_free_amount = obj["totalTaxFreeAmount"]
    if not isinstance(total_tax_free_amount, int):
        raise ValueError(f"{repr(total_tax_free_amount)} is not int")
    if "totalAmount" not in obj:
        raise KeyError(f"'totalAmount' is not in {obj}")
    total_amount = obj["totalAmount"]
    if not isinstance(total_amount, int):
        raise ValueError(f"{repr(total_amount)} is not int")
    return PaymentReconciliationVatReportSummary(total_supply_amount, total_vat_amount, total_tax_free_amount, total_amount)
