from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field
from ...b2b.counterparty.b2b_counterparty_contact_input import B2bCounterpartyContactInput, _deserialize_b2b_counterparty_contact_input, _serialize_b2b_counterparty_contact_input

@dataclass
class B2bCounterpartyInput:
    """거래처 입력 정보
    """
    brn: str
    """사업자등록번호

    `-` 없이 숫자로만 구성됩니다.
    """
    name: Optional[str] = field(default=None)
    """거래처명
    """
    representative_name: Optional[str] = field(default=None)
    """대표자 성명
    """
    address: Optional[str] = field(default=None)
    """주소
    """
    business_type: Optional[str] = field(default=None)
    """업태
    """
    business_class: Optional[str] = field(default=None)
    """업종
    """
    contact: Optional[B2bCounterpartyContactInput] = field(default=None)
    """담당자 정보
    """
    additional_contacts: Optional[list[B2bCounterpartyContactInput]] = field(default=None)
    """추가 담당자 목록

    최대 5명까지 등록할 수 있습니다.
    """
    memo: Optional[str] = field(default=None)
    """메모
    """


def _serialize_b2b_counterparty_input(obj: B2bCounterpartyInput) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["brn"] = obj.brn
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
        entity["contact"] = _serialize_b2b_counterparty_contact_input(obj.contact)
    if obj.additional_contacts is not None:
        entity["additionalContacts"] = list(map(_serialize_b2b_counterparty_contact_input, obj.additional_contacts))
    if obj.memo is not None:
        entity["memo"] = obj.memo
    return entity


def _deserialize_b2b_counterparty_input(obj: Any) -> B2bCounterpartyInput:
    if not isinstance(obj, dict):
        raise ValueError("Expected dict for obj")
    if "brn" not in obj:
        raise KeyError("Missing required field 'brn'")
    brn = obj["brn"]
    if not isinstance(brn, str):
        raise ValueError("Expected str for brn")
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
        contact = _deserialize_b2b_counterparty_contact_input(contact)
    else:
        contact = None
    if "additionalContacts" in obj:
        additional_contacts = obj["additionalContacts"]
        if not isinstance(additional_contacts, list):
            raise ValueError("Expected list for additional_contacts")
        for i, item in enumerate(additional_contacts):
            item = _deserialize_b2b_counterparty_contact_input(item)
            additional_contacts[i] = item
    else:
        additional_contacts = None
    if "memo" in obj:
        memo = obj["memo"]
        if not isinstance(memo, str):
            raise ValueError("Expected str for memo")
    else:
        memo = None
    return B2bCounterpartyInput(brn, name, representative_name, address, business_type, business_class, contact, additional_contacts, memo)
