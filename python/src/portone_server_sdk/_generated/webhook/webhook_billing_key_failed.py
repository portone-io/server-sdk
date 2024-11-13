from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field
from portone_server_sdk._generated.webhook.webhook_billing_key_data_failed import WebhookBillingKeyDataFailed, _deserialize_webhook_billing_key_data_failed

@dataclass
class WebhookBillingKeyFailed:
    """빌링키 발급이 실패했을 때
    """
    timestamp: str
    """해당 웹훅을 트리거한 이벤트의 발생 시각(RFC 3339 형식)입니다. 고객사 서버가 웹훅을 수신하는 데 실패하여 재시도가 일어나도 이 값은 동일하게 유지됩니다.
    (RFC 3339 date-time)
    """
    data: WebhookBillingKeyDataFailed
    """웹훅을 트리거한 이벤트의 실제 세부 내용입니다.
    """


def _deserialize_webhook_billing_key_failed(obj: Any) -> WebhookBillingKeyFailed:
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
    data = _deserialize_webhook_billing_key_data_failed(data)
    return WebhookBillingKeyFailed(timestamp, data)