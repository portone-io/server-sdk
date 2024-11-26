from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class InstantPaymentMethodInputVirtualAccountOptionFixed:
    """고정식 가상계좌 발급 유형

    pgAccountId, accountNumber 유형 중 한 개의 필드만 입력합니다.
    """
    pg_account_id: Optional[str] = field(default=None)
    """Account ID 고정식 가상계좌

    고객사가 가상계좌번호를 직접 관리하지 않고 PG사가 pgAccountId에 매핑되는 가상계좌번호를 내려주는 방식입니다.
    동일한 pgAccountId로 가상계좌 발급 요청시에는 항상 같은 가상계좌번호가 내려옵니다.
    """
    account_number: Optional[str] = field(default=None)
    """Account Number 고정식 가상계좌

    PG사가 일정 개수만큼의 가상계좌번호를 발급하여 고객사에게 미리 전달하고 고객사가 그 중 하나를 선택하여 사용하는 방식입니다.
    """


def _serialize_instant_payment_method_input_virtual_account_option_fixed(obj: InstantPaymentMethodInputVirtualAccountOptionFixed) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    if obj.pg_account_id is not None:
        entity["pgAccountId"] = obj.pg_account_id
    if obj.account_number is not None:
        entity["accountNumber"] = obj.account_number
    return entity


def _deserialize_instant_payment_method_input_virtual_account_option_fixed(obj: Any) -> InstantPaymentMethodInputVirtualAccountOptionFixed:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "pgAccountId" in obj:
        pg_account_id = obj["pgAccountId"]
        if not isinstance(pg_account_id, str):
            raise ValueError(f"{repr(pg_account_id)} is not str")
    else:
        pg_account_id = None
    if "accountNumber" in obj:
        account_number = obj["accountNumber"]
        if not isinstance(account_number, str):
            raise ValueError(f"{repr(account_number)} is not str")
    else:
        account_number = None
    return InstantPaymentMethodInputVirtualAccountOptionFixed(pg_account_id, account_number)
