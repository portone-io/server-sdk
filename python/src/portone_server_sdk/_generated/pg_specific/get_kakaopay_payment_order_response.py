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
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["statusCode"] = obj.status_code
    entity["body"] = obj.body
    return entity


def _deserialize_get_kakaopay_payment_order_response(obj: Any) -> GetKakaopayPaymentOrderResponse:
    if not isinstance(obj, dict):
        raise ValueError("Expected dict for obj")
    if "statusCode" not in obj:
        raise KeyError("Missing required field 'statusCode'")
    status_code = obj["statusCode"]
    if not isinstance(status_code, int):
        raise ValueError("Expected int for status_code")
    if "body" not in obj:
        raise KeyError("Missing required field 'body'")
    body = obj["body"]
    if not isinstance(body, str):
        raise ValueError("Expected str for body")
    return GetKakaopayPaymentOrderResponse(status_code, body)
