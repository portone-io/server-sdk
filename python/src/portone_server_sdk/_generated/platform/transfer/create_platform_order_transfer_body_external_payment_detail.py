from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field
from portone_server_sdk._generated.common.currency import Currency, _deserialize_currency, _serialize_currency
from portone_server_sdk._generated.platform.transfer.platform_payment_method_input import PlatformPaymentMethodInput, _deserialize_platform_payment_method_input, _serialize_platform_payment_method_input

@dataclass
class CreatePlatformOrderTransferBodyExternalPaymentDetail:
    """외부 결제 상세 정보
    """
    currency: Currency
    """통화
    """
    order_name: Optional[str]
    """주문 명
    """
    paid_at: Optional[str]
    """결제 일시
    (RFC 3339 date-time)
    """
    method: Optional[PlatformPaymentMethodInput]
    """결제 수단
    """


def _serialize_create_platform_order_transfer_body_external_payment_detail(obj: CreatePlatformOrderTransferBodyExternalPaymentDetail) -> Any:
    entity = {}
    entity["currency"] = _serialize_currency(obj.currency)
    if obj.order_name is not None:
        entity["orderName"] = obj.order_name
    if obj.paid_at is not None:
        entity["paidAt"] = obj.paid_at
    if obj.method is not None:
        entity["method"] = _serialize_platform_payment_method_input(obj.method)
    return entity


def _deserialize_create_platform_order_transfer_body_external_payment_detail(obj: Any) -> CreatePlatformOrderTransferBodyExternalPaymentDetail:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
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
    if "paidAt" in obj:
        paid_at = obj["paidAt"]
        if not isinstance(paid_at, str):
            raise ValueError(f"{repr(paid_at)} is not str")
    else:
        paid_at = None
    if "method" in obj:
        method = obj["method"]
        method = _deserialize_platform_payment_method_input(method)
    else:
        method = None
    return CreatePlatformOrderTransferBodyExternalPaymentDetail(currency, order_name, paid_at, method)
