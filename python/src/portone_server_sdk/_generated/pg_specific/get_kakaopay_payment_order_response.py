from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class GetKakaopayPaymentOrderResponse:
    """카카오페이 주문 조회 응답
    """
    status_code: int
    """HTTP 상태 코드
    (int32)
    """
    body: str
    """HTTP 응답 본문 (JSON)
    """


def _serialize_get_kakaopay_payment_order_response(obj: GetKakaopayPaymentOrderResponse) -> Any:
    entity = {}
    entity["statusCode"] = obj.status_code
    entity["body"] = obj.body
    return entity


def _deserialize_get_kakaopay_payment_order_response(obj: Any) -> GetKakaopayPaymentOrderResponse:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "statusCode" not in obj:
        raise KeyError(f"'statusCode' is not in {obj}")
    status_code = obj["statusCode"]
    if not isinstance(status_code, int):
        raise ValueError(f"{repr(status_code)} is not int")
    if "body" not in obj:
        raise KeyError(f"'body' is not in {obj}")
    body = obj["body"]
    if not isinstance(body, str):
        raise ValueError(f"{repr(body)} is not str")
    return GetKakaopayPaymentOrderResponse(status_code, body)
