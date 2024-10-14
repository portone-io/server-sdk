from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field
from portone_server_sdk._generated.payment.billing_key.billing_key_text_search_field import BillingKeyTextSearchField, _deserialize_billing_key_text_search_field, _serialize_billing_key_text_search_field

@dataclass
class BillingKeyTextSearch:
    """통합검색 입력 정보
    """
    field: BillingKeyTextSearchField
    value: str


def _serialize_billing_key_text_search(obj: BillingKeyTextSearch) -> Any:
    entity = {}
    entity["field"] = _serialize_billing_key_text_search_field(obj.field)
    entity["value"] = obj.value
    return entity


def _deserialize_billing_key_text_search(obj: Any) -> BillingKeyTextSearch:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "field" not in obj:
        raise KeyError(f"'field' is not in {obj}")
    field = obj["field"]
    field = _deserialize_billing_key_text_search_field(field)
    if "value" not in obj:
        raise KeyError(f"'value' is not in {obj}")
    value = obj["value"]
    if not isinstance(value, str):
        raise ValueError(f"{repr(value)} is not str")
    return BillingKeyTextSearch(field, value)
