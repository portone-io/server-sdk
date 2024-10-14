from __future__ import annotations
from typing import Any, Literal, Optional
from dataclasses import dataclass, field
from portone_server_sdk._generated.payment.billing_key.billing_key_failure import BillingKeyFailure, _deserialize_billing_key_failure, _serialize_billing_key_failure
from portone_server_sdk._generated.common.selected_channel import SelectedChannel, _deserialize_selected_channel, _serialize_selected_channel

@dataclass
class FailedPgBillingKeyIssueResponse:
    """빌링키 발급 실패 채널 응답
    """
    type: Literal["FAILED"] = field(repr=False)
    channel: SelectedChannel
    """채널

    빌링키 발급을 시도한 채널입니다.
    """
    failure: BillingKeyFailure
    """발급 실패 상세 정보
    """


def _serialize_failed_pg_billing_key_issue_response(obj: FailedPgBillingKeyIssueResponse) -> Any:
    entity = {}
    entity["type"] = "FAILED"
    entity["channel"] = _serialize_selected_channel(obj.channel)
    entity["failure"] = _serialize_billing_key_failure(obj.failure)
    return entity


def _deserialize_failed_pg_billing_key_issue_response(obj: Any) -> FailedPgBillingKeyIssueResponse:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "type" not in obj:
        raise KeyError(f"'type' is not in {obj}")
    type = obj["type"]
    if type != "FAILED":
        raise ValueError(f"{repr(type)} is not 'FAILED'")
    if "channel" not in obj:
        raise KeyError(f"'channel' is not in {obj}")
    channel = obj["channel"]
    channel = _deserialize_selected_channel(channel)
    if "failure" not in obj:
        raise KeyError(f"'failure' is not in {obj}")
    failure = obj["failure"]
    failure = _deserialize_billing_key_failure(failure)
    return FailedPgBillingKeyIssueResponse(type, channel, failure)
