from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field
from ...platform.bulk_account_transfer.platform_bulk_account_transfer_stats import PlatformBulkAccountTransferStats, _deserialize_platform_bulk_account_transfer_stats, _serialize_platform_bulk_account_transfer_stats
from ...platform.bulk_account_transfer.platform_bulk_account_transfer_status import PlatformBulkAccountTransferStatus, _deserialize_platform_bulk_account_transfer_status, _serialize_platform_bulk_account_transfer_status

@dataclass
class PlatformBulkAccountTransfer:
    id: str
    """일괄 이체 고유 아이디
    """
    graphql_id: str
    creator_id: str
    bank_account_id: str
    """출금 계좌 아이디
    """
    bank_account_graphql_id: str
    total_amount: int
    """(int64)
    """
    status: PlatformBulkAccountTransferStatus
    stats: PlatformBulkAccountTransferStats
    status_updated_at: str
    """(RFC 3339 date-time)
    """
    created_at: str
    """(RFC 3339 date-time)
    """
    updated_at: str
    """(RFC 3339 date-time)
    """
    scheduled_at: Optional[str] = field(default=None)
    """(RFC 3339 date-time)
    """


def _serialize_platform_bulk_account_transfer(obj: PlatformBulkAccountTransfer) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["id"] = obj.id
    entity["graphqlId"] = obj.graphql_id
    entity["creatorId"] = obj.creator_id
    entity["bankAccountId"] = obj.bank_account_id
    entity["bankAccountGraphqlId"] = obj.bank_account_graphql_id
    entity["totalAmount"] = obj.total_amount
    entity["status"] = _serialize_platform_bulk_account_transfer_status(obj.status)
    entity["stats"] = _serialize_platform_bulk_account_transfer_stats(obj.stats)
    entity["statusUpdatedAt"] = obj.status_updated_at
    entity["createdAt"] = obj.created_at
    entity["updatedAt"] = obj.updated_at
    if obj.scheduled_at is not None:
        entity["scheduledAt"] = obj.scheduled_at
    return entity


def _deserialize_platform_bulk_account_transfer(obj: Any) -> PlatformBulkAccountTransfer:
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
    if "creatorId" not in obj:
        raise KeyError(f"'creatorId' is not in {obj}")
    creator_id = obj["creatorId"]
    if not isinstance(creator_id, str):
        raise ValueError(f"{repr(creator_id)} is not str")
    if "bankAccountId" not in obj:
        raise KeyError(f"'bankAccountId' is not in {obj}")
    bank_account_id = obj["bankAccountId"]
    if not isinstance(bank_account_id, str):
        raise ValueError(f"{repr(bank_account_id)} is not str")
    if "bankAccountGraphqlId" not in obj:
        raise KeyError(f"'bankAccountGraphqlId' is not in {obj}")
    bank_account_graphql_id = obj["bankAccountGraphqlId"]
    if not isinstance(bank_account_graphql_id, str):
        raise ValueError(f"{repr(bank_account_graphql_id)} is not str")
    if "totalAmount" not in obj:
        raise KeyError(f"'totalAmount' is not in {obj}")
    total_amount = obj["totalAmount"]
    if not isinstance(total_amount, int):
        raise ValueError(f"{repr(total_amount)} is not int")
    if "status" not in obj:
        raise KeyError(f"'status' is not in {obj}")
    status = obj["status"]
    status = _deserialize_platform_bulk_account_transfer_status(status)
    if "stats" not in obj:
        raise KeyError(f"'stats' is not in {obj}")
    stats = obj["stats"]
    stats = _deserialize_platform_bulk_account_transfer_stats(stats)
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
    return PlatformBulkAccountTransfer(id, graphql_id, creator_id, bank_account_id, bank_account_graphql_id, total_amount, status, stats, status_updated_at, created_at, updated_at, scheduled_at)
