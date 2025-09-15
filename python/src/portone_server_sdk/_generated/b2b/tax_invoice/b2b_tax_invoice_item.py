from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field
from ...b2b.tax_invoice.decimal import Decimal, _deserialize_decimal, _serialize_decimal

@dataclass
class B2bTaxInvoiceItem:
    """품목
    """
    purchase_date: Optional[str] = field(default=None)
    """결제일

    날짜를 나타내는 문자열로, `yyyy-MM-dd` 형식을 따릅니다.
    (yyyy-MM-dd)
    """
    name: Optional[str] = field(default=None)
    """품명

    최대 100자
    """
    spec: Optional[str] = field(default=None)
    """규격

    최대 100자
    """
    quantity: Optional[Decimal] = field(default=None)
    """수량

    입력 범위 : -99999999.99 ~ 999999999.99
    `quantity.scale`의 입력 범위 : 0 ~ 2
    `quantity.value` * 10^-`quantity.scale` 단위로 치환됩니다.
    """
    unit_cost_amount: Optional[Decimal] = field(default=None)
    """단가

    입력 범위 : -99999999999999.99 ~ 999999999999999.99
    `unitCostAmount.scale`의 입력 범위 : 0 ~ 2
    `unitCostAmount.value` * 10^-`unitCostAmount.scale` 단위로 치환됩니다.
    """
    supply_cost_amount: Optional[int] = field(default=None)
    """공급가액
    (int64)
    """
    tax_amount: Optional[int] = field(default=None)
    """세액
    (int64)
    """
    remark: Optional[str] = field(default=None)
    """비고
    """


def _serialize_b2b_tax_invoice_item(obj: B2bTaxInvoiceItem) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    if obj.purchase_date is not None:
        entity["purchaseDate"] = obj.purchase_date
    if obj.name is not None:
        entity["name"] = obj.name
    if obj.spec is not None:
        entity["spec"] = obj.spec
    if obj.quantity is not None:
        entity["quantity"] = _serialize_decimal(obj.quantity)
    if obj.unit_cost_amount is not None:
        entity["unitCostAmount"] = _serialize_decimal(obj.unit_cost_amount)
    if obj.supply_cost_amount is not None:
        entity["supplyCostAmount"] = obj.supply_cost_amount
    if obj.tax_amount is not None:
        entity["taxAmount"] = obj.tax_amount
    if obj.remark is not None:
        entity["remark"] = obj.remark
    return entity


def _deserialize_b2b_tax_invoice_item(obj: Any) -> B2bTaxInvoiceItem:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "purchaseDate" in obj:
        purchase_date = obj["purchaseDate"]
        if not isinstance(purchase_date, str):
            raise ValueError(f"{repr(purchase_date)} is not str")
    else:
        purchase_date = None
    if "name" in obj:
        name = obj["name"]
        if not isinstance(name, str):
            raise ValueError(f"{repr(name)} is not str")
    else:
        name = None
    if "spec" in obj:
        spec = obj["spec"]
        if not isinstance(spec, str):
            raise ValueError(f"{repr(spec)} is not str")
    else:
        spec = None
    if "quantity" in obj:
        quantity = obj["quantity"]
        quantity = _deserialize_decimal(quantity)
    else:
        quantity = None
    if "unitCostAmount" in obj:
        unit_cost_amount = obj["unitCostAmount"]
        unit_cost_amount = _deserialize_decimal(unit_cost_amount)
    else:
        unit_cost_amount = None
    if "supplyCostAmount" in obj:
        supply_cost_amount = obj["supplyCostAmount"]
        if not isinstance(supply_cost_amount, int):
            raise ValueError(f"{repr(supply_cost_amount)} is not int")
    else:
        supply_cost_amount = None
    if "taxAmount" in obj:
        tax_amount = obj["taxAmount"]
        if not isinstance(tax_amount, int):
            raise ValueError(f"{repr(tax_amount)} is not int")
    else:
        tax_amount = None
    if "remark" in obj:
        remark = obj["remark"]
        if not isinstance(remark, str):
            raise ValueError(f"{repr(remark)} is not str")
    else:
        remark = None
    return B2bTaxInvoiceItem(purchase_date, name, spec, quantity, unit_cost_amount, supply_cost_amount, tax_amount, remark)
