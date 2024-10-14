from __future__ import annotations
from typing import Any, Literal, Optional
from dataclasses import dataclass, field
from portone_server_sdk._generated.platform.transfer.platform_cancellable_amount_type import PlatformCancellableAmountType, _deserialize_platform_cancellable_amount_type, _serialize_platform_cancellable_amount_type

@dataclass
class PlatformCancellableAmountExceededError:
    """취소 가능한 금액이 초과한 경우
    """
    type: Literal["PLATFORM_CANCELLABLE_AMOUNT_EXCEEDED"] = field(repr=False)
    cancellable_amount: int
    """(int64)
    """
    request_amount: int
    """(int64)
    """
    amount_type: PlatformCancellableAmountType
    message: Optional[str]


def _serialize_platform_cancellable_amount_exceeded_error(obj: PlatformCancellableAmountExceededError) -> Any:
    entity = {}
    entity["type"] = "PLATFORM_CANCELLABLE_AMOUNT_EXCEEDED"
    entity["cancellableAmount"] = obj.cancellable_amount
    entity["requestAmount"] = obj.request_amount
    entity["amountType"] = _serialize_platform_cancellable_amount_type(obj.amount_type)
    if obj.message is not None:
        entity["message"] = obj.message
    return entity


def _deserialize_platform_cancellable_amount_exceeded_error(obj: Any) -> PlatformCancellableAmountExceededError:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "type" not in obj:
        raise KeyError(f"'type' is not in {obj}")
    type = obj["type"]
    if type != "PLATFORM_CANCELLABLE_AMOUNT_EXCEEDED":
        raise ValueError(f"{repr(type)} is not 'PLATFORM_CANCELLABLE_AMOUNT_EXCEEDED'")
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
    if "amountType" not in obj:
        raise KeyError(f"'amountType' is not in {obj}")
    amount_type = obj["amountType"]
    amount_type = _deserialize_platform_cancellable_amount_type(amount_type)
    if "message" in obj:
        message = obj["message"]
        if not isinstance(message, str):
            raise ValueError(f"{repr(message)} is not str")
    else:
        message = None
    return PlatformCancellableAmountExceededError(type, cancellable_amount, request_amount, amount_type, message)
