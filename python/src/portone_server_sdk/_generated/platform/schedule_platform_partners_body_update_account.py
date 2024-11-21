from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field
from ..common.bank import Bank, _deserialize_bank, _serialize_bank
from ..common.currency import Currency, _deserialize_currency, _serialize_currency

@dataclass
class SchedulePlatformPartnersBodyUpdateAccount:
    """파트너 계좌 업데이트를 위한 입력 정보
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
    account_verification_id: Optional[str] = field(default=None)
    """계좌 검증 아이디
    """


def _serialize_schedule_platform_partners_body_update_account(obj: SchedulePlatformPartnersBodyUpdateAccount) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["bank"] = _serialize_bank(obj.bank)
    entity["currency"] = _serialize_currency(obj.currency)
    entity["number"] = obj.number
    entity["holder"] = obj.holder
    if obj.account_verification_id is not None:
        entity["accountVerificationId"] = obj.account_verification_id
    return entity


def _deserialize_schedule_platform_partners_body_update_account(obj: Any) -> SchedulePlatformPartnersBodyUpdateAccount:
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
    if "accountVerificationId" in obj:
        account_verification_id = obj["accountVerificationId"]
        if not isinstance(account_verification_id, str):
            raise ValueError(f"{repr(account_verification_id)} is not str")
    else:
        account_verification_id = None
    return SchedulePlatformPartnersBodyUpdateAccount(bank, currency, number, holder, account_verification_id)
