from __future__ import annotations
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
    tag: Optional[str]
    """태그
    """


def _serialize_platform_order_transfer_product(obj: PlatformOrderTransferProduct) -> Any:
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
        raise ValueError(f"{repr(obj)} is not dict")
    if "id" not in obj:
        raise KeyError(f"'id' is not in {obj}")
    id = obj["id"]
    if not isinstance(id, str):
        raise ValueError(f"{repr(id)} is not str")
    if "name" not in obj:
        raise KeyError(f"'name' is not in {obj}")
    name = obj["name"]
    if not isinstance(name, str):
        raise ValueError(f"{repr(name)} is not str")
    if "amount" not in obj:
        raise KeyError(f"'amount' is not in {obj}")
    amount = obj["amount"]
    if not isinstance(amount, int):
        raise ValueError(f"{repr(amount)} is not int")
    if "taxFreeAmount" not in obj:
        raise KeyError(f"'taxFreeAmount' is not in {obj}")
    tax_free_amount = obj["taxFreeAmount"]
    if not isinstance(tax_free_amount, int):
        raise ValueError(f"{repr(tax_free_amount)} is not int")
    if "tag" in obj:
        tag = obj["tag"]
        if not isinstance(tag, str):
            raise ValueError(f"{repr(tag)} is not str")
    else:
        tag = None
    return PlatformOrderTransferProduct(id, name, amount, tax_free_amount, tag)
