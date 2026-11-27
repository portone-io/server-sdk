from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field
from ..common.country import Country, _deserialize_country, _serialize_country

@dataclass
class SeparatedAddressInput:
    """분리 형식 주소 입력 정보
    """
    address_line_1: str
    """상세 주소 1
    """
    address_line_2: str
    """상세 주소 2
    """
    city: Optional[str] = field(default=None)
    """시/군/구
    """
    province: Optional[str] = field(default=None)
    """주/도/시
    """
    country: Optional[Country] = field(default=None)
    """국가
    """


def _serialize_separated_address_input(obj: SeparatedAddressInput) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["addressLine1"] = obj.address_line_1
    entity["addressLine2"] = obj.address_line_2
    if obj.city is not None:
        entity["city"] = obj.city
    if obj.province is not None:
        entity["province"] = obj.province
    if obj.country is not None:
        entity["country"] = _serialize_country(obj.country)
    return entity


def _deserialize_separated_address_input(obj: Any) -> SeparatedAddressInput:
    if not isinstance(obj, dict):
        raise ValueError("Expected dict for obj")
    if "addressLine1" not in obj:
        raise KeyError("Missing required field 'addressLine1'")
    address_line_1 = obj["addressLine1"]
    if not isinstance(address_line_1, str):
        raise ValueError("Expected str for address_line_1")
    if "addressLine2" not in obj:
        raise KeyError("Missing required field 'addressLine2'")
    address_line_2 = obj["addressLine2"]
    if not isinstance(address_line_2, str):
        raise ValueError("Expected str for address_line_2")
    if "city" in obj:
        city = obj["city"]
        if not isinstance(city, str):
            raise ValueError("Expected str for city")
    else:
        city = None
    if "province" in obj:
        province = obj["province"]
        if not isinstance(province, str):
            raise ValueError("Expected str for province")
    else:
        province = None
    if "country" in obj:
        country = obj["country"]
        country = _deserialize_country(country)
    else:
        country = None
    return SeparatedAddressInput(address_line_1, address_line_2, city, province, country)
