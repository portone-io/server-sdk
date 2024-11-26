from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field
from ..common.card_brand import CardBrand, _deserialize_card_brand, _serialize_card_brand
from ..common.card_owner_type import CardOwnerType, _deserialize_card_owner_type, _serialize_card_owner_type
from ..common.card_type import CardType, _deserialize_card_type, _serialize_card_type

@dataclass
class Card:
    """카드 상세 정보
    """
    publisher: Optional[str] = field(default=None)
    """발행사 코드
    """
    issuer: Optional[str] = field(default=None)
    """발급사 코드
    """
    brand: Optional[CardBrand] = field(default=None)
    """카드 브랜드
    """
    type: Optional[CardType] = field(default=None)
    """카드 유형
    """
    owner_type: Optional[CardOwnerType] = field(default=None)
    """카드 소유주 유형
    """
    bin: Optional[str] = field(default=None)
    """카드 번호 앞 6자리 또는 8자리의 BIN (Bank Identification Number)
    """
    name: Optional[str] = field(default=None)
    """카드 상품명
    """
    number: Optional[str] = field(default=None)
    """마스킹된 카드 번호
    """


def _serialize_card(obj: Card) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    if obj.publisher is not None:
        entity["publisher"] = obj.publisher
    if obj.issuer is not None:
        entity["issuer"] = obj.issuer
    if obj.brand is not None:
        entity["brand"] = _serialize_card_brand(obj.brand)
    if obj.type is not None:
        entity["type"] = _serialize_card_type(obj.type)
    if obj.owner_type is not None:
        entity["ownerType"] = _serialize_card_owner_type(obj.owner_type)
    if obj.bin is not None:
        entity["bin"] = obj.bin
    if obj.name is not None:
        entity["name"] = obj.name
    if obj.number is not None:
        entity["number"] = obj.number
    return entity


def _deserialize_card(obj: Any) -> Card:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "publisher" in obj:
        publisher = obj["publisher"]
        if not isinstance(publisher, str):
            raise ValueError(f"{repr(publisher)} is not str")
    else:
        publisher = None
    if "issuer" in obj:
        issuer = obj["issuer"]
        if not isinstance(issuer, str):
            raise ValueError(f"{repr(issuer)} is not str")
    else:
        issuer = None
    if "brand" in obj:
        brand = obj["brand"]
        brand = _deserialize_card_brand(brand)
    else:
        brand = None
    if "type" in obj:
        type = obj["type"]
        type = _deserialize_card_type(type)
    else:
        type = None
    if "ownerType" in obj:
        owner_type = obj["ownerType"]
        owner_type = _deserialize_card_owner_type(owner_type)
    else:
        owner_type = None
    if "bin" in obj:
        bin = obj["bin"]
        if not isinstance(bin, str):
            raise ValueError(f"{repr(bin)} is not str")
    else:
        bin = None
    if "name" in obj:
        name = obj["name"]
        if not isinstance(name, str):
            raise ValueError(f"{repr(name)} is not str")
    else:
        name = None
    if "number" in obj:
        number = obj["number"]
        if not isinstance(number, str):
            raise ValueError(f"{repr(number)} is not str")
    else:
        number = None
    return Card(publisher, issuer, brand, type, owner_type, bin, name, number)
