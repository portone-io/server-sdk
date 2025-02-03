from __future__ import annotations
from typing import Any, Optional, Union
from ...payment.billing_key.channel_specific_failure_invalid_request import ChannelSpecificFailureInvalidRequest, _deserialize_channel_specific_failure_invalid_request, _serialize_channel_specific_failure_invalid_request
from ...payment.billing_key.channel_specific_failure_pg_provider import ChannelSpecificFailurePgProvider, _deserialize_channel_specific_failure_pg_provider, _serialize_channel_specific_failure_pg_provider

ChannelSpecificFailure = Union[ChannelSpecificFailureInvalidRequest, ChannelSpecificFailurePgProvider, dict]


def _serialize_channel_specific_failure(obj: ChannelSpecificFailure) -> Any:
    if isinstance(obj, dict):
        return obj
    if isinstance(obj, ChannelSpecificFailureInvalidRequest):
        return _serialize_channel_specific_failure_invalid_request(obj)
    if isinstance(obj, ChannelSpecificFailurePgProvider):
        return _serialize_channel_specific_failure_pg_provider(obj)


def _deserialize_channel_specific_failure(obj: Any) -> ChannelSpecificFailure:
    try:
        return _deserialize_channel_specific_failure_invalid_request(obj)
    except Exception:
        pass
    try:
        return _deserialize_channel_specific_failure_pg_provider(obj)
    except Exception:
        pass
    raise ValueError(f"{repr(obj)} is not ChannelSpecificFailure")
