from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field
from ...common.date_time_range import DateTimeRange, _deserialize_date_time_range, _serialize_date_time_range
from ...platform.account_transfer.platform_account_transfer_type import PlatformAccountTransferType, _deserialize_platform_account_transfer_type, _serialize_platform_account_transfer_type
from ...platform.account_transfer.status import Status, _deserialize_status, _serialize_status

@dataclass
class PlatformAccountTransferFilter:
    trade_timestamp_range: Optional[DateTimeRange] = field(default=None)
    """거래 시간 범위
    """
    account_transfer_id: Optional[str] = field(default=None)
    """이체 아이디
    """
    types: Optional[list[PlatformAccountTransferType]] = field(default=None)
    """구분
    """
    statuses: Optional[list[Status]] = field(default=None)
    """상태
    """
    depositor_name: Optional[str] = field(default=None)
    """입금자명
    """
    deposit_account_holder: Optional[str] = field(default=None)
    """예금주
    """
    deposit_memo: Optional[str] = field(default=None)
    """받는 이 통장 메모
    """
    withdrawal_memo: Optional[str] = field(default=None)
    """보내는 이 통장 메모
    """


def _serialize_platform_account_transfer_filter(obj: PlatformAccountTransferFilter) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    if obj.trade_timestamp_range is not None:
        entity["tradeTimestampRange"] = _serialize_date_time_range(obj.trade_timestamp_range)
    if obj.account_transfer_id is not None:
        entity["accountTransferId"] = obj.account_transfer_id
    if obj.types is not None:
        entity["types"] = list(map(_serialize_platform_account_transfer_type, obj.types))
    if obj.statuses is not None:
        entity["statuses"] = list(map(_serialize_status, obj.statuses))
    if obj.depositor_name is not None:
        entity["depositorName"] = obj.depositor_name
    if obj.deposit_account_holder is not None:
        entity["depositAccountHolder"] = obj.deposit_account_holder
    if obj.deposit_memo is not None:
        entity["depositMemo"] = obj.deposit_memo
    if obj.withdrawal_memo is not None:
        entity["withdrawalMemo"] = obj.withdrawal_memo
    return entity


def _deserialize_platform_account_transfer_filter(obj: Any) -> PlatformAccountTransferFilter:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "tradeTimestampRange" in obj:
        trade_timestamp_range = obj["tradeTimestampRange"]
        trade_timestamp_range = _deserialize_date_time_range(trade_timestamp_range)
    else:
        trade_timestamp_range = None
    if "accountTransferId" in obj:
        account_transfer_id = obj["accountTransferId"]
        if not isinstance(account_transfer_id, str):
            raise ValueError(f"{repr(account_transfer_id)} is not str")
    else:
        account_transfer_id = None
    if "types" in obj:
        types = obj["types"]
        if not isinstance(types, list):
            raise ValueError(f"{repr(types)} is not list")
        for i, item in enumerate(types):
            item = _deserialize_platform_account_transfer_type(item)
            types[i] = item
    else:
        types = None
    if "statuses" in obj:
        statuses = obj["statuses"]
        if not isinstance(statuses, list):
            raise ValueError(f"{repr(statuses)} is not list")
        for i, item in enumerate(statuses):
            item = _deserialize_status(item)
            statuses[i] = item
    else:
        statuses = None
    if "depositorName" in obj:
        depositor_name = obj["depositorName"]
        if not isinstance(depositor_name, str):
            raise ValueError(f"{repr(depositor_name)} is not str")
    else:
        depositor_name = None
    if "depositAccountHolder" in obj:
        deposit_account_holder = obj["depositAccountHolder"]
        if not isinstance(deposit_account_holder, str):
            raise ValueError(f"{repr(deposit_account_holder)} is not str")
    else:
        deposit_account_holder = None
    if "depositMemo" in obj:
        deposit_memo = obj["depositMemo"]
        if not isinstance(deposit_memo, str):
            raise ValueError(f"{repr(deposit_memo)} is not str")
    else:
        deposit_memo = None
    if "withdrawalMemo" in obj:
        withdrawal_memo = obj["withdrawalMemo"]
        if not isinstance(withdrawal_memo, str):
            raise ValueError(f"{repr(withdrawal_memo)} is not str")
    else:
        withdrawal_memo = None
    return PlatformAccountTransferFilter(trade_timestamp_range, account_transfer_id, types, statuses, depositor_name, deposit_account_holder, deposit_memo, withdrawal_memo)
