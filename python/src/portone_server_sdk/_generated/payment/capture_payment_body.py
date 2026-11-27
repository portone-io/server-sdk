from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class CapturePaymentBody:
    """수동 매입 입력 정보
    """
    store_id: Optional[str] = field(default=None)
    """상점 아이디

    접근 권한이 있는 상점 아이디만 입력 가능하며, 미입력시 인증 정보의 상점 아이디를 사용합니다.
    """


def _serialize_capture_payment_body(obj: CapturePaymentBody) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    if obj.store_id is not None:
        entity["storeId"] = obj.store_id
    return entity


def _deserialize_capture_payment_body(obj: Any) -> CapturePaymentBody:
    if not isinstance(obj, dict):
        raise ValueError("Expected dict for obj")
    if "storeId" in obj:
        store_id = obj["storeId"]
        if not isinstance(store_id, str):
            raise ValueError("Expected str for store_id")
    else:
        store_id = None
    return CapturePaymentBody(store_id)
