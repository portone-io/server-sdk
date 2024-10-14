from __future__ import annotations
from typing import Any, Literal, Optional
from dataclasses import dataclass, field
from portone_server_sdk._generated.identity_verification.identity_verification_verified_customer import IdentityVerificationVerifiedCustomer, _deserialize_identity_verification_verified_customer, _serialize_identity_verification_verified_customer
from portone_server_sdk._generated.common.selected_channel import SelectedChannel, _deserialize_selected_channel, _serialize_selected_channel

@dataclass
class VerifiedIdentityVerification:
    """완료된 본인인증 내역
    """
    status: Literal["VERIFIED"] = field(repr=False)
    """본인인증 상태
    """
    id: str
    """본인인증 내역 아이디
    """
    verified_customer: IdentityVerificationVerifiedCustomer
    """인증된 고객 정보
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
    verified_at: str
    """본인인증 완료 시점
    (RFC 3339 date-time)
    """
    pg_tx_id: str
    """본인인증 내역 PG사 아이디
    """
    pg_raw_response: str
    """PG사 응답 데이터
    """
    channel: Optional[SelectedChannel]
    """사용된 본인인증 채널
    """
    custom_data: Optional[str]
    """사용자 지정 데이터
    """


def _serialize_verified_identity_verification(obj: VerifiedIdentityVerification) -> Any:
    entity = {}
    entity["status"] = "VERIFIED"
    entity["id"] = obj.id
    entity["verifiedCustomer"] = _serialize_identity_verification_verified_customer(obj.verified_customer)
    entity["requestedAt"] = obj.requested_at
    entity["updatedAt"] = obj.updated_at
    entity["statusChangedAt"] = obj.status_changed_at
    entity["verifiedAt"] = obj.verified_at
    entity["pgTxId"] = obj.pg_tx_id
    entity["pgRawResponse"] = obj.pg_raw_response
    if obj.channel is not None:
        entity["channel"] = _serialize_selected_channel(obj.channel)
    if obj.custom_data is not None:
        entity["customData"] = obj.custom_data
    return entity


def _deserialize_verified_identity_verification(obj: Any) -> VerifiedIdentityVerification:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "status" not in obj:
        raise KeyError(f"'status' is not in {obj}")
    status = obj["status"]
    if status != "VERIFIED":
        raise ValueError(f"{repr(status)} is not 'VERIFIED'")
    if "id" not in obj:
        raise KeyError(f"'id' is not in {obj}")
    id = obj["id"]
    if not isinstance(id, str):
        raise ValueError(f"{repr(id)} is not str")
    if "verifiedCustomer" not in obj:
        raise KeyError(f"'verifiedCustomer' is not in {obj}")
    verified_customer = obj["verifiedCustomer"]
    verified_customer = _deserialize_identity_verification_verified_customer(verified_customer)
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
    if "verifiedAt" not in obj:
        raise KeyError(f"'verifiedAt' is not in {obj}")
    verified_at = obj["verifiedAt"]
    if not isinstance(verified_at, str):
        raise ValueError(f"{repr(verified_at)} is not str")
    if "pgTxId" not in obj:
        raise KeyError(f"'pgTxId' is not in {obj}")
    pg_tx_id = obj["pgTxId"]
    if not isinstance(pg_tx_id, str):
        raise ValueError(f"{repr(pg_tx_id)} is not str")
    if "pgRawResponse" not in obj:
        raise KeyError(f"'pgRawResponse' is not in {obj}")
    pg_raw_response = obj["pgRawResponse"]
    if not isinstance(pg_raw_response, str):
        raise ValueError(f"{repr(pg_raw_response)} is not str")
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
    return VerifiedIdentityVerification(status, id, verified_customer, requested_at, updated_at, status_changed_at, verified_at, pg_tx_id, pg_raw_response, channel, custom_data)
