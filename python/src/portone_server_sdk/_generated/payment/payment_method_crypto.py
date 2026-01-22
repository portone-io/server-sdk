from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class PaymentMethodCrypto:
    """암호화폐 결제 상세 정보
    """
    pass


def _serialize_payment_method_crypto(obj: PaymentMethodCrypto) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["type"] = "PaymentMethodCrypto"
    return entity


def _deserialize_payment_method_crypto(obj: Any) -> PaymentMethodCrypto:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "type" not in obj:
        raise KeyError(f"'type' is not in {obj}")
    type = obj["type"]
    if type != "PaymentMethodCrypto":
        raise ValueError(f"{repr(type)} is not 'PaymentMethodCrypto'")
    return PaymentMethodCrypto()
