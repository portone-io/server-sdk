from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field
from ...b2b.counterparty.b2b_counterparty_business_status import B2bCounterpartyBusinessStatus, _deserialize_b2b_counterparty_business_status, _serialize_b2b_counterparty_business_status
from ...b2b.counterparty.b2b_counterparty_contact import B2bCounterpartyContact, _deserialize_b2b_counterparty_contact, _serialize_b2b_counterparty_contact
from ...b2b.counterparty.b2b_counterparty_verification import B2bCounterpartyVerification, _deserialize_b2b_counterparty_verification, _serialize_b2b_counterparty_verification
from ...b2b.counterparty.b2b_nts_connection_status import B2bNtsConnectionStatus, _deserialize_b2b_nts_connection_status, _serialize_b2b_nts_connection_status

@dataclass
class B2bCounterparty:
    """거래처

    B2B 거래처 정보입니다.
    """
    id: str
    """거래처 고유 아이디
    """
    graphql_id: str
    is_for_test: bool
    """테스트 모드 여부
    """
    brn: str
    """사업자등록번호

    `-` 없이 숫자로만 구성됩니다.
    """
    company_name: str
    """상호명
    """
    representative_name: str
    """대표자 성명
    """
    contact: B2bCounterpartyContact
    """담당자 정보
    """
    additional_contacts: list[B2bCounterpartyContact]
    """추가 담당자 목록

    최대 5명까지 등록할 수 있습니다.
    """
    nts_connection_status: B2bNtsConnectionStatus
    """국세청 연동 상태
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
    memo: Optional[str] = field(default=None)
    """메모
    """
    nts_connected_at: Optional[str] = field(default=None)
    """국세청 연동 시각
    (RFC 3339 date-time)
    """
    nts_connection_failed_reason: Optional[str] = field(default=None)
    """국세청 연동 실패 사유
    """
    partner_id: Optional[str] = field(default=None)
    """파트너 연동 ID

    파트너 연동 거래처인 경우에만 존재합니다.
    """
    business_status: Optional[B2bCounterpartyBusinessStatus] = field(default=None)
    """휴폐업 상태
    """
    business_status_checked_at: Optional[str] = field(default=None)
    """휴폐업 상태 확인 시각
    (RFC 3339 date-time)
    """
    business_status_verification: Optional[B2bCounterpartyVerification] = field(default=None)
    """휴폐업 상태 검증 정보
    """
    business_info_verification: Optional[B2bCounterpartyVerification] = field(default=None)
    """사업자 정보 검증 정보
    """
    applied_at: Optional[str] = field(default=None)
    """적용 시각
    (RFC 3339 date-time)
    """


def _serialize_b2b_counterparty(obj: B2bCounterparty) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["id"] = obj.id
    entity["graphqlId"] = obj.graphql_id
    entity["isForTest"] = obj.is_for_test
    entity["brn"] = obj.brn
    entity["companyName"] = obj.company_name
    entity["representativeName"] = obj.representative_name
    entity["contact"] = _serialize_b2b_counterparty_contact(obj.contact)
    entity["additionalContacts"] = list(map(_serialize_b2b_counterparty_contact, obj.additional_contacts))
    entity["ntsConnectionStatus"] = _serialize_b2b_nts_connection_status(obj.nts_connection_status)
    if obj.address is not None:
        entity["address"] = obj.address
    if obj.business_type is not None:
        entity["businessType"] = obj.business_type
    if obj.business_class is not None:
        entity["businessClass"] = obj.business_class
    if obj.memo is not None:
        entity["memo"] = obj.memo
    if obj.nts_connected_at is not None:
        entity["ntsConnectedAt"] = obj.nts_connected_at
    if obj.nts_connection_failed_reason is not None:
        entity["ntsConnectionFailedReason"] = obj.nts_connection_failed_reason
    if obj.partner_id is not None:
        entity["partnerId"] = obj.partner_id
    if obj.business_status is not None:
        entity["businessStatus"] = _serialize_b2b_counterparty_business_status(obj.business_status)
    if obj.business_status_checked_at is not None:
        entity["businessStatusCheckedAt"] = obj.business_status_checked_at
    if obj.business_status_verification is not None:
        entity["businessStatusVerification"] = _serialize_b2b_counterparty_verification(obj.business_status_verification)
    if obj.business_info_verification is not None:
        entity["businessInfoVerification"] = _serialize_b2b_counterparty_verification(obj.business_info_verification)
    if obj.applied_at is not None:
        entity["appliedAt"] = obj.applied_at
    return entity


def _deserialize_b2b_counterparty(obj: Any) -> B2bCounterparty:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "id" not in obj:
        raise KeyError(f"'id' is not in {obj}")
    id = obj["id"]
    if not isinstance(id, str):
        raise ValueError(f"{repr(id)} is not str")
    if "graphqlId" not in obj:
        raise KeyError(f"'graphqlId' is not in {obj}")
    graphql_id = obj["graphqlId"]
    if not isinstance(graphql_id, str):
        raise ValueError(f"{repr(graphql_id)} is not str")
    if "isForTest" not in obj:
        raise KeyError(f"'isForTest' is not in {obj}")
    is_for_test = obj["isForTest"]
    if not isinstance(is_for_test, bool):
        raise ValueError(f"{repr(is_for_test)} is not bool")
    if "brn" not in obj:
        raise KeyError(f"'brn' is not in {obj}")
    brn = obj["brn"]
    if not isinstance(brn, str):
        raise ValueError(f"{repr(brn)} is not str")
    if "companyName" not in obj:
        raise KeyError(f"'companyName' is not in {obj}")
    company_name = obj["companyName"]
    if not isinstance(company_name, str):
        raise ValueError(f"{repr(company_name)} is not str")
    if "representativeName" not in obj:
        raise KeyError(f"'representativeName' is not in {obj}")
    representative_name = obj["representativeName"]
    if not isinstance(representative_name, str):
        raise ValueError(f"{repr(representative_name)} is not str")
    if "contact" not in obj:
        raise KeyError(f"'contact' is not in {obj}")
    contact = obj["contact"]
    contact = _deserialize_b2b_counterparty_contact(contact)
    if "additionalContacts" not in obj:
        raise KeyError(f"'additionalContacts' is not in {obj}")
    additional_contacts = obj["additionalContacts"]
    if not isinstance(additional_contacts, list):
        raise ValueError(f"{repr(additional_contacts)} is not list")
    for i, item in enumerate(additional_contacts):
        item = _deserialize_b2b_counterparty_contact(item)
        additional_contacts[i] = item
    if "ntsConnectionStatus" not in obj:
        raise KeyError(f"'ntsConnectionStatus' is not in {obj}")
    nts_connection_status = obj["ntsConnectionStatus"]
    nts_connection_status = _deserialize_b2b_nts_connection_status(nts_connection_status)
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
    if "memo" in obj:
        memo = obj["memo"]
        if not isinstance(memo, str):
            raise ValueError(f"{repr(memo)} is not str")
    else:
        memo = None
    if "ntsConnectedAt" in obj:
        nts_connected_at = obj["ntsConnectedAt"]
        if not isinstance(nts_connected_at, str):
            raise ValueError(f"{repr(nts_connected_at)} is not str")
    else:
        nts_connected_at = None
    if "ntsConnectionFailedReason" in obj:
        nts_connection_failed_reason = obj["ntsConnectionFailedReason"]
        if not isinstance(nts_connection_failed_reason, str):
            raise ValueError(f"{repr(nts_connection_failed_reason)} is not str")
    else:
        nts_connection_failed_reason = None
    if "partnerId" in obj:
        partner_id = obj["partnerId"]
        if not isinstance(partner_id, str):
            raise ValueError(f"{repr(partner_id)} is not str")
    else:
        partner_id = None
    if "businessStatus" in obj:
        business_status = obj["businessStatus"]
        business_status = _deserialize_b2b_counterparty_business_status(business_status)
    else:
        business_status = None
    if "businessStatusCheckedAt" in obj:
        business_status_checked_at = obj["businessStatusCheckedAt"]
        if not isinstance(business_status_checked_at, str):
            raise ValueError(f"{repr(business_status_checked_at)} is not str")
    else:
        business_status_checked_at = None
    if "businessStatusVerification" in obj:
        business_status_verification = obj["businessStatusVerification"]
        business_status_verification = _deserialize_b2b_counterparty_verification(business_status_verification)
    else:
        business_status_verification = None
    if "businessInfoVerification" in obj:
        business_info_verification = obj["businessInfoVerification"]
        business_info_verification = _deserialize_b2b_counterparty_verification(business_info_verification)
    else:
        business_info_verification = None
    if "appliedAt" in obj:
        applied_at = obj["appliedAt"]
        if not isinstance(applied_at, str):
            raise ValueError(f"{repr(applied_at)} is not str")
    else:
        applied_at = None
    return B2bCounterparty(id, graphql_id, is_for_test, brn, company_name, representative_name, contact, additional_contacts, nts_connection_status, address, business_type, business_class, memo, nts_connected_at, nts_connection_failed_reason, partner_id, business_status, business_status_checked_at, business_status_verification, business_info_verification, applied_at)
