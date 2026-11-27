from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class PaymentSessionColors:
    """체크아웃 페이지 색 설정
    """
    primary: Optional[str] = field(default=None)
    """주 색상

    CSS 색 문자열 형식
    """
    primary_hover: Optional[str] = field(default=None)
    """호버 주 색상

    CSS 색 문자열 형식
    """
    primary_light: Optional[str] = field(default=None)
    """밝은 주 색상

    CSS 색 문자열 형식
    """


def _serialize_payment_session_colors(obj: PaymentSessionColors) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    if obj.primary is not None:
        entity["primary"] = obj.primary
    if obj.primary_hover is not None:
        entity["primaryHover"] = obj.primary_hover
    if obj.primary_light is not None:
        entity["primaryLight"] = obj.primary_light
    return entity


def _deserialize_payment_session_colors(obj: Any) -> PaymentSessionColors:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "primary" in obj:
        primary = obj["primary"]
        if not isinstance(primary, str):
            raise ValueError(f"{repr(primary)} is not str")
    else:
        primary = None
    if "primaryHover" in obj:
        primary_hover = obj["primaryHover"]
        if not isinstance(primary_hover, str):
            raise ValueError(f"{repr(primary_hover)} is not str")
    else:
        primary_hover = None
    if "primaryLight" in obj:
        primary_light = obj["primaryLight"]
        if not isinstance(primary_light, str):
            raise ValueError(f"{repr(primary_light)} is not str")
    else:
        primary_light = None
    return PaymentSessionColors(primary, primary_hover, primary_light)
