from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field
from ...common.date_time_range import DateTimeRange, _deserialize_date_time_range, _serialize_date_time_range
from ...platform.account_transfer.platform_account_transfer_status import PlatformAccountTransferStatus, _deserialize_platform_account_transfer_status, _serialize_platform_account_transfer_status
from ...platform.account_transfer.platform_account_transfer_type import PlatformAccountTransferType, _deserialize_platform_account_transfer_type, _serialize_platform_account_transfer_type

@dataclass
class PlatformAccountTransferFilter:
    trade_timestamp_range: Optional[DateTimeRange] = field(default=None)
    """이체 일시 범위
    """
    created_timestamp_range: Optional[DateTimeRange] = field(default=None)
    """생성 일시 범위
    """
    status_updated_timestamp_range: Optional[DateTimeRange] = field(default=None)
    """상태 업데이트 일시 범위
    """
    scheduled_timestamp_range: Optional[DateTimeRange] = field(default=None)
    """이체 예정 일시 범위
    """
    account_transfer_id: Optional[str] = field(default=None)
    """이체 아이디
    """
    bank_account_id: Optional[str] = field(default=None)
    """계좌 아이디
    """
    bulk_account_transfer_id: Optional[str] = field(default=None)
    """일괄 이체 아이디
    """
    payout_id: Optional[str] = field(default=None)
    """지급 아이디
    """
    account_transfer_ids: Optional[list[str]] = field(default=None)
    """이체 아이디 리스트
    """
    types: Optional[list[PlatformAccountTransferType]] = field(default=None)
    """구분
    """
    statuses: Optional[list[PlatformAccountTransferStatus]] = field(default=None)
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
    if obj.created_timestamp_range is not None:
        entity["createdTimestampRange"] = _serialize_date_time_range(obj.created_timestamp_range)
    if obj.status_updated_timestamp_range is not None:
        entity["statusUpdatedTimestampRange"] = _serialize_date_time_range(obj.status_updated_timestamp_range)
    if obj.scheduled_timestamp_range is not None:
        entity["scheduledTimestampRange"] = _serialize_date_time_range(obj.scheduled_timestamp_range)
    if obj.account_transfer_id is not None:
        entity["accountTransferId"] = obj.account_transfer_id
    if obj.bank_account_id is not None:
        entity["bankAccountId"] = obj.bank_account_id
    if obj.bulk_account_transfer_id is not None:
        entity["bulkAccountTransferId"] = obj.bulk_account_transfer_id
    if obj.payout_id is not None:
        entity["payoutId"] = obj.payout_id
    if obj.account_transfer_ids is not None:
        entity["accountTransferIds"] = obj.account_transfer_ids
    if obj.types is not None:
        entity["types"] = list(map(_serialize_platform_account_transfer_type, obj.types))
    if obj.statuses is not None:
        entity["statuses"] = list(map(_serialize_platform_account_transfer_status, obj.statuses))
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
    if "createdTimestampRange" in obj:
        created_timestamp_range = obj["createdTimestampRange"]
        created_timestamp_range = _deserialize_date_time_range(created_timestamp_range)
    else:
        created_timestamp_range = None
    if "statusUpdatedTimestampRange" in obj:
        status_updated_timestamp_range = obj["statusUpdatedTimestampRange"]
        status_updated_timestamp_range = _deserialize_date_time_range(status_updated_timestamp_range)
    else:
        status_updated_timestamp_range = None
    if "scheduledTimestampRange" in obj:
        scheduled_timestamp_range = obj["scheduledTimestampRange"]
        scheduled_timestamp_range = _deserialize_date_time_range(scheduled_timestamp_range)
    else:
        scheduled_timestamp_range = None
    if "accountTransferId" in obj:
        account_transfer_id = obj["accountTransferId"]
        if not isinstance(account_transfer_id, str):
            raise ValueError(f"{repr(account_transfer_id)} is not str")
    else:
        account_transfer_id = None
    if "bankAccountId" in obj:
        bank_account_id = obj["bankAccountId"]
        if not isinstance(bank_account_id, str):
            raise ValueError(f"{repr(bank_account_id)} is not str")
    else:
        bank_account_id = None
    if "bulkAccountTransferId" in obj:
        bulk_account_transfer_id = obj["bulkAccountTransferId"]
        if not isinstance(bulk_account_transfer_id, str):
            raise ValueError(f"{repr(bulk_account_transfer_id)} is not str")
    else:
        bulk_account_transfer_id = None
    if "payoutId" in obj:
        payout_id = obj["payoutId"]
        if not isinstance(payout_id, str):
            raise ValueError(f"{repr(payout_id)} is not str")
    else:
        payout_id = None
    if "accountTransferIds" in obj:
        account_transfer_ids = obj["accountTransferIds"]
        if not isinstance(account_transfer_ids, list):
            raise ValueError(f"{repr(account_transfer_ids)} is not list")
        for i, item in enumerate(account_transfer_ids):
            if not isinstance(item, str):
                raise ValueError(f"{repr(item)} is not str")
    else:
        account_transfer_ids = None
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
            item = _deserialize_platform_account_transfer_status(item)
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
    return PlatformAccountTransferFilter(trade_timestamp_range, created_timestamp_range, status_updated_timestamp_range, scheduled_timestamp_range, account_transfer_id, bank_account_id, bulk_account_transfer_id, payout_id, account_transfer_ids, types, statuses, depositor_name, deposit_account_holder, deposit_memo, withdrawal_memo)
