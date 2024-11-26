from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field
from ...common.currency import Currency, _deserialize_currency, _serialize_currency
from ...common.payment_method_type import PaymentMethodType, _deserialize_payment_method_type, _serialize_payment_method_type

@dataclass
class PlatformTransferSummaryExternalPayment:
    id: str
    currency: Currency
    order_name: Optional[str] = field(default=None)
    method_type: Optional[PaymentMethodType] = field(default=None)


def _serialize_platform_transfer_summary_external_payment(obj: PlatformTransferSummaryExternalPayment) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["type"] = "EXTERNAL"
    entity["id"] = obj.id
    entity["currency"] = _serialize_currency(obj.currency)
    if obj.order_name is not None:
        entity["orderName"] = obj.order_name
    if obj.method_type is not None:
        entity["methodType"] = _serialize_payment_method_type(obj.method_type)
    return entity


def _deserialize_platform_transfer_summary_external_payment(obj: Any) -> PlatformTransferSummaryExternalPayment:
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
    if "methodType" in obj:
        method_type = obj["methodType"]
        method_type = _deserialize_payment_method_type(method_type)
    else:
        method_type = None
    return PlatformTransferSummaryExternalPayment(id, currency, order_name, method_type)
