from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class SendIdentityVerificationBodyCustomer:
    """본인인증 요청을 위한 고객 정보
    """
    name: str
    """이름
    """
    phone_number: str
    """전화번호

    특수 문자(-) 없이 숫자만 입력합니다.
    """
    ip_address: str
    """IP 주소

    고객의 요청 속도 제한에 사용됩니다.
    """
    id: Optional[str] = field(default=None)
    """식별 아이디
    """
    identity_number: Optional[str] = field(default=None)
    """주민등록번호 앞 7자리

    SMS 방식의 경우 필수로 입력합니다.
    """


def _serialize_send_identity_verification_body_customer(obj: SendIdentityVerificationBodyCustomer) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["name"] = obj.name
    entity["phoneNumber"] = obj.phone_number
    entity["ipAddress"] = obj.ip_address
    if obj.id is not None:
        entity["id"] = obj.id
    if obj.identity_number is not None:
        entity["identityNumber"] = obj.identity_number
    return entity


def _deserialize_send_identity_verification_body_customer(obj: Any) -> SendIdentityVerificationBodyCustomer:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "name" not in obj:
        raise KeyError(f"'name' is not in {obj}")
    name = obj["name"]
    if not isinstance(name, str):
        raise ValueError(f"{repr(name)} is not str")
    if "phoneNumber" not in obj:
        raise KeyError(f"'phoneNumber' is not in {obj}")
    phone_number = obj["phoneNumber"]
    if not isinstance(phone_number, str):
        raise ValueError(f"{repr(phone_number)} is not str")
    if "ipAddress" not in obj:
        raise KeyError(f"'ipAddress' is not in {obj}")
    ip_address = obj["ipAddress"]
    if not isinstance(ip_address, str):
        raise ValueError(f"{repr(ip_address)} is not str")
    if "id" in obj:
        id = obj["id"]
        if not isinstance(id, str):
            raise ValueError(f"{repr(id)} is not str")
    else:
        id = None
    if "identityNumber" in obj:
        identity_number = obj["identityNumber"]
        if not isinstance(identity_number, str):
            raise ValueError(f"{repr(identity_number)} is not str")
    else:
        identity_number = None
    return SendIdentityVerificationBodyCustomer(name, phone_number, ip_address, id, identity_number)
