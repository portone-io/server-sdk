from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field
from ..payment.payment_text_search_field import PaymentTextSearchField, _deserialize_payment_text_search_field, _serialize_payment_text_search_field

@dataclass
class PaymentTextSearch:
    """통합검색 입력 정보
    """
    field: PaymentTextSearchField
    value: str


def _serialize_payment_text_search(obj: PaymentTextSearch) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["field"] = _serialize_payment_text_search_field(obj.field)
    entity["value"] = obj.value
    return entity


def _deserialize_payment_text_search(obj: Any) -> PaymentTextSearch:
    if not isinstance(obj, dict):
        raise ValueError("Expected dict for obj")
    if "field" not in obj:
        raise KeyError("Missing required field 'field'")
    field = obj["field"]
    field = _deserialize_payment_text_search_field(field)
    if "value" not in obj:
        raise KeyError("Missing required field 'value'")
    value = obj["value"]
    if not isinstance(value, str):
        raise ValueError("Expected str for value")
    return PaymentTextSearch(field, value)
