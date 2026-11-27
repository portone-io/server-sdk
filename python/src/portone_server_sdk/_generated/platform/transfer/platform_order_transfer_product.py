from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class PlatformOrderTransferProduct:
    """상품
    """
    id: str
    """상품 아이디
    """
    name: str
    """상품 이름
    """
    amount: int
    """상품 금액
    (int64)
    """
    tax_free_amount: int
    """상품 면세 금액
    (int64)
    """
    tag: Optional[str] = field(default=None)
    """태그
    """


def _serialize_platform_order_transfer_product(obj: PlatformOrderTransferProduct) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["id"] = obj.id
    entity["name"] = obj.name
    entity["amount"] = obj.amount
    entity["taxFreeAmount"] = obj.tax_free_amount
    if obj.tag is not None:
        entity["tag"] = obj.tag
    return entity


def _deserialize_platform_order_transfer_product(obj: Any) -> PlatformOrderTransferProduct:
    if not isinstance(obj, dict):
        raise ValueError("Expected dict for obj")
    if "id" not in obj:
        raise KeyError("Missing required field 'id'")
    id = obj["id"]
    if not isinstance(id, str):
        raise ValueError("Expected str for id")
    if "name" not in obj:
        raise KeyError("Missing required field 'name'")
    name = obj["name"]
    if not isinstance(name, str):
        raise ValueError("Expected str for name")
    if "amount" not in obj:
        raise KeyError("Missing required field 'amount'")
    amount = obj["amount"]
    if not isinstance(amount, int):
        raise ValueError("Expected int for amount")
    if "taxFreeAmount" not in obj:
        raise KeyError("Missing required field 'taxFreeAmount'")
    tax_free_amount = obj["taxFreeAmount"]
    if not isinstance(tax_free_amount, int):
        raise ValueError("Expected int for tax_free_amount")
    if "tag" in obj:
        tag = obj["tag"]
        if not isinstance(tag, str):
            raise ValueError("Expected str for tag")
    else:
        tag = None
    return PlatformOrderTransferProduct(id, name, amount, tax_free_amount, tag)
