from __future__ import annotations
from typing import Any, Literal, Optional
from dataclasses import dataclass, field
from portone_server_sdk._generated.identity_verification.identity_verification_requested_customer import IdentityVerificationRequestedCustomer, _deserialize_identity_verification_requested_customer, _serialize_identity_verification_requested_customer
from portone_server_sdk._generated.common.selected_channel import SelectedChannel, _deserialize_selected_channel, _serialize_selected_channel

@dataclass
class ReadyIdentityVerification:
    """준비 상태의 본인인증 내역
    """
    status: Literal["READY"] = field(repr=False)
    """본인인증 상태
    """
    id: str
    """본인인증 내역 아이디
    """
    requested_customer: IdentityVerificationRequestedCustomer
    """요청 시 고객 정보
    """
    requested_at: str
    """본인인증 요청 시점
    (RFC 3339 date-time)
    """
    updated_at: str
    """업데이트 시점
    (RFC 3339 date-time)
    """
    status_changed_at: str
    """상태 업데이트 시점
    (RFC 3339 date-time)
    """
    channel: Optional[SelectedChannel]
    """사용된 본인인증 채널
    """
    custom_data: Optional[str]
    """사용자 지정 데이터
    """


def _serialize_ready_identity_verification(obj: ReadyIdentityVerification) -> Any:
    entity = {}
    entity["status"] = "READY"
    entity["id"] = obj.id
    entity["requestedCustomer"] = _serialize_identity_verification_requested_customer(obj.requested_customer)
    entity["requestedAt"] = obj.requested_at
    entity["updatedAt"] = obj.updated_at
    entity["statusChangedAt"] = obj.status_changed_at
    if obj.channel is not None:
        entity["channel"] = _serialize_selected_channel(obj.channel)
    if obj.custom_data is not None:
        entity["customData"] = obj.custom_data
    return entity


def _deserialize_ready_identity_verification(obj: Any) -> ReadyIdentityVerification:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "status" not in obj:
        raise KeyError(f"'status' is not in {obj}")
    status = obj["status"]
    if status != "READY":
        raise ValueError(f"{repr(status)} is not 'READY'")
    if "id" not in obj:
        raise KeyError(f"'id' is not in {obj}")
    id = obj["id"]
    if not isinstance(id, str):
        raise ValueError(f"{repr(id)} is not str")
    if "requestedCustomer" not in obj:
        raise KeyError(f"'requestedCustomer' is not in {obj}")
    requested_customer = obj["requestedCustomer"]
    requested_customer = _deserialize_identity_verification_requested_customer(requested_customer)
    if "requestedAt" not in obj:
        raise KeyError(f"'requestedAt' is not in {obj}")
    requested_at = obj["requestedAt"]
    if not isinstance(requested_at, str):
        raise ValueError(f"{repr(requested_at)} is not str")
    if "updatedAt" not in obj:
        raise KeyError(f"'updatedAt' is not in {obj}")
    updated_at = obj["updatedAt"]
    if not isinstance(updated_at, str):
        raise ValueError(f"{repr(updated_at)} is not str")
    if "statusChangedAt" not in obj:
        raise KeyError(f"'statusChangedAt' is not in {obj}")
    status_changed_at = obj["statusChangedAt"]
    if not isinstance(status_changed_at, str):
        raise ValueError(f"{repr(status_changed_at)} is not str")
    if "channel" in obj:
        channel = obj["channel"]
        channel = _deserialize_selected_channel(channel)
    else:
        channel = None
    if "customData" in obj:
        custom_data = obj["customData"]
        if not isinstance(custom_data, str):
            raise ValueError(f"{repr(custom_data)} is not str")
    else:
        custom_data = None
    return ReadyIdentityVerification(status, id, requested_customer, requested_at, updated_at, status_changed_at, channel, custom_data)
