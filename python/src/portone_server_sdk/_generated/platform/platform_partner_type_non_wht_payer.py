from __future__ import annotations
from typing import Any, Literal, Optional
from dataclasses import dataclass, field

@dataclass
class PlatformPartnerTypeNonWhtPayer:
    """원천징수 비대상자 파트너 정보

    비사업자 유형의 파트너 추가 정보 입니다.
    """
    type: Literal["NON_WHT_PAYER"] = field(repr=False)
    birthdate: Optional[str]
    """생년월일

    날짜를 나타내는 문자열로, `yyyy-MM-dd` 형식을 따릅니다.
    """


def _serialize_platform_partner_type_non_wht_payer(obj: PlatformPartnerTypeNonWhtPayer) -> Any:
    entity = {}
    entity["type"] = "NON_WHT_PAYER"
    if obj.birthdate is not None:
        entity["birthdate"] = obj.birthdate
    return entity


def _deserialize_platform_partner_type_non_wht_payer(obj: Any) -> PlatformPartnerTypeNonWhtPayer:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "type" not in obj:
        raise KeyError(f"'type' is not in {obj}")
    type = obj["type"]
    if type != "NON_WHT_PAYER":
        raise ValueError(f"{repr(type)} is not 'NON_WHT_PAYER'")
    if "birthdate" in obj:
        birthdate = obj["birthdate"]
        if not isinstance(birthdate, str):
            raise ValueError(f"{repr(birthdate)} is not str")
    else:
        birthdate = None
    return PlatformPartnerTypeNonWhtPayer(type, birthdate)
