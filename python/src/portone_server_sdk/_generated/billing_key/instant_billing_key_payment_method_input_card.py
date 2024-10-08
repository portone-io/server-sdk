from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field
from portone_server_sdk._generated.common.card_credential import CardCredential, _deserialize_card_credential, _serialize_card_credential

@dataclass
class InstantBillingKeyPaymentMethodInputCard:
    """카드 수단 정보 입력 양식
    """
    credential: CardCredential


def _serialize_instant_billing_key_payment_method_input_card(obj: InstantBillingKeyPaymentMethodInputCard) -> Any:
    entity = {}
    entity["credential"] = _serialize_card_credential(obj.credential)
    return entity


def _deserialize_instant_billing_key_payment_method_input_card(obj: Any) -> InstantBillingKeyPaymentMethodInputCard:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "credential" not in obj:
        raise KeyError(f"'credential' is not in {obj}")
    credential = obj["credential"]
    credential = _deserialize_card_credential(credential)
    return InstantBillingKeyPaymentMethodInputCard(credential)
