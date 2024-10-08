from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class B2bTaxInvoiceItem:
    """품목
    """
    purchase_date: Optional[str]
    """결제일

    날짜를 나타내는 문자열로, `yyyy-MM-dd` 형식을 따릅니다.
    """
    name: Optional[str]
    """품명

    최대 100자
    """
    spec: Optional[str]
    """규격

    최대 100자
    """
    quantity: Optional[int]
    """수량

    입력 범위 : -99999999.99 ~ 999999999.99, 10^-quantityScale 단위로 치환됨
    (int64)
    """
    quantity_scale: Optional[int]
    """수량 단위

    입력 범위 : 0 ~ 2, 기본값: 0
    (int32)
    """
    unit_cost_amount: Optional[int]
    """단가

    입력 범위 : -99999999999999.99 ~ 999999999999999.99
    (int64)
    """
    unit_cost_amount_scale: Optional[int]
    """단가 단위

    입력 범위 : 0 ~ 2, 기본값: 0
    (int32)
    """
    supply_cost_amount: Optional[int]
    """공급가액
    (int64)
    """
    tax_amount: Optional[int]
    """세액
    (int64)
    """
    remark: Optional[str]
    """비고
    """


def _serialize_b2b_tax_invoice_item(obj: B2bTaxInvoiceItem) -> Any:
    entity = {}
    if obj.purchase_date is not None:
        entity["purchaseDate"] = obj.purchase_date
    if obj.name is not None:
        entity["name"] = obj.name
    if obj.spec is not None:
        entity["spec"] = obj.spec
    if obj.quantity is not None:
        entity["quantity"] = obj.quantity
    if obj.quantity_scale is not None:
        entity["quantityScale"] = obj.quantity_scale
    if obj.unit_cost_amount is not None:
        entity["unitCostAmount"] = obj.unit_cost_amount
    if obj.unit_cost_amount_scale is not None:
        entity["unitCostAmountScale"] = obj.unit_cost_amount_scale
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
        if not isinstance(quantity, int):
            raise ValueError(f"{repr(quantity)} is not int")
    else:
        quantity = None
    if "quantityScale" in obj:
        quantity_scale = obj["quantityScale"]
        if not isinstance(quantity_scale, int):
            raise ValueError(f"{repr(quantity_scale)} is not int")
    else:
        quantity_scale = None
    if "unitCostAmount" in obj:
        unit_cost_amount = obj["unitCostAmount"]
        if not isinstance(unit_cost_amount, int):
            raise ValueError(f"{repr(unit_cost_amount)} is not int")
    else:
        unit_cost_amount = None
    if "unitCostAmountScale" in obj:
        unit_cost_amount_scale = obj["unitCostAmountScale"]
        if not isinstance(unit_cost_amount_scale, int):
            raise ValueError(f"{repr(unit_cost_amount_scale)} is not int")
    else:
        unit_cost_amount_scale = None
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
    return B2bTaxInvoiceItem(purchase_date, name, spec, quantity, quantity_scale, unit_cost_amount, unit_cost_amount_scale, supply_cost_amount, tax_amount, remark)
