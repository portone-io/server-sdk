from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field
from portone_server_sdk._generated.common.b2b_company_contact import B2bCompanyContact, _deserialize_b2b_company_contact, _serialize_b2b_company_contact

@dataclass
class UpdateB2bContactResponse:
    """담당자 정보 수정 응답
    """
    contact: B2bCompanyContact
    """담당자 정보
    """


def _serialize_update_b2b_contact_response(obj: UpdateB2bContactResponse) -> Any:
    entity = {}
    entity["contact"] = _serialize_b2b_company_contact(obj.contact)
    return entity


def _deserialize_update_b2b_contact_response(obj: Any) -> UpdateB2bContactResponse:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "contact" not in obj:
        raise KeyError(f"'contact' is not in {obj}")
    contact = obj["contact"]
    contact = _deserialize_b2b_company_contact(contact)
    return UpdateB2bContactResponse(contact)
