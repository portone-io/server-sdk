from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field
from portone_server_sdk._generated.common.customer_separated_name import CustomerSeparatedName, _deserialize_customer_separated_name, _serialize_customer_separated_name

@dataclass
class CustomerNameInput:
    """고객 이름 입력 정보

    두 개의 이름 형식 중 한 가지만 선택하여 입력해주세요.
    """
    full: Optional[str]
    """한 줄 이름 형식
    """
    separated: Optional[CustomerSeparatedName]
    """분리형 이름 형식
    """


def _serialize_customer_name_input(obj: CustomerNameInput) -> Any:
    entity = {}
    if obj.full is not None:
        entity["full"] = obj.full
    if obj.separated is not None:
        entity["separated"] = _serialize_customer_separated_name(obj.separated)
    return entity


def _deserialize_customer_name_input(obj: Any) -> CustomerNameInput:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "full" in obj:
        full = obj["full"]
        if not isinstance(full, str):
            raise ValueError(f"{repr(full)} is not str")
    else:
        full = None
    if "separated" in obj:
        separated = obj["separated"]
        separated = _deserialize_customer_separated_name(separated)
    else:
        separated = None
    return CustomerNameInput(full, separated)
