from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field
from ...platform.platform_partner_taxation_type import PlatformPartnerTaxationType, _deserialize_platform_partner_taxation_type, _serialize_platform_partner_taxation_type

@dataclass
class CreatePlatformPartnerBodyTypeBusiness:
    company_name: str
    """상호명
    """
    business_registration_number: str
    """사업자등록번호
    """
    representative_name: str
    """대표자 이름
    """
    taxation_type: Optional[PlatformPartnerTaxationType] = field(default=None)
    """사업자 유형

    값을 입력하지 않으면 일반 과세로 설정됩니다.
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
    company_verification_id: Optional[str] = field(default=None)
    """사업자 조회 검증 아이디
    """


def _serialize_create_platform_partner_body_type_business(obj: CreatePlatformPartnerBodyTypeBusiness) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["companyName"] = obj.company_name
    entity["businessRegistrationNumber"] = obj.business_registration_number
    entity["representativeName"] = obj.representative_name
    if obj.taxation_type is not None:
        entity["taxationType"] = _serialize_platform_partner_taxation_type(obj.taxation_type)
    if obj.company_address is not None:
        entity["companyAddress"] = obj.company_address
    if obj.business_type is not None:
        entity["businessType"] = obj.business_type
    if obj.business_class is not None:
        entity["businessClass"] = obj.business_class
    if obj.company_verification_id is not None:
        entity["companyVerificationId"] = obj.company_verification_id
    return entity


def _deserialize_create_platform_partner_body_type_business(obj: Any) -> CreatePlatformPartnerBodyTypeBusiness:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "companyName" not in obj:
        raise KeyError(f"'companyName' is not in {obj}")
    company_name = obj["companyName"]
    if not isinstance(company_name, str):
        raise ValueError(f"{repr(company_name)} is not str")
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
    if "taxationType" in obj:
        taxation_type = obj["taxationType"]
        taxation_type = _deserialize_platform_partner_taxation_type(taxation_type)
    else:
        taxation_type = None
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
    if "companyVerificationId" in obj:
        company_verification_id = obj["companyVerificationId"]
        if not isinstance(company_verification_id, str):
            raise ValueError(f"{repr(company_verification_id)} is not str")
    else:
        company_verification_id = None
    return CreatePlatformPartnerBodyTypeBusiness(company_name, business_registration_number, representative_name, taxation_type, company_address, business_type, business_class, company_verification_id)
