from __future__ import annotations
from typing import Any, Literal, Optional
from dataclasses import dataclass, field
from portone_server_sdk._generated.webhook.webhook_billing_key_request_failed_data import WebhookBillingKeyRequestFailedData, _deserialize_webhook_billing_key_request_failed_data, _serialize_webhook_billing_key_request_failed_data

@dataclass
class WebhookBillingKeyRequestFailed:
    """빌링키 발급이 실패했을 때
    """
    type: Literal["BillingKey.Failed"] = field(repr=False)
    """웹훅을 트리거한 이벤트의 타입입니다.
    """
    timestamp: str
    """해당 웹훅을 트리거한 이벤트의 발생 시각(RFC 3339 형식)입니다. 고객사 서버가 웹훅을 수신하는 데 실패하여 재시도가 일어나도 이 값은 동일하게 유지됩니다.
    (RFC 3339 date-time)
    """
    data: WebhookBillingKeyRequestFailedData
    """웹훅을 트리거한 이벤트의 실제 세부 내용입니다.
    """


def _serialize_webhook_billing_key_request_failed(obj: WebhookBillingKeyRequestFailed) -> Any:
    entity = {}
    entity["type"] = "BillingKey.Failed"
    entity["timestamp"] = obj.timestamp
    entity["data"] = _serialize_webhook_billing_key_request_failed_data(obj.data)
    return entity


def _deserialize_webhook_billing_key_request_failed(obj: Any) -> WebhookBillingKeyRequestFailed:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "type" not in obj:
        raise KeyError(f"'type' is not in {obj}")
    type = obj["type"]
    if type != "BillingKey.Failed":
        raise ValueError(f"{repr(type)} is not 'BillingKey.Failed'")
    if "timestamp" not in obj:
        raise KeyError(f"'timestamp' is not in {obj}")
    timestamp = obj["timestamp"]
    if not isinstance(timestamp, str):
        raise ValueError(f"{repr(timestamp)} is not str")
    if "data" not in obj:
        raise KeyError(f"'data' is not in {obj}")
    data = obj["data"]
    data = _deserialize_webhook_billing_key_request_failed_data(data)
    return WebhookBillingKeyRequestFailed(type, timestamp, data)
