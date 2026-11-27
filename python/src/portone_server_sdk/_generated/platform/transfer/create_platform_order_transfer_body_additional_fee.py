from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class CreatePlatformOrderTransferBodyAdditionalFee:
    """추가 수수료 정보
    """
    policy_id: str
    """추가 수수료 정책 아이디
    """


def _serialize_create_platform_order_transfer_body_additional_fee(obj: CreatePlatformOrderTransferBodyAdditionalFee) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["policyId"] = obj.policy_id
    return entity


def _deserialize_create_platform_order_transfer_body_additional_fee(obj: Any) -> CreatePlatformOrderTransferBodyAdditionalFee:
    if not isinstance(obj, dict):
        raise ValueError("Expected dict for obj")
    if "policyId" not in obj:
        raise KeyError("Missing required field 'policyId'")
    policy_id = obj["policyId"]
    if not isinstance(policy_id, str):
        raise ValueError("Expected str for policy_id")
    return CreatePlatformOrderTransferBodyAdditionalFee(policy_id)
