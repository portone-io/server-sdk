from __future__ import annotations
from typing import Any, Optional, Union
from ...platform.transfer.platform_transfer_summary_external_payment import PlatformTransferSummaryExternalPayment, _deserialize_platform_transfer_summary_external_payment, _serialize_platform_transfer_summary_external_payment
from ...platform.transfer.platform_transfer_summary_port_one_payment import PlatformTransferSummaryPortOnePayment, _deserialize_platform_transfer_summary_port_one_payment, _serialize_platform_transfer_summary_port_one_payment

PlatformTransferSummaryPayment = Union[PlatformTransferSummaryExternalPayment, PlatformTransferSummaryPortOnePayment, dict]


def _serialize_platform_transfer_summary_payment(obj: PlatformTransferSummaryPayment) -> Any:
    if isinstance(obj, dict):
        return obj
    if isinstance(obj, PlatformTransferSummaryExternalPayment):
        return _serialize_platform_transfer_summary_external_payment(obj)
    if isinstance(obj, PlatformTransferSummaryPortOnePayment):
        return _serialize_platform_transfer_summary_port_one_payment(obj)


def _deserialize_platform_transfer_summary_payment(obj: Any) -> PlatformTransferSummaryPayment:
    try:
        return _deserialize_platform_transfer_summary_external_payment(obj)
    except Exception:
        pass
    try:
        return _deserialize_platform_transfer_summary_port_one_payment(obj)
    except Exception:
        pass
    raise ValueError(f"{repr(obj)} is not PlatformTransferSummaryPayment")
