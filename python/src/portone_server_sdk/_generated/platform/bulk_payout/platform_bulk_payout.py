from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field
from ...platform.bulk_payout.platform_bulk_payout_stats import PlatformBulkPayoutStats, _deserialize_platform_bulk_payout_stats, _serialize_platform_bulk_payout_stats
from ...platform.bulk_payout.platform_bulk_payout_status import PlatformBulkPayoutStatus, _deserialize_platform_bulk_payout_status, _serialize_platform_bulk_payout_status
from ...platform.platform_payout_method import PlatformPayoutMethod, _deserialize_platform_payout_method, _serialize_platform_payout_method

@dataclass
class PlatformBulkPayout:
    id: str
    """일괄 지급 고유 아이디
    """
    graphql_id: str
    name: str
    """이름
    """
    creator_id: str
    """생성자 아이디
    """
    method: PlatformPayoutMethod
    """지급 유형
    """
    total_payout_amount: int
    """총 지급 금액
    (int64)
    """
    total_settlement_amount: int
    """총 정산 금액
    (int64)
    """
    status: PlatformBulkPayoutStatus
    """상태
    """
    payout_stats: PlatformBulkPayoutStats
    """지급 통계
    """
    status_updated_at: str
    """상태 업데이트 일시
    (RFC 3339 date-time)
    """
    created_at: str
    """생성 일시
    (RFC 3339 date-time)
    """
    updated_at: str
    """업데이트 일시
    (RFC 3339 date-time)
    """


def _serialize_platform_bulk_payout(obj: PlatformBulkPayout) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["id"] = obj.id
    entity["graphqlId"] = obj.graphql_id
    entity["name"] = obj.name
    entity["creatorId"] = obj.creator_id
    entity["method"] = _serialize_platform_payout_method(obj.method)
    entity["totalPayoutAmount"] = obj.total_payout_amount
    entity["totalSettlementAmount"] = obj.total_settlement_amount
    entity["status"] = _serialize_platform_bulk_payout_status(obj.status)
    entity["payoutStats"] = _serialize_platform_bulk_payout_stats(obj.payout_stats)
    entity["statusUpdatedAt"] = obj.status_updated_at
    entity["createdAt"] = obj.created_at
    entity["updatedAt"] = obj.updated_at
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
    if "totalPayoutAmount" not in obj:
        raise KeyError(f"'totalPayoutAmount' is not in {obj}")
    total_payout_amount = obj["totalPayoutAmount"]
    if not isinstance(total_payout_amount, int):
        raise ValueError(f"{repr(total_payout_amount)} is not int")
    if "totalSettlementAmount" not in obj:
        raise KeyError(f"'totalSettlementAmount' is not in {obj}")
    total_settlement_amount = obj["totalSettlementAmount"]
    if not isinstance(total_settlement_amount, int):
        raise ValueError(f"{repr(total_settlement_amount)} is not int")
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
    return PlatformBulkPayout(id, graphql_id, name, creator_id, method, total_payout_amount, total_settlement_amount, status, payout_stats, status_updated_at, created_at, updated_at)
