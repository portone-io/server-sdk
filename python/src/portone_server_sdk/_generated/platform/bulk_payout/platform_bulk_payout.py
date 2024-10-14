from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field
from portone_server_sdk._generated.platform.bulk_payout.platform_bulk_payout_stats import PlatformBulkPayoutStats, _deserialize_platform_bulk_payout_stats, _serialize_platform_bulk_payout_stats
from portone_server_sdk._generated.platform.bulk_payout.platform_bulk_payout_status import PlatformBulkPayoutStatus, _deserialize_platform_bulk_payout_status, _serialize_platform_bulk_payout_status
from portone_server_sdk._generated.platform.platform_payout_method import PlatformPayoutMethod, _deserialize_platform_payout_method, _serialize_platform_payout_method

@dataclass
class PlatformBulkPayout:
    id: str
    """일괄 지급 고유 아이디
    """
    graphql_id: str
    name: str
    creator_id: str
    method: PlatformPayoutMethod
    are_payouts_generated: bool
    total_payout_amount: int
    """(int64)
    """
    status: PlatformBulkPayoutStatus
    payout_stats: PlatformBulkPayoutStats
    status_updated_at: str
    """(RFC 3339 date-time)
    """
    created_at: str
    """(RFC 3339 date-time)
    """
    updated_at: str
    """(RFC 3339 date-time)
    """
    scheduled_at: Optional[str]
    """(RFC 3339 date-time)
    """


def _serialize_platform_bulk_payout(obj: PlatformBulkPayout) -> Any:
    entity = {}
    entity["id"] = obj.id
    entity["graphqlId"] = obj.graphql_id
    entity["name"] = obj.name
    entity["creatorId"] = obj.creator_id
    entity["method"] = _serialize_platform_payout_method(obj.method)
    entity["arePayoutsGenerated"] = obj.are_payouts_generated
    entity["totalPayoutAmount"] = obj.total_payout_amount
    entity["status"] = _serialize_platform_bulk_payout_status(obj.status)
    entity["payoutStats"] = _serialize_platform_bulk_payout_stats(obj.payout_stats)
    entity["statusUpdatedAt"] = obj.status_updated_at
    entity["createdAt"] = obj.created_at
    entity["updatedAt"] = obj.updated_at
    if obj.scheduled_at is not None:
        entity["scheduledAt"] = obj.scheduled_at
    return entity


def _deserialize_platform_bulk_payout(obj: Any) -> PlatformBulkPayout:
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
    if "creatorId" not in obj:
        raise KeyError(f"'creatorId' is not in {obj}")
    creator_id = obj["creatorId"]
    if not isinstance(creator_id, str):
        raise ValueError(f"{repr(creator_id)} is not str")
    if "method" not in obj:
        raise KeyError(f"'method' is not in {obj}")
    method = obj["method"]
    method = _deserialize_platform_payout_method(method)
    if "arePayoutsGenerated" not in obj:
        raise KeyError(f"'arePayoutsGenerated' is not in {obj}")
    are_payouts_generated = obj["arePayoutsGenerated"]
    if not isinstance(are_payouts_generated, bool):
        raise ValueError(f"{repr(are_payouts_generated)} is not bool")
    if "totalPayoutAmount" not in obj:
        raise KeyError(f"'totalPayoutAmount' is not in {obj}")
    total_payout_amount = obj["totalPayoutAmount"]
    if not isinstance(total_payout_amount, int):
        raise ValueError(f"{repr(total_payout_amount)} is not int")
    if "status" not in obj:
        raise KeyError(f"'status' is not in {obj}")
    status = obj["status"]
    status = _deserialize_platform_bulk_payout_status(status)
    if "payoutStats" not in obj:
        raise KeyError(f"'payoutStats' is not in {obj}")
    payout_stats = obj["payoutStats"]
    payout_stats = _deserialize_platform_bulk_payout_stats(payout_stats)
    if "statusUpdatedAt" not in obj:
        raise KeyError(f"'statusUpdatedAt' is not in {obj}")
    status_updated_at = obj["statusUpdatedAt"]
    if not isinstance(status_updated_at, str):
        raise ValueError(f"{repr(status_updated_at)} is not str")
    if "createdAt" not in obj:
        raise KeyError(f"'createdAt' is not in {obj}")
    created_at = obj["createdAt"]
    if not isinstance(created_at, str):
        raise ValueError(f"{repr(created_at)} is not str")
    if "updatedAt" not in obj:
        raise KeyError(f"'updatedAt' is not in {obj}")
    updated_at = obj["updatedAt"]
    if not isinstance(updated_at, str):
        raise ValueError(f"{repr(updated_at)} is not str")
    if "scheduledAt" in obj:
        scheduled_at = obj["scheduledAt"]
        if not isinstance(scheduled_at, str):
            raise ValueError(f"{repr(scheduled_at)} is not str")
    else:
        scheduled_at = None
    return PlatformBulkPayout(id, graphql_id, name, creator_id, method, are_payouts_generated, total_payout_amount, status, payout_stats, status_updated_at, created_at, updated_at, scheduled_at)
