from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class PaymentMethodConvenienceStore:
    """편의점 결제 상세 정보
    """
    pass


def _serialize_payment_method_convenience_store(obj: PaymentMethodConvenienceStore) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["type"] = "PaymentMethodConvenienceStore"
    return entity


def _deserialize_payment_method_convenience_store(obj: Any) -> PaymentMethodConvenienceStore:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "type" not in obj:
        raise KeyError(f"'type' is not in {obj}")
    type = obj["type"]
    if type != "PaymentMethodConvenienceStore":
        raise ValueError(f"{repr(type)} is not 'PaymentMethodConvenienceStore'")
    return PaymentMethodConvenienceStore()
