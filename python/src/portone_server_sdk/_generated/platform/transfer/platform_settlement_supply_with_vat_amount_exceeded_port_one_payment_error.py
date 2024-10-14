from __future__ import annotations
from typing import Any, Literal, Optional
from dataclasses import dataclass, field

@dataclass
class PlatformSettlementSupplyWithVatAmountExceededPortOnePaymentError:
    """정산 요청 공급대가가 포트원 결제 내역의 공급대가를 초과한 경우
    """
    type: Literal["PLATFORM_SETTLEMENT_SUPPLY_WITH_VAT_AMOUNT_EXCEEDED_PORT_ONE_PAYMENT"] = field(repr=False)
    registered_settlement_supply_with_vat_amount: int
    """(int64)
    """
    request_settlement_supply_with_vat_amount: int
    """(int64)
    """
    port_one_supply_with_vat_amount: int
    """(int64)
    """
    message: Optional[str]


def _serialize_platform_settlement_supply_with_vat_amount_exceeded_port_one_payment_error(obj: PlatformSettlementSupplyWithVatAmountExceededPortOnePaymentError) -> Any:
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
        raise ValueError(f"{repr(obj)} is not dict")
    if "type" not in obj:
        raise KeyError(f"'type' is not in {obj}")
    type = obj["type"]
    if type != "PLATFORM_SETTLEMENT_SUPPLY_WITH_VAT_AMOUNT_EXCEEDED_PORT_ONE_PAYMENT":
        raise ValueError(f"{repr(type)} is not 'PLATFORM_SETTLEMENT_SUPPLY_WITH_VAT_AMOUNT_EXCEEDED_PORT_ONE_PAYMENT'")
    if "registeredSettlementSupplyWithVatAmount" not in obj:
        raise KeyError(f"'registeredSettlementSupplyWithVatAmount' is not in {obj}")
    registered_settlement_supply_with_vat_amount = obj["registeredSettlementSupplyWithVatAmount"]
    if not isinstance(registered_settlement_supply_with_vat_amount, int):
        raise ValueError(f"{repr(registered_settlement_supply_with_vat_amount)} is not int")
    if "requestSettlementSupplyWithVatAmount" not in obj:
        raise KeyError(f"'requestSettlementSupplyWithVatAmount' is not in {obj}")
    request_settlement_supply_with_vat_amount = obj["requestSettlementSupplyWithVatAmount"]
    if not isinstance(request_settlement_supply_with_vat_amount, int):
        raise ValueError(f"{repr(request_settlement_supply_with_vat_amount)} is not int")
    if "portOneSupplyWithVatAmount" not in obj:
        raise KeyError(f"'portOneSupplyWithVatAmount' is not in {obj}")
    port_one_supply_with_vat_amount = obj["portOneSupplyWithVatAmount"]
    if not isinstance(port_one_supply_with_vat_amount, int):
        raise ValueError(f"{repr(port_one_supply_with_vat_amount)} is not int")
    if "message" in obj:
        message = obj["message"]
        if not isinstance(message, str):
            raise ValueError(f"{repr(message)} is not str")
    else:
        message = None
    return PlatformSettlementSupplyWithVatAmountExceededPortOnePaymentError(type, registered_settlement_supply_with_vat_amount, request_settlement_supply_with_vat_amount, port_one_supply_with_vat_amount, message)
