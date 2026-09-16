from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class PaymentSessionAgreement:
    """결제 세션 약관
    """
    name: str
    """약관 이름
    """
    url: str
    """약관 URL
    """


def _serialize_payment_session_agreement(obj: PaymentSessionAgreement) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["name"] = obj.name
    entity["url"] = obj.url
    return entity


def _deserialize_payment_session_agreement(obj: Any) -> PaymentSessionAgreement:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "name" not in obj:
        raise KeyError(f"'name' is not in {obj}")
    name = obj["name"]
    if not isinstance(name, str):
        raise ValueError(f"{repr(name)} is not str")
    if "url" not in obj:
        raise KeyError(f"'url' is not in {obj}")
    url = obj["url"]
    if not isinstance(url, str):
        raise ValueError(f"{repr(url)} is not str")
    return PaymentSessionAgreement(name, url)
