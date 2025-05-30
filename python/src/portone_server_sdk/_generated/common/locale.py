from __future__ import annotations
from typing import Any, Literal, Optional, Union

Locale = Union[Literal["KO_KR", "EN_US", "ZH_CN", "ZH_TW", "JA_JP", "RU_RU", "TH_TH", "VI_VN"], str]
"""결제 언어
"""


def _serialize_locale(obj: Locale) -> Any:
    if isinstance(obj, dict):
        return obj
    return obj


def _deserialize_locale(obj: Any) -> Locale:
    return obj
