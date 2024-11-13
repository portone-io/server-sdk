from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class ConfirmEscrowBody:
    """에스크로 구매 확정 입력 정보
    """
    store_id: Optional[str] = field(default=None)
    """상점 아이디

    접근 권한이 있는 상점 아이디만 입력 가능하며, 미입력시 토큰에 담긴 상점 아이디를 사용합니다.
    """
    from_store: Optional[bool] = field(default=None)
    """확인 주체가 상점인지 여부

    구매확정요청 주체가 고객사 관리자인지 구매자인지 구분하기 위한 필드입니다.
    네이버페이 전용 파라미터이며, 구분이 모호한 경우 고객사 관리자(true)로 입력합니다.
    """


def _serialize_confirm_escrow_body(obj: ConfirmEscrowBody) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    if obj.store_id is not None:
        entity["storeId"] = obj.store_id
    if obj.from_store is not None:
        entity["fromStore"] = obj.from_store
    return entity


def _deserialize_confirm_escrow_body(obj: Any) -> ConfirmEscrowBody:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "storeId" in obj:
        store_id = obj["storeId"]
        if not isinstance(store_id, str):
            raise ValueError(f"{repr(store_id)} is not str")
    else:
        store_id = None
    if "fromStore" in obj:
        from_store = obj["fromStore"]
        if not isinstance(from_store, bool):
            raise ValueError(f"{repr(from_store)} is not bool")
    else:
        from_store = None
    return ConfirmEscrowBody(store_id, from_store)
