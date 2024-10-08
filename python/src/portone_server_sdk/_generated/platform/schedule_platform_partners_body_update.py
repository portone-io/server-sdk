from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field
from portone_server_sdk._generated.platform.platform_properties import PlatformProperties, _deserialize_platform_properties, _serialize_platform_properties
from portone_server_sdk._generated.platform.schedule_platform_partners_body_update_account import SchedulePlatformPartnersBodyUpdateAccount, _deserialize_schedule_platform_partners_body_update_account, _serialize_schedule_platform_partners_body_update_account
from portone_server_sdk._generated.platform.schedule_platform_partners_body_update_contact import SchedulePlatformPartnersBodyUpdateContact, _deserialize_schedule_platform_partners_body_update_contact, _serialize_schedule_platform_partners_body_update_contact
from portone_server_sdk._generated.platform.schedule_platform_partners_body_update_type import SchedulePlatformPartnersBodyUpdateType, _deserialize_schedule_platform_partners_body_update_type, _serialize_schedule_platform_partners_body_update_type

@dataclass
class SchedulePlatformPartnersBodyUpdate:
    name: Optional[str]
    contact: Optional[SchedulePlatformPartnersBodyUpdateContact]
    type: Optional[SchedulePlatformPartnersBodyUpdateType]
    account: Optional[SchedulePlatformPartnersBodyUpdateAccount]
    default_contract_id: Optional[str]
    memo: Optional[str]
    tags: Optional[list[str]]
    user_defined_properties: Optional[PlatformProperties]


def _serialize_schedule_platform_partners_body_update(obj: SchedulePlatformPartnersBodyUpdate) -> Any:
    entity = {}
    if obj.name is not None:
        entity["name"] = obj.name
    if obj.contact is not None:
        entity["contact"] = _serialize_schedule_platform_partners_body_update_contact(obj.contact)
    if obj.type is not None:
        entity["type"] = _serialize_schedule_platform_partners_body_update_type(obj.type)
    if obj.account is not None:
        entity["account"] = _serialize_schedule_platform_partners_body_update_account(obj.account)
    if obj.default_contract_id is not None:
        entity["defaultContractId"] = obj.default_contract_id
    if obj.memo is not None:
        entity["memo"] = obj.memo
    if obj.tags is not None:
        entity["tags"] = obj.tags
    if obj.user_defined_properties is not None:
        entity["userDefinedProperties"] = _serialize_platform_properties(obj.user_defined_properties)
    return entity


def _deserialize_schedule_platform_partners_body_update(obj: Any) -> SchedulePlatformPartnersBodyUpdate:
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
        contact = _deserialize_schedule_platform_partners_body_update_contact(contact)
    else:
        contact = None
    if "type" in obj:
        type = obj["type"]
        type = _deserialize_schedule_platform_partners_body_update_type(type)
    else:
        type = None
    if "account" in obj:
        account = obj["account"]
        account = _deserialize_schedule_platform_partners_body_update_account(account)
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
    if "userDefinedProperties" in obj:
        user_defined_properties = obj["userDefinedProperties"]
        user_defined_properties = _deserialize_platform_properties(user_defined_properties)
    else:
        user_defined_properties = None
    return SchedulePlatformPartnersBodyUpdate(name, contact, type, account, default_contract_id, memo, tags, user_defined_properties)
