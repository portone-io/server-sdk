from __future__ import annotations
from typing import Any, Optional, Union
from portone_server_sdk._generated.platform.transfer.platform_manual_transfer import PlatformManualTransfer, _deserialize_platform_manual_transfer, _serialize_platform_manual_transfer
from portone_server_sdk._generated.platform.transfer.platform_order_cancel_transfer import PlatformOrderCancelTransfer, _deserialize_platform_order_cancel_transfer, _serialize_platform_order_cancel_transfer
from portone_server_sdk._generated.platform.transfer.platform_order_transfer import PlatformOrderTransfer, _deserialize_platform_order_transfer, _serialize_platform_order_transfer

PlatformTransfer = Union[PlatformManualTransfer, PlatformOrderTransfer, PlatformOrderCancelTransfer]
"""정산건

정산건은 파트너에 정산해줄 정산 금액과 정산 방식 등이 포함되어 있는 정산 정보입니다.
정산 방식은은 주문 정산, 주문 취소 정산, 수기 정산이 있습니다.
"""


def _serialize_platform_transfer(obj: PlatformTransfer) -> Any:
    if obj.type == "MANUAL":
        return _serialize_platform_manual_transfer(obj)
    if obj.type == "ORDER":
        return _serialize_platform_order_transfer(obj)
    if obj.type == "ORDER_CANCEL":
        return _serialize_platform_order_cancel_transfer(obj)


def _deserialize_platform_transfer(obj: Any) -> PlatformTransfer:
    try:
        return _deserialize_platform_manual_transfer(obj)
    except Exception:
        pass
    try:
        return _deserialize_platform_order_transfer(obj)
    except Exception:
        pass
    try:
        return _deserialize_platform_order_cancel_transfer(obj)
    except Exception:
        pass
    raise ValueError(f"{repr(obj)} is not PlatformTransfer")
