from __future__ import annotations
from typing import Any, Optional, Union
from ..common.one_line_address import OneLineAddress, _deserialize_one_line_address, _serialize_one_line_address
from ..common.separated_address import SeparatedAddress, _deserialize_separated_address, _serialize_separated_address

Address = Union[OneLineAddress, SeparatedAddress, dict]
"""분리 형식 주소

oneLine(한 줄 형식 주소) 필드는 항상 존재합니다.
"""


def _serialize_address(obj: Address) -> Any:
    if isinstance(obj, dict):
        return obj
    if isinstance(obj, OneLineAddress):
        return _serialize_one_line_address(obj)
    if isinstance(obj, SeparatedAddress):
        return _serialize_separated_address(obj)


def _deserialize_address(obj: Any) -> Address:
    try:
        return _deserialize_one_line_address(obj)
    except Exception:
        pass
    try:
        return _deserialize_separated_address(obj)
    except Exception:
        pass
    raise ValueError(f"{repr(obj)} is not Address")
