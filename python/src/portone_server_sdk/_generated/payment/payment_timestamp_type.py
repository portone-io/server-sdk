from __future__ import annotations
from typing import Any, Literal, Optional, Union

PaymentTimestampType = Union[Literal["CREATED_AT", "STATUS_CHANGED_AT"], str]
"""조회 시점 기준

어떤 시점을 기준으로 조회를 할 것인지 선택합니다.
CREATED_AT: 결제 건 생성 시점을 기준으로 조회합니다.
STATUS_CHANGED_AT: 상태 승인 시점을 기준으로 조회합니다. 결제 건의 최종 상태에 따라 검색 기준이 다르게 적용됩니다.
ready -> 결제 요청 시점 기준
paid -> 결제 완료 시점 기준
cancelled -> 결제 취소 시점 기준
failed -> 결제 실패 시점 기준
값을 입력하지 않으면 STATUS_CHANGED_AT 으로 자동 적용됩니다.
"""


def _serialize_payment_timestamp_type(obj: PaymentTimestampType) -> Any:
    if isinstance(obj, dict):
        return obj
    return obj


def _deserialize_payment_timestamp_type(obj: Any) -> PaymentTimestampType:
    return obj
