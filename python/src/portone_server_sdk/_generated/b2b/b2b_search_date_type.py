from __future__ import annotations
from typing import Any, Literal, Optional

B2bSearchDateType = Literal["REGISTER", "WRITE", "ISSUE"]
"""조회 기준
"""


def _serialize_b2b_search_date_type(obj: B2bSearchDateType) -> Any:
    return obj


def _deserialize_b2b_search_date_type(obj: Any) -> B2bSearchDateType:
    if obj not in ["REGISTER", "WRITE", "ISSUE"]:
        raise ValueError(f"{repr(obj)} is not B2bSearchDateType")
    return obj
