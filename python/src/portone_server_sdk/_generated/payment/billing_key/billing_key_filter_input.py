from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field
from portone_server_sdk._generated.payment.billing_key.billing_key_payment_method_type import BillingKeyPaymentMethodType, _deserialize_billing_key_payment_method_type, _serialize_billing_key_payment_method_type
from portone_server_sdk._generated.payment.billing_key.billing_key_status import BillingKeyStatus, _deserialize_billing_key_status, _serialize_billing_key_status
from portone_server_sdk._generated.payment.billing_key.billing_key_text_search import BillingKeyTextSearch, _deserialize_billing_key_text_search, _serialize_billing_key_text_search
from portone_server_sdk._generated.payment.billing_key.billing_key_time_range_field import BillingKeyTimeRangeField, _deserialize_billing_key_time_range_field, _serialize_billing_key_time_range_field
from portone_server_sdk._generated.common.payment_client_type import PaymentClientType, _deserialize_payment_client_type, _serialize_payment_client_type
from portone_server_sdk._generated.payment.billing_key.pg_company import PgCompany, _deserialize_pg_company, _serialize_pg_company
from portone_server_sdk._generated.common.pg_provider import PgProvider, _deserialize_pg_provider, _serialize_pg_provider
from portone_server_sdk._generated.common.port_one_version import PortOneVersion, _deserialize_port_one_version, _serialize_port_one_version

@dataclass
class BillingKeyFilterInput:
    """빌링키 다건 조회를 위한 입력 정보
    """
    store_id: Optional[str]
    """상점 아이디

    Merchant 사용자만 사용가능하며, 지정되지 않은 경우 고객사 전체 빌링키를 조회합니다.
    """
    time_range_field: Optional[BillingKeyTimeRangeField]
    """조회 기준 시점 유형
    """
    from_: Optional[str]
    """조회 기준 시점 범위의 시작

    값을 입력하지 않으면 end의 90일 전으로 설정됩니다.
    (RFC 3339 date-time)
    """
    until: Optional[str]
    """조회 기준 시점 범위의 끝

    값을 입력하지 않으면 현재 시점으로 설정됩니다.
    (RFC 3339 date-time)
    """
    status: Optional[list[BillingKeyStatus]]
    """빌링키 상태 리스트

    값을 입력하지 않으면 빌링키 상태 필터링이 적용되지 않습니다.
    """
    channel_group_ids: Optional[list[str]]
    """채널 그룹 아이디 리스트

    값을 입력하지 않으면 스마트 라우팅 그룹 아이디 필터링이 적용되지 않습니다.
    """
    customer_id: Optional[str]
    """고객 ID
    """
    platform_type: Optional[PaymentClientType]
    """플랫폼 유형
    """
    text_search: Optional[BillingKeyTextSearch]
    """통합 검색 필터
    """
    pg_providers: Optional[list[PgProvider]]
    """PG사 결제 모듈 리스트

    값을 입력하지 않으면 PG사 결제 모듈 필터링이 적용되지 않습니다.
    """
    pg_companies: Optional[list[PgCompany]]
    """PG사 리스트

    값을 입력하지 않으면 PG사 필터링이 적용되지 않습니다.
    """
    methods: Optional[list[BillingKeyPaymentMethodType]]
    """결제수단 리스트

    값을 입력하지 않으면 결제수단 필터링이 적용되지 않습니다.
    """
    version: Optional[PortOneVersion]
    """포트원 버전
    """


def _serialize_billing_key_filter_input(obj: BillingKeyFilterInput) -> Any:
    entity = {}
    if obj.store_id is not None:
        entity["storeId"] = obj.store_id
    if obj.time_range_field is not None:
        entity["timeRangeField"] = _serialize_billing_key_time_range_field(obj.time_range_field)
    if obj.from_ is not None:
        entity["from"] = obj.from_
    if obj.until is not None:
        entity["until"] = obj.until
    if obj.status is not None:
        entity["status"] = list(map(_serialize_billing_key_status, obj.status))
    if obj.channel_group_ids is not None:
        entity["channelGroupIds"] = obj.channel_group_ids
    if obj.customer_id is not None:
        entity["customerId"] = obj.customer_id
    if obj.platform_type is not None:
        entity["platformType"] = _serialize_payment_client_type(obj.platform_type)
    if obj.text_search is not None:
        entity["textSearch"] = _serialize_billing_key_text_search(obj.text_search)
    if obj.pg_providers is not None:
        entity["pgProviders"] = list(map(_serialize_pg_provider, obj.pg_providers))
    if obj.pg_companies is not None:
        entity["pgCompanies"] = list(map(_serialize_pg_company, obj.pg_companies))
    if obj.methods is not None:
        entity["methods"] = list(map(_serialize_billing_key_payment_method_type, obj.methods))
    if obj.version is not None:
        entity["version"] = _serialize_port_one_version(obj.version)
    return entity


def _deserialize_billing_key_filter_input(obj: Any) -> BillingKeyFilterInput:
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
        time_range_field = _deserialize_billing_key_time_range_field(time_range_field)
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
    if "status" in obj:
        status = obj["status"]
        if not isinstance(status, list):
            raise ValueError(f"{repr(status)} is not list")
        for i, item in enumerate(status):
            item = _deserialize_billing_key_status(item)
            status[i] = item
    else:
        status = None
    if "channelGroupIds" in obj:
        channel_group_ids = obj["channelGroupIds"]
        if not isinstance(channel_group_ids, list):
            raise ValueError(f"{repr(channel_group_ids)} is not list")
        for i, item in enumerate(channel_group_ids):
            if not isinstance(item, str):
                raise ValueError(f"{repr(item)} is not str")
    else:
        channel_group_ids = None
    if "customerId" in obj:
        customer_id = obj["customerId"]
        if not isinstance(customer_id, str):
            raise ValueError(f"{repr(customer_id)} is not str")
    else:
        customer_id = None
    if "platformType" in obj:
        platform_type = obj["platformType"]
        platform_type = _deserialize_payment_client_type(platform_type)
    else:
        platform_type = None
    if "textSearch" in obj:
        text_search = obj["textSearch"]
        text_search = _deserialize_billing_key_text_search(text_search)
    else:
        text_search = None
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
    if "methods" in obj:
        methods = obj["methods"]
        if not isinstance(methods, list):
            raise ValueError(f"{repr(methods)} is not list")
        for i, item in enumerate(methods):
            item = _deserialize_billing_key_payment_method_type(item)
            methods[i] = item
    else:
        methods = None
    if "version" in obj:
        version = obj["version"]
        version = _deserialize_port_one_version(version)
    else:
        version = None
    return BillingKeyFilterInput(store_id, time_range_field, from_, until, status, channel_group_ids, customer_id, platform_type, text_search, pg_providers, pg_companies, methods, version)
