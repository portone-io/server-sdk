from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field
from ..common.bank import Bank, _deserialize_bank, _serialize_bank
from ..common.currency import Currency, _deserialize_currency, _serialize_currency
from ..platform.platform_account_status import PlatformAccountStatus, _deserialize_platform_account_status, _serialize_platform_account_status

@dataclass
class PlatformAccount:
    """플랫폼 정산 계좌

    `currency` 가 KRW 일 경우 예금주 조회 API 를 통해 올바른 계좌인지 검증합니다. 그 외의 화폐일 경우 따로 검증하지는 않습니다.
    """
    bank: Bank
    """은행
    """
    currency: Currency
    """정산에 사용할 통화
    """
    number: str
    """계좌번호
    """
    holder: str
    """예금주명
    """
    status: PlatformAccountStatus
    """계좌 상태
    """


def _serialize_platform_account(obj: PlatformAccount) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["bank"] = _serialize_bank(obj.bank)
    entity["currency"] = _serialize_currency(obj.currency)
    entity["number"] = obj.number
    entity["holder"] = obj.holder
    entity["status"] = _serialize_platform_account_status(obj.status)
    return entity


def _deserialize_platform_account(obj: Any) -> PlatformAccount:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "bank" not in obj:
        raise KeyError(f"'bank' is not in {obj}")
    bank = obj["bank"]
    bank = _deserialize_bank(bank)
    if "currency" not in obj:
        raise KeyError(f"'currency' is not in {obj}")
    currency = obj["currency"]
    currency = _deserialize_currency(currency)
    if "number" not in obj:
        raise KeyError(f"'number' is not in {obj}")
    number = obj["number"]
    if not isinstance(number, str):
        raise ValueError(f"{repr(number)} is not str")
    if "holder" not in obj:
        raise KeyError(f"'holder' is not in {obj}")
    holder = obj["holder"]
    if not isinstance(holder, str):
        raise ValueError(f"{repr(holder)} is not str")
    if "status" not in obj:
        raise KeyError(f"'status' is not in {obj}")
    status = obj["status"]
    status = _deserialize_platform_account_status(status)
    return PlatformAccount(bank, currency, number, holder, status)
