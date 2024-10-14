from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field
from portone_server_sdk._generated.payment.billing_key.billing_key_info_summary import BillingKeyInfoSummary, _deserialize_billing_key_info_summary, _serialize_billing_key_info_summary
from portone_server_sdk._generated.payment.billing_key.channel_specific_failure import ChannelSpecificFailure, _deserialize_channel_specific_failure, _serialize_channel_specific_failure

@dataclass
class IssueBillingKeyResponse:
    """빌링키 발급 성공 응답
    """
    billing_key_info: BillingKeyInfoSummary
    """빌링키 정보
    """
    channel_specific_failures: Optional[list[ChannelSpecificFailure]]
    """발급에 실패한 채널이 있을시 실패 정보
    """


def _serialize_issue_billing_key_response(obj: IssueBillingKeyResponse) -> Any:
    entity = {}
    entity["billingKeyInfo"] = _serialize_billing_key_info_summary(obj.billing_key_info)
    if obj.channel_specific_failures is not None:
        entity["channelSpecificFailures"] = list(map(_serialize_channel_specific_failure, obj.channel_specific_failures))
    return entity


def _deserialize_issue_billing_key_response(obj: Any) -> IssueBillingKeyResponse:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "billingKeyInfo" not in obj:
        raise KeyError(f"'billingKeyInfo' is not in {obj}")
    billing_key_info = obj["billingKeyInfo"]
    billing_key_info = _deserialize_billing_key_info_summary(billing_key_info)
    if "channelSpecificFailures" in obj:
        channel_specific_failures = obj["channelSpecificFailures"]
        if not isinstance(channel_specific_failures, list):
            raise ValueError(f"{repr(channel_specific_failures)} is not list")
        for i, item in enumerate(channel_specific_failures):
            item = _deserialize_channel_specific_failure(item)
            channel_specific_failures[i] = item
    else:
        channel_specific_failures = None
    return IssueBillingKeyResponse(billing_key_info, channel_specific_failures)
