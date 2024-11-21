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
    """빌링크 발급 완료 시점
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
        raise ValueError(f"{repr(obj)} is not dict")
    if "billingKey" not in obj:
        raise KeyError(f"'billingKey' is not in {obj}")
    billing_key = obj["billingKey"]
    if not isinstance(billing_key, str):
        raise ValueError(f"{repr(billing_key)} is not str")
    if "issuedAt" not in obj:
        raise KeyError(f"'issuedAt' is not in {obj}")
    issued_at = obj["issuedAt"]
    if not isinstance(issued_at, str):
        raise ValueError(f"{repr(issued_at)} is not str")
    if "channels" in obj:
        channels = obj["channels"]
        if not isinstance(channels, list):
            raise ValueError(f"{repr(channels)} is not list")
        for i, item in enumerate(channels):
            item = _deserialize_selected_channel(item)
            channels[i] = item
    else:
        channels = None
    return BillingKeyInfoSummary(billing_key, issued_at, channels)
