from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field
from ...common.currency import Currency, _deserialize_currency, _serialize_currency

@dataclass
class PlatformAdditionalFixedAmountFeeCurrencyAndSettlementCurrencyMismatchedError:
    id: str
    graphql_id: str
    fee_currency: Currency
    settlement_currency: Currency
    message: Optional[str] = field(default=None)


def _serialize_platform_additional_fixed_amount_fee_currency_and_settlement_currency_mismatched_error(obj: PlatformAdditionalFixedAmountFeeCurrencyAndSettlementCurrencyMismatchedError) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["type"] = "PLATFORM_ADDITIONAL_FIXED_AMOUNT_FEE_CURRENCY_AND_SETTLEMENT_CURRENCY_MISMATCHED"
    entity["id"] = obj.id
    entity["graphqlId"] = obj.graphql_id
    entity["feeCurrency"] = _serialize_currency(obj.fee_currency)
    entity["settlementCurrency"] = _serialize_currency(obj.settlement_currency)
    if obj.message is not None:
        entity["message"] = obj.message
    return entity


def _deserialize_platform_additional_fixed_amount_fee_currency_and_settlement_currency_mismatched_error(obj: Any) -> PlatformAdditionalFixedAmountFeeCurrencyAndSettlementCurrencyMismatchedError:
    if not isinstance(obj, dict):
        raise ValueError("Expected dict for obj")
    if "type" not in obj:
        raise KeyError("Missing required field 'type'")
    type = obj["type"]
    if type != "PLATFORM_ADDITIONAL_FIXED_AMOUNT_FEE_CURRENCY_AND_SETTLEMENT_CURRENCY_MISMATCHED":
        raise ValueError("Expected 'PLATFORM_ADDITIONAL_FIXED_AMOUNT_FEE_CURRENCY_AND_SETTLEMENT_CURRENCY_MISMATCHED' for type")
    if "id" not in obj:
        raise KeyError("Missing required field 'id'")
    id = obj["id"]
    if not isinstance(id, str):
        raise ValueError("Expected str for id")
    if "graphqlId" not in obj:
        raise KeyError("Missing required field 'graphqlId'")
    graphql_id = obj["graphqlId"]
    if not isinstance(graphql_id, str):
        raise ValueError("Expected str for graphql_id")
    if "feeCurrency" not in obj:
        raise KeyError("Missing required field 'feeCurrency'")
    fee_currency = obj["feeCurrency"]
    fee_currency = _deserialize_currency(fee_currency)
    if "settlementCurrency" not in obj:
        raise KeyError("Missing required field 'settlementCurrency'")
    settlement_currency = obj["settlementCurrency"]
    settlement_currency = _deserialize_currency(settlement_currency)
    if "message" in obj:
        message = obj["message"]
        if not isinstance(message, str):
            raise ValueError("Expected str for message")
    else:
        message = None
    return PlatformAdditionalFixedAmountFeeCurrencyAndSettlementCurrencyMismatchedError(id, graphql_id, fee_currency, settlement_currency, message)
