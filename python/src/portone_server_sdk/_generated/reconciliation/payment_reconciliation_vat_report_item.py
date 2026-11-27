from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field
from ..reconciliation.simplified_payment_method_type import SimplifiedPaymentMethodType, _deserialize_simplified_payment_method_type, _serialize_simplified_payment_method_type

@dataclass
class PaymentReconciliationVatReportItem:
    payment_method: SimplifiedPaymentMethodType
    """결제수단
    """
    supply_amount: int
    """공급가액
    (int64)
    """
    vat_amount: int
    """부가세 금액
    (int64)
    """
    tax_free_amount: int
    """면세 금액
    (int64)
    """
    total_amount: int
    """총 금액
    (int64)
    """


def _serialize_payment_reconciliation_vat_report_item(obj: PaymentReconciliationVatReportItem) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["paymentMethod"] = _serialize_simplified_payment_method_type(obj.payment_method)
    entity["supplyAmount"] = obj.supply_amount
    entity["vatAmount"] = obj.vat_amount
    entity["taxFreeAmount"] = obj.tax_free_amount
    entity["totalAmount"] = obj.total_amount
    return entity


def _deserialize_payment_reconciliation_vat_report_item(obj: Any) -> PaymentReconciliationVatReportItem:
    if not isinstance(obj, dict):
        raise ValueError("Expected dict for obj")
    if "paymentMethod" not in obj:
        raise KeyError("Missing required field 'paymentMethod'")
    payment_method = obj["paymentMethod"]
    payment_method = _deserialize_simplified_payment_method_type(payment_method)
    if "supplyAmount" not in obj:
        raise KeyError("Missing required field 'supplyAmount'")
    supply_amount = obj["supplyAmount"]
    if not isinstance(supply_amount, int):
        raise ValueError("Expected int for supply_amount")
    if "vatAmount" not in obj:
        raise KeyError("Missing required field 'vatAmount'")
    vat_amount = obj["vatAmount"]
    if not isinstance(vat_amount, int):
        raise ValueError("Expected int for vat_amount")
    if "taxFreeAmount" not in obj:
        raise KeyError("Missing required field 'taxFreeAmount'")
    tax_free_amount = obj["taxFreeAmount"]
    if not isinstance(tax_free_amount, int):
        raise ValueError("Expected int for tax_free_amount")
    if "totalAmount" not in obj:
        raise KeyError("Missing required field 'totalAmount'")
    total_amount = obj["totalAmount"]
    if not isinstance(total_amount, int):
        raise ValueError("Expected int for total_amount")
    return PaymentReconciliationVatReportItem(payment_method, supply_amount, vat_amount, tax_free_amount, total_amount)
