from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field
from ...platform.partner.platform_bulk_task_progress_stats import PlatformBulkTaskProgressStats, _deserialize_platform_bulk_task_progress_stats, _serialize_platform_bulk_task_progress_stats
from ...platform.partner.platform_bulk_task_status import PlatformBulkTaskStatus, _deserialize_platform_bulk_task_status, _serialize_platform_bulk_task_status
from ...platform.partner.platform_bulk_task_type import PlatformBulkTaskType, _deserialize_platform_bulk_task_type, _serialize_platform_bulk_task_type

@dataclass
class PlatformBulkTask:
    id: str
    graphql_id: str
    status: PlatformBulkTaskStatus
    type: PlatformBulkTaskType
    progress_stats: PlatformBulkTaskProgressStats
    is_for_test: bool
    status_updated_at: str
    """(RFC 3339 date-time)
    """
    created_at: str
    """(RFC 3339 date-time)
    """
    updated_at: str
    """(RFC 3339 date-time)
    """


def _serialize_platform_bulk_task(obj: PlatformBulkTask) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["id"] = obj.id
    entity["graphqlId"] = obj.graphql_id
    entity["status"] = _serialize_platform_bulk_task_status(obj.status)
    entity["type"] = _serialize_platform_bulk_task_type(obj.type)
    entity["progressStats"] = _serialize_platform_bulk_task_progress_stats(obj.progress_stats)
    entity["isForTest"] = obj.is_for_test
    entity["statusUpdatedAt"] = obj.status_updated_at
    entity["createdAt"] = obj.created_at
    entity["updatedAt"] = obj.updated_at
    return entity


def _deserialize_platform_bulk_task(obj: Any) -> PlatformBulkTask:
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
    if "status" not in obj:
        raise KeyError("Missing required field 'status'")
    status = obj["status"]
    status = _deserialize_platform_bulk_task_status(status)
    if "type" not in obj:
        raise KeyError("Missing required field 'type'")
    type = obj["type"]
    type = _deserialize_platform_bulk_task_type(type)
    if "progressStats" not in obj:
        raise KeyError("Missing required field 'progressStats'")
    progress_stats = obj["progressStats"]
    progress_stats = _deserialize_platform_bulk_task_progress_stats(progress_stats)
    if "isForTest" not in obj:
        raise KeyError("Missing required field 'isForTest'")
    is_for_test = obj["isForTest"]
    if not isinstance(is_for_test, bool):
        raise ValueError("Expected bool for is_for_test")
    if "statusUpdatedAt" not in obj:
        raise KeyError("Missing required field 'statusUpdatedAt'")
    status_updated_at = obj["statusUpdatedAt"]
    if not isinstance(status_updated_at, str):
        raise ValueError("Expected str for status_updated_at")
    if "createdAt" not in obj:
        raise KeyError("Missing required field 'createdAt'")
    created_at = obj["createdAt"]
    if not isinstance(created_at, str):
        raise ValueError("Expected str for created_at")
    if "updatedAt" not in obj:
        raise KeyError("Missing required field 'updatedAt'")
    updated_at = obj["updatedAt"]
    if not isinstance(updated_at, str):
        raise ValueError("Expected str for updated_at")
    return PlatformBulkTask(id, graphql_id, status, type, progress_stats, is_for_test, status_updated_at, created_at, updated_at)
