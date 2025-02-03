from __future__ import annotations
from typing import Any, Optional, Union
from ...platform.transfer.platform_manual_transfer_summary import PlatformManualTransferSummary, _deserialize_platform_manual_transfer_summary, _serialize_platform_manual_transfer_summary
from ...platform.transfer.platform_order_cancel_transfer_summary import PlatformOrderCancelTransferSummary, _deserialize_platform_order_cancel_transfer_summary, _serialize_platform_order_cancel_transfer_summary
from ...platform.transfer.platform_order_transfer_summary import PlatformOrderTransferSummary, _deserialize_platform_order_transfer_summary, _serialize_platform_order_transfer_summary

PlatformTransferSummary = Union[PlatformManualTransferSummary, PlatformOrderTransferSummary, PlatformOrderCancelTransferSummary, dict]


def _serialize_platform_transfer_summary(obj: PlatformTransferSummary) -> Any:
    if isinstance(obj, dict):
        return obj
    if isinstance(obj, PlatformManualTransferSummary):
        return _serialize_platform_manual_transfer_summary(obj)
    if isinstance(obj, PlatformOrderTransferSummary):
        return _serialize_platform_order_transfer_summary(obj)
    if isinstance(obj, PlatformOrderCancelTransferSummary):
        return _serialize_platform_order_cancel_transfer_summary(obj)


def _deserialize_platform_transfer_summary(obj: Any) -> PlatformTransferSummary:
    try:
        return _deserialize_platform_manual_transfer_summary(obj)
    except Exception:
        pass
    try:
        return _deserialize_platform_order_transfer_summary(obj)
    except Exception:
        pass
    try:
        return _deserialize_platform_order_cancel_transfer_summary(obj)
    except Exception:
        pass
    raise ValueError(f"{repr(obj)} is not PlatformTransferSummary")
