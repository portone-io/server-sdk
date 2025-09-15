from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field
from ...common.date_time_range import DateTimeRange, _deserialize_date_time_range, _serialize_date_time_range

@dataclass
class PlatformPayoutFilterInputCriteria:
    """검색 기준 입력 정보
    """
    timestamp_range: Optional[DateTimeRange] = field(default=None)
    """생성 일시 범위
    """
    status_updated_timestamp_range: Optional[DateTimeRange] = field(default=None)
    """상태 업데이트 일시 범위
    """
    scheduled_timestamp_range: Optional[DateTimeRange] = field(default=None)
    """지급 예정 일시 범위
    """
    settlement_statement_issued_timestamp_range: Optional[DateTimeRange] = field(default=None)
    """정산 내역서 발송 일시 범위
    """
    payout_id: Optional[str] = field(default=None)
    """지급 아이디
    """
    bulk_payout_id: Optional[str] = field(default=None)
    """일괄 지급 아이디
    """
    tax_invoice_id: Optional[str] = field(default=None)
    """세금계산서 아이디
    """
    settlement_statement_id: Optional[str] = field(default=None)
    """정산 내역서 아이디
    """


def _serialize_platform_payout_filter_input_criteria(obj: PlatformPayoutFilterInputCriteria) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    if obj.timestamp_range is not None:
        entity["timestampRange"] = _serialize_date_time_range(obj.timestamp_range)
    if obj.status_updated_timestamp_range is not None:
        entity["statusUpdatedTimestampRange"] = _serialize_date_time_range(obj.status_updated_timestamp_range)
    if obj.scheduled_timestamp_range is not None:
        entity["scheduledTimestampRange"] = _serialize_date_time_range(obj.scheduled_timestamp_range)
    if obj.settlement_statement_issued_timestamp_range is not None:
        entity["settlementStatementIssuedTimestampRange"] = _serialize_date_time_range(obj.settlement_statement_issued_timestamp_range)
    if obj.payout_id is not None:
        entity["payoutId"] = obj.payout_id
    if obj.bulk_payout_id is not None:
        entity["bulkPayoutId"] = obj.bulk_payout_id
    if obj.tax_invoice_id is not None:
        entity["taxInvoiceId"] = obj.tax_invoice_id
    if obj.settlement_statement_id is not None:
        entity["settlementStatementId"] = obj.settlement_statement_id
    return entity


def _deserialize_platform_payout_filter_input_criteria(obj: Any) -> PlatformPayoutFilterInputCriteria:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "timestampRange" in obj:
        timestamp_range = obj["timestampRange"]
        timestamp_range = _deserialize_date_time_range(timestamp_range)
    else:
        timestamp_range = None
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
    if "settlementStatementIssuedTimestampRange" in obj:
        settlement_statement_issued_timestamp_range = obj["settlementStatementIssuedTimestampRange"]
        settlement_statement_issued_timestamp_range = _deserialize_date_time_range(settlement_statement_issued_timestamp_range)
    else:
        settlement_statement_issued_timestamp_range = None
    if "payoutId" in obj:
        payout_id = obj["payoutId"]
        if not isinstance(payout_id, str):
            raise ValueError(f"{repr(payout_id)} is not str")
    else:
        payout_id = None
    if "bulkPayoutId" in obj:
        bulk_payout_id = obj["bulkPayoutId"]
        if not isinstance(bulk_payout_id, str):
            raise ValueError(f"{repr(bulk_payout_id)} is not str")
    else:
        bulk_payout_id = None
    if "taxInvoiceId" in obj:
        tax_invoice_id = obj["taxInvoiceId"]
        if not isinstance(tax_invoice_id, str):
            raise ValueError(f"{repr(tax_invoice_id)} is not str")
    else:
        tax_invoice_id = None
    if "settlementStatementId" in obj:
        settlement_statement_id = obj["settlementStatementId"]
        if not isinstance(settlement_statement_id, str):
            raise ValueError(f"{repr(settlement_statement_id)} is not str")
    else:
        settlement_statement_id = None
    return PlatformPayoutFilterInputCriteria(timestamp_range, status_updated_timestamp_range, scheduled_timestamp_range, settlement_statement_issued_timestamp_range, payout_id, bulk_payout_id, tax_invoice_id, settlement_statement_id)
