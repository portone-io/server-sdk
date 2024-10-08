from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field
from portone_server_sdk._generated.payment.payment_text_search_field import PaymentTextSearchField, _deserialize_payment_text_search_field, _serialize_payment_text_search_field

@dataclass
class PaymentTextSearch:
    """통합검색 입력 정보
    """
    field: PaymentTextSearchField
    value: str


def _serialize_payment_text_search(obj: PaymentTextSearch) -> Any:
    entity = {}
    entity["field"] = _serialize_payment_text_search_field(obj.field)
    entity["value"] = obj.value
    return entity


def _deserialize_payment_text_search(obj: Any) -> PaymentTextSearch:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "field" not in obj:
        raise KeyError(f"'field' is not in {obj}")
    field = obj["field"]
    field = _deserialize_payment_text_search_field(field)
    if "value" not in obj:
        raise KeyError(f"'value' is not in {obj}")
    value = obj["value"]
    if not isinstance(value, str):
        raise ValueError(f"{repr(value)} is not str")
    return PaymentTextSearch(field, value)
