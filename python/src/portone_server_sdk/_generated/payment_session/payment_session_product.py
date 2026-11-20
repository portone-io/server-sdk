from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class PaymentSessionProduct:
    """결제 세션 주문 항목
    """
    name: str
    """상품 이름
    """
    unit_price: int
    """상품 단가
    (int64)
    """
    quantity: int
    """상품 수량
    (int32)
    """
    id: Optional[str] = field(default=None)
    """항목 아이디
    """
    code: Optional[str] = field(default=None)
    """상품 코드
    """
    start_date: Optional[str] = field(default=None)
    """제공 시작일

    구독 등 제공 기간이 있는 상품의 경우 입력하세요.
    (yyyy-MM-dd)
    """
    end_date: Optional[str] = field(default=None)
    """제공 종료일

    구독 등 제공 기간이 있는 상품의 경우 입력하세요.
    (yyyy-MM-dd)
    """
    url: Optional[str] = field(default=None)
    """판매 링크
    """
    n_pay_category_type: Optional[str] = field(default=None)
    """네이버페이 카테고리 타입
    """
    n_pay_category_id: Optional[str] = field(default=None)
    """네이버페이 카테고리 아이디
    """
    n_pay_uid: Optional[str] = field(default=None)
    """네이버페이 상품 식별자
    """


def _serialize_payment_session_product(obj: PaymentSessionProduct) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["name"] = obj.name
    entity["unitPrice"] = obj.unit_price
    entity["quantity"] = obj.quantity
    if obj.id is not None:
        entity["id"] = obj.id
    if obj.code is not None:
        entity["code"] = obj.code
    if obj.start_date is not None:
        entity["startDate"] = obj.start_date
    if obj.end_date is not None:
        entity["endDate"] = obj.end_date
    if obj.url is not None:
        entity["url"] = obj.url
    if obj.n_pay_category_type is not None:
        entity["nPayCategoryType"] = obj.n_pay_category_type
    if obj.n_pay_category_id is not None:
        entity["nPayCategoryId"] = obj.n_pay_category_id
    if obj.n_pay_uid is not None:
        entity["nPayUid"] = obj.n_pay_uid
    return entity


def _deserialize_payment_session_product(obj: Any) -> PaymentSessionProduct:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "name" not in obj:
        raise KeyError(f"'name' is not in {obj}")
    name = obj["name"]
    if not isinstance(name, str):
        raise ValueError(f"{repr(name)} is not str")
    if "unitPrice" not in obj:
        raise KeyError(f"'unitPrice' is not in {obj}")
    unit_price = obj["unitPrice"]
    if not isinstance(unit_price, int):
        raise ValueError(f"{repr(unit_price)} is not int")
    if "quantity" not in obj:
        raise KeyError(f"'quantity' is not in {obj}")
    quantity = obj["quantity"]
    if not isinstance(quantity, int):
        raise ValueError(f"{repr(quantity)} is not int")
    if "id" in obj:
        id = obj["id"]
        if not isinstance(id, str):
            raise ValueError(f"{repr(id)} is not str")
    else:
        id = None
    if "code" in obj:
        code = obj["code"]
        if not isinstance(code, str):
            raise ValueError(f"{repr(code)} is not str")
    else:
        code = None
    if "startDate" in obj:
        start_date = obj["startDate"]
        if not isinstance(start_date, str):
            raise ValueError(f"{repr(start_date)} is not str")
    else:
        start_date = None
    if "endDate" in obj:
        end_date = obj["endDate"]
        if not isinstance(end_date, str):
            raise ValueError(f"{repr(end_date)} is not str")
    else:
        end_date = None
    if "url" in obj:
        url = obj["url"]
        if not isinstance(url, str):
            raise ValueError(f"{repr(url)} is not str")
    else:
        url = None
    if "nPayCategoryType" in obj:
        n_pay_category_type = obj["nPayCategoryType"]
        if not isinstance(n_pay_category_type, str):
            raise ValueError(f"{repr(n_pay_category_type)} is not str")
    else:
        n_pay_category_type = None
    if "nPayCategoryId" in obj:
        n_pay_category_id = obj["nPayCategoryId"]
        if not isinstance(n_pay_category_id, str):
            raise ValueError(f"{repr(n_pay_category_id)} is not str")
    else:
        n_pay_category_id = None
    if "nPayUid" in obj:
        n_pay_uid = obj["nPayUid"]
        if not isinstance(n_pay_uid, str):
            raise ValueError(f"{repr(n_pay_uid)} is not str")
    else:
        n_pay_uid = None
    return PaymentSessionProduct(name, unit_price, quantity, id, code, start_date, end_date, url, n_pay_category_type, n_pay_category_id, n_pay_uid)
