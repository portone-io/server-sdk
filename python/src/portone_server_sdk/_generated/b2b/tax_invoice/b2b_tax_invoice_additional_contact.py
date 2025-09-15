from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class B2bTaxInvoiceAdditionalContact:
    """추가 담당자
    """
    email: str
    """이메일
    """
    name: Optional[str] = field(default=None)
    """성명

    최대 100자
    """


def _serialize_b2b_tax_invoice_additional_contact(obj: B2bTaxInvoiceAdditionalContact) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["email"] = obj.email
    if obj.name is not None:
        entity["name"] = obj.name
    return entity


def _deserialize_b2b_tax_invoice_additional_contact(obj: Any) -> B2bTaxInvoiceAdditionalContact:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "email" not in obj:
        raise KeyError(f"'email' is not in {obj}")
    email = obj["email"]
    if not isinstance(email, str):
        raise ValueError(f"{repr(email)} is not str")
    if "name" in obj:
        name = obj["name"]
        if not isinstance(name, str):
            raise ValueError(f"{repr(name)} is not str")
    else:
        name = None
    return B2bTaxInvoiceAdditionalContact(email, name)
