from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class UpdatePlatformPartnerBodyTypeNonWhtPayer:
    birthdate: Optional[str]
    """생년월일

    날짜를 나타내는 문자열로, `yyyy-MM-dd` 형식을 따릅니다.
    """


def _serialize_update_platform_partner_body_type_non_wht_payer(obj: UpdatePlatformPartnerBodyTypeNonWhtPayer) -> Any:
    entity = {}
    if obj.birthdate is not None:
        entity["birthdate"] = obj.birthdate
    return entity


def _deserialize_update_platform_partner_body_type_non_wht_payer(obj: Any) -> UpdatePlatformPartnerBodyTypeNonWhtPayer:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "birthdate" in obj:
        birthdate = obj["birthdate"]
        if not isinstance(birthdate, str):
            raise ValueError(f"{repr(birthdate)} is not str")
    else:
        birthdate = None
    return UpdatePlatformPartnerBodyTypeNonWhtPayer(birthdate)