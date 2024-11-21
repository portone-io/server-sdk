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
    return entity


def _deserialize_issue_failed_cash_receipt(obj: Any) -> IssueFailedCashReceipt:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "status" not in obj:
        raise KeyError(f"'status' is not in {obj}")
    status = obj["status"]
    if status != "ISSUE_FAILED":
        raise ValueError(f"{repr(status)} is not 'ISSUE_FAILED'")
    if "merchantId" not in obj:
        raise KeyError(f"'merchantId' is not in {obj}")
    merchant_id = obj["merchantId"]
    if not isinstance(merchant_id, str):
        raise ValueError(f"{repr(merchant_id)} is not str")
    if "storeId" not in obj:
        raise KeyError(f"'storeId' is not in {obj}")
    store_id = obj["storeId"]
    if not isinstance(store_id, str):
        raise ValueError(f"{repr(store_id)} is not str")
    if "paymentId" not in obj:
        raise KeyError(f"'paymentId' is not in {obj}")
    payment_id = obj["paymentId"]
    if not isinstance(payment_id, str):
        raise ValueError(f"{repr(payment_id)} is not str")
    if "orderName" not in obj:
        raise KeyError(f"'orderName' is not in {obj}")
    order_name = obj["orderName"]
    if not isinstance(order_name, str):
        raise ValueError(f"{repr(order_name)} is not str")
    if "isManual" not in obj:
        raise KeyError(f"'isManual' is not in {obj}")
    is_manual = obj["isManual"]
    if not isinstance(is_manual, bool):
        raise ValueError(f"{repr(is_manual)} is not bool")
    if "channel" in obj:
        channel = obj["channel"]
        channel = _deserialize_selected_channel(channel)
    else:
        channel = None
    return IssueFailedCashReceipt(merchant_id, store_id, payment_id, order_name, is_manual, channel)
