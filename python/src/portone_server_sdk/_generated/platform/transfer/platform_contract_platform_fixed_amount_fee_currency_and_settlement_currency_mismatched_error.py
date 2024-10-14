from __future__ import annotations
from typing import Any, Literal, Optional
from dataclasses import dataclass, field
from portone_server_sdk._generated.common.currency import Currency, _deserialize_currency, _serialize_currency

@dataclass
class PlatformContractPlatformFixedAmountFeeCurrencyAndSettlementCurrencyMismatchedError:
    type: Literal["PLATFORM_CONTRACT_PLATFORM_FIXED_AMOUNT_FEE_CURRENCY_AND_SETTLEMENT_CURRENCY_MISMATCHED"] = field(repr=False)
    id: str
    graphql_id: str
    fee_currency: Currency
    settlement_currency: Currency
    message: Optional[str]


def _serialize_platform_contract_platform_fixed_amount_fee_currency_and_settlement_currency_mismatched_error(obj: PlatformContractPlatformFixedAmountFeeCurrencyAndSettlementCurrencyMismatchedError) -> Any:
    entity = {}
    entity["type"] = "PLATFORM_CONTRACT_PLATFORM_FIXED_AMOUNT_FEE_CURRENCY_AND_SETTLEMENT_CURRENCY_MISMATCHED"
    entity["id"] = obj.id
    entity["graphqlId"] = obj.graphql_id
    entity["feeCurrency"] = _serialize_currency(obj.fee_currency)
    entity["settlementCurrency"] = _serialize_currency(obj.settlement_currency)
    if obj.message is not None:
        entity["message"] = obj.message
    return entity


def _deserialize_platform_contract_platform_fixed_amount_fee_currency_and_settlement_currency_mismatched_error(obj: Any) -> PlatformContractPlatformFixedAmountFeeCurrencyAndSettlementCurrencyMismatchedError:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "type" not in obj:
        raise KeyError(f"'type' is not in {obj}")
    type = obj["type"]
    if type != "PLATFORM_CONTRACT_PLATFORM_FIXED_AMOUNT_FEE_CURRENCY_AND_SETTLEMENT_CURRENCY_MISMATCHED":
        raise ValueError(f"{repr(type)} is not 'PLATFORM_CONTRACT_PLATFORM_FIXED_AMOUNT_FEE_CURRENCY_AND_SETTLEMENT_CURRENCY_MISMATCHED'")
    if "id" not in obj:
        raise KeyError(f"'id' is not in {obj}")
    id = obj["id"]
    if not isinstance(id, str):
        raise ValueError(f"{repr(id)} is not str")
    if "graphqlId" not in obj:
        raise KeyError(f"'graphqlId' is not in {obj}")
    graphql_id = obj["graphqlId"]
    if not isinstance(graphql_id, str):
        raise ValueError(f"{repr(graphql_id)} is not str")
    if "feeCurrency" not in obj:
        raise KeyError(f"'feeCurrency' is not in {obj}")
    fee_currency = obj["feeCurrency"]
    fee_currency = _deserialize_currency(fee_currency)
    if "settlementCurrency" not in obj:
        raise KeyError(f"'settlementCurrency' is not in {obj}")
    settlement_currency = obj["settlementCurrency"]
    settlement_currency = _deserialize_currency(settlement_currency)
    if "message" in obj:
        message = obj["message"]
        if not isinstance(message, str):
            raise ValueError(f"{repr(message)} is not str")
    else:
        message = None
    return PlatformContractPlatformFixedAmountFeeCurrencyAndSettlementCurrencyMismatchedError(type, id, graphql_id, fee_currency, settlement_currency, message)
