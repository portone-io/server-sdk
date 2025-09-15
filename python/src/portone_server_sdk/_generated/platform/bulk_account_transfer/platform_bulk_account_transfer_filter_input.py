from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field
from ...platform.bulk_account_transfer.platform_bulk_account_transfer_filter_input_criteria import PlatformBulkAccountTransferFilterInputCriteria, _deserialize_platform_bulk_account_transfer_filter_input_criteria, _serialize_platform_bulk_account_transfer_filter_input_criteria
from ...platform.bulk_account_transfer.platform_bulk_account_transfer_status import PlatformBulkAccountTransferStatus, _deserialize_platform_bulk_account_transfer_status, _serialize_platform_bulk_account_transfer_status

@dataclass
class PlatformBulkAccountTransferFilterInput:
    statuses: Optional[list[PlatformBulkAccountTransferStatus]] = field(default=None)
    criteria: Optional[PlatformBulkAccountTransferFilterInputCriteria] = field(default=None)


def _serialize_platform_bulk_account_transfer_filter_input(obj: PlatformBulkAccountTransferFilterInput) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    if obj.statuses is not None:
        entity["statuses"] = list(map(_serialize_platform_bulk_account_transfer_status, obj.statuses))
    if obj.criteria is not None:
        entity["criteria"] = _serialize_platform_bulk_account_transfer_filter_input_criteria(obj.criteria)
    return entity


def _deserialize_platform_bulk_account_transfer_filter_input(obj: Any) -> PlatformBulkAccountTransferFilterInput:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "statuses" in obj:
        statuses = obj["statuses"]
        if not isinstance(statuses, list):
            raise ValueError(f"{repr(statuses)} is not list")
        for i, item in enumerate(statuses):
            item = _deserialize_platform_bulk_account_transfer_status(item)
            statuses[i] = item
    else:
        statuses = None
    if "criteria" in obj:
        criteria = obj["criteria"]
        criteria = _deserialize_platform_bulk_account_transfer_filter_input_criteria(criteria)
    else:
        criteria = None
    return PlatformBulkAccountTransferFilterInput(statuses, criteria)
