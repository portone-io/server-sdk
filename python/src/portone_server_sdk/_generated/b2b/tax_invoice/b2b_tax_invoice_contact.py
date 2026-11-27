from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class B2bTaxInvoiceContact:
    """세금계산서 담당자
    """
    email: str
    """이메일
    """
    name: Optional[str] = field(default=None)
    """성명
    """
    department: Optional[str] = field(default=None)
    """부서
    """
    phone_number: Optional[str] = field(default=None)
    """전화번호
    """
    mobile_phone_number: Optional[str] = field(default=None)
    """휴대전화번호
    """


def _serialize_b2b_tax_invoice_contact(obj: B2bTaxInvoiceContact) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["email"] = obj.email
    if obj.name is not None:
        entity["name"] = obj.name
    if obj.department is not None:
        entity["department"] = obj.department
    if obj.phone_number is not None:
        entity["phoneNumber"] = obj.phone_number
    if obj.mobile_phone_number is not None:
        entity["mobilePhoneNumber"] = obj.mobile_phone_number
    return entity


def _deserialize_b2b_tax_invoice_contact(obj: Any) -> B2bTaxInvoiceContact:
    if not isinstance(obj, dict):
        raise ValueError("Expected dict for obj")
    if "email" not in obj:
        raise KeyError("Missing required field 'email'")
    email = obj["email"]
    if not isinstance(email, str):
        raise ValueError("Expected str for email")
    if "name" in obj:
        name = obj["name"]
        if not isinstance(name, str):
            raise ValueError("Expected str for name")
    else:
        name = None
    if "department" in obj:
        department = obj["department"]
        if not isinstance(department, str):
            raise ValueError("Expected str for department")
    else:
        department = None
    if "phoneNumber" in obj:
        phone_number = obj["phoneNumber"]
        if not isinstance(phone_number, str):
            raise ValueError("Expected str for phone_number")
    else:
        phone_number = None
    if "mobilePhoneNumber" in obj:
        mobile_phone_number = obj["mobilePhoneNumber"]
        if not isinstance(mobile_phone_number, str):
            raise ValueError("Expected str for mobile_phone_number")
    else:
        mobile_phone_number = None
    return B2bTaxInvoiceContact(email, name, department, phone_number, mobile_phone_number)
