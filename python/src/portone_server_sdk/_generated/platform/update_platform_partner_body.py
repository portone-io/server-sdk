from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field
from ..platform.platform_properties import PlatformProperties, _deserialize_platform_properties, _serialize_platform_properties
from ..platform.update_platform_partner_body_account import UpdatePlatformPartnerBodyAccount, _deserialize_update_platform_partner_body_account, _serialize_update_platform_partner_body_account
from ..platform.update_platform_partner_body_contact import UpdatePlatformPartnerBodyContact, _deserialize_update_platform_partner_body_contact, _serialize_update_platform_partner_body_contact
from ..platform.update_platform_partner_body_type import UpdatePlatformPartnerBodyType, _deserialize_update_platform_partner_body_type, _serialize_update_platform_partner_body_type

@dataclass
class UpdatePlatformPartnerBody:
    """파트너 업데이트를 위한 입력 정보

    값이 명시되지 않은 필드는 업데이트되지 않습니다.
    """
    name: Optional[str] = field(default=None)
    """파트너 법인명 혹은 이름
    """
    contact: Optional[UpdatePlatformPartnerBodyContact] = field(default=None)
    """파트너 담당자 연락 정보
    """
    account: Optional[UpdatePlatformPartnerBodyAccount] = field(default=None)
    """정산 계좌
    """
    default_contract_id: Optional[str] = field(default=None)
    """파트너에 설정된 기본 계약 아이디
    """
    memo: Optional[str] = field(default=None)
    """파트너에 대한 메모
    """
    tags: Optional[list[str]] = field(default=None)
    """파트너의 태그 리스트
    """
    type: Optional[UpdatePlatformPartnerBodyType] = field(default=None)
    """파트너 유형별 정보
    """
    user_defined_properties: Optional[PlatformProperties] = field(default=None)
    """사용자 정의 속성
    """


def _serialize_update_platform_partner_body(obj: UpdatePlatformPartnerBody) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    if obj.name is not None:
        entity["name"] = obj.name
    if obj.contact is not None:
        entity["contact"] = _serialize_update_platform_partner_body_contact(obj.contact)
    if obj.account is not None:
        entity["account"] = _serialize_update_platform_partner_body_account(obj.account)
    if obj.default_contract_id is not None:
        entity["defaultContractId"] = obj.default_contract_id
    if obj.memo is not None:
        entity["memo"] = obj.memo
    if obj.tags is not None:
        entity["tags"] = obj.tags
    if obj.type is not None:
        entity["type"] = _serialize_update_platform_partner_body_type(obj.type)
    if obj.user_defined_properties is not None:
        entity["userDefinedProperties"] = _serialize_platform_properties(obj.user_defined_properties)
    return entity


def _deserialize_update_platform_partner_body(obj: Any) -> UpdatePlatformPartnerBody:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "name" in obj:
        name = obj["name"]
        if not isinstance(name, str):
            raise ValueError(f"{repr(name)} is not str")
    else:
        name = None
    if "contact" in obj:
        contact = obj["contact"]
        contact = _deserialize_update_platform_partner_body_contact(contact)
    else:
        contact = None
    if "account" in obj:
        account = obj["account"]
        account = _deserialize_update_platform_partner_body_account(account)
    else:
        account = None
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
    if "tags" in obj:
        tags = obj["tags"]
        if not isinstance(tags, list):
            raise ValueError(f"{repr(tags)} is not list")
        for i, item in enumerate(tags):
            if not isinstance(item, str):
                raise ValueError(f"{repr(item)} is not str")
    else:
        tags = None
    if "type" in obj:
        type = obj["type"]
        type = _deserialize_update_platform_partner_body_type(type)
    else:
        type = None
    if "userDefinedProperties" in obj:
        user_defined_properties = obj["userDefinedProperties"]
        user_defined_properties = _deserialize_platform_properties(user_defined_properties)
    else:
        user_defined_properties = None
    return UpdatePlatformPartnerBody(name, contact, account, default_contract_id, memo, tags, type, user_defined_properties)
