from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class RevokePaymentSchedulesBody:
    """결제 예약 건 취소 요청 입력 정보
    """
    store_id: Optional[str] = field(default=None)
    """상점 아이디

    접근 권한이 있는 상점 아이디만 입력 가능하며, 미입력시 토큰에 담긴 상점 아이디를 사용합니다.
    """
    billing_key: Optional[str] = field(default=None)
    """빌링키
    """
    schedule_ids: Optional[list[str]] = field(default=None)
    """결제 예약 건 아이디 목록
    """


def _serialize_revoke_payment_schedules_body(obj: RevokePaymentSchedulesBody) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    if obj.store_id is not None:
        entity["storeId"] = obj.store_id
    if obj.billing_key is not None:
        entity["billingKey"] = obj.billing_key
    if obj.schedule_ids is not None:
        entity["scheduleIds"] = obj.schedule_ids
    return entity


def _deserialize_revoke_payment_schedules_body(obj: Any) -> RevokePaymentSchedulesBody:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "storeId" in obj:
        store_id = obj["storeId"]
        if not isinstance(store_id, str):
            raise ValueError(f"{repr(store_id)} is not str")
    else:
        store_id = None
    if "billingKey" in obj:
        billing_key = obj["billingKey"]
        if not isinstance(billing_key, str):
            raise ValueError(f"{repr(billing_key)} is not str")
    else:
        billing_key = None
    if "scheduleIds" in obj:
        schedule_ids = obj["scheduleIds"]
        if not isinstance(schedule_ids, list):
            raise ValueError(f"{repr(schedule_ids)} is not list")
        for i, item in enumerate(schedule_ids):
            if not isinstance(item, str):
                raise ValueError(f"{repr(item)} is not str")
    else:
        schedule_ids = None
    return RevokePaymentSchedulesBody(store_id, billing_key, schedule_ids)
