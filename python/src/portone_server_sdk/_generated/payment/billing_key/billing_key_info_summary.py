from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field
from ...common.selected_channel import SelectedChannel, _deserialize_selected_channel, _serialize_selected_channel

@dataclass
class BillingKeyInfoSummary:
    billing_key: str
    """발급된 빌링키
    """
    issued_at: str
    """빌링키 발급 완료 시점
    (RFC 3339 date-time)
    """
    channels: Optional[list[SelectedChannel]] = field(default=None)
    """발급된 채널
    """


def _serialize_billing_key_info_summary(obj: BillingKeyInfoSummary) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["billingKey"] = obj.billing_key
    entity["issuedAt"] = obj.issued_at
    if obj.channels is not None:
        entity["channels"] = list(map(_serialize_selected_channel, obj.channels))
    return entity


def _deserialize_billing_key_info_summary(obj: Any) -> BillingKeyInfoSummary:
    if not isinstance(obj, dict):
        raise ValueError("Expected dict for obj")
    if "billingKey" not in obj:
        raise KeyError("Missing required field 'billingKey'")
    billing_key = obj["billingKey"]
    if not isinstance(billing_key, str):
        raise ValueError("Expected str for billing_key")
    if "issuedAt" not in obj:
        raise KeyError("Missing required field 'issuedAt'")
    issued_at = obj["issuedAt"]
    if not isinstance(issued_at, str):
        raise ValueError("Expected str for issued_at")
    if "channels" in obj:
        channels = obj["channels"]
        if not isinstance(channels, list):
            raise ValueError("Expected list for channels")
        for i, item in enumerate(channels):
            item = _deserialize_selected_channel(item)
            channels[i] = item
    else:
        channels = None
    return BillingKeyInfoSummary(billing_key, issued_at, channels)
