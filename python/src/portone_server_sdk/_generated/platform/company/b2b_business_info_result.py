from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field
from ...platform.company.b2b_business_info import B2bBusinessInfo, _deserialize_b2b_business_info, _serialize_b2b_business_info

@dataclass
class B2bBusinessInfoResult:
    """사업자등록 정보조회 결과
    """
    brn: str
    """사업자등록번호
    """
    business_info: Optional[B2bBusinessInfo] = field(default=None)
    """사업자등록 정보
    """
    error: Optional[str] = field(default=None)
    """조회 실패 시 에러 메시지
    """
    verification_id: Optional[str] = field(default=None)
    """조회 결과 ID

    거래처 생성/수정 시 사업자 정보 조회 결과를 재사용하기 위한 ID입니다. 조회 성공 시에만 설정됩니다.
    """


def _serialize_b2b_business_info_result(obj: B2bBusinessInfoResult) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["brn"] = obj.brn
    if obj.business_info is not None:
        entity["businessInfo"] = _serialize_b2b_business_info(obj.business_info)
    if obj.error is not None:
        entity["error"] = obj.error
    if obj.verification_id is not None:
        entity["verificationId"] = obj.verification_id
    return entity


def _deserialize_b2b_business_info_result(obj: Any) -> B2bBusinessInfoResult:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "brn" not in obj:
        raise KeyError(f"'brn' is not in {obj}")
    brn = obj["brn"]
    if not isinstance(brn, str):
        raise ValueError(f"{repr(brn)} is not str")
    if "businessInfo" in obj:
        business_info = obj["businessInfo"]
        business_info = _deserialize_b2b_business_info(business_info)
    else:
        business_info = None
    if "error" in obj:
        error = obj["error"]
        if not isinstance(error, str):
            raise ValueError(f"{repr(error)} is not str")
    else:
        error = None
    if "verificationId" in obj:
        verification_id = obj["verificationId"]
        if not isinstance(verification_id, str):
            raise ValueError(f"{repr(verification_id)} is not str")
    else:
        verification_id = None
    return B2bBusinessInfoResult(brn, business_info, error, verification_id)
