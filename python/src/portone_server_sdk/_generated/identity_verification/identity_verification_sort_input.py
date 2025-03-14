from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field
from ..identity_verification.identity_verification_sort_by import IdentityVerificationSortBy, _deserialize_identity_verification_sort_by, _serialize_identity_verification_sort_by
from ..common.sort_order import SortOrder, _deserialize_sort_order, _serialize_sort_order

@dataclass
class IdentityVerificationSortInput:
    """본인인증 내역 다건 조회 시 정렬 조건
    """
    by: Optional[IdentityVerificationSortBy] = field(default=None)
    """정렬 기준 필드

    어떤 필드를 기준으로 정렬할 지 결정합니다. 비워서 보낼 경우, REQUESTED_AT이 기본값으로 설정됩니다.
    """
    order: Optional[SortOrder] = field(default=None)
    """정렬 순서

    어떤 순서로 정렬할 지 결정합니다. 비워서 보낼 경우, DESC(내림차순)가 기본값으로 설정됩니다.
    """


def _serialize_identity_verification_sort_input(obj: IdentityVerificationSortInput) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    if obj.by is not None:
        entity["by"] = _serialize_identity_verification_sort_by(obj.by)
    if obj.order is not None:
        entity["order"] = _serialize_sort_order(obj.order)
    return entity


def _deserialize_identity_verification_sort_input(obj: Any) -> IdentityVerificationSortInput:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "by" in obj:
        by = obj["by"]
        by = _deserialize_identity_verification_sort_by(by)
    else:
        by = None
    if "order" in obj:
        order = obj["order"]
        order = _deserialize_sort_order(order)
    else:
        order = None
    return IdentityVerificationSortInput(by, order)
