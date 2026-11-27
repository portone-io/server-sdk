from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field
from ..identity_verification.identity_verification_verified_customer import IdentityVerificationVerifiedCustomer, _deserialize_identity_verification_verified_customer, _serialize_identity_verification_verified_customer
from ..common.port_one_version import PortOneVersion, _deserialize_port_one_version, _serialize_port_one_version
from ..common.selected_channel import SelectedChannel, _deserialize_selected_channel, _serialize_selected_channel

@dataclass
class VerifiedIdentityVerification:
    """완료된 본인인증 내역
    """
    """본인인증 상태
    """
    id: str
    """고객사 본인인증 번호
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
    version: PortOneVersion
    """포트원 버전
    """
    channel: Optional[SelectedChannel] = field(default=None)
    """사용된 본인인증 채널
    """
    custom_data: Optional[str] = field(default=None)
    """사용자 지정 데이터
    """


def _serialize_verified_identity_verification(obj: VerifiedIdentityVerification) -> Any:
    if isinstance(obj, dict):
        return obj
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
    entity["version"] = _serialize_port_one_version(obj.version)
    if obj.channel is not None:
        entity["channel"] = _serialize_selected_channel(obj.channel)
    if obj.custom_data is not None:
        entity["customData"] = obj.custom_data
    return entity


def _deserialize_verified_identity_verification(obj: Any) -> VerifiedIdentityVerification:
    if not isinstance(obj, dict):
        raise ValueError("Expected dict for obj")
    if "status" not in obj:
        raise KeyError("Missing required field 'status'")
    status = obj["status"]
    if status != "VERIFIED":
        raise ValueError("Expected 'VERIFIED' for status")
    if "id" not in obj:
        raise KeyError("Missing required field 'id'")
    id = obj["id"]
    if not isinstance(id, str):
        raise ValueError("Expected str for id")
    if "verifiedCustomer" not in obj:
        raise KeyError("Missing required field 'verifiedCustomer'")
    verified_customer = obj["verifiedCustomer"]
    verified_customer = _deserialize_identity_verification_verified_customer(verified_customer)
    if "requestedAt" not in obj:
        raise KeyError("Missing required field 'requestedAt'")
    requested_at = obj["requestedAt"]
    if not isinstance(requested_at, str):
        raise ValueError("Expected str for requested_at")
    if "updatedAt" not in obj:
        raise KeyError("Missing required field 'updatedAt'")
    updated_at = obj["updatedAt"]
    if not isinstance(updated_at, str):
        raise ValueError("Expected str for updated_at")
    if "statusChangedAt" not in obj:
        raise KeyError("Missing required field 'statusChangedAt'")
    status_changed_at = obj["statusChangedAt"]
    if not isinstance(status_changed_at, str):
        raise ValueError("Expected str for status_changed_at")
    if "verifiedAt" not in obj:
        raise KeyError("Missing required field 'verifiedAt'")
    verified_at = obj["verifiedAt"]
    if not isinstance(verified_at, str):
        raise ValueError("Expected str for verified_at")
    if "pgTxId" not in obj:
        raise KeyError("Missing required field 'pgTxId'")
    pg_tx_id = obj["pgTxId"]
    if not isinstance(pg_tx_id, str):
        raise ValueError("Expected str for pg_tx_id")
    if "pgRawResponse" not in obj:
        raise KeyError("Missing required field 'pgRawResponse'")
    pg_raw_response = obj["pgRawResponse"]
    if not isinstance(pg_raw_response, str):
        raise ValueError("Expected str for pg_raw_response")
    if "version" not in obj:
        raise KeyError("Missing required field 'version'")
    version = obj["version"]
    version = _deserialize_port_one_version(version)
    if "channel" in obj:
        channel = obj["channel"]
        channel = _deserialize_selected_channel(channel)
    else:
        channel = None
    if "customData" in obj:
        custom_data = obj["customData"]
        if not isinstance(custom_data, str):
            raise ValueError("Expected str for custom_data")
    else:
        custom_data = None
    return VerifiedIdentityVerification(id, verified_customer, requested_at, updated_at, status_changed_at, verified_at, pg_tx_id, pg_raw_response, version, channel, custom_data)
