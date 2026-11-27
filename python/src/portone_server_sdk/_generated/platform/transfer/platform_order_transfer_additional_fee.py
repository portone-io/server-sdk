from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field
from ...platform.platform_additional_fee_policy import PlatformAdditionalFeePolicy, _deserialize_platform_additional_fee_policy, _serialize_platform_additional_fee_policy

@dataclass
class PlatformOrderTransferAdditionalFee:
    """추가 수수료 정보
    """
    policy: PlatformAdditionalFeePolicy
    """추가 수수료 정책
    """
    amount: int
    """추가 수수료 금액
    (int64)
    """
    vat: int
    """추가 수수료 부가세 금액
    (int64)
    """


def _serialize_platform_order_transfer_additional_fee(obj: PlatformOrderTransferAdditionalFee) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["policy"] = _serialize_platform_additional_fee_policy(obj.policy)
    entity["amount"] = obj.amount
    entity["vat"] = obj.vat
    return entity


def _deserialize_platform_order_transfer_additional_fee(obj: Any) -> PlatformOrderTransferAdditionalFee:
    if not isinstance(obj, dict):
        raise ValueError("Expected dict for obj")
    if "policy" not in obj:
        raise KeyError("Missing required field 'policy'")
    policy = obj["policy"]
    policy = _deserialize_platform_additional_fee_policy(policy)
    if "amount" not in obj:
        raise KeyError("Missing required field 'amount'")
    amount = obj["amount"]
    if not isinstance(amount, int):
        raise ValueError("Expected int for amount")
    if "vat" not in obj:
        raise KeyError("Missing required field 'vat'")
    vat = obj["vat"]
    if not isinstance(vat, int):
        raise ValueError("Expected int for vat")
    return PlatformOrderTransferAdditionalFee(policy, amount, vat)
