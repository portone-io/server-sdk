from __future__ import annotations
from typing import Any, Literal, Optional
from dataclasses import dataclass, field
from portone_server_sdk._generated.common.currency import Currency, _deserialize_currency, _serialize_currency
from portone_server_sdk._generated.platform.transfer.platform_payment_method import PlatformPaymentMethod, _deserialize_platform_payment_method, _serialize_platform_payment_method

@dataclass
class PlatformExternalPayment:
    """외부 결제 정보
    """
    type: Literal["EXTERNAL"] = field(repr=False)
    id: str
    """결제 아이디
    """
    currency: Currency
    """통화
    """
    order_name: Optional[str]
    """주문 명
    """
    method: Optional[PlatformPaymentMethod]
    """결제 수단
    """
    paid_at: Optional[str]
    """결제 일시
    (RFC 3339 date-time)
    """


def _serialize_platform_external_payment(obj: PlatformExternalPayment) -> Any:
    entity = {}
    entity["type"] = "EXTERNAL"
    entity["id"] = obj.id
    entity["currency"] = _serialize_currency(obj.currency)
    if obj.order_name is not None:
        entity["orderName"] = obj.order_name
    if obj.method is not None:
        entity["method"] = _serialize_platform_payment_method(obj.method)
    if obj.paid_at is not None:
        entity["paidAt"] = obj.paid_at
    return entity


def _deserialize_platform_external_payment(obj: Any) -> PlatformExternalPayment:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "type" not in obj:
        raise KeyError(f"'type' is not in {obj}")
    type = obj["type"]
    if type != "EXTERNAL":
        raise ValueError(f"{repr(type)} is not 'EXTERNAL'")
    if "id" not in obj:
        raise KeyError(f"'id' is not in {obj}")
    id = obj["id"]
    if not isinstance(id, str):
        raise ValueError(f"{repr(id)} is not str")
    if "currency" not in obj:
        raise KeyError(f"'currency' is not in {obj}")
    currency = obj["currency"]
    currency = _deserialize_currency(currency)
    if "orderName" in obj:
        order_name = obj["orderName"]
        if not isinstance(order_name, str):
            raise ValueError(f"{repr(order_name)} is not str")
    else:
        order_name = None
    if "method" in obj:
        method = obj["method"]
        method = _deserialize_platform_payment_method(method)
    else:
        method = None
    if "paidAt" in obj:
        paid_at = obj["paidAt"]
        if not isinstance(paid_at, str):
            raise ValueError(f"{repr(paid_at)} is not str")
    else:
        paid_at = None
    return PlatformExternalPayment(type, id, currency, order_name, method, paid_at)
