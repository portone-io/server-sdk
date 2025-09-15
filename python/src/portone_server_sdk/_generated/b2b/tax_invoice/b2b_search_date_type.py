from __future__ import annotations
from typing import Any, Literal, Optional, Union

B2bSearchDateType = Union[Literal["REGISTER", "WRITE", "ISSUE"], str]
"""조회 기준
"""


def _serialize_b2b_search_date_type(obj: B2bSearchDateType) -> Any:
    if isinstance(obj, dict):
        return obj
    return obj


def _deserialize_b2b_search_date_type(obj: Any) -> B2bSearchDateType:
    return obj
