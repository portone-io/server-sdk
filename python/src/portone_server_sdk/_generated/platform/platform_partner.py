from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field
from ..platform.platform_account import PlatformAccount, _deserialize_platform_account, _serialize_platform_account
from ..platform.platform_contact import PlatformContact, _deserialize_platform_contact, _serialize_platform_contact
from ..platform.platform_partner_status import PlatformPartnerStatus, _deserialize_platform_partner_status, _serialize_platform_partner_status
from ..platform.platform_partner_type import PlatformPartnerType, _deserialize_platform_partner_type, _serialize_platform_partner_type
from ..platform.platform_properties import PlatformProperties, _deserialize_platform_properties, _serialize_platform_properties

@dataclass
class PlatformPartner:
    """파트너

    파트너는 고객사가 정산해주어야 할 대상입니다.
    기본 사업자 정보와 정산정보, 그리고 적용될 계약의 정보를 등록 및 관리할 수 있습니다.
    """
    id: str
    """파트너 고유 아이디
    """
    graphql_id: str
    name: str
    """파트너 법인명 혹은 이름
    """
    contact: PlatformContact
    """파트너 담당자 연락 정보
    """
    account: PlatformAccount
    """정산 계좌
    """
    status: PlatformPartnerStatus
    """파트너의 상태
    """
    default_contract_id: str
    """파트너에 설정된 기본 계약 아이디
    """
    tags: list[str]
    """파트너의 태그 리스트
    """
    type: PlatformPartnerType
    """파트너 유형별 정보
    """
    is_archived: bool
    """보관 여부
    """
    applied_at: str
    """변경 적용 시점
    (RFC 3339 date-time)
    """
    user_defined_properties: PlatformProperties
    """사용자 정의 속성
    """
    memo: Optional[str] = field(default=None)
    """파트너에 대한 메모
    """


def _serialize_platform_partner(obj: PlatformPartner) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["id"] = obj.id
    entity["graphqlId"] = obj.graphql_id
    entity["name"] = obj.name
    entity["contact"] = _serialize_platform_contact(obj.contact)
    entity["account"] = _serialize_platform_account(obj.account)
    entity["status"] = _serialize_platform_partner_status(obj.status)
    entity["defaultContractId"] = obj.default_contract_id
    entity["tags"] = obj.tags
    entity["type"] = _serialize_platform_partner_type(obj.type)
    entity["isArchived"] = obj.is_archived
    entity["appliedAt"] = obj.applied_at
    entity["userDefinedProperties"] = _serialize_platform_properties(obj.user_defined_properties)
    if obj.memo is not None:
        entity["memo"] = obj.memo
    return entity


def _deserialize_platform_partner(obj: Any) -> PlatformPartner:
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
    if "name" not in obj:
        raise KeyError(f"'name' is not in {obj}")
    name = obj["name"]
    if not isinstance(name, str):
        raise ValueError(f"{repr(name)} is not str")
    if "contact" not in obj:
        raise KeyError(f"'contact' is not in {obj}")
    contact = obj["contact"]
    contact = _deserialize_platform_contact(contact)
    if "account" not in obj:
        raise KeyError(f"'account' is not in {obj}")
    account = obj["account"]
    account = _deserialize_platform_account(account)
    if "status" not in obj:
        raise KeyError(f"'status' is not in {obj}")
    status = obj["status"]
    status = _deserialize_platform_partner_status(status)
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
    type = _deserialize_platform_partner_type(type)
    if "isArchived" not in obj:
        raise KeyError(f"'isArchived' is not in {obj}")
    is_archived = obj["isArchived"]
    if not isinstance(is_archived, bool):
        raise ValueError(f"{repr(is_archived)} is not bool")
    if "appliedAt" not in obj:
        raise KeyError(f"'appliedAt' is not in {obj}")
    applied_at = obj["appliedAt"]
    if not isinstance(applied_at, str):
        raise ValueError(f"{repr(applied_at)} is not str")
    if "userDefinedProperties" not in obj:
        raise KeyError(f"'userDefinedProperties' is not in {obj}")
    user_defined_properties = obj["userDefinedProperties"]
    user_defined_properties = _deserialize_platform_properties(user_defined_properties)
    if "memo" in obj:
        memo = obj["memo"]
        if not isinstance(memo, str):
            raise ValueError(f"{repr(memo)} is not str")
    else:
        memo = None
    return PlatformPartner(id, graphql_id, name, contact, account, status, default_contract_id, tags, type, is_archived, applied_at, user_defined_properties, memo)
