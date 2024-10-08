from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field
from portone_server_sdk._generated.platform.transfer.create_platform_order_transfer_body_order_line import CreatePlatformOrderTransferBodyOrderLine, _deserialize_create_platform_order_transfer_body_order_line, _serialize_create_platform_order_transfer_body_order_line

@dataclass
class CreatePlatformOrderTransferBodyOrderDetail:
    """주문 정보

    주문 금액 또는 주문 항목 하나만 입력 가능합니다.
    """
    order_amount: Optional[int]
    """주문 금액
    (int64)
    """
    order_lines: Optional[list[CreatePlatformOrderTransferBodyOrderLine]]
    """주문 항목 리스트
    """


def _serialize_create_platform_order_transfer_body_order_detail(obj: CreatePlatformOrderTransferBodyOrderDetail) -> Any:
    entity = {}
    if obj.order_amount is not None:
        entity["orderAmount"] = obj.order_amount
    if obj.order_lines is not None:
        entity["orderLines"] = list(map(_serialize_create_platform_order_transfer_body_order_line, obj.order_lines))
    return entity


def _deserialize_create_platform_order_transfer_body_order_detail(obj: Any) -> CreatePlatformOrderTransferBodyOrderDetail:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "orderAmount" in obj:
        order_amount = obj["orderAmount"]
        if not isinstance(order_amount, int):
            raise ValueError(f"{repr(order_amount)} is not int")
    else:
        order_amount = None
    if "orderLines" in obj:
        order_lines = obj["orderLines"]
        if not isinstance(order_lines, list):
            raise ValueError(f"{repr(order_lines)} is not list")
        for i, item in enumerate(order_lines):
            item = _deserialize_create_platform_order_transfer_body_order_line(item)
            order_lines[i] = item
    else:
        order_lines = None
    return CreatePlatformOrderTransferBodyOrderDetail(order_amount, order_lines)
