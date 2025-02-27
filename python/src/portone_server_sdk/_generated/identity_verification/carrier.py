from __future__ import annotations
from typing import Any, Literal, Optional, Union

Carrier = Union[Literal["SKT", "KT", "LGU", "SKT_MVNO", "KT_MVNO", "LGU_MVNO"], str]
"""통신사
"""


def _serialize_carrier(obj: Carrier) -> Any:
    if isinstance(obj, dict):
        return obj
    return obj


def _deserialize_carrier(obj: Any) -> Carrier:
    return obj
