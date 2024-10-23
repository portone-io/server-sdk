from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class ValidateB2bCertificateResponse:
    """인증서 유효성 검증 응답 정보
    """
    is_valid: bool
    """인증서 유효 여부
    """


def _serialize_validate_b2b_certificate_response(obj: ValidateB2bCertificateResponse) -> Any:
    entity = {}
    entity["isValid"] = obj.is_valid
    return entity


def _deserialize_validate_b2b_certificate_response(obj: Any) -> ValidateB2bCertificateResponse:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "isValid" not in obj:
        raise KeyError(f"'isValid' is not in {obj}")
    is_valid = obj["isValid"]
    if not isinstance(is_valid, bool):
        raise ValueError(f"{repr(is_valid)} is not bool")
    return ValidateB2bCertificateResponse(is_valid)
