from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field
from portone_server_sdk._generated.platform.bulk_payout.platform_bulk_payout_filter_input_criteria import PlatformBulkPayoutFilterInputCriteria, _deserialize_platform_bulk_payout_filter_input_criteria, _serialize_platform_bulk_payout_filter_input_criteria
from portone_server_sdk._generated.platform.bulk_payout.platform_bulk_payout_status import PlatformBulkPayoutStatus, _deserialize_platform_bulk_payout_status, _serialize_platform_bulk_payout_status
from portone_server_sdk._generated.platform.platform_payout_method import PlatformPayoutMethod, _deserialize_platform_payout_method, _serialize_platform_payout_method

@dataclass
class PlatformBulkPayoutFilterInput:
    statuses: Optional[list[PlatformBulkPayoutStatus]]
    methods: Optional[list[PlatformPayoutMethod]]
    criteria: Optional[PlatformBulkPayoutFilterInputCriteria]


def _serialize_platform_bulk_payout_filter_input(obj: PlatformBulkPayoutFilterInput) -> Any:
    entity = {}
    if obj.statuses is not None:
        entity["statuses"] = list(map(_serialize_platform_bulk_payout_status, obj.statuses))
    if obj.methods is not None:
        entity["methods"] = list(map(_serialize_platform_payout_method, obj.methods))
    if obj.criteria is not None:
        entity["criteria"] = _serialize_platform_bulk_payout_filter_input_criteria(obj.criteria)
    return entity


def _deserialize_platform_bulk_payout_filter_input(obj: Any) -> PlatformBulkPayoutFilterInput:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "statuses" in obj:
        statuses = obj["statuses"]
        if not isinstance(statuses, list):
            raise ValueError(f"{repr(statuses)} is not list")
        for i, item in enumerate(statuses):
            item = _deserialize_platform_bulk_payout_status(item)
            statuses[i] = item
    else:
        statuses = None
    if "methods" in obj:
        methods = obj["methods"]
        if not isinstance(methods, list):
            raise ValueError(f"{repr(methods)} is not list")
        for i, item in enumerate(methods):
            item = _deserialize_platform_payout_method(item)
            methods[i] = item
    else:
        methods = None
    if "criteria" in obj:
        criteria = obj["criteria"]
        criteria = _deserialize_platform_bulk_payout_filter_input_criteria(criteria)
    else:
        criteria = None
    return PlatformBulkPayoutFilterInput(statuses, methods, criteria)
