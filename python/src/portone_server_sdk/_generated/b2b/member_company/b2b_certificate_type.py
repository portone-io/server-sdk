from __future__ import annotations
from typing import Any, Literal, Optional

B2bCertificateType = Literal["E_TAX", "PORTONE", "ETC"]
"""인증서 타입
"""


def _serialize_b2b_certificate_type(obj: B2bCertificateType) -> Any:
    return obj


def _deserialize_b2b_certificate_type(obj: Any) -> B2bCertificateType:
    if obj not in ["E_TAX", "PORTONE", "ETC"]:
        raise ValueError(f"{repr(obj)} is not B2bCertificateType")
    return obj
