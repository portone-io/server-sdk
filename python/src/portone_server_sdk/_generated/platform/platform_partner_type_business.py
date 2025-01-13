from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field
from ..platform.platform_partner_business_status import PlatformPartnerBusinessStatus, _deserialize_platform_partner_business_status, _serialize_platform_partner_business_status
from ..platform.platform_partner_member_company_connection_status import PlatformPartnerMemberCompanyConnectionStatus, _deserialize_platform_partner_member_company_connection_status, _serialize_platform_partner_member_company_connection_status
from ..platform.platform_partner_taxation_type import PlatformPartnerTaxationType, _deserialize_platform_partner_taxation_type, _serialize_platform_partner_taxation_type

@dataclass
class PlatformPartnerTypeBusiness:
    """사업자 파트너 정보

    사업자 유형의 파트너 추가 정보 입니다.
    """
    company_name: str
    """상호명
    """
    taxation_type: PlatformPartnerTaxationType
    """과세 유형
    """
    business_status: PlatformPartnerBusinessStatus
    """사업자 상태
    """
    business_registration_number: str
    """사업자등록번호
    """
    representative_name: str
    """대표자 이름
    """
    member_company_connection_status: PlatformPartnerMemberCompanyConnectionStatus
    """연동사업자 연동 상태
    """
    company_address: Optional[str] = field(default=None)
    """사업장 주소
    """
    business_type: Optional[str] = field(default=None)
    """업태
    """
    business_class: Optional[str] = field(default=None)
    """업종
    """
    member_company_connection_failed_reason: Optional[str] = field(default=None)
    """연동사업자 연동 실패 사유
    """


def _serialize_platform_partner_type_business(obj: PlatformPartnerTypeBusiness) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["type"] = "BUSINESS"
    entity["companyName"] = obj.company_name
    entity["taxationType"] = _serialize_platform_partner_taxation_type(obj.taxation_type)
    entity["businessStatus"] = _serialize_platform_partner_business_status(obj.business_status)
    entity["businessRegistrationNumber"] = obj.business_registration_number
    entity["representativeName"] = obj.representative_name
    entity["memberCompanyConnectionStatus"] = _serialize_platform_partner_member_company_connection_status(obj.member_company_connection_status)
    if obj.company_address is not None:
        entity["companyAddress"] = obj.company_address
    if obj.business_type is not None:
        entity["businessType"] = obj.business_type
    if obj.business_class is not None:
        entity["businessClass"] = obj.business_class
    if obj.member_company_connection_failed_reason is not None:
        entity["memberCompanyConnectionFailedReason"] = obj.member_company_connection_failed_reason
    return entity


def _deserialize_platform_partner_type_business(obj: Any) -> PlatformPartnerTypeBusiness:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "type" not in obj:
        raise KeyError(f"'type' is not in {obj}")
    type = obj["type"]
    if type != "BUSINESS":
        raise ValueError(f"{repr(type)} is not 'BUSINESS'")
    if "companyName" not in obj:
        raise KeyError(f"'companyName' is not in {obj}")
    company_name = obj["companyName"]
    if not isinstance(company_name, str):
        raise ValueError(f"{repr(company_name)} is not str")
    if "taxationType" not in obj:
        raise KeyError(f"'taxationType' is not in {obj}")
    taxation_type = obj["taxationType"]
    taxation_type = _deserialize_platform_partner_taxation_type(taxation_type)
    if "businessStatus" not in obj:
        raise KeyError(f"'businessStatus' is not in {obj}")
    business_status = obj["businessStatus"]
    business_status = _deserialize_platform_partner_business_status(business_status)
    if "businessRegistrationNumber" not in obj:
        raise KeyError(f"'businessRegistrationNumber' is not in {obj}")
    business_registration_number = obj["businessRegistrationNumber"]
    if not isinstance(business_registration_number, str):
        raise ValueError(f"{repr(business_registration_number)} is not str")
    if "representativeName" not in obj:
        raise KeyError(f"'representativeName' is not in {obj}")
    representative_name = obj["representativeName"]
    if not isinstance(representative_name, str):
        raise ValueError(f"{repr(representative_name)} is not str")
    if "memberCompanyConnectionStatus" not in obj:
        raise KeyError(f"'memberCompanyConnectionStatus' is not in {obj}")
    member_company_connection_status = obj["memberCompanyConnectionStatus"]
    member_company_connection_status = _deserialize_platform_partner_member_company_connection_status(member_company_connection_status)
    if "companyAddress" in obj:
        company_address = obj["companyAddress"]
        if not isinstance(company_address, str):
            raise ValueError(f"{repr(company_address)} is not str")
    else:
        company_address = None
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
    if "memberCompanyConnectionFailedReason" in obj:
        member_company_connection_failed_reason = obj["memberCompanyConnectionFailedReason"]
        if not isinstance(member_company_connection_failed_reason, str):
            raise ValueError(f"{repr(member_company_connection_failed_reason)} is not str")
    else:
        member_company_connection_failed_reason = None
    return PlatformPartnerTypeBusiness(company_name, taxation_type, business_status, business_registration_number, representative_name, member_company_connection_status, company_address, business_type, business_class, member_company_connection_failed_reason)
