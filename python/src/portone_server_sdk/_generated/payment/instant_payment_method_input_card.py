from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field
from ..common.card_credential import CardCredential, _deserialize_card_credential, _serialize_card_credential

@dataclass
class InstantPaymentMethodInputCard:
    """카드 수단 정보 입력 정보
    """
    credential: CardCredential
    """카드 인증 관련 정보
    """
    installment_month: Optional[int] = field(default=None)
    """카드 할부 개월 수
    (int32)
    """
    use_free_installment_plan: Optional[bool] = field(default=None)
    """무이자 할부 적용 여부
    """
    use_free_interest_from_merchant: Optional[bool] = field(default=None)
    """무이자 할부 이자를 고객사가 부담할지 여부
    """
    use_card_point: Optional[bool] = field(default=None)
    """카드 포인트 사용 여부
    """


def _serialize_instant_payment_method_input_card(obj: InstantPaymentMethodInputCard) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["credential"] = _serialize_card_credential(obj.credential)
    if obj.installment_month is not None:
        entity["installmentMonth"] = obj.installment_month
    if obj.use_free_installment_plan is not None:
        entity["useFreeInstallmentPlan"] = obj.use_free_installment_plan
    if obj.use_free_interest_from_merchant is not None:
        entity["useFreeInterestFromMerchant"] = obj.use_free_interest_from_merchant
    if obj.use_card_point is not None:
        entity["useCardPoint"] = obj.use_card_point
    return entity


def _deserialize_instant_payment_method_input_card(obj: Any) -> InstantPaymentMethodInputCard:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "credential" not in obj:
        raise KeyError(f"'credential' is not in {obj}")
    credential = obj["credential"]
    credential = _deserialize_card_credential(credential)
    if "installmentMonth" in obj:
        installment_month = obj["installmentMonth"]
        if not isinstance(installment_month, int):
            raise ValueError(f"{repr(installment_month)} is not int")
    else:
        installment_month = None
    if "useFreeInstallmentPlan" in obj:
        use_free_installment_plan = obj["useFreeInstallmentPlan"]
        if not isinstance(use_free_installment_plan, bool):
            raise ValueError(f"{repr(use_free_installment_plan)} is not bool")
    else:
        use_free_installment_plan = None
    if "useFreeInterestFromMerchant" in obj:
        use_free_interest_from_merchant = obj["useFreeInterestFromMerchant"]
        if not isinstance(use_free_interest_from_merchant, bool):
            raise ValueError(f"{repr(use_free_interest_from_merchant)} is not bool")
    else:
        use_free_interest_from_merchant = None
    if "useCardPoint" in obj:
        use_card_point = obj["useCardPoint"]
        if not isinstance(use_card_point, bool):
            raise ValueError(f"{repr(use_card_point)} is not bool")
    else:
        use_card_point = None
    return InstantPaymentMethodInputCard(credential, installment_month, use_free_installment_plan, use_free_interest_from_merchant, use_card_point)
