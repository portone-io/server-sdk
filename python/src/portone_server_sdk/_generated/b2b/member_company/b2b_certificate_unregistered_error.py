from __future__ import annotations
from typing import Any, Literal, Optional
from dataclasses import dataclass, field

@dataclass
class B2bCertificateUnregisteredError:
    """인증서가 등록되어 있지 않은 경우
    """
    type: Literal["B2B_CERTIFICATE_UNREGISTERED"] = field(repr=False)
    message: Optional[str]


def _serialize_b2b_certificate_unregistered_error(obj: B2bCertificateUnregisteredError) -> Any:
    entity = {}
    entity["type"] = "B2B_CERTIFICATE_UNREGISTERED"
    if obj.message is not None:
        entity["message"] = obj.message
    return entity


def _deserialize_b2b_certificate_unregistered_error(obj: Any) -> B2bCertificateUnregisteredError:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "type" not in obj:
        raise KeyError(f"'type' is not in {obj}")
    type = obj["type"]
    if type != "B2B_CERTIFICATE_UNREGISTERED":
        raise ValueError(f"{repr(type)} is not 'B2B_CERTIFICATE_UNREGISTERED'")
    if "message" in obj:
        message = obj["message"]
        if not isinstance(message, str):
            raise ValueError(f"{repr(message)} is not str")
    else:
        message = None
    return B2bCertificateUnregisteredError(type, message)
