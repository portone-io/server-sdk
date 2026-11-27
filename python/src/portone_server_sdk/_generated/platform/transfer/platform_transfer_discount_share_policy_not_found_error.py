from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class PlatformTransferDiscountSharePolicyNotFoundError:
    discount_share_policy_id: str
    discount_share_policy_graphql_id: str
    product_id: Optional[str] = field(default=None)
    message: Optional[str] = field(default=None)


def _serialize_platform_transfer_discount_share_policy_not_found_error(obj: PlatformTransferDiscountSharePolicyNotFoundError) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["type"] = "PLATFORM_TRANSFER_DISCOUNT_SHARE_POLICY_NOT_FOUND"
    entity["discountSharePolicyId"] = obj.discount_share_policy_id
    entity["discountSharePolicyGraphqlId"] = obj.discount_share_policy_graphql_id
    if obj.product_id is not None:
        entity["productId"] = obj.product_id
    if obj.message is not None:
        entity["message"] = obj.message
    return entity


def _deserialize_platform_transfer_discount_share_policy_not_found_error(obj: Any) -> PlatformTransferDiscountSharePolicyNotFoundError:
    if not isinstance(obj, dict):
        raise ValueError("Expected dict for obj")
    if "type" not in obj:
        raise KeyError("Missing required field 'type'")
    type = obj["type"]
    if type != "PLATFORM_TRANSFER_DISCOUNT_SHARE_POLICY_NOT_FOUND":
        raise ValueError("Expected 'PLATFORM_TRANSFER_DISCOUNT_SHARE_POLICY_NOT_FOUND' for type")
    if "discountSharePolicyId" not in obj:
        raise KeyError("Missing required field 'discountSharePolicyId'")
    discount_share_policy_id = obj["discountSharePolicyId"]
    if not isinstance(discount_share_policy_id, str):
        raise ValueError("Expected str for discount_share_policy_id")
    if "discountSharePolicyGraphqlId" not in obj:
        raise KeyError("Missing required field 'discountSharePolicyGraphqlId'")
    discount_share_policy_graphql_id = obj["discountSharePolicyGraphqlId"]
    if not isinstance(discount_share_policy_graphql_id, str):
        raise ValueError("Expected str for discount_share_policy_graphql_id")
    if "productId" in obj:
        product_id = obj["productId"]
        if not isinstance(product_id, str):
            raise ValueError("Expected str for product_id")
    else:
        product_id = None
    if "message" in obj:
        message = obj["message"]
        if not isinstance(message, str):
            raise ValueError("Expected str for message")
    else:
        message = None
    return PlatformTransferDiscountSharePolicyNotFoundError(discount_share_policy_id, discount_share_policy_graphql_id, product_id, message)
