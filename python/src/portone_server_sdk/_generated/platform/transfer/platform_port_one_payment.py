from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field
from ...common.currency import Currency, _deserialize_currency, _serialize_currency
from ...platform.transfer.platform_payment_method import PlatformPaymentMethod, _deserialize_platform_payment_method, _serialize_platform_payment_method

@dataclass
class PlatformPortOnePayment:
    """포트원 결제 정보
    """
    id: str
    """결제 아이디
    """
    store_id: str
    """상점 아이디
    """
    channel_key: str
    """채널 키
    """
    order_name: str
    """주문 명
    """
    currency: Currency
    """통화
    """
    paid_at: str
    """결제 일시
    (RFC 3339 date-time)
    """
    method: Optional[PlatformPaymentMethod] = field(default=None)
    """결제 수단
    """


def _serialize_platform_port_one_payment(obj: PlatformPortOnePayment) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["type"] = "PORT_ONE"
    entity["id"] = obj.id
    entity["storeId"] = obj.store_id
    entity["channelKey"] = obj.channel_key
    entity["orderName"] = obj.order_name
    entity["currency"] = _serialize_currency(obj.currency)
    entity["paidAt"] = obj.paid_at
    if obj.method is not None:
        entity["method"] = _serialize_platform_payment_method(obj.method)
    return entity


def _deserialize_platform_port_one_payment(obj: Any) -> PlatformPortOnePayment:
    if not isinstance(obj, dict):
        raise ValueError("Expected dict for obj")
    if "type" not in obj:
        raise KeyError("Missing required field 'type'")
    type = obj["type"]
    if type != "PORT_ONE":
        raise ValueError("Expected 'PORT_ONE' for type")
    if "id" not in obj:
        raise KeyError("Missing required field 'id'")
    id = obj["id"]
    if not isinstance(id, str):
        raise ValueError("Expected str for id")
    if "storeId" not in obj:
        raise KeyError("Missing required field 'storeId'")
    store_id = obj["storeId"]
    if not isinstance(store_id, str):
        raise ValueError("Expected str for store_id")
    if "channelKey" not in obj:
        raise KeyError("Missing required field 'channelKey'")
    channel_key = obj["channelKey"]
    if not isinstance(channel_key, str):
        raise ValueError("Expected str for channel_key")
    if "orderName" not in obj:
        raise KeyError("Missing required field 'orderName'")
    order_name = obj["orderName"]
    if not isinstance(order_name, str):
        raise ValueError("Expected str for order_name")
    if "currency" not in obj:
        raise KeyError("Missing required field 'currency'")
    currency = obj["currency"]
    currency = _deserialize_currency(currency)
    if "paidAt" not in obj:
        raise KeyError("Missing required field 'paidAt'")
    paid_at = obj["paidAt"]
    if not isinstance(paid_at, str):
        raise ValueError("Expected str for paid_at")
    if "method" in obj:
        method = obj["method"]
        method = _deserialize_platform_payment_method(method)
    else:
        method = None
    return PlatformPortOnePayment(id, store_id, channel_key, order_name, currency, paid_at, method)
