from __future__ import annotations
from typing import Any, Literal, Optional
from dataclasses import dataclass, field

@dataclass
class B2bForeignExchangeAccountError:
    """계좌 정보 조회가 불가능한 외화 계좌인 경우
    """
    type: Literal["B2B_FOREIGN_EXCHANGE_ACCOUNT"] = field(repr=False)
    message: Optional[str]


def _serialize_b2b_foreign_exchange_account_error(obj: B2bForeignExchangeAccountError) -> Any:
    entity = {}
    entity["type"] = "B2B_FOREIGN_EXCHANGE_ACCOUNT"
    if obj.message is not None:
        entity["message"] = obj.message
    return entity


def _deserialize_b2b_foreign_exchange_account_error(obj: Any) -> B2bForeignExchangeAccountError:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "type" not in obj:
        raise KeyError(f"'type' is not in {obj}")
    type = obj["type"]
    if type != "B2B_FOREIGN_EXCHANGE_ACCOUNT":
        raise ValueError(f"{repr(type)} is not 'B2B_FOREIGN_EXCHANGE_ACCOUNT'")
    if "message" in obj:
        message = obj["message"]
        if not isinstance(message, str):
            raise ValueError(f"{repr(message)} is not str")
    else:
        message = None
    return B2bForeignExchangeAccountError(type, message)
