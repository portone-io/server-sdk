from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field
from ...b2b.counterparty.b2b_counterparty_business_status import B2bCounterpartyBusinessStatus, _deserialize_b2b_counterparty_business_status, _serialize_b2b_counterparty_business_status
from ...b2b.counterparty.b2b_nts_connection_status import B2bNtsConnectionStatus, _deserialize_b2b_nts_connection_status, _serialize_b2b_nts_connection_status

@dataclass
class B2bCounterpartyFilter:
    """거래처 검색 필터
    """
    id: Optional[str] = field(default=None)
    """거래처 ID

    prefix 검색
    """
    brn: Optional[str] = field(default=None)
    """사업자등록번호
    """
    company_name: Optional[str] = field(default=None)
    """거래처명

    포함 검색
    """
    representative_name: Optional[str] = field(default=None)
    """대표자명
    """
    contact_name: Optional[str] = field(default=None)
    """담당자 이름
    """
    contact_phone: Optional[str] = field(default=None)
    """담당자 전화번호
    """
    contact_email: Optional[str] = field(default=None)
    """담당자 이메일
    """
    business_statuses: Optional[list[B2bCounterpartyBusinessStatus]] = field(default=None)
    """휴폐업 상태
    """
    nts_connection_statuses: Optional[list[B2bNtsConnectionStatus]] = field(default=None)
    """국세청 연동 상태
    """
    counterparty_ids: Optional[list[str]] = field(default=None)
    """거래처 ID 목록

    특정 ID 목록으로 필터링
    """


def _serialize_b2b_counterparty_filter(obj: B2bCounterpartyFilter) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    if obj.id is not None:
        entity["id"] = obj.id
    if obj.brn is not None:
        entity["brn"] = obj.brn
    if obj.company_name is not None:
        entity["companyName"] = obj.company_name
    if obj.representative_name is not None:
        entity["representativeName"] = obj.representative_name
    if obj.contact_name is not None:
        entity["contactName"] = obj.contact_name
    if obj.contact_phone is not None:
        entity["contactPhone"] = obj.contact_phone
    if obj.contact_email is not None:
        entity["contactEmail"] = obj.contact_email
    if obj.business_statuses is not None:
        entity["businessStatuses"] = list(map(_serialize_b2b_counterparty_business_status, obj.business_statuses))
    if obj.nts_connection_statuses is not None:
        entity["ntsConnectionStatuses"] = list(map(_serialize_b2b_nts_connection_status, obj.nts_connection_statuses))
    if obj.counterparty_ids is not None:
        entity["counterpartyIds"] = obj.counterparty_ids
    return entity


def _deserialize_b2b_counterparty_filter(obj: Any) -> B2bCounterpartyFilter:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "id" in obj:
        id = obj["id"]
        if not isinstance(id, str):
            raise ValueError(f"{repr(id)} is not str")
    else:
        id = None
    if "brn" in obj:
        brn = obj["brn"]
        if not isinstance(brn, str):
            raise ValueError(f"{repr(brn)} is not str")
    else:
        brn = None
    if "companyName" in obj:
        company_name = obj["companyName"]
        if not isinstance(company_name, str):
            raise ValueError(f"{repr(company_name)} is not str")
    else:
        company_name = None
    if "representativeName" in obj:
        representative_name = obj["representativeName"]
        if not isinstance(representative_name, str):
            raise ValueError(f"{repr(representative_name)} is not str")
    else:
        representative_name = None
    if "contactName" in obj:
        contact_name = obj["contactName"]
        if not isinstance(contact_name, str):
            raise ValueError(f"{repr(contact_name)} is not str")
    else:
        contact_name = None
    if "contactPhone" in obj:
        contact_phone = obj["contactPhone"]
        if not isinstance(contact_phone, str):
            raise ValueError(f"{repr(contact_phone)} is not str")
    else:
        contact_phone = None
    if "contactEmail" in obj:
        contact_email = obj["contactEmail"]
        if not isinstance(contact_email, str):
            raise ValueError(f"{repr(contact_email)} is not str")
    else:
        contact_email = None
    if "businessStatuses" in obj:
        business_statuses = obj["businessStatuses"]
        if not isinstance(business_statuses, list):
            raise ValueError(f"{repr(business_statuses)} is not list")
        for i, item in enumerate(business_statuses):
            item = _deserialize_b2b_counterparty_business_status(item)
            business_statuses[i] = item
    else:
        business_statuses = None
    if "ntsConnectionStatuses" in obj:
        nts_connection_statuses = obj["ntsConnectionStatuses"]
        if not isinstance(nts_connection_statuses, list):
            raise ValueError(f"{repr(nts_connection_statuses)} is not list")
        for i, item in enumerate(nts_connection_statuses):
            item = _deserialize_b2b_nts_connection_status(item)
            nts_connection_statuses[i] = item
    else:
        nts_connection_statuses = None
    if "counterpartyIds" in obj:
        counterparty_ids = obj["counterpartyIds"]
        if not isinstance(counterparty_ids, list):
            raise ValueError(f"{repr(counterparty_ids)} is not list")
        for i, item in enumerate(counterparty_ids):
            if not isinstance(item, str):
                raise ValueError(f"{repr(item)} is not str")
    else:
        counterparty_ids = None
    return B2bCounterpartyFilter(id, brn, company_name, representative_name, contact_name, contact_phone, contact_email, business_statuses, nts_connection_statuses, counterparty_ids)
