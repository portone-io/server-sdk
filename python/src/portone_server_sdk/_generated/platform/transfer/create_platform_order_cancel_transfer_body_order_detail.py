from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field
from ...platform.transfer.create_platform_order_cancel_transfer_body_order_detail_all import CreatePlatformOrderCancelTransferBodyOrderDetailAll, _deserialize_create_platform_order_cancel_transfer_body_order_detail_all, _serialize_create_platform_order_cancel_transfer_body_order_detail_all
from ...platform.transfer.create_platform_order_cancel_transfer_body_order_line import CreatePlatformOrderCancelTransferBodyOrderLine, _deserialize_create_platform_order_cancel_transfer_body_order_line, _serialize_create_platform_order_cancel_transfer_body_order_line

@dataclass
class CreatePlatformOrderCancelTransferBodyOrderDetail:
    """주문 취소 정보

    orderAmount, orderLines, all 중에서 하나만 입력하여야 합니다.
    """
    order_amount: Optional[int] = field(default=None)
    """주문 취소 금액
    (int64)
    """
    order_lines: Optional[list[CreatePlatformOrderCancelTransferBodyOrderLine]] = field(default=None)
    """주문 취소 항목 리스트
    """
    all: Optional[CreatePlatformOrderCancelTransferBodyOrderDetailAll] = field(default=None)
    """전체 금액 취소
    """


def _serialize_create_platform_order_cancel_transfer_body_order_detail(obj: CreatePlatformOrderCancelTransferBodyOrderDetail) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    if obj.order_amount is not None:
        entity["orderAmount"] = obj.order_amount
    if obj.order_lines is not None:
        entity["orderLines"] = list(map(_serialize_create_platform_order_cancel_transfer_body_order_line, obj.order_lines))
    if obj.all is not None:
        entity["all"] = _serialize_create_platform_order_cancel_transfer_body_order_detail_all(obj.all)
    return entity


def _deserialize_create_platform_order_cancel_transfer_body_order_detail(obj: Any) -> CreatePlatformOrderCancelTransferBodyOrderDetail:
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
            item = _deserialize_create_platform_order_cancel_transfer_body_order_line(item)
            order_lines[i] = item
    else:
        order_lines = None
    if "all" in obj:
        all = obj["all"]
        all = _deserialize_create_platform_order_cancel_transfer_body_order_detail_all(all)
    else:
        all = None
    return CreatePlatformOrderCancelTransferBodyOrderDetail(order_amount, order_lines, all)
