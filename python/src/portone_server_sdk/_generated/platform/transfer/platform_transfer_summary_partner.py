from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field
from portone_server_sdk._generated.platform.platform_partner_taxation_type import PlatformPartnerTaxationType, _deserialize_platform_partner_taxation_type, _serialize_platform_partner_taxation_type
from portone_server_sdk._generated.platform.transfer.platform_transfer_summary_partner_type import PlatformTransferSummaryPartnerType, _deserialize_platform_transfer_summary_partner_type, _serialize_platform_transfer_summary_partner_type

@dataclass
class PlatformTransferSummaryPartner:
    id: str
    graphql_id: str
    name: str
    type: PlatformTransferSummaryPartnerType
    taxation_type: Optional[PlatformPartnerTaxationType]


def _serialize_platform_transfer_summary_partner(obj: PlatformTransferSummaryPartner) -> Any:
    entity = {}
    entity["id"] = obj.id
    entity["graphqlId"] = obj.graphql_id
    entity["name"] = obj.name
    entity["type"] = _serialize_platform_transfer_summary_partner_type(obj.type)
    if obj.taxation_type is not None:
        entity["taxationType"] = _serialize_platform_partner_taxation_type(obj.taxation_type)
    return entity


def _deserialize_platform_transfer_summary_partner(obj: Any) -> PlatformTransferSummaryPartner:
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
    if "type" not in obj:
        raise KeyError(f"'type' is not in {obj}")
    type = obj["type"]
    type = _deserialize_platform_transfer_summary_partner_type(type)
    if "taxationType" in obj:
        taxation_type = obj["taxationType"]
        taxation_type = _deserialize_platform_partner_taxation_type(taxation_type)
    else:
        taxation_type = None
    return PlatformTransferSummaryPartner(id, graphql_id, name, type, taxation_type)
