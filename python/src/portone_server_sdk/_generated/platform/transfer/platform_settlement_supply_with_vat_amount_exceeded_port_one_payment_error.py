from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class PlatformSettlementSupplyWithVatAmountExceededPortOnePaymentError:
    """정산 요청 공급대가가 포트원 결제 내역의 공급대가를 초과한 경우
    """
    registered_settlement_supply_with_vat_amount: int
    """(int64)
    """
    request_settlement_supply_with_vat_amount: int
    """(int64)
    """
    port_one_supply_with_vat_amount: int
    """(int64)
    """
    message: Optional[str] = field(default=None)


def _serialize_platform_settlement_supply_with_vat_amount_exceeded_port_one_payment_error(obj: PlatformSettlementSupplyWithVatAmountExceededPortOnePaymentError) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["type"] = "PLATFORM_SETTLEMENT_SUPPLY_WITH_VAT_AMOUNT_EXCEEDED_PORT_ONE_PAYMENT"
    entity["registeredSettlementSupplyWithVatAmount"] = obj.registered_settlement_supply_with_vat_amount
    entity["requestSettlementSupplyWithVatAmount"] = obj.request_settlement_supply_with_vat_amount
    entity["portOneSupplyWithVatAmount"] = obj.port_one_supply_with_vat_amount
    if obj.message is not None:
        entity["message"] = obj.message
    return entity


def _deserialize_platform_settlement_supply_with_vat_amount_exceeded_port_one_payment_error(obj: Any) -> PlatformSettlementSupplyWithVatAmountExceededPortOnePaymentError:
    if not isinstance(obj, dict):
        raise ValueError("Expected dict for obj")
    if "type" not in obj:
        raise KeyError("Missing required field 'type'")
    type = obj["type"]
    if type != "PLATFORM_SETTLEMENT_SUPPLY_WITH_VAT_AMOUNT_EXCEEDED_PORT_ONE_PAYMENT":
        raise ValueError("Expected 'PLATFORM_SETTLEMENT_SUPPLY_WITH_VAT_AMOUNT_EXCEEDED_PORT_ONE_PAYMENT' for type")
    if "registeredSettlementSupplyWithVatAmount" not in obj:
        raise KeyError("Missing required field 'registeredSettlementSupplyWithVatAmount'")
    registered_settlement_supply_with_vat_amount = obj["registeredSettlementSupplyWithVatAmount"]
    if not isinstance(registered_settlement_supply_with_vat_amount, int):
        raise ValueError("Expected int for registered_settlement_supply_with_vat_amount")
    if "requestSettlementSupplyWithVatAmount" not in obj:
        raise KeyError("Missing required field 'requestSettlementSupplyWithVatAmount'")
    request_settlement_supply_with_vat_amount = obj["requestSettlementSupplyWithVatAmount"]
    if not isinstance(request_settlement_supply_with_vat_amount, int):
        raise ValueError("Expected int for request_settlement_supply_with_vat_amount")
    if "portOneSupplyWithVatAmount" not in obj:
        raise KeyError("Missing required field 'portOneSupplyWithVatAmount'")
    port_one_supply_with_vat_amount = obj["portOneSupplyWithVatAmount"]
    if not isinstance(port_one_supply_with_vat_amount, int):
        raise ValueError("Expected int for port_one_supply_with_vat_amount")
    if "message" in obj:
        message = obj["message"]
        if not isinstance(message, str):
            raise ValueError("Expected str for message")
    else:
        message = None
    return PlatformSettlementSupplyWithVatAmountExceededPortOnePaymentError(registered_settlement_supply_with_vat_amount, request_settlement_supply_with_vat_amount, port_one_supply_with_vat_amount, message)
