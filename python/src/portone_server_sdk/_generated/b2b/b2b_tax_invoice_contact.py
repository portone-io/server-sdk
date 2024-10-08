from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class B2bTaxInvoiceContact:
    """세금계산서 담당자
    """
    name: Optional[str]
    """성명
    """
    department: Optional[str]
    """부서
    """
    phone_number: Optional[str]
    """전화번호
    """
    mobile_phone_number: Optional[str]
    """휴대전화번호
    """
    email: Optional[str]
    """이메일
    """


def _serialize_b2b_tax_invoice_contact(obj: B2bTaxInvoiceContact) -> Any:
    entity = {}
    if obj.name is not None:
        entity["name"] = obj.name
    if obj.department is not None:
        entity["department"] = obj.department
    if obj.phone_number is not None:
        entity["phoneNumber"] = obj.phone_number
    if obj.mobile_phone_number is not None:
        entity["mobilePhoneNumber"] = obj.mobile_phone_number
    if obj.email is not None:
        entity["email"] = obj.email
    return entity


def _deserialize_b2b_tax_invoice_contact(obj: Any) -> B2bTaxInvoiceContact:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "name" in obj:
        name = obj["name"]
        if not isinstance(name, str):
            raise ValueError(f"{repr(name)} is not str")
    else:
        name = None
    if "department" in obj:
        department = obj["department"]
        if not isinstance(department, str):
            raise ValueError(f"{repr(department)} is not str")
    else:
        department = None
    if "phoneNumber" in obj:
        phone_number = obj["phoneNumber"]
        if not isinstance(phone_number, str):
            raise ValueError(f"{repr(phone_number)} is not str")
    else:
        phone_number = None
    if "mobilePhoneNumber" in obj:
        mobile_phone_number = obj["mobilePhoneNumber"]
        if not isinstance(mobile_phone_number, str):
            raise ValueError(f"{repr(mobile_phone_number)} is not str")
    else:
        mobile_phone_number = None
    if "email" in obj:
        email = obj["email"]
        if not isinstance(email, str):
            raise ValueError(f"{repr(email)} is not str")
    else:
        email = None
    return B2bTaxInvoiceContact(name, department, phone_number, mobile_phone_number, email)
