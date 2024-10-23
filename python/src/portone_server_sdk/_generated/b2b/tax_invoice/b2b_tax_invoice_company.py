from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field
from portone_server_sdk._generated.b2b.tax_invoice.b2b_tax_invoice_contact import B2bTaxInvoiceContact, _deserialize_b2b_tax_invoice_contact, _serialize_b2b_tax_invoice_contact

@dataclass
class B2bTaxInvoiceCompany:
    brn: str
    """사업자등록번호

    `-`를 제외한 10자리
    """
    tax_registration_id: Optional[str]
    """종사업자 식별 번호

    4자리 고정
    """
    name: Optional[str]
    """상호명

    최대 200자
    """
    representative_name: Optional[str]
    """대표자 성명

    최대 100자
    """
    address: Optional[str]
    """주소

    최대 300자
    """
    business_type: Optional[str]
    """업태

    최대 100자
    """
    business_class: Optional[str]
    """종목

    최대 100자
    """
    contact: Optional[B2bTaxInvoiceContact]
    """담당자
    """


def _serialize_b2b_tax_invoice_company(obj: B2bTaxInvoiceCompany) -> Any:
    entity = {}
    entity["brn"] = obj.brn
    if obj.tax_registration_id is not None:
        entity["taxRegistrationId"] = obj.tax_registration_id
    if obj.name is not None:
        entity["name"] = obj.name
    if obj.representative_name is not None:
        entity["representativeName"] = obj.representative_name
    if obj.address is not None:
        entity["address"] = obj.address
    if obj.business_type is not None:
        entity["businessType"] = obj.business_type
    if obj.business_class is not None:
        entity["businessClass"] = obj.business_class
    if obj.contact is not None:
        entity["contact"] = _serialize_b2b_tax_invoice_contact(obj.contact)
    return entity


def _deserialize_b2b_tax_invoice_company(obj: Any) -> B2bTaxInvoiceCompany:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "brn" not in obj:
        raise KeyError(f"'brn' is not in {obj}")
    brn = obj["brn"]
    if not isinstance(brn, str):
        raise ValueError(f"{repr(brn)} is not str")
    if "taxRegistrationId" in obj:
        tax_registration_id = obj["taxRegistrationId"]
        if not isinstance(tax_registration_id, str):
            raise ValueError(f"{repr(tax_registration_id)} is not str")
    else:
        tax_registration_id = None
    if "name" in obj:
        name = obj["name"]
        if not isinstance(name, str):
            raise ValueError(f"{repr(name)} is not str")
    else:
        name = None
    if "representativeName" in obj:
        representative_name = obj["representativeName"]
        if not isinstance(representative_name, str):
            raise ValueError(f"{repr(representative_name)} is not str")
    else:
        representative_name = None
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
    if "contact" in obj:
        contact = obj["contact"]
        contact = _deserialize_b2b_tax_invoice_contact(contact)
    else:
        contact = None
    return B2bTaxInvoiceCompany(brn, tax_registration_id, name, representative_name, address, business_type, business_class, contact)
