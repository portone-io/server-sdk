from __future__ import annotations
from typing import Any, Literal, Optional
from dataclasses import dataclass, field
from portone_server_sdk._generated.common.country import Country, _deserialize_country, _serialize_country

@dataclass
class SeparatedAddress:
    """분리 형식 주소

    한 줄 형식 주소와 분리 형식 주소 모두 존재합니다.
    한 줄 형식 주소는 분리 형식 주소를 이어 붙인 형태로 생성됩니다.
    """
    type: Literal["SEPARATED"] = field(repr=False)
    one_line: str
    """주소 (한 줄)
    """
    address_line_1: str
    """상세 주소 1
    """
    address_line_2: str
    """상세 주소 2
    """
    city: Optional[str]
    """시/군/구
    """
    province: Optional[str]
    """주/도/시
    """
    country: Optional[Country]
    """국가
    """


def _serialize_separated_address(obj: SeparatedAddress) -> Any:
    entity = {}
    entity["type"] = "SEPARATED"
    entity["oneLine"] = obj.one_line
    entity["addressLine1"] = obj.address_line_1
    entity["addressLine2"] = obj.address_line_2
    if obj.city is not None:
        entity["city"] = obj.city
    if obj.province is not None:
        entity["province"] = obj.province
    if obj.country is not None:
        entity["country"] = _serialize_country(obj.country)
    return entity


def _deserialize_separated_address(obj: Any) -> SeparatedAddress:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "type" not in obj:
        raise KeyError(f"'type' is not in {obj}")
    type = obj["type"]
    if type != "SEPARATED":
        raise ValueError(f"{repr(type)} is not 'SEPARATED'")
    if "oneLine" not in obj:
        raise KeyError(f"'oneLine' is not in {obj}")
    one_line = obj["oneLine"]
    if not isinstance(one_line, str):
        raise ValueError(f"{repr(one_line)} is not str")
    if "addressLine1" not in obj:
        raise KeyError(f"'addressLine1' is not in {obj}")
    address_line_1 = obj["addressLine1"]
    if not isinstance(address_line_1, str):
        raise ValueError(f"{repr(address_line_1)} is not str")
    if "addressLine2" not in obj:
        raise KeyError(f"'addressLine2' is not in {obj}")
    address_line_2 = obj["addressLine2"]
    if not isinstance(address_line_2, str):
        raise ValueError(f"{repr(address_line_2)} is not str")
    if "city" in obj:
        city = obj["city"]
        if not isinstance(city, str):
            raise ValueError(f"{repr(city)} is not str")
    else:
        city = None
    if "province" in obj:
        province = obj["province"]
        if not isinstance(province, str):
            raise ValueError(f"{repr(province)} is not str")
    else:
        province = None
    if "country" in obj:
        country = obj["country"]
        country = _deserialize_country(country)
    else:
        country = None
    return SeparatedAddress(type, one_line, address_line_1, address_line_2, city, province, country)
