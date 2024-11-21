from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field
from ...platform.partner.create_platform_partner_body_account import CreatePlatformPartnerBodyAccount, _deserialize_create_platform_partner_body_account, _serialize_create_platform_partner_body_account
from ...platform.partner.create_platform_partner_body_contact import CreatePlatformPartnerBodyContact, _deserialize_create_platform_partner_body_contact, _serialize_create_platform_partner_body_contact
from ...platform.partner.create_platform_partner_body_type import CreatePlatformPartnerBodyType, _deserialize_create_platform_partner_body_type, _serialize_create_platform_partner_body_type
from ...platform.platform_properties import PlatformProperties, _deserialize_platform_properties, _serialize_platform_properties

@dataclass
class CreatePlatformPartnerBody:
    """파트너 생성을 위한 입력 정보
    """
    name: str
    """파트너 법인명 혹은 이름
    """
    contact: CreatePlatformPartnerBodyContact
    """파트너 담당자 연락 정보
    """
    account: CreatePlatformPartnerBodyAccount
    """정산 계좌

    파트너의 사업자등록번호가 존재하는 경우 명시합니다. 별도로 검증하지는 않으며, 번호와 기호 모두 입력 가능합니다.
    """
    default_contract_id: str
    """기본 계약 아이디

    이미 존재하는 계약 아이디를 등록해야 합니다.
    """
    tags: list[str]
    """파트너에 부여할 태그 리스트

    최대 10개까지 입력할 수 있습니다.
    """
    type: CreatePlatformPartnerBodyType
    """파트너 유형별 추가 정보

    사업자/원천징수 대상자 중 추가할 파트너의 유형에 따른 정보를 입력해야 합니다.
    """
    id: Optional[str] = field(default=None)
    """파트너에 부여할 고유 아이디

    고객사 서버에 등록된 파트너 지칭 아이디와 동일하게 설정하는 것을 권장합니다. 명시하지 않는 경우 포트원이 임의의 아이디를 발급해드립니다.
    """
    memo: Optional[str] = field(default=None)
    """파트너에 대한 메모

    총 256자까지 입력할 수 있습니다.
    """
    user_defined_properties: Optional[PlatformProperties] = field(default=None)
    """사용자 정의 속성
    """


def _serialize_create_platform_partner_body(obj: CreatePlatformPartnerBody) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["name"] = obj.name
    entity["contact"] = _serialize_create_platform_partner_body_contact(obj.contact)
    entity["account"] = _serialize_create_platform_partner_body_account(obj.account)
    entity["defaultContractId"] = obj.default_contract_id
    entity["tags"] = obj.tags
    entity["type"] = _serialize_create_platform_partner_body_type(obj.type)
    if obj.id is not None:
        entity["id"] = obj.id
    if obj.memo is not None:
        entity["memo"] = obj.memo
    if obj.user_defined_properties is not None:
        entity["userDefinedProperties"] = _serialize_platform_properties(obj.user_defined_properties)
    return entity


def _deserialize_create_platform_partner_body(obj: Any) -> CreatePlatformPartnerBody:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "name" not in obj:
        raise KeyError(f"'name' is not in {obj}")
    name = obj["name"]
    if not isinstance(name, str):
        raise ValueError(f"{repr(name)} is not str")
    if "contact" not in obj:
        raise KeyError(f"'contact' is not in {obj}")
    contact = obj["contact"]
    contact = _deserialize_create_platform_partner_body_contact(contact)
    if "account" not in obj:
        raise KeyError(f"'account' is not in {obj}")
    account = obj["account"]
    account = _deserialize_create_platform_partner_body_account(account)
    if "defaultContractId" not in obj:
        raise KeyError(f"'defaultContractId' is not in {obj}")
    default_contract_id = obj["defaultContractId"]
    if not isinstance(default_contract_id, str):
        raise ValueError(f"{repr(default_contract_id)} is not str")
    if "tags" not in obj:
        raise KeyError(f"'tags' is not in {obj}")
    tags = obj["tags"]
    if not isinstance(tags, list):
        raise ValueError(f"{repr(tags)} is not list")
    for i, item in enumerate(tags):
        if not isinstance(item, str):
            raise ValueError(f"{repr(item)} is not str")
    if "type" not in obj:
        raise KeyError(f"'type' is not in {obj}")
    type = obj["type"]
    type = _deserialize_create_platform_partner_body_type(type)
    if "id" in obj:
        id = obj["id"]
        if not isinstance(id, str):
            raise ValueError(f"{repr(id)} is not str")
    else:
        id = None
    if "memo" in obj:
        memo = obj["memo"]
        if not isinstance(memo, str):
            raise ValueError(f"{repr(memo)} is not str")
    else:
        memo = None
    if "userDefinedProperties" in obj:
        user_defined_properties = obj["userDefinedProperties"]
        user_defined_properties = _deserialize_platform_properties(user_defined_properties)
    else:
        user_defined_properties = None
    return CreatePlatformPartnerBody(name, contact, account, default_contract_id, tags, type, id, memo, user_defined_properties)
