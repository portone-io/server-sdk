from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class PlatformPartnerFilterInputKeyword:
    """파트너 검색 키워드 입력 정보

    검색 키워드 적용을 위한 옵션으로, 명시된 키워드를 포함하는 파트너만 조회합니다. 하나의 하위 필드에만 값을 명시하여 요청합니다.
    """
    id: Optional[str] = field(default=None)
    """해당 값이 포함된 id 를 가진 파트너만 조회합니다.
    """
    name: Optional[str] = field(default=None)
    """해당 값이 포함된 이름 을 가진 파트너만 조회합니다.
    """
    email: Optional[str] = field(default=None)
    """해당 값이 포함된 이메일 주소를 가진 파트너만 조회합니다.
    """
    business_registration_number: Optional[str] = field(default=None)
    """해당 값이 포함된 사업자등록번호를 가진 파트너만 조회합니다.
    """
    default_contract_id: Optional[str] = field(default=None)
    """해당 값이 포함된 기본 계약 아이디를 가진 파트너만 조회합니다.
    """
    memo: Optional[str] = field(default=None)
    """해당 값이 포함된 메모를 가진 파트너만 조회합니다.
    """
    account_number: Optional[str] = field(default=None)
    """해당 값이 포함된 계좌번호를 가진 파트너만 조회합니다.
    """
    account_holder: Optional[str] = field(default=None)
    """해당 값이 포함된 계좌 예금주명을 가진 파트너만 조회합니다.
    """


def _serialize_platform_partner_filter_input_keyword(obj: PlatformPartnerFilterInputKeyword) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    if obj.id is not None:
        entity["id"] = obj.id
    if obj.name is not None:
        entity["name"] = obj.name
    if obj.email is not None:
        entity["email"] = obj.email
    if obj.business_registration_number is not None:
        entity["businessRegistrationNumber"] = obj.business_registration_number
    if obj.default_contract_id is not None:
        entity["defaultContractId"] = obj.default_contract_id
    if obj.memo is not None:
        entity["memo"] = obj.memo
    if obj.account_number is not None:
        entity["accountNumber"] = obj.account_number
    if obj.account_holder is not None:
        entity["accountHolder"] = obj.account_holder
    return entity


def _deserialize_platform_partner_filter_input_keyword(obj: Any) -> PlatformPartnerFilterInputKeyword:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "id" in obj:
        id = obj["id"]
        if not isinstance(id, str):
            raise ValueError(f"{repr(id)} is not str")
    else:
        id = None
    if "name" in obj:
        name = obj["name"]
        if not isinstance(name, str):
            raise ValueError(f"{repr(name)} is not str")
    else:
        name = None
    if "email" in obj:
        email = obj["email"]
        if not isinstance(email, str):
            raise ValueError(f"{repr(email)} is not str")
    else:
        email = None
    if "businessRegistrationNumber" in obj:
        business_registration_number = obj["businessRegistrationNumber"]
        if not isinstance(business_registration_number, str):
            raise ValueError(f"{repr(business_registration_number)} is not str")
    else:
        business_registration_number = None
    if "defaultContractId" in obj:
        default_contract_id = obj["defaultContractId"]
        if not isinstance(default_contract_id, str):
            raise ValueError(f"{repr(default_contract_id)} is not str")
    else:
        default_contract_id = None
    if "memo" in obj:
        memo = obj["memo"]
        if not isinstance(memo, str):
            raise ValueError(f"{repr(memo)} is not str")
    else:
        memo = None
    if "accountNumber" in obj:
        account_number = obj["accountNumber"]
        if not isinstance(account_number, str):
            raise ValueError(f"{repr(account_number)} is not str")
    else:
        account_number = None
    if "accountHolder" in obj:
        account_holder = obj["accountHolder"]
        if not isinstance(account_holder, str):
            raise ValueError(f"{repr(account_holder)} is not str")
    else:
        account_holder = None
    return PlatformPartnerFilterInputKeyword(id, name, email, business_registration_number, default_contract_id, memo, account_number, account_holder)
