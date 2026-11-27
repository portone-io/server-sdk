from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class PlatformCancellableDiscountAmountExceededError:
    discount_share_policy_id: str
    discount_share_policy_graphql_id: str
    cancellable_amount: int
    """(int64)
    """
    request_amount: int
    """(int64)
    """
    product_id: Optional[str] = field(default=None)
    message: Optional[str] = field(default=None)


def _serialize_platform_cancellable_discount_amount_exceeded_error(obj: PlatformCancellableDiscountAmountExceededError) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["type"] = "PLATFORM_CANCELLABLE_DISCOUNT_AMOUNT_EXCEEDED"
    entity["discountSharePolicyId"] = obj.discount_share_policy_id
    entity["discountSharePolicyGraphqlId"] = obj.discount_share_policy_graphql_id
    entity["cancellableAmount"] = obj.cancellable_amount
    entity["requestAmount"] = obj.request_amount
    if obj.product_id is not None:
        entity["productId"] = obj.product_id
    if obj.message is not None:
        entity["message"] = obj.message
    return entity


def _deserialize_platform_cancellable_discount_amount_exceeded_error(obj: Any) -> PlatformCancellableDiscountAmountExceededError:
    if not isinstance(obj, dict):
        raise ValueError("Expected dict for obj")
    if "type" not in obj:
        raise KeyError("Missing required field 'type'")
    type = obj["type"]
    if type != "PLATFORM_CANCELLABLE_DISCOUNT_AMOUNT_EXCEEDED":
        raise ValueError("Expected 'PLATFORM_CANCELLABLE_DISCOUNT_AMOUNT_EXCEEDED' for type")
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
    if "cancellableAmount" not in obj:
        raise KeyError("Missing required field 'cancellableAmount'")
    cancellable_amount = obj["cancellableAmount"]
    if not isinstance(cancellable_amount, int):
        raise ValueError("Expected int for cancellable_amount")
    if "requestAmount" not in obj:
        raise KeyError("Missing required field 'requestAmount'")
    request_amount = obj["requestAmount"]
    if not isinstance(request_amount, int):
        raise ValueError("Expected int for request_amount")
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
    return PlatformCancellableDiscountAmountExceededError(discount_share_policy_id, discount_share_policy_graphql_id, cancellable_amount, request_amount, product_id, message)
