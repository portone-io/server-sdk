from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class PlatformSettlementTaxFreeAmountExceededPortOnePaymentError:
    """정산 요청 면세 금액이 포트원 결제 내역의 면세 금액을 초과한 경우
    """
    registered_settlement_tax_free_amount: int
    """(int64)
    """
    request_settlement_tax_free_amount: int
    """(int64)
    """
    port_one_tax_free_amount: int
    """(int64)
    """
    message: Optional[str] = field(default=None)


def _serialize_platform_settlement_tax_free_amount_exceeded_port_one_payment_error(obj: PlatformSettlementTaxFreeAmountExceededPortOnePaymentError) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["type"] = "PLATFORM_SETTLEMENT_TAX_FREE_AMOUNT_EXCEEDED_PORT_ONE_PAYMENT"
    entity["registeredSettlementTaxFreeAmount"] = obj.registered_settlement_tax_free_amount
    entity["requestSettlementTaxFreeAmount"] = obj.request_settlement_tax_free_amount
    entity["portOneTaxFreeAmount"] = obj.port_one_tax_free_amount
    if obj.message is not None:
        entity["message"] = obj.message
    return entity


def _deserialize_platform_settlement_tax_free_amount_exceeded_port_one_payment_error(obj: Any) -> PlatformSettlementTaxFreeAmountExceededPortOnePaymentError:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "type" not in obj:
        raise KeyError(f"'type' is not in {obj}")
    type = obj["type"]
    if type != "PLATFORM_SETTLEMENT_TAX_FREE_AMOUNT_EXCEEDED_PORT_ONE_PAYMENT":
        raise ValueError(f"{repr(type)} is not 'PLATFORM_SETTLEMENT_TAX_FREE_AMOUNT_EXCEEDED_PORT_ONE_PAYMENT'")
    if "registeredSettlementTaxFreeAmount" not in obj:
        raise KeyError(f"'registeredSettlementTaxFreeAmount' is not in {obj}")
    registered_settlement_tax_free_amount = obj["registeredSettlementTaxFreeAmount"]
    if not isinstance(registered_settlement_tax_free_amount, int):
        raise ValueError(f"{repr(registered_settlement_tax_free_amount)} is not int")
    if "requestSettlementTaxFreeAmount" not in obj:
        raise KeyError(f"'requestSettlementTaxFreeAmount' is not in {obj}")
    request_settlement_tax_free_amount = obj["requestSettlementTaxFreeAmount"]
    if not isinstance(request_settlement_tax_free_amount, int):
        raise ValueError(f"{repr(request_settlement_tax_free_amount)} is not int")
    if "portOneTaxFreeAmount" not in obj:
        raise KeyError(f"'portOneTaxFreeAmount' is not in {obj}")
    port_one_tax_free_amount = obj["portOneTaxFreeAmount"]
    if not isinstance(port_one_tax_free_amount, int):
        raise ValueError(f"{repr(port_one_tax_free_amount)} is not int")
    if "message" in obj:
        message = obj["message"]
        if not isinstance(message, str):
            raise ValueError(f"{repr(message)} is not str")
    else:
        message = None
    return PlatformSettlementTaxFreeAmountExceededPortOnePaymentError(registered_settlement_tax_free_amount, request_settlement_tax_free_amount, port_one_tax_free_amount, message)
