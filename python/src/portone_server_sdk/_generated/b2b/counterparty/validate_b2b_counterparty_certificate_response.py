from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class ValidateB2bCounterpartyCertificateResponse:
    """인증서 유효성 검증 응답 정보
    """
    is_valid: bool
    """인증서 유효 여부
    """


def _serialize_validate_b2b_counterparty_certificate_response(obj: ValidateB2bCounterpartyCertificateResponse) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["isValid"] = obj.is_valid
    return entity


def _deserialize_validate_b2b_counterparty_certificate_response(obj: Any) -> ValidateB2bCounterpartyCertificateResponse:
    if not isinstance(obj, dict):
        raise ValueError("Expected dict for obj")
    if "isValid" not in obj:
        raise KeyError("Missing required field 'isValid'")
    is_valid = obj["isValid"]
    if not isinstance(is_valid, bool):
        raise ValueError("Expected bool for is_valid")
    return ValidateB2bCounterpartyCertificateResponse(is_valid)
