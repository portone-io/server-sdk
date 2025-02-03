from __future__ import annotations
from typing import Any, Optional, Union
from ...payment.billing_key.deleted_billing_key_info import DeletedBillingKeyInfo, _deserialize_deleted_billing_key_info, _serialize_deleted_billing_key_info
from ...payment.billing_key.issued_billing_key_info import IssuedBillingKeyInfo, _deserialize_issued_billing_key_info, _serialize_issued_billing_key_info

BillingKeyInfo = Union[DeletedBillingKeyInfo, IssuedBillingKeyInfo, dict]
"""빌링키 정보
"""


def _serialize_billing_key_info(obj: BillingKeyInfo) -> Any:
    if isinstance(obj, dict):
        return obj
    if isinstance(obj, DeletedBillingKeyInfo):
        return _serialize_deleted_billing_key_info(obj)
    if isinstance(obj, IssuedBillingKeyInfo):
        return _serialize_issued_billing_key_info(obj)


def _deserialize_billing_key_info(obj: Any) -> BillingKeyInfo:
    try:
        return _deserialize_deleted_billing_key_info(obj)
    except Exception:
        pass
    try:
        return _deserialize_issued_billing_key_info(obj)
    except Exception:
        pass
    raise ValueError(f"{repr(obj)} is not BillingKeyInfo")
