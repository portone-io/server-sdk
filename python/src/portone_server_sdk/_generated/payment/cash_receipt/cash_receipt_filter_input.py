from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field
from ...payment.cash_receipt.cash_receipt_status import CashReceiptStatus, _deserialize_cash_receipt_status, _serialize_cash_receipt_status
from ...payment.cash_receipt.cash_receipt_time_range_field import CashReceiptTimeRangeField, _deserialize_cash_receipt_time_range_field, _serialize_cash_receipt_time_range_field
from ...common.cash_receipt_type import CashReceiptType, _deserialize_cash_receipt_type, _serialize_cash_receipt_type
from ...common.pg_company import PgCompany, _deserialize_pg_company, _serialize_pg_company
from ...common.pg_provider import PgProvider, _deserialize_pg_provider, _serialize_pg_provider
from ...common.port_one_version import PortOneVersion, _deserialize_port_one_version, _serialize_port_one_version

@dataclass
class CashReceiptFilterInput:
    """현금영수증 다건 조회를 위한 입력 정보
    """
    store_id: Optional[str] = field(default=None)
    """상점 아이디

    Merchant 사용자만 사용가능하며, 지정되지 않은 경우 고객사 전체 현금영수증을 조회합니다.
    """
    time_range_field: Optional[CashReceiptTimeRangeField] = field(default=None)
    """조회 기준 시점 유형

    값을 입력하지 않으면 ISSUED_AT으로 설정됩니다.
    """
    from_: Optional[str] = field(default=None)
    """조회 기준 시점 범위의 시작

    값을 입력하지 않으면 end의 90일 전으로 설정됩니다.
    (RFC 3339 date-time)
    """
    until: Optional[str] = field(default=None)
    """조회 기준 시점 범위의 끝

    값을 입력하지 않으면 현재 시점으로 설정됩니다.
    (RFC 3339 date-time)
    """
    payment_id: Optional[str] = field(default=None)
    """고객사 결제 아이디
    """
    is_test: Optional[bool] = field(default=None)
    """테스트 결제 필터링
    """
    order_name: Optional[str] = field(default=None)
    """주문명
    """
    statuses: Optional[list[CashReceiptStatus]] = field(default=None)
    """현금영수증 발급 상태 리스트

    값을 입력하지 않으면 필터링이 적용되지 않습니다.
    """
    is_manual: Optional[bool] = field(default=None)
    """수동 발급 여부
    """
    pg_receipt_id: Optional[str] = field(default=None)
    """PG사 현금영수증 발급 번호
    """
    pg_merchant_id: Optional[str] = field(default=None)
    """PG 상점아이디
    """
    pg_providers: Optional[list[PgProvider]] = field(default=None)
    """PG사 결제 모듈 리스트

    값을 입력하지 않으면 PG사 결제 모듈 필터링이 적용되지 않습니다.
    """
    pg_companies: Optional[list[PgCompany]] = field(default=None)
    """PG사 리스트

    값을 입력하지 않으면 PG사 필터링이 적용되지 않습니다.
    """
    version: Optional[PortOneVersion] = field(default=None)
    """포트원 버전
    """
    types: Optional[list[CashReceiptType]] = field(default=None)
    """현금영수증 유형 리스트

    값을 입력하지 않으면 필터링이 적용되지 않습니다.
    """


def _serialize_cash_receipt_filter_input(obj: CashReceiptFilterInput) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    if obj.store_id is not None:
        entity["storeId"] = obj.store_id
    if obj.time_range_field is not None:
        entity["timeRangeField"] = _serialize_cash_receipt_time_range_field(obj.time_range_field)
    if obj.from_ is not None:
        entity["from"] = obj.from_
    if obj.until is not None:
        entity["until"] = obj.until
    if obj.payment_id is not None:
        entity["paymentId"] = obj.payment_id
    if obj.is_test is not None:
        entity["isTest"] = obj.is_test
    if obj.order_name is not None:
        entity["orderName"] = obj.order_name
    if obj.statuses is not None:
        entity["statuses"] = list(map(_serialize_cash_receipt_status, obj.statuses))
    if obj.is_manual is not None:
        entity["isManual"] = obj.is_manual
    if obj.pg_receipt_id is not None:
        entity["pgReceiptId"] = obj.pg_receipt_id
    if obj.pg_merchant_id is not None:
        entity["pgMerchantId"] = obj.pg_merchant_id
    if obj.pg_providers is not None:
        entity["pgProviders"] = list(map(_serialize_pg_provider, obj.pg_providers))
    if obj.pg_companies is not None:
        entity["pgCompanies"] = list(map(_serialize_pg_company, obj.pg_companies))
    if obj.version is not None:
        entity["version"] = _serialize_port_one_version(obj.version)
    if obj.types is not None:
        entity["types"] = list(map(_serialize_cash_receipt_type, obj.types))
    return entity


def _deserialize_cash_receipt_filter_input(obj: Any) -> CashReceiptFilterInput:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "storeId" in obj:
        store_id = obj["storeId"]
        if not isinstance(store_id, str):
            raise ValueError(f"{repr(store_id)} is not str")
    else:
        store_id = None
    if "timeRangeField" in obj:
        time_range_field = obj["timeRangeField"]
        time_range_field = _deserialize_cash_receipt_time_range_field(time_range_field)
    else:
        time_range_field = None
    if "from" in obj:
        from_ = obj["from"]
        if not isinstance(from_, str):
            raise ValueError(f"{repr(from_)} is not str")
    else:
        from_ = None
    if "until" in obj:
        until = obj["until"]
        if not isinstance(until, str):
            raise ValueError(f"{repr(until)} is not str")
    else:
        until = None
    if "paymentId" in obj:
        payment_id = obj["paymentId"]
        if not isinstance(payment_id, str):
            raise ValueError(f"{repr(payment_id)} is not str")
    else:
        payment_id = None
    if "isTest" in obj:
        is_test = obj["isTest"]
        if not isinstance(is_test, bool):
            raise ValueError(f"{repr(is_test)} is not bool")
    else:
        is_test = None
    if "orderName" in obj:
        order_name = obj["orderName"]
        if not isinstance(order_name, str):
            raise ValueError(f"{repr(order_name)} is not str")
    else:
        order_name = None
    if "statuses" in obj:
        statuses = obj["statuses"]
        if not isinstance(statuses, list):
            raise ValueError(f"{repr(statuses)} is not list")
        for i, item in enumerate(statuses):
            item = _deserialize_cash_receipt_status(item)
            statuses[i] = item
    else:
        statuses = None
    if "isManual" in obj:
        is_manual = obj["isManual"]
        if not isinstance(is_manual, bool):
            raise ValueError(f"{repr(is_manual)} is not bool")
    else:
        is_manual = None
    if "pgReceiptId" in obj:
        pg_receipt_id = obj["pgReceiptId"]
        if not isinstance(pg_receipt_id, str):
            raise ValueError(f"{repr(pg_receipt_id)} is not str")
    else:
        pg_receipt_id = None
    if "pgMerchantId" in obj:
        pg_merchant_id = obj["pgMerchantId"]
        if not isinstance(pg_merchant_id, str):
            raise ValueError(f"{repr(pg_merchant_id)} is not str")
    else:
        pg_merchant_id = None
    if "pgProviders" in obj:
        pg_providers = obj["pgProviders"]
        if not isinstance(pg_providers, list):
            raise ValueError(f"{repr(pg_providers)} is not list")
        for i, item in enumerate(pg_providers):
            item = _deserialize_pg_provider(item)
            pg_providers[i] = item
    else:
        pg_providers = None
    if "pgCompanies" in obj:
        pg_companies = obj["pgCompanies"]
        if not isinstance(pg_companies, list):
            raise ValueError(f"{repr(pg_companies)} is not list")
        for i, item in enumerate(pg_companies):
            item = _deserialize_pg_company(item)
            pg_companies[i] = item
    else:
        pg_companies = None
    if "version" in obj:
        version = obj["version"]
        version = _deserialize_port_one_version(version)
    else:
        version = None
    if "types" in obj:
        types = obj["types"]
        if not isinstance(types, list):
            raise ValueError(f"{repr(types)} is not list")
        for i, item in enumerate(types):
            item = _deserialize_cash_receipt_type(item)
            types[i] = item
    else:
        types = None
    return CashReceiptFilterInput(store_id, time_range_field, from_, until, payment_id, is_test, order_name, statuses, is_manual, pg_receipt_id, pg_merchant_id, pg_providers, pg_companies, version, types)
