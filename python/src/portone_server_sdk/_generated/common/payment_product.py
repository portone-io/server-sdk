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
    link: Optional[str] = field(default=None)
    """판매 링크
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
    if obj.link is not None:
        entity["link"] = obj.link
    return entity


def _deserialize_payment_product(obj: Any) -> PaymentProduct:
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
    if "quantity" not in obj:
        raise KeyError("Missing required field 'quantity'")
    quantity = obj["quantity"]
    if not isinstance(quantity, int):
        raise ValueError("Expected int for quantity")
    if "tag" in obj:
        tag = obj["tag"]
        if not isinstance(tag, str):
            raise ValueError("Expected str for tag")
    else:
        tag = None
    if "code" in obj:
        code = obj["code"]
        if not isinstance(code, str):
            raise ValueError("Expected str for code")
    else:
        code = None
    if "link" in obj:
        link = obj["link"]
        if not isinstance(link, str):
            raise ValueError("Expected str for link")
    else:
        link = None
    return PaymentProduct(id, name, amount, quantity, tag, code, link)
