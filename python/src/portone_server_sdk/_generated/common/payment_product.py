from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class PaymentProduct:
    """상품 정보
    """
    id: str
    """상품 고유 식별자

    고객사가 직접 부여한 식별자입니다.
    """
    name: str
    """상품명
    """
    amount: int
    """상품 단위가격
    (int64)
    """
    quantity: int
    """주문 수량
    (int32)
    """
    tag: Optional[str] = field(default=None)
    """상품 태그

    카테고리 등으로 활용될 수 있습니다.
    """
    code: Optional[str] = field(default=None)
    """상품 코드
    """


def _serialize_payment_product(obj: PaymentProduct) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["id"] = obj.id
    entity["name"] = obj.name
    entity["amount"] = obj.amount
    entity["quantity"] = obj.quantity
    if obj.tag is not None:
        entity["tag"] = obj.tag
    if obj.code is not None:
        entity["code"] = obj.code
    return entity


def _deserialize_payment_product(obj: Any) -> PaymentProduct:
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
    if "quantity" not in obj:
        raise KeyError(f"'quantity' is not in {obj}")
    quantity = obj["quantity"]
    if not isinstance(quantity, int):
        raise ValueError(f"{repr(quantity)} is not int")
    if "tag" in obj:
        tag = obj["tag"]
        if not isinstance(tag, str):
            raise ValueError(f"{repr(tag)} is not str")
    else:
        tag = None
    if "code" in obj:
        code = obj["code"]
        if not isinstance(code, str):
            raise ValueError(f"{repr(code)} is not str")
    else:
        code = None
    return PaymentProduct(id, name, amount, quantity, tag, code)
