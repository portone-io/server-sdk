from __future__ import annotations
from typing import Any, Literal, Optional
from dataclasses import dataclass, field

@dataclass
class B2bCompanyAlreadyRegisteredError:
    """사업자가 이미 연동되어 있는 경우
    """
    type: Literal["B2B_COMPANY_ALREADY_REGISTERED"] = field(repr=False)
    message: Optional[str]


def _serialize_b2b_company_already_registered_error(obj: B2bCompanyAlreadyRegisteredError) -> Any:
    entity = {}
    entity["type"] = "B2B_COMPANY_ALREADY_REGISTERED"
    if obj.message is not None:
        entity["message"] = obj.message
    return entity


def _deserialize_b2b_company_already_registered_error(obj: Any) -> B2bCompanyAlreadyRegisteredError:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "type" not in obj:
        raise KeyError(f"'type' is not in {obj}")
    type = obj["type"]
    if type != "B2B_COMPANY_ALREADY_REGISTERED":
        raise ValueError(f"{repr(type)} is not 'B2B_COMPANY_ALREADY_REGISTERED'")
    if "message" in obj:
        message = obj["message"]
        if not isinstance(message, str):
            raise ValueError(f"{repr(message)} is not str")
    else:
        message = None
    return B2bCompanyAlreadyRegisteredError(type, message)
