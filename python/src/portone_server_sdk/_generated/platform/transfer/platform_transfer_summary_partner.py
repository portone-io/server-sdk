from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field
from ...platform.platform_partner_taxation_type import PlatformPartnerTaxationType, _deserialize_platform_partner_taxation_type, _serialize_platform_partner_taxation_type
from ...platform.transfer.platform_transfer_summary_partner_type import PlatformTransferSummaryPartnerType, _deserialize_platform_transfer_summary_partner_type, _serialize_platform_transfer_summary_partner_type
from ...platform.transfer.platform_user_defined_property_key_value import PlatformUserDefinedPropertyKeyValue, _deserialize_platform_user_defined_property_key_value, _serialize_platform_user_defined_property_key_value

@dataclass
class PlatformTransferSummaryPartner:
    id: str
    graphql_id: str
    name: str
    type: PlatformTransferSummaryPartnerType
    user_defined_properties: list[PlatformUserDefinedPropertyKeyValue]
    """사용자 정의 속성
    """
    taxation_type: Optional[PlatformPartnerTaxationType] = field(default=None)


def _serialize_platform_transfer_summary_partner(obj: PlatformTransferSummaryPartner) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["id"] = obj.id
    entity["graphqlId"] = obj.graphql_id
    entity["name"] = obj.name
    entity["type"] = _serialize_platform_transfer_summary_partner_type(obj.type)
    entity["userDefinedProperties"] = list(map(_serialize_platform_user_defined_property_key_value, obj.user_defined_properties))
    if obj.taxation_type is not None:
        entity["taxationType"] = _serialize_platform_partner_taxation_type(obj.taxation_type)
    return entity


def _deserialize_platform_transfer_summary_partner(obj: Any) -> PlatformTransferSummaryPartner:
    if not isinstance(obj, dict):
        raise ValueError("Expected dict for obj")
    if "id" not in obj:
        raise KeyError("Missing required field 'id'")
    id = obj["id"]
    if not isinstance(id, str):
        raise ValueError("Expected str for id")
    if "graphqlId" not in obj:
        raise KeyError("Missing required field 'graphqlId'")
    graphql_id = obj["graphqlId"]
    if not isinstance(graphql_id, str):
        raise ValueError("Expected str for graphql_id")
    if "name" not in obj:
        raise KeyError("Missing required field 'name'")
    name = obj["name"]
    if not isinstance(name, str):
        raise ValueError("Expected str for name")
    if "type" not in obj:
        raise KeyError("Missing required field 'type'")
    type = obj["type"]
    type = _deserialize_platform_transfer_summary_partner_type(type)
    if "userDefinedProperties" not in obj:
        raise KeyError("Missing required field 'userDefinedProperties'")
    user_defined_properties = obj["userDefinedProperties"]
    if not isinstance(user_defined_properties, list):
        raise ValueError("Expected list for user_defined_properties")
    for i, item in enumerate(user_defined_properties):
        item = _deserialize_platform_user_defined_property_key_value(item)
        user_defined_properties[i] = item
    if "taxationType" in obj:
        taxation_type = obj["taxationType"]
        taxation_type = _deserialize_platform_partner_taxation_type(taxation_type)
    else:
        taxation_type = None
    return PlatformTransferSummaryPartner(id, graphql_id, name, type, user_defined_properties, taxation_type)
