from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field
from ..payment.register_store_receipt_body_item import RegisterStoreReceiptBodyItem, _deserialize_register_store_receipt_body_item, _serialize_register_store_receipt_body_item

@dataclass
class RegisterStoreReceiptBody:
    """영수증 내 하위 상점 거래 등록 정보
    """
    items: list[RegisterStoreReceiptBodyItem]
    """하위 상점 거래 목록
    """
    store_id: Optional[str] = field(default=None)
    """상점 아이디
    """


def _serialize_register_store_receipt_body(obj: RegisterStoreReceiptBody) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["items"] = list(map(_serialize_register_store_receipt_body_item, obj.items))
    if obj.store_id is not None:
        entity["storeId"] = obj.store_id
    return entity


def _deserialize_register_store_receipt_body(obj: Any) -> RegisterStoreReceiptBody:
    if not isinstance(obj, dict):
        raise ValueError("Expected dict for obj")
    if "items" not in obj:
        raise KeyError("Missing required field 'items'")
    items = obj["items"]
    if not isinstance(items, list):
        raise ValueError("Expected list for items")
    for i, item in enumerate(items):
        item = _deserialize_register_store_receipt_body_item(item)
        items[i] = item
    if "storeId" in obj:
        store_id = obj["storeId"]
        if not isinstance(store_id, str):
            raise ValueError("Expected str for store_id")
    else:
        store_id = None
    return RegisterStoreReceiptBody(items, store_id)
