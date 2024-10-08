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
    entity = {}
    entity["holderName"] = obj.holder_name
    entity["accountVerificationId"] = obj.account_verification_id
    return entity


def _deserialize_platform_account_holder(obj: Any) -> PlatformAccountHolder:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "holderName" not in obj:
        raise KeyError(f"'holderName' is not in {obj}")
    holder_name = obj["holderName"]
    if not isinstance(holder_name, str):
        raise ValueError(f"{repr(holder_name)} is not str")
    if "accountVerificationId" not in obj:
        raise KeyError(f"'accountVerificationId' is not in {obj}")
    account_verification_id = obj["accountVerificationId"]
    if not isinstance(account_verification_id, str):
        raise ValueError(f"{repr(account_verification_id)} is not str")
    return PlatformAccountHolder(holder_name, account_verification_id)
