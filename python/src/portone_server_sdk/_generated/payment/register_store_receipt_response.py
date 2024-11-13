from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class RegisterStoreReceiptResponse:
    """영수증 내 하위 상점 거래 등록 응답
    """
    receipt_url: Optional[str] = field(default=None)
    """결제 영수증 URL
    """


def _serialize_register_store_receipt_response(obj: RegisterStoreReceiptResponse) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    if obj.receipt_url is not None:
        entity["receiptUrl"] = obj.receipt_url
    return entity


def _deserialize_register_store_receipt_response(obj: Any) -> RegisterStoreReceiptResponse:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "receiptUrl" in obj:
        receipt_url = obj["receiptUrl"]
        if not isinstance(receipt_url, str):
            raise ValueError(f"{repr(receipt_url)} is not str")
    else:
        receipt_url = None
    return RegisterStoreReceiptResponse(receipt_url)
