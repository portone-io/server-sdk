from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class PlatformAccountHolder:
    """예금주 조회 성공 응답 정보
    """
    holder_name: str
    """계좌 예금주 이름
    """
    account_verification_id: str
    """계좌 검증 아이디
    """


def _serialize_platform_account_holder(obj: PlatformAccountHolder) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["holderName"] = obj.holder_name
    entity["accountVerificationId"] = obj.account_verification_id
    return entity


def _deserialize_platform_account_holder(obj: Any) -> PlatformAccountHolder:
    if not isinstance(obj, dict):
        raise ValueError("Expected dict for obj")
    if "holderName" not in obj:
        raise KeyError("Missing required field 'holderName'")
    holder_name = obj["holderName"]
    if not isinstance(holder_name, str):
        raise ValueError("Expected str for holder_name")
    if "accountVerificationId" not in obj:
        raise KeyError("Missing required field 'accountVerificationId'")
    account_verification_id = obj["accountVerificationId"]
    if not isinstance(account_verification_id, str):
        raise ValueError("Expected str for account_verification_id")
    return PlatformAccountHolder(holder_name, account_verification_id)
