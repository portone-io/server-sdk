from __future__ import annotations
from typing import Any, Literal, Optional
from dataclasses import dataclass, field
from portone_server_sdk._generated.common.currency import Currency, _deserialize_currency, _serialize_currency
from portone_server_sdk._generated.payment.promotion.promotion_card_company import PromotionCardCompany, _deserialize_promotion_card_company, _serialize_promotion_card_company
from portone_server_sdk._generated.payment.promotion.promotion_discount import PromotionDiscount, _deserialize_promotion_discount, _serialize_promotion_discount
from portone_server_sdk._generated.payment.promotion.promotion_status import PromotionStatus, _deserialize_promotion_status, _serialize_promotion_status

@dataclass
class CardPromotion:
    """카드 프로모션
    """
    type: Literal["CARD"] = field(repr=False)
    """프로모션 유형
    """
    id: str
    """프로모션 아이디
    """
    store_id: str
    """상점 아이디
    """
    name: str
    """프로모션 이름
    """
    discount_type: PromotionDiscount
    """할인 유형
    """
    total_budget: int
    """총 예산
    (int64)
    """
    spent_amount: int
    """소진 금액
    (int64)
    """
    currency: Currency
    """금액 화폐
    """
    start_at: str
    """프로모션 시작 시각
    (RFC 3339 date-time)
    """
    end_at: str
    """프로모션 종료 시각
    (RFC 3339 date-time)
    """
    card_company: PromotionCardCompany
    """프로모션 카드사
    """
    status: PromotionStatus
    """프로모션 상태
    """
    created_at: str
    """프로모션 생성 시각
    (RFC 3339 date-time)
    """
    min_payment_amount: Optional[int]
    """최소 결제 금액
    (int64)
    """
    max_discount_amount: Optional[int]
    """최대 할인 금액
    (int64)
    """
    terminated_at: Optional[str]
    """프로모션 중단 시각
    (RFC 3339 date-time)
    """


def _serialize_card_promotion(obj: CardPromotion) -> Any:
    entity = {}
    entity["type"] = "CARD"
    entity["id"] = obj.id
    entity["storeId"] = obj.store_id
    entity["name"] = obj.name
    entity["discountType"] = _serialize_promotion_discount(obj.discount_type)
    entity["totalBudget"] = obj.total_budget
    entity["spentAmount"] = obj.spent_amount
    entity["currency"] = _serialize_currency(obj.currency)
    entity["startAt"] = obj.start_at
    entity["endAt"] = obj.end_at
    entity["cardCompany"] = _serialize_promotion_card_company(obj.card_company)
    entity["status"] = _serialize_promotion_status(obj.status)
    entity["createdAt"] = obj.created_at
    if obj.min_payment_amount is not None:
        entity["minPaymentAmount"] = obj.min_payment_amount
    if obj.max_discount_amount is not None:
        entity["maxDiscountAmount"] = obj.max_discount_amount
    if obj.terminated_at is not None:
        entity["terminatedAt"] = obj.terminated_at
    return entity


def _deserialize_card_promotion(obj: Any) -> CardPromotion:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "type" not in obj:
        raise KeyError(f"'type' is not in {obj}")
    type = obj["type"]
    if type != "CARD":
        raise ValueError(f"{repr(type)} is not 'CARD'")
    if "id" not in obj:
        raise KeyError(f"'id' is not in {obj}")
    id = obj["id"]
    if not isinstance(id, str):
        raise ValueError(f"{repr(id)} is not str")
    if "storeId" not in obj:
        raise KeyError(f"'storeId' is not in {obj}")
    store_id = obj["storeId"]
    if not isinstance(store_id, str):
        raise ValueError(f"{repr(store_id)} is not str")
    if "name" not in obj:
        raise KeyError(f"'name' is not in {obj}")
    name = obj["name"]
    if not isinstance(name, str):
        raise ValueError(f"{repr(name)} is not str")
    if "discountType" not in obj:
        raise KeyError(f"'discountType' is not in {obj}")
    discount_type = obj["discountType"]
    discount_type = _deserialize_promotion_discount(discount_type)
    if "totalBudget" not in obj:
        raise KeyError(f"'totalBudget' is not in {obj}")
    total_budget = obj["totalBudget"]
    if not isinstance(total_budget, int):
        raise ValueError(f"{repr(total_budget)} is not int")
    if "spentAmount" not in obj:
        raise KeyError(f"'spentAmount' is not in {obj}")
    spent_amount = obj["spentAmount"]
    if not isinstance(spent_amount, int):
        raise ValueError(f"{repr(spent_amount)} is not int")
    if "currency" not in obj:
        raise KeyError(f"'currency' is not in {obj}")
    currency = obj["currency"]
    currency = _deserialize_currency(currency)
    if "startAt" not in obj:
        raise KeyError(f"'startAt' is not in {obj}")
    start_at = obj["startAt"]
    if not isinstance(start_at, str):
        raise ValueError(f"{repr(start_at)} is not str")
    if "endAt" not in obj:
        raise KeyError(f"'endAt' is not in {obj}")
    end_at = obj["endAt"]
    if not isinstance(end_at, str):
        raise ValueError(f"{repr(end_at)} is not str")
    if "cardCompany" not in obj:
        raise KeyError(f"'cardCompany' is not in {obj}")
    card_company = obj["cardCompany"]
    card_company = _deserialize_promotion_card_company(card_company)
    if "status" not in obj:
        raise KeyError(f"'status' is not in {obj}")
    status = obj["status"]
    status = _deserialize_promotion_status(status)
    if "createdAt" not in obj:
        raise KeyError(f"'createdAt' is not in {obj}")
    created_at = obj["createdAt"]
    if not isinstance(created_at, str):
        raise ValueError(f"{repr(created_at)} is not str")
    if "minPaymentAmount" in obj:
        min_payment_amount = obj["minPaymentAmount"]
        if not isinstance(min_payment_amount, int):
            raise ValueError(f"{repr(min_payment_amount)} is not int")
    else:
        min_payment_amount = None
    if "maxDiscountAmount" in obj:
        max_discount_amount = obj["maxDiscountAmount"]
        if not isinstance(max_discount_amount, int):
            raise ValueError(f"{repr(max_discount_amount)} is not int")
    else:
        max_discount_amount = None
    if "terminatedAt" in obj:
        terminated_at = obj["terminatedAt"]
        if not isinstance(terminated_at, str):
            raise ValueError(f"{repr(terminated_at)} is not str")
    else:
        terminated_at = None
    return CardPromotion(type, id, store_id, name, discount_type, total_budget, spent_amount, currency, start_at, end_at, card_company, status, created_at, min_payment_amount, max_discount_amount, terminated_at)
