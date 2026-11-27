from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field
from ...b2b.tax_invoice.b2b_tax_invoice_contact import B2bTaxInvoiceContact, _deserialize_b2b_tax_invoice_contact, _serialize_b2b_tax_invoice_contact

@dataclass
class B2bTaxInvoiceCompany:
    brn: Optional[str] = field(default=None)
    """사업자등록번호

    `-`를 제외한 10자리
    """
    counterparty_id: Optional[str] = field(default=None)
    """거래처 ID
    """
    tax_registration_id: Optional[str] = field(default=None)
    """종사업자 식별 번호

    4자리 고정
    """
    name: Optional[str] = field(default=None)
    """상호명

    최대 200자
    """
    representative_name: Optional[str] = field(default=None)
    """대표자 성명

    최대 100자
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
    contact: Optional[B2bTaxInvoiceContact] = field(default=None)
    """담당자
    """


def _serialize_b2b_tax_invoice_company(obj: B2bTaxInvoiceCompany) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    if obj.brn is not None:
        entity["brn"] = obj.brn
    if obj.counterparty_id is not None:
        entity["counterpartyId"] = obj.counterparty_id
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
        raise ValueError("Expected dict for obj")
    if "brn" in obj:
        brn = obj["brn"]
        if not isinstance(brn, str):
            raise ValueError("Expected str for brn")
    else:
        brn = None
    if "counterpartyId" in obj:
        counterparty_id = obj["counterpartyId"]
        if not isinstance(counterparty_id, str):
            raise ValueError("Expected str for counterparty_id")
    else:
        counterparty_id = None
    if "taxRegistrationId" in obj:
        tax_registration_id = obj["taxRegistrationId"]
        if not isinstance(tax_registration_id, str):
            raise ValueError("Expected str for tax_registration_id")
    else:
        tax_registration_id = None
    if "name" in obj:
        name = obj["name"]
        if not isinstance(name, str):
            raise ValueError("Expected str for name")
    else:
        name = None
    if "representativeName" in obj:
        representative_name = obj["representativeName"]
        if not isinstance(representative_name, str):
            raise ValueError("Expected str for representative_name")
    else:
        representative_name = None
    if "address" in obj:
        address = obj["address"]
        if not isinstance(address, str):
            raise ValueError("Expected str for address")
    else:
        address = None
    if "businessType" in obj:
        business_type = obj["businessType"]
        if not isinstance(business_type, str):
            raise ValueError("Expected str for business_type")
    else:
        business_type = None
    if "businessClass" in obj:
        business_class = obj["businessClass"]
        if not isinstance(business_class, str):
            raise ValueError("Expected str for business_class")
    else:
        business_class = None
    if "contact" in obj:
        contact = obj["contact"]
        contact = _deserialize_b2b_tax_invoice_contact(contact)
    else:
        contact = None
    return B2bTaxInvoiceCompany(brn, counterparty_id, tax_registration_id, name, representative_name, address, business_type, business_class, contact)
