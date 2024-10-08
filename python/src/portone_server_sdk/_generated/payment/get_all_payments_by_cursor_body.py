from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class GetAllPaymentsByCursorBody:
    """결제 건 커서 기반 대용량 다건 조회를 위한 입력 정보
    """
    store_id: Optional[str]
    """상점 아이디

    접근 권한이 있는 상점 아이디만 입력 가능하며, 미입력시 토큰에 담긴 상점 아이디를 사용합니다.
    """
    from_: Optional[str]
    """결제 건 생성시점 범위 조건의 시작

    값을 입력하지 않으면 end의 90일 전으로 설정됩니다.
    (RFC 3339 date-time)
    """
    until: Optional[str]
    """결제 건 생성시점 범위 조건의 끝

    값을 입력하지 않으면 현재 시점으로 설정됩니다.
    (RFC 3339 date-time)
    """
    cursor: Optional[str]
    """커서

    결제 건 리스트 중 어디서부터 읽어야 할지 가리키는 값입니다. 최초 요청일 경우 값을 입력하지 마시되, 두번째 요청 부터는 이전 요청 응답값의 cursor를 입력해주시면 됩니다.
    """
    size: Optional[int]
    """페이지 크기

    미입력 시 기본값은 10 이며 최대 1000까지 허용
    (int32)
    """


def _serialize_get_all_payments_by_cursor_body(obj: GetAllPaymentsByCursorBody) -> Any:
    entity = {}
    if obj.store_id is not None:
        entity["storeId"] = obj.store_id
    if obj.from_ is not None:
        entity["from"] = obj.from_
    if obj.until is not None:
        entity["until"] = obj.until
    if obj.cursor is not None:
        entity["cursor"] = obj.cursor
    if obj.size is not None:
        entity["size"] = obj.size
    return entity


def _deserialize_get_all_payments_by_cursor_body(obj: Any) -> GetAllPaymentsByCursorBody:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "storeId" in obj:
        store_id = obj["storeId"]
        if not isinstance(store_id, str):
            raise ValueError(f"{repr(store_id)} is not str")
    else:
        store_id = None
    if "from" in obj:
        from_ = obj["from"]
        if not isinstance(from_, str):
            raise ValueError(f"{repr(from_)} is not str")
    else:
        from_ = None
    if "until" in obj:
        until = obj["until"]
        if not isinstance(until, str):
            raise ValueError(f"{repr(until)} is not str")
    else:
        until = None
    if "cursor" in obj:
        cursor = obj["cursor"]
        if not isinstance(cursor, str):
            raise ValueError(f"{repr(cursor)} is not str")
    else:
        cursor = None
    if "size" in obj:
        size = obj["size"]
        if not isinstance(size, int):
            raise ValueError(f"{repr(size)} is not int")
    else:
        size = None
    return GetAllPaymentsByCursorBody(store_id, from_, until, cursor, size)
