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
        raise ValueError(f"{repr(obj)} is not dict")
    if "type" not in obj:
        raise KeyError(f"'type' is not in {obj}")
    type = obj["type"]
    if type != "PORT_ONE":
        raise ValueError(f"{repr(type)} is not 'PORT_ONE'")
    if "id" not in obj:
        raise KeyError(f"'id' is not in {obj}")
    id = obj["id"]
    if not isinstance(id, str):
        raise ValueError(f"{repr(id)} is not str")
    if "storeId" not in obj:
        raise KeyError(f"'storeId' is not in {obj}")
    store_id = obj["storeId"]
    if not isinstance(store_id, str):
        raise ValueError(f"{repr(store_id)} is not str")
    if "channelKey" not in obj:
        raise KeyError(f"'channelKey' is not in {obj}")
    channel_key = obj["channelKey"]
    if not isinstance(channel_key, str):
        raise ValueError(f"{repr(channel_key)} is not str")
    if "orderName" not in obj:
        raise KeyError(f"'orderName' is not in {obj}")
    order_name = obj["orderName"]
    if not isinstance(order_name, str):
        raise ValueError(f"{repr(order_name)} is not str")
    if "currency" not in obj:
        raise KeyError(f"'currency' is not in {obj}")
    currency = obj["currency"]
    currency = _deserialize_currency(currency)
    if "paidAt" not in obj:
        raise KeyError(f"'paidAt' is not in {obj}")
    paid_at = obj["paidAt"]
    if not isinstance(paid_at, str):
        raise ValueError(f"{repr(paid_at)} is not str")
    if "method" in obj:
        method = obj["method"]
        method = _deserialize_platform_payment_method(method)
    else:
        method = None
    return PlatformPortOnePayment(id, store_id, channel_key, order_name, currency, paid_at, method)
