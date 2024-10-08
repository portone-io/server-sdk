from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class ResendWebhookBody:
    """웹훅 재발송을 위한 입력 정보
    """
    store_id: Optional[str]
    """상점 아이디

    접근 권한이 있는 상점 아이디만 입력 가능하며, 미입력시 토큰에 담긴 상점 아이디를 사용합니다.
    """
    webhook_id: Optional[str]
    """웹훅 아이디

    입력하지 않으면 결제 건의 가장 최근 웹훅 아이디가 기본 적용됩니다
    """


def _serialize_resend_webhook_body(obj: ResendWebhookBody) -> Any:
    entity = {}
    if obj.store_id is not None:
        entity["storeId"] = obj.store_id
    if obj.webhook_id is not None:
        entity["webhookId"] = obj.webhook_id
    return entity


def _deserialize_resend_webhook_body(obj: Any) -> ResendWebhookBody:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "storeId" in obj:
        store_id = obj["storeId"]
        if not isinstance(store_id, str):
            raise ValueError(f"{repr(store_id)} is not str")
    else:
        store_id = None
    if "webhookId" in obj:
        webhook_id = obj["webhookId"]
        if not isinstance(webhook_id, str):
            raise ValueError(f"{repr(webhook_id)} is not str")
    else:
        webhook_id = None
    return ResendWebhookBody(store_id, webhook_id)
