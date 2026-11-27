from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field
from ...common.currency import Currency, _deserialize_currency, _serialize_currency
from ...payment.promotion.promotion_card_company import PromotionCardCompany, _deserialize_promotion_card_company, _serialize_promotion_card_company
from ...payment.promotion.promotion_discount_policy import PromotionDiscountPolicy, _deserialize_promotion_discount_policy, _serialize_promotion_discount_policy
from ...payment.promotion.promotion_recover_option import PromotionRecoverOption, _deserialize_promotion_recover_option, _serialize_promotion_recover_option
from ...payment.promotion.promotion_status import PromotionStatus, _deserialize_promotion_status, _serialize_promotion_status

@dataclass
class CardPromotion:
    """카드 프로모션
    """
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
    discount_policy: PromotionDiscountPolicy
    """할인 정책
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
    recover_option: PromotionRecoverOption
    """결제 취소 시 프로모션 예산 복구 옵션
    """
    max_discount_amount: Optional[int] = field(default=None)
    """최대 할인 금액
    (int64)
    """
    terminated_at: Optional[str] = field(default=None)
    """프로모션 중단 시각
    (RFC 3339 date-time)
    """


def _serialize_card_promotion(obj: CardPromotion) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["type"] = "CARD"
    entity["id"] = obj.id
    entity["storeId"] = obj.store_id
    entity["name"] = obj.name
    entity["discountPolicy"] = _serialize_promotion_discount_policy(obj.discount_policy)
    entity["totalBudget"] = obj.total_budget
    entity["spentAmount"] = obj.spent_amount
    entity["currency"] = _serialize_currency(obj.currency)
    entity["startAt"] = obj.start_at
    entity["endAt"] = obj.end_at
    entity["cardCompany"] = _serialize_promotion_card_company(obj.card_company)
    entity["status"] = _serialize_promotion_status(obj.status)
    entity["createdAt"] = obj.created_at
    entity["recoverOption"] = _serialize_promotion_recover_option(obj.recover_option)
    if obj.max_discount_amount is not None:
        entity["maxDiscountAmount"] = obj.max_discount_amount
    if obj.terminated_at is not None:
        entity["terminatedAt"] = obj.terminated_at
    return entity


def _deserialize_card_promotion(obj: Any) -> CardPromotion:
    if not isinstance(obj, dict):
        raise ValueError("Expected dict for obj")
    if "type" not in obj:
        raise KeyError("Missing required field 'type'")
    type = obj["type"]
    if type != "CARD":
        raise ValueError("Expected 'CARD' for type")
    if "id" not in obj:
        raise KeyError("Missing required field 'id'")
    id = obj["id"]
    if not isinstance(id, str):
        raise ValueError("Expected str for id")
    if "storeId" not in obj:
        raise KeyError("Missing required field 'storeId'")
    store_id = obj["storeId"]
    if not isinstance(store_id, str):
        raise ValueError("Expected str for store_id")
    if "name" not in obj:
        raise KeyError("Missing required field 'name'")
    name = obj["name"]
    if not isinstance(name, str):
        raise ValueError("Expected str for name")
    if "discountPolicy" not in obj:
        raise KeyError("Missing required field 'discountPolicy'")
    discount_policy = obj["discountPolicy"]
    discount_policy = _deserialize_promotion_discount_policy(discount_policy)
    if "totalBudget" not in obj:
        raise KeyError("Missing required field 'totalBudget'")
    total_budget = obj["totalBudget"]
    if not isinstance(total_budget, int):
        raise ValueError("Expected int for total_budget")
    if "spentAmount" not in obj:
        raise KeyError("Missing required field 'spentAmount'")
    spent_amount = obj["spentAmount"]
    if not isinstance(spent_amount, int):
        raise ValueError("Expected int for spent_amount")
    if "currency" not in obj:
        raise KeyError("Missing required field 'currency'")
    currency = obj["currency"]
    currency = _deserialize_currency(currency)
    if "startAt" not in obj:
        raise KeyError("Missing required field 'startAt'")
    start_at = obj["startAt"]
    if not isinstance(start_at, str):
        raise ValueError("Expected str for start_at")
    if "endAt" not in obj:
        raise KeyError("Missing required field 'endAt'")
    end_at = obj["endAt"]
    if not isinstance(end_at, str):
        raise ValueError("Expected str for end_at")
    if "cardCompany" not in obj:
        raise KeyError("Missing required field 'cardCompany'")
    card_company = obj["cardCompany"]
    card_company = _deserialize_promotion_card_company(card_company)
    if "status" not in obj:
        raise KeyError("Missing required field 'status'")
    status = obj["status"]
    status = _deserialize_promotion_status(status)
    if "createdAt" not in obj:
        raise KeyError("Missing required field 'createdAt'")
    created_at = obj["createdAt"]
    if not isinstance(created_at, str):
        raise ValueError("Expected str for created_at")
    if "recoverOption" not in obj:
        raise KeyError("Missing required field 'recoverOption'")
    recover_option = obj["recoverOption"]
    recover_option = _deserialize_promotion_recover_option(recover_option)
    if "maxDiscountAmount" in obj:
        max_discount_amount = obj["maxDiscountAmount"]
        if not isinstance(max_discount_amount, int):
            raise ValueError("Expected int for max_discount_amount")
    else:
        max_discount_amount = None
    if "terminatedAt" in obj:
        terminated_at = obj["terminatedAt"]
        if not isinstance(terminated_at, str):
            raise ValueError("Expected str for terminated_at")
    else:
        terminated_at = None
    return CardPromotion(id, store_id, name, discount_policy, total_budget, spent_amount, currency, start_at, end_at, card_company, status, created_at, recover_option, max_discount_amount, terminated_at)
