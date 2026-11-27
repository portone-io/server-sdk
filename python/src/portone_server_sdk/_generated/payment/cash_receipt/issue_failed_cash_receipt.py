from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field
from ...common.selected_channel import SelectedChannel, _deserialize_selected_channel, _serialize_selected_channel

@dataclass
class IssueFailedCashReceipt:
    """발급 실패
    """
    """현금영수증 상태
    """
    merchant_id: str
    """고객사 아이디
    """
    store_id: str
    """상점 아이디
    """
    payment_id: str
    """결제 건 아이디
    """
    order_name: str
    """주문명
    """
    is_manual: bool
    """수동 발급 여부
    """
    channel: Optional[SelectedChannel] = field(default=None)
    """현금영수증 발급에 사용된 채널
    """
    status_updated_at: Optional[str] = field(default=None)
    """상태 업데이트 시점
    (RFC 3339 date-time)
    """


def _serialize_issue_failed_cash_receipt(obj: IssueFailedCashReceipt) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["status"] = "ISSUE_FAILED"
    entity["merchantId"] = obj.merchant_id
    entity["storeId"] = obj.store_id
    entity["paymentId"] = obj.payment_id
    entity["orderName"] = obj.order_name
    entity["isManual"] = obj.is_manual
    if obj.channel is not None:
        entity["channel"] = _serialize_selected_channel(obj.channel)
    if obj.status_updated_at is not None:
        entity["statusUpdatedAt"] = obj.status_updated_at
    return entity


def _deserialize_issue_failed_cash_receipt(obj: Any) -> IssueFailedCashReceipt:
    if not isinstance(obj, dict):
        raise ValueError("Expected dict for obj")
    if "status" not in obj:
        raise KeyError("Missing required field 'status'")
    status = obj["status"]
    if status != "ISSUE_FAILED":
        raise ValueError("Expected 'ISSUE_FAILED' for status")
    if "merchantId" not in obj:
        raise KeyError("Missing required field 'merchantId'")
    merchant_id = obj["merchantId"]
    if not isinstance(merchant_id, str):
        raise ValueError("Expected str for merchant_id")
    if "storeId" not in obj:
        raise KeyError("Missing required field 'storeId'")
    store_id = obj["storeId"]
    if not isinstance(store_id, str):
        raise ValueError("Expected str for store_id")
    if "paymentId" not in obj:
        raise KeyError("Missing required field 'paymentId'")
    payment_id = obj["paymentId"]
    if not isinstance(payment_id, str):
        raise ValueError("Expected str for payment_id")
    if "orderName" not in obj:
        raise KeyError("Missing required field 'orderName'")
    order_name = obj["orderName"]
    if not isinstance(order_name, str):
        raise ValueError("Expected str for order_name")
    if "isManual" not in obj:
        raise KeyError("Missing required field 'isManual'")
    is_manual = obj["isManual"]
    if not isinstance(is_manual, bool):
        raise ValueError("Expected bool for is_manual")
    if "channel" in obj:
        channel = obj["channel"]
        channel = _deserialize_selected_channel(channel)
    else:
        channel = None
    if "statusUpdatedAt" in obj:
        status_updated_at = obj["statusUpdatedAt"]
        if not isinstance(status_updated_at, str):
            raise ValueError("Expected str for status_updated_at")
    else:
        status_updated_at = None
    return IssueFailedCashReceipt(merchant_id, store_id, payment_id, order_name, is_manual, channel, status_updated_at)
