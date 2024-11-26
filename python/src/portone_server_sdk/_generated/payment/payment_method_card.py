from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field
from ..common.card import Card, _deserialize_card, _serialize_card
from ..payment.payment_installment import PaymentInstallment, _deserialize_payment_installment, _serialize_payment_installment

@dataclass
class PaymentMethodCard:
    """결제수단 카드 정보
    """
    card: Optional[Card] = field(default=None)
    """카드 상세 정보
    """
    approval_number: Optional[str] = field(default=None)
    """승인 번호
    """
    installment: Optional[PaymentInstallment] = field(default=None)
    """할부 정보
    """
    point_used: Optional[bool] = field(default=None)
    """카드 포인트 사용여부
    """


def _serialize_payment_method_card(obj: PaymentMethodCard) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["type"] = "PaymentMethodCard"
    if obj.card is not None:
        entity["card"] = _serialize_card(obj.card)
    if obj.approval_number is not None:
        entity["approvalNumber"] = obj.approval_number
    if obj.installment is not None:
        entity["installment"] = _serialize_payment_installment(obj.installment)
    if obj.point_used is not None:
        entity["pointUsed"] = obj.point_used
    return entity


def _deserialize_payment_method_card(obj: Any) -> PaymentMethodCard:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "type" not in obj:
        raise KeyError(f"'type' is not in {obj}")
    type = obj["type"]
    if type != "PaymentMethodCard":
        raise ValueError(f"{repr(type)} is not 'PaymentMethodCard'")
    if "card" in obj:
        card = obj["card"]
        card = _deserialize_card(card)
    else:
        card = None
    if "approvalNumber" in obj:
        approval_number = obj["approvalNumber"]
        if not isinstance(approval_number, str):
            raise ValueError(f"{repr(approval_number)} is not str")
    else:
        approval_number = None
    if "installment" in obj:
        installment = obj["installment"]
        installment = _deserialize_payment_installment(installment)
    else:
        installment = None
    if "pointUsed" in obj:
        point_used = obj["pointUsed"]
        if not isinstance(point_used, bool):
            raise ValueError(f"{repr(point_used)} is not bool")
    else:
        point_used = None
    return PaymentMethodCard(card, approval_number, installment, point_used)
