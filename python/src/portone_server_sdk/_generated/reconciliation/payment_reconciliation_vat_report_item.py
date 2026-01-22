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
        raise ValueError(f"{repr(obj)} is not dict")
    if "paymentMethod" not in obj:
        raise KeyError(f"'paymentMethod' is not in {obj}")
    payment_method = obj["paymentMethod"]
    payment_method = _deserialize_simplified_payment_method_type(payment_method)
    if "supplyAmount" not in obj:
        raise KeyError(f"'supplyAmount' is not in {obj}")
    supply_amount = obj["supplyAmount"]
    if not isinstance(supply_amount, int):
        raise ValueError(f"{repr(supply_amount)} is not int")
    if "vatAmount" not in obj:
        raise KeyError(f"'vatAmount' is not in {obj}")
    vat_amount = obj["vatAmount"]
    if not isinstance(vat_amount, int):
        raise ValueError(f"{repr(vat_amount)} is not int")
    if "taxFreeAmount" not in obj:
        raise KeyError(f"'taxFreeAmount' is not in {obj}")
    tax_free_amount = obj["taxFreeAmount"]
    if not isinstance(tax_free_amount, int):
        raise ValueError(f"{repr(tax_free_amount)} is not int")
    if "totalAmount" not in obj:
        raise KeyError(f"'totalAmount' is not in {obj}")
    total_amount = obj["totalAmount"]
    if not isinstance(total_amount, int):
        raise ValueError(f"{repr(total_amount)} is not int")
    return PaymentReconciliationVatReportItem(payment_method, supply_amount, vat_amount, tax_free_amount, total_amount)
