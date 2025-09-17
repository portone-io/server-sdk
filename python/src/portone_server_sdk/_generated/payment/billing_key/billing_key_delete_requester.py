from __future__ import annotations
from typing import Any, Literal, Optional, Union

BillingKeyDeleteRequester = Union[Literal["CUSTOMER", "ADMIN"], str]
"""빌링키 삭제 요청 주체
"""


def _serialize_billing_key_delete_requester(obj: BillingKeyDeleteRequester) -> Any:
    if isinstance(obj, dict):
        return obj
    return obj


def _deserialize_billing_key_delete_requester(obj: Any) -> BillingKeyDeleteRequester:
    return obj
