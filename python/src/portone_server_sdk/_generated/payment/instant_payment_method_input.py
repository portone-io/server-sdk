from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field
from portone_server_sdk._generated.payment.instant_payment_method_input_card import InstantPaymentMethodInputCard, _deserialize_instant_payment_method_input_card, _serialize_instant_payment_method_input_card
from portone_server_sdk._generated.payment.instant_payment_method_input_virtual_account import InstantPaymentMethodInputVirtualAccount, _deserialize_instant_payment_method_input_virtual_account, _serialize_instant_payment_method_input_virtual_account

@dataclass
class InstantPaymentMethodInput:
    """수기 결제 수단 입력 정보

    하나의 필드만 입력합니다.
    """
    card: Optional[InstantPaymentMethodInputCard]
    """카드
    """
    virtual_account: Optional[InstantPaymentMethodInputVirtualAccount]
    """가상계좌
    """


def _serialize_instant_payment_method_input(obj: InstantPaymentMethodInput) -> Any:
    entity = {}
    if obj.card is not None:
        entity["card"] = _serialize_instant_payment_method_input_card(obj.card)
    if obj.virtual_account is not None:
        entity["virtualAccount"] = _serialize_instant_payment_method_input_virtual_account(obj.virtual_account)
    return entity


def _deserialize_instant_payment_method_input(obj: Any) -> InstantPaymentMethodInput:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "card" in obj:
        card = obj["card"]
        card = _deserialize_instant_payment_method_input_card(card)
    else:
        card = None
    if "virtualAccount" in obj:
        virtual_account = obj["virtualAccount"]
        virtual_account = _deserialize_instant_payment_method_input_virtual_account(virtual_account)
    else:
        virtual_account = None
    return InstantPaymentMethodInput(card, virtual_account)
