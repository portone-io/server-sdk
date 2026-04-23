from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class B2bCounterpartyCreateOptions:
    """거래처 생성 옵션
    """
    check_business_info: Optional[bool] = field(default=None)
    """사업자 정보 조회 여부

    true인 경우 사업자 정보를 조회하여 거래처에 반영합니다.
    """
    check_business_status: Optional[bool] = field(default=None)
    """휴폐업 상태 조회 여부

    true인 경우 휴폐업 상태를 조회하여 거래처에 반영합니다.
    """
    business_info_verification_id: Optional[str] = field(default=None)
    """사업자 정보 조회 결과 ID

    이전에 조회한 사업자 정보 조회 결과의 ID를 입력하면 재조회 없이 해당 결과를 사용합니다.
    """
    business_status_verification_id: Optional[str] = field(default=None)
    """휴폐업 상태 조회 결과 ID

    이전에 조회한 휴폐업 상태 조회 결과의 ID를 입력하면 재조회 없이 해당 결과를 사용합니다.
    """


def _serialize_b2b_counterparty_create_options(obj: B2bCounterpartyCreateOptions) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    if obj.check_business_info is not None:
        entity["checkBusinessInfo"] = obj.check_business_info
    if obj.check_business_status is not None:
        entity["checkBusinessStatus"] = obj.check_business_status
    if obj.business_info_verification_id is not None:
        entity["businessInfoVerificationId"] = obj.business_info_verification_id
    if obj.business_status_verification_id is not None:
        entity["businessStatusVerificationId"] = obj.business_status_verification_id
    return entity


def _deserialize_b2b_counterparty_create_options(obj: Any) -> B2bCounterpartyCreateOptions:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "checkBusinessInfo" in obj:
        check_business_info = obj["checkBusinessInfo"]
        if not isinstance(check_business_info, bool):
            raise ValueError(f"{repr(check_business_info)} is not bool")
    else:
        check_business_info = None
    if "checkBusinessStatus" in obj:
        check_business_status = obj["checkBusinessStatus"]
        if not isinstance(check_business_status, bool):
            raise ValueError(f"{repr(check_business_status)} is not bool")
    else:
        check_business_status = None
    if "businessInfoVerificationId" in obj:
        business_info_verification_id = obj["businessInfoVerificationId"]
        if not isinstance(business_info_verification_id, str):
            raise ValueError(f"{repr(business_info_verification_id)} is not str")
    else:
        business_info_verification_id = None
    if "businessStatusVerificationId" in obj:
        business_status_verification_id = obj["businessStatusVerificationId"]
        if not isinstance(business_status_verification_id, str):
            raise ValueError(f"{repr(business_status_verification_id)} is not str")
    else:
        business_status_verification_id = None
    return B2bCounterpartyCreateOptions(check_business_info, check_business_status, business_info_verification_id, business_status_verification_id)
