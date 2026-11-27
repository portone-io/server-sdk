from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field
from ...common.currency import Currency, _deserialize_currency, _serialize_currency
from ...common.payment_method_type import PaymentMethodType, _deserialize_payment_method_type, _serialize_payment_method_type

@dataclass
class PlatformTransferSummaryPortOnePayment:
    id: str
    order_name: str
    currency: Currency
    method_type: Optional[PaymentMethodType] = field(default=None)


def _serialize_platform_transfer_summary_port_one_payment(obj: PlatformTransferSummaryPortOnePayment) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["type"] = "PORT_ONE"
    entity["id"] = obj.id
    entity["orderName"] = obj.order_name
    entity["currency"] = _serialize_currency(obj.currency)
    if obj.method_type is not None:
        entity["methodType"] = _serialize_payment_method_type(obj.method_type)
    return entity


def _deserialize_platform_transfer_summary_port_one_payment(obj: Any) -> PlatformTransferSummaryPortOnePayment:
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
    if "orderName" not in obj:
        raise KeyError("Missing required field 'orderName'")
    order_name = obj["orderName"]
    if not isinstance(order_name, str):
        raise ValueError("Expected str for order_name")
    if "currency" not in obj:
        raise KeyError("Missing required field 'currency'")
    currency = obj["currency"]
    currency = _deserialize_currency(currency)
    if "methodType" in obj:
        method_type = obj["methodType"]
        method_type = _deserialize_payment_method_type(method_type)
    else:
        method_type = None
    return PlatformTransferSummaryPortOnePayment(id, order_name, currency, method_type)
