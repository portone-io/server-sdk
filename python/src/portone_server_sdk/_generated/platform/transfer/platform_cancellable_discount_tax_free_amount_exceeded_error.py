from __future__ import annotations
from typing import Any, Literal, Optional
from dataclasses import dataclass, field

@dataclass
class PlatformCancellableDiscountTaxFreeAmountExceededError:
    type: Literal["PLATFORM_CANCELLABLE_DISCOUNT_TAX_FREE_AMOUNT_EXCEEDED"] = field(repr=False)
    discount_share_policy_id: str
    discount_share_policy_graphql_id: str
    cancellable_amount: int
    """(int64)
    """
    request_amount: int
    """(int64)
    """
    product_id: Optional[str]
    message: Optional[str]


def _serialize_platform_cancellable_discount_tax_free_amount_exceeded_error(obj: PlatformCancellableDiscountTaxFreeAmountExceededError) -> Any:
    entity = {}
    entity["type"] = "PLATFORM_CANCELLABLE_DISCOUNT_TAX_FREE_AMOUNT_EXCEEDED"
    entity["discountSharePolicyId"] = obj.discount_share_policy_id
    entity["discountSharePolicyGraphqlId"] = obj.discount_share_policy_graphql_id
    entity["cancellableAmount"] = obj.cancellable_amount
    entity["requestAmount"] = obj.request_amount
    if obj.product_id is not None:
        entity["productId"] = obj.product_id
    if obj.message is not None:
        entity["message"] = obj.message
    return entity


def _deserialize_platform_cancellable_discount_tax_free_amount_exceeded_error(obj: Any) -> PlatformCancellableDiscountTaxFreeAmountExceededError:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "type" not in obj:
        raise KeyError(f"'type' is not in {obj}")
    type = obj["type"]
    if type != "PLATFORM_CANCELLABLE_DISCOUNT_TAX_FREE_AMOUNT_EXCEEDED":
        raise ValueError(f"{repr(type)} is not 'PLATFORM_CANCELLABLE_DISCOUNT_TAX_FREE_AMOUNT_EXCEEDED'")
    if "discountSharePolicyId" not in obj:
        raise KeyError(f"'discountSharePolicyId' is not in {obj}")
    discount_share_policy_id = obj["discountSharePolicyId"]
    if not isinstance(discount_share_policy_id, str):
        raise ValueError(f"{repr(discount_share_policy_id)} is not str")
    if "discountSharePolicyGraphqlId" not in obj:
        raise KeyError(f"'discountSharePolicyGraphqlId' is not in {obj}")
    discount_share_policy_graphql_id = obj["discountSharePolicyGraphqlId"]
    if not isinstance(discount_share_policy_graphql_id, str):
        raise ValueError(f"{repr(discount_share_policy_graphql_id)} is not str")
    if "cancellableAmount" not in obj:
        raise KeyError(f"'cancellableAmount' is not in {obj}")
    cancellable_amount = obj["cancellableAmount"]
    if not isinstance(cancellable_amount, int):
        raise ValueError(f"{repr(cancellable_amount)} is not int")
    if "requestAmount" not in obj:
        raise KeyError(f"'requestAmount' is not in {obj}")
    request_amount = obj["requestAmount"]
    if not isinstance(request_amount, int):
        raise ValueError(f"{repr(request_amount)} is not int")
    if "productId" in obj:
        product_id = obj["productId"]
        if not isinstance(product_id, str):
            raise ValueError(f"{repr(product_id)} is not str")
    else:
        product_id = None
    if "message" in obj:
        message = obj["message"]
        if not isinstance(message, str):
            raise ValueError(f"{repr(message)} is not str")
    else:
        message = None
    return PlatformCancellableDiscountTaxFreeAmountExceededError(type, discount_share_policy_id, discount_share_policy_graphql_id, cancellable_amount, request_amount, product_id, message)
