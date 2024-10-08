from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field
from portone_server_sdk._generated.payment.payment_webhook_payment_status import PaymentWebhookPaymentStatus, _deserialize_payment_webhook_payment_status, _serialize_payment_webhook_payment_status
from portone_server_sdk._generated.payment.payment_webhook_request import PaymentWebhookRequest, _deserialize_payment_webhook_request, _serialize_payment_webhook_request
from portone_server_sdk._generated.payment.payment_webhook_response import PaymentWebhookResponse, _deserialize_payment_webhook_response, _serialize_payment_webhook_response
from portone_server_sdk._generated.payment.payment_webhook_status import PaymentWebhookStatus, _deserialize_payment_webhook_status, _serialize_payment_webhook_status
from portone_server_sdk._generated.payment.payment_webhook_trigger import PaymentWebhookTrigger, _deserialize_payment_webhook_trigger, _serialize_payment_webhook_trigger

@dataclass
class PaymentWebhook:
    """성공 웹훅 내역
    """
    id: str
    """웹훅 아이디
    """
    url: str
    """웹훅이 발송된 url

    V1 결제 건인 경우, 값이 존재하지 않습니다.
    """
    payment_status: Optional[PaymentWebhookPaymentStatus]
    """웹훅 발송 시 결제 건 상태

    V1 결제 건인 경우, 값이 존재하지 않습니다.
    """
    status: Optional[PaymentWebhookStatus]
    """웹훅 상태
    """
    is_async: Optional[bool]
    """비동기 웹훅 여부

    V1 결제 건인 경우, 값이 존재하지 않습니다.
    """
    current_execution_count: Optional[int]
    """현재 발송 횟수
    (int32)
    """
    max_execution_count: Optional[int]
    """최대 발송 횟수
    (int32)
    """
    trigger: Optional[PaymentWebhookTrigger]
    """웹훅 실행 맥락
    """
    request: Optional[PaymentWebhookRequest]
    """웹훅 요청 정보
    """
    response: Optional[PaymentWebhookResponse]
    """웹훅 응답 정보
    """
    triggered_at: Optional[str]
    """웹훅 처리 시작 시점
    (RFC 3339 date-time)
    """


def _serialize_payment_webhook(obj: PaymentWebhook) -> Any:
    entity = {}
    entity["id"] = obj.id
    entity["url"] = obj.url
    if obj.payment_status is not None:
        entity["paymentStatus"] = _serialize_payment_webhook_payment_status(obj.payment_status)
    if obj.status is not None:
        entity["status"] = _serialize_payment_webhook_status(obj.status)
    if obj.is_async is not None:
        entity["isAsync"] = obj.is_async
    if obj.current_execution_count is not None:
        entity["currentExecutionCount"] = obj.current_execution_count
    if obj.max_execution_count is not None:
        entity["maxExecutionCount"] = obj.max_execution_count
    if obj.trigger is not None:
        entity["trigger"] = _serialize_payment_webhook_trigger(obj.trigger)
    if obj.request is not None:
        entity["request"] = _serialize_payment_webhook_request(obj.request)
    if obj.response is not None:
        entity["response"] = _serialize_payment_webhook_response(obj.response)
    if obj.triggered_at is not None:
        entity["triggeredAt"] = obj.triggered_at
    return entity


def _deserialize_payment_webhook(obj: Any) -> PaymentWebhook:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "id" not in obj:
        raise KeyError(f"'id' is not in {obj}")
    id = obj["id"]
    if not isinstance(id, str):
        raise ValueError(f"{repr(id)} is not str")
    if "url" not in obj:
        raise KeyError(f"'url' is not in {obj}")
    url = obj["url"]
    if not isinstance(url, str):
        raise ValueError(f"{repr(url)} is not str")
    if "paymentStatus" in obj:
        payment_status = obj["paymentStatus"]
        payment_status = _deserialize_payment_webhook_payment_status(payment_status)
    else:
        payment_status = None
    if "status" in obj:
        status = obj["status"]
        status = _deserialize_payment_webhook_status(status)
    else:
        status = None
    if "isAsync" in obj:
        is_async = obj["isAsync"]
        if not isinstance(is_async, bool):
            raise ValueError(f"{repr(is_async)} is not bool")
    else:
        is_async = None
    if "currentExecutionCount" in obj:
        current_execution_count = obj["currentExecutionCount"]
        if not isinstance(current_execution_count, int):
            raise ValueError(f"{repr(current_execution_count)} is not int")
    else:
        current_execution_count = None
    if "maxExecutionCount" in obj:
        max_execution_count = obj["maxExecutionCount"]
        if not isinstance(max_execution_count, int):
            raise ValueError(f"{repr(max_execution_count)} is not int")
    else:
        max_execution_count = None
    if "trigger" in obj:
        trigger = obj["trigger"]
        trigger = _deserialize_payment_webhook_trigger(trigger)
    else:
        trigger = None
    if "request" in obj:
        request = obj["request"]
        request = _deserialize_payment_webhook_request(request)
    else:
        request = None
    if "response" in obj:
        response = obj["response"]
        response = _deserialize_payment_webhook_response(response)
    else:
        response = None
    if "triggeredAt" in obj:
        triggered_at = obj["triggeredAt"]
        if not isinstance(triggered_at, str):
            raise ValueError(f"{repr(triggered_at)} is not str")
    else:
        triggered_at = None
    return PaymentWebhook(id, url, payment_status, status, is_async, current_execution_count, max_execution_count, trigger, request, response, triggered_at)
