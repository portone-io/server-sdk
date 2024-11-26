from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field
from ...platform.transfer.platform_port_one_payment_cancel_amount_type import PlatformPortOnePaymentCancelAmountType, _deserialize_platform_port_one_payment_cancel_amount_type, _serialize_platform_port_one_payment_cancel_amount_type

@dataclass
class PlatformSettlementCancelAmountExceededPortOneCancelError:
    """정산 취소 요청 금액이 포트원 결제 취소 내역의 취소 금액을 초과한 경우
    """
    registered_settlement_cancel_amount: int
    """(int64)
    """
    request_settlement_cancel_amount: int
    """(int64)
    """
    port_one_cancel_amount: int
    """(int64)
    """
    amount_type: PlatformPortOnePaymentCancelAmountType
    message: Optional[str] = field(default=None)


def _serialize_platform_settlement_cancel_amount_exceeded_port_one_cancel_error(obj: PlatformSettlementCancelAmountExceededPortOneCancelError) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["type"] = "PLATFORM_SETTLEMENT_CANCEL_AMOUNT_EXCEEDED_PORT_ONE_CANCEL"
    entity["registeredSettlementCancelAmount"] = obj.registered_settlement_cancel_amount
    entity["requestSettlementCancelAmount"] = obj.request_settlement_cancel_amount
    entity["portOneCancelAmount"] = obj.port_one_cancel_amount
    entity["amountType"] = _serialize_platform_port_one_payment_cancel_amount_type(obj.amount_type)
    if obj.message is not None:
        entity["message"] = obj.message
    return entity


def _deserialize_platform_settlement_cancel_amount_exceeded_port_one_cancel_error(obj: Any) -> PlatformSettlementCancelAmountExceededPortOneCancelError:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "type" not in obj:
        raise KeyError(f"'type' is not in {obj}")
    type = obj["type"]
    if type != "PLATFORM_SETTLEMENT_CANCEL_AMOUNT_EXCEEDED_PORT_ONE_CANCEL":
        raise ValueError(f"{repr(type)} is not 'PLATFORM_SETTLEMENT_CANCEL_AMOUNT_EXCEEDED_PORT_ONE_CANCEL'")
    if "registeredSettlementCancelAmount" not in obj:
        raise KeyError(f"'registeredSettlementCancelAmount' is not in {obj}")
    registered_settlement_cancel_amount = obj["registeredSettlementCancelAmount"]
    if not isinstance(registered_settlement_cancel_amount, int):
        raise ValueError(f"{repr(registered_settlement_cancel_amount)} is not int")
    if "requestSettlementCancelAmount" not in obj:
        raise KeyError(f"'requestSettlementCancelAmount' is not in {obj}")
    request_settlement_cancel_amount = obj["requestSettlementCancelAmount"]
    if not isinstance(request_settlement_cancel_amount, int):
        raise ValueError(f"{repr(request_settlement_cancel_amount)} is not int")
    if "portOneCancelAmount" not in obj:
        raise KeyError(f"'portOneCancelAmount' is not in {obj}")
    port_one_cancel_amount = obj["portOneCancelAmount"]
    if not isinstance(port_one_cancel_amount, int):
        raise ValueError(f"{repr(port_one_cancel_amount)} is not int")
    if "amountType" not in obj:
        raise KeyError(f"'amountType' is not in {obj}")
    amount_type = obj["amountType"]
    amount_type = _deserialize_platform_port_one_payment_cancel_amount_type(amount_type)
    if "message" in obj:
        message = obj["message"]
        if not isinstance(message, str):
            raise ValueError(f"{repr(message)} is not str")
    else:
        message = None
    return PlatformSettlementCancelAmountExceededPortOneCancelError(registered_settlement_cancel_amount, request_settlement_cancel_amount, port_one_cancel_amount, amount_type, message)
