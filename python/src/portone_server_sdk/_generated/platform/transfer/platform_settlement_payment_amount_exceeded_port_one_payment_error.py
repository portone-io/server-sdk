from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class PlatformSettlementPaymentAmountExceededPortOnePaymentError:
    """정산 요청 결제 금액이 포트원 결제 내역의 결제 금액을 초과한 경우
    """
    registered_settlement_payment_amount: int
    """(int64)
    """
    request_settlement_payment_amount: int
    """(int64)
    """
    port_one_payment_amount: int
    """(int64)
    """
    message: Optional[str] = field(default=None)


def _serialize_platform_settlement_payment_amount_exceeded_port_one_payment_error(obj: PlatformSettlementPaymentAmountExceededPortOnePaymentError) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["type"] = "PLATFORM_SETTLEMENT_PAYMENT_AMOUNT_EXCEEDED_PORT_ONE_PAYMENT"
    entity["registeredSettlementPaymentAmount"] = obj.registered_settlement_payment_amount
    entity["requestSettlementPaymentAmount"] = obj.request_settlement_payment_amount
    entity["portOnePaymentAmount"] = obj.port_one_payment_amount
    if obj.message is not None:
        entity["message"] = obj.message
    return entity


def _deserialize_platform_settlement_payment_amount_exceeded_port_one_payment_error(obj: Any) -> PlatformSettlementPaymentAmountExceededPortOnePaymentError:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "type" not in obj:
        raise KeyError(f"'type' is not in {obj}")
    type = obj["type"]
    if type != "PLATFORM_SETTLEMENT_PAYMENT_AMOUNT_EXCEEDED_PORT_ONE_PAYMENT":
        raise ValueError(f"{repr(type)} is not 'PLATFORM_SETTLEMENT_PAYMENT_AMOUNT_EXCEEDED_PORT_ONE_PAYMENT'")
    if "registeredSettlementPaymentAmount" not in obj:
        raise KeyError(f"'registeredSettlementPaymentAmount' is not in {obj}")
    registered_settlement_payment_amount = obj["registeredSettlementPaymentAmount"]
    if not isinstance(registered_settlement_payment_amount, int):
        raise ValueError(f"{repr(registered_settlement_payment_amount)} is not int")
    if "requestSettlementPaymentAmount" not in obj:
        raise KeyError(f"'requestSettlementPaymentAmount' is not in {obj}")
    request_settlement_payment_amount = obj["requestSettlementPaymentAmount"]
    if not isinstance(request_settlement_payment_amount, int):
        raise ValueError(f"{repr(request_settlement_payment_amount)} is not int")
    if "portOnePaymentAmount" not in obj:
        raise KeyError(f"'portOnePaymentAmount' is not in {obj}")
    port_one_payment_amount = obj["portOnePaymentAmount"]
    if not isinstance(port_one_payment_amount, int):
        raise ValueError(f"{repr(port_one_payment_amount)} is not int")
    if "message" in obj:
        message = obj["message"]
        if not isinstance(message, str):
            raise ValueError(f"{repr(message)} is not str")
    else:
        message = None
    return PlatformSettlementPaymentAmountExceededPortOnePaymentError(registered_settlement_payment_amount, request_settlement_payment_amount, port_one_payment_amount, message)
