from __future__ import annotations
from typing import Any, Literal, Optional, Union

B2bNtsConnectionStatus = Union[Literal["NOT_CONNECTED", "PENDING_CONNECT", "CONNECTED", "PENDING_DISCONNECT", "ERROR"], str]
"""국세청 연동 상태
"""


def _serialize_b2b_nts_connection_status(obj: B2bNtsConnectionStatus) -> Any:
    if isinstance(obj, dict):
        return obj
    return obj


def _deserialize_b2b_nts_connection_status(obj: Any) -> B2bNtsConnectionStatus:
    return obj
