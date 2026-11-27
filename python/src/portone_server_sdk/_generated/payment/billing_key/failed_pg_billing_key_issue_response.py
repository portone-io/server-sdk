from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field
from ...payment.billing_key.billing_key_failure import BillingKeyFailure, _deserialize_billing_key_failure, _serialize_billing_key_failure
from ...common.selected_channel import SelectedChannel, _deserialize_selected_channel, _serialize_selected_channel

@dataclass
class FailedPgBillingKeyIssueResponse:
    """빌링키 발급 실패 채널 응답
    """
    channel: SelectedChannel
    """채널

    빌링키 발급을 시도한 채널입니다.
    """
    failure: BillingKeyFailure
    """발급 실패 상세 정보
    """


def _serialize_failed_pg_billing_key_issue_response(obj: FailedPgBillingKeyIssueResponse) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["type"] = "FAILED"
    entity["channel"] = _serialize_selected_channel(obj.channel)
    entity["failure"] = _serialize_billing_key_failure(obj.failure)
    return entity


def _deserialize_failed_pg_billing_key_issue_response(obj: Any) -> FailedPgBillingKeyIssueResponse:
    if not isinstance(obj, dict):
        raise ValueError("Expected dict for obj")
    if "type" not in obj:
        raise KeyError("Missing required field 'type'")
    type = obj["type"]
    if type != "FAILED":
        raise ValueError("Expected 'FAILED' for type")
    if "channel" not in obj:
        raise KeyError("Missing required field 'channel'")
    channel = obj["channel"]
    channel = _deserialize_selected_channel(channel)
    if "failure" not in obj:
        raise KeyError("Missing required field 'failure'")
    failure = obj["failure"]
    failure = _deserialize_billing_key_failure(failure)
    return FailedPgBillingKeyIssueResponse(channel, failure)
