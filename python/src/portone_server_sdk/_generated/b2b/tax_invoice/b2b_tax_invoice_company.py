from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field
from ...b2b.tax_invoice.b2b_tax_invoice_contact import B2bTaxInvoiceContact, _deserialize_b2b_tax_invoice_contact, _serialize_b2b_tax_invoice_contact

@dataclass
class B2bTaxInvoiceCompany:
    brn: str
    """사업자등록번호

    `-`를 제외한 10자리
    """
    name: str
    """상호명

    최대 200자
    """
    representative_name: str
    """대표자 성명

    최대 100자
    """
    contact: B2bTaxInvoiceContact
    """담당자
    """
    tax_registration_id: Optional[str] = field(default=None)
    """종사업자 식별 번호

    4자리 고정
    """
    address: Optional[str] = field(default=None)
    """주소

    최대 300자
    """
    business_type: Optional[str] = field(default=None)
    """업태

    최대 100자
    """
    business_class: Optional[str] = field(default=None)
    """종목

    최대 100자
    """


def _serialize_b2b_tax_invoice_company(obj: B2bTaxInvoiceCompany) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["brn"] = obj.brn
    entity["name"] = obj.name
    entity["representativeName"] = obj.representative_name
    entity["contact"] = _serialize_b2b_tax_invoice_contact(obj.contact)
    if obj.tax_registration_id is not None:
        entity["taxRegistrationId"] = obj.tax_registration_id
    if obj.address is not None:
        entity["address"] = obj.address
    if obj.business_type is not None:
        entity["businessType"] = obj.business_type
    if obj.business_class is not None:
        entity["businessClass"] = obj.business_class
    return entity


def _deserialize_b2b_tax_invoice_company(obj: Any) -> B2bTaxInvoiceCompany:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "brn" not in obj:
        raise KeyError(f"'brn' is not in {obj}")
    brn = obj["brn"]
    if not isinstance(brn, str):
        raise ValueError(f"{repr(brn)} is not str")
    if "name" not in obj:
        raise KeyError(f"'name' is not in {obj}")
    name = obj["name"]
    if not isinstance(name, str):
        raise ValueError(f"{repr(name)} is not str")
    if "representativeName" not in obj:
        raise KeyError(f"'representativeName' is not in {obj}")
    representative_name = obj["representativeName"]
    if not isinstance(representative_name, str):
        raise ValueError(f"{repr(representative_name)} is not str")
    if "contact" not in obj:
        raise KeyError(f"'contact' is not in {obj}")
    contact = obj["contact"]
    contact = _deserialize_b2b_tax_invoice_contact(contact)
    if "taxRegistrationId" in obj:
        tax_registration_id = obj["taxRegistrationId"]
        if not isinstance(tax_registration_id, str):
            raise ValueError(f"{repr(tax_registration_id)} is not str")
    else:
        tax_registration_id = None
    if "address" in obj:
        address = obj["address"]
        if not isinstance(address, str):
            raise ValueError(f"{repr(address)} is not str")
    else:
        address = None
    if "businessType" in obj:
        business_type = obj["businessType"]
        if not isinstance(business_type, str):
            raise ValueError(f"{repr(business_type)} is not str")
    else:
        business_type = None
    if "businessClass" in obj:
        business_class = obj["businessClass"]
        if not isinstance(business_class, str):
            raise ValueError(f"{repr(business_class)} is not str")
    else:
        business_class = None
    return B2bTaxInvoiceCompany(brn, name, representative_name, contact, tax_registration_id, address, business_type, business_class)
