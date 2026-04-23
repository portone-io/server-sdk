from __future__ import annotations
from typing import Any, Literal, Optional, Union

B2bCertificateType = Union[Literal["E_TAX", "PORTONE", "ETC"], str]
"""인증서 타입
"""


def _serialize_b2b_certificate_type(obj: B2bCertificateType) -> Any:
    if isinstance(obj, dict):
        return obj
    return obj


def _deserialize_b2b_certificate_type(obj: Any) -> B2bCertificateType:
    return obj
