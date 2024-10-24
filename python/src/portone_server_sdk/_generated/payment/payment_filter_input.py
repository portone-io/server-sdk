from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field
from portone_server_sdk._generated.common.card_brand import CardBrand, _deserialize_card_brand, _serialize_card_brand
from portone_server_sdk._generated.common.card_owner_type import CardOwnerType, _deserialize_card_owner_type, _serialize_card_owner_type
from portone_server_sdk._generated.common.card_type import CardType, _deserialize_card_type, _serialize_card_type
from portone_server_sdk._generated.common.cash_receipt_input_type import CashReceiptInputType, _deserialize_cash_receipt_input_type, _serialize_cash_receipt_input_type
from portone_server_sdk._generated.common.currency import Currency, _deserialize_currency, _serialize_currency
from portone_server_sdk._generated.common.date_time_range import DateTimeRange, _deserialize_date_time_range, _serialize_date_time_range
from portone_server_sdk._generated.payment.payment_cash_receipt_status import PaymentCashReceiptStatus, _deserialize_payment_cash_receipt_status, _serialize_payment_cash_receipt_status
from portone_server_sdk._generated.common.payment_client_type import PaymentClientType, _deserialize_payment_client_type, _serialize_payment_client_type
from portone_server_sdk._generated.payment.payment_filter_input_escrow_status import PaymentFilterInputEscrowStatus, _deserialize_payment_filter_input_escrow_status, _serialize_payment_filter_input_escrow_status
from portone_server_sdk._generated.payment.payment_method_gift_certificate_type import PaymentMethodGiftCertificateType, _deserialize_payment_method_gift_certificate_type, _serialize_payment_method_gift_certificate_type
from portone_server_sdk._generated.common.payment_method_type import PaymentMethodType, _deserialize_payment_method_type, _serialize_payment_method_type
from portone_server_sdk._generated.payment.payment_sort_by import PaymentSortBy, _deserialize_payment_sort_by, _serialize_payment_sort_by
from portone_server_sdk._generated.payment.payment_status import PaymentStatus, _deserialize_payment_status, _serialize_payment_status
from portone_server_sdk._generated.payment.payment_text_search import PaymentTextSearch, _deserialize_payment_text_search, _serialize_payment_text_search
from portone_server_sdk._generated.payment.payment_timestamp_type import PaymentTimestampType, _deserialize_payment_timestamp_type, _serialize_payment_timestamp_type
from portone_server_sdk._generated.payment.payment_webhook_status import PaymentWebhookStatus, _deserialize_payment_webhook_status, _serialize_payment_webhook_status
from portone_server_sdk._generated.common.pg_provider import PgProvider, _deserialize_pg_provider, _serialize_pg_provider
from portone_server_sdk._generated.common.port_one_version import PortOneVersion, _deserialize_port_one_version, _serialize_port_one_version
from portone_server_sdk._generated.common.sort_order import SortOrder, _deserialize_sort_order, _serialize_sort_order

@dataclass
class PaymentFilterInput:
    """결제 건 다건 조회를 위한 입력 정보
    """
    merchant_id: Optional[str]
    """고객사 아이디
    """
    store_id: Optional[str]
    """상점 아이디

    Merchant 사용자만 사용가능하며, 지정되지 않은 경우 고객사 전체 결제 건을 조회합니다.
    """
    timestamp_type: Optional[PaymentTimestampType]
    """조회 기준 시점 유형
    """
    from_: Optional[str]
    """결제 요청/상태 승인 시점 범위의 시작

    값을 입력하지 않으면 end의 90일 전으로 설정됩니다.
    (RFC 3339 date-time)
    """
    until: Optional[str]
    """결제 요청/상태 승인 시점 범위의 끝

    값을 입력하지 않으면 현재 시점으로 설정됩니다.
    (RFC 3339 date-time)
    """
    status: Optional[list[PaymentStatus]]
    """결제 상태 리스트

    값을 입력하지 않으면 결제상태 필터링이 적용되지 않습니다.
    """
    methods: Optional[list[PaymentMethodType]]
    """결제수단 리스트

    값을 입력하지 않으면 결제수단 필터링이 적용되지 않습니다.
    """
    pg_provider: Optional[list[PgProvider]]
    """PG사 리스트

    값을 입력하지 않으면 결제대행사 필터링이 적용되지 않습니다.
    """
    is_test: Optional[bool]
    """테스트 결제 필터링
    """
    is_scheduled: Optional[bool]
    """결제 예약 건 필터링
    """
    sort_by: Optional[PaymentSortBy]
    """결제 건 정렬 기준
    """
    sort_order: Optional[SortOrder]
    """결제 건 정렬 방식
    """
    version: Optional[PortOneVersion]
    """포트원 버전
    """
    webhook_status: Optional[PaymentWebhookStatus]
    """웹훅 상태
    """
    platform_type: Optional[PaymentClientType]
    """플랫폼 유형
    """
    currency: Optional[Currency]
    """통화
    """
    is_escrow: Optional[bool]
    """에스크로 결제 여부
    """
    escrow_status: Optional[PaymentFilterInputEscrowStatus]
    """에스크로 결제의 배송 정보 상태
    """
    card_brand: Optional[CardBrand]
    """카드 브랜드
    """
    card_type: Optional[CardType]
    """카드 유형
    """
    card_owner_type: Optional[CardOwnerType]
    """카드 소유주 유형
    """
    gift_certificate_type: Optional[PaymentMethodGiftCertificateType]
    """상품권 종류
    """
    cash_receipt_type: Optional[CashReceiptInputType]
    """현금영수증 유형
    """
    cash_receipt_status: Optional[PaymentCashReceiptStatus]
    """현금영수증 상태
    """
    cash_receipt_issued_at_range: Optional[DateTimeRange]
    """현금영수증 발급 시간 범위
    """
    cash_receipt_cancelled_at_range: Optional[DateTimeRange]
    """현금영수증 취소 시간 범위
    """
    text_search: Optional[list[PaymentTextSearch]]
    """통합 검색 리스트 필터
    """


def _serialize_payment_filter_input(obj: PaymentFilterInput) -> Any:
    entity = {}
    if obj.merchant_id is not None:
        entity["merchantId"] = obj.merchant_id
    if obj.store_id is not None:
        entity["storeId"] = obj.store_id
    if obj.timestamp_type is not None:
        entity["timestampType"] = _serialize_payment_timestamp_type(obj.timestamp_type)
    if obj.from_ is not None:
        entity["from"] = obj.from_
    if obj.until is not None:
        entity["until"] = obj.until
    if obj.status is not None:
        entity["status"] = list(map(_serialize_payment_status, obj.status))
    if obj.methods is not None:
        entity["methods"] = list(map(_serialize_payment_method_type, obj.methods))
    if obj.pg_provider is not None:
        entity["pgProvider"] = list(map(_serialize_pg_provider, obj.pg_provider))
    if obj.is_test is not None:
        entity["isTest"] = obj.is_test
    if obj.is_scheduled is not None:
        entity["isScheduled"] = obj.is_scheduled
    if obj.sort_by is not None:
        entity["sortBy"] = _serialize_payment_sort_by(obj.sort_by)
    if obj.sort_order is not None:
        entity["sortOrder"] = _serialize_sort_order(obj.sort_order)
    if obj.version is not None:
        entity["version"] = _serialize_port_one_version(obj.version)
    if obj.webhook_status is not None:
        entity["webhookStatus"] = _serialize_payment_webhook_status(obj.webhook_status)
    if obj.platform_type is not None:
        entity["platformType"] = _serialize_payment_client_type(obj.platform_type)
    if obj.currency is not None:
        entity["currency"] = _serialize_currency(obj.currency)
    if obj.is_escrow is not None:
        entity["isEscrow"] = obj.is_escrow
    if obj.escrow_status is not None:
        entity["escrowStatus"] = _serialize_payment_filter_input_escrow_status(obj.escrow_status)
    if obj.card_brand is not None:
        entity["cardBrand"] = _serialize_card_brand(obj.card_brand)
    if obj.card_type is not None:
        entity["cardType"] = _serialize_card_type(obj.card_type)
    if obj.card_owner_type is not None:
        entity["cardOwnerType"] = _serialize_card_owner_type(obj.card_owner_type)
    if obj.gift_certificate_type is not None:
        entity["giftCertificateType"] = _serialize_payment_method_gift_certificate_type(obj.gift_certificate_type)
    if obj.cash_receipt_type is not None:
        entity["cashReceiptType"] = _serialize_cash_receipt_input_type(obj.cash_receipt_type)
    if obj.cash_receipt_status is not None:
        entity["cashReceiptStatus"] = _serialize_payment_cash_receipt_status(obj.cash_receipt_status)
    if obj.cash_receipt_issued_at_range is not None:
        entity["cashReceiptIssuedAtRange"] = _serialize_date_time_range(obj.cash_receipt_issued_at_range)
    if obj.cash_receipt_cancelled_at_range is not None:
        entity["cashReceiptCancelledAtRange"] = _serialize_date_time_range(obj.cash_receipt_cancelled_at_range)
    if obj.text_search is not None:
        entity["textSearch"] = list(map(_serialize_payment_text_search, obj.text_search))
    return entity


def _deserialize_payment_filter_input(obj: Any) -> PaymentFilterInput:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "merchantId" in obj:
        merchant_id = obj["merchantId"]
        if not isinstance(merchant_id, str):
            raise ValueError(f"{repr(merchant_id)} is not str")
    else:
        merchant_id = None
    if "storeId" in obj:
        store_id = obj["storeId"]
        if not isinstance(store_id, str):
            raise ValueError(f"{repr(store_id)} is not str")
    else:
        store_id = None
    if "timestampType" in obj:
        timestamp_type = obj["timestampType"]
        timestamp_type = _deserialize_payment_timestamp_type(timestamp_type)
    else:
        timestamp_type = None
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
            item = _deserialize_payment_status(item)
            status[i] = item
    else:
        status = None
    if "methods" in obj:
        methods = obj["methods"]
        if not isinstance(methods, list):
            raise ValueError(f"{repr(methods)} is not list")
        for i, item in enumerate(methods):
            item = _deserialize_payment_method_type(item)
            methods[i] = item
    else:
        methods = None
    if "pgProvider" in obj:
        pg_provider = obj["pgProvider"]
        if not isinstance(pg_provider, list):
            raise ValueError(f"{repr(pg_provider)} is not list")
        for i, item in enumerate(pg_provider):
            item = _deserialize_pg_provider(item)
            pg_provider[i] = item
    else:
        pg_provider = None
    if "isTest" in obj:
        is_test = obj["isTest"]
        if not isinstance(is_test, bool):
            raise ValueError(f"{repr(is_test)} is not bool")
    else:
        is_test = None
    if "isScheduled" in obj:
        is_scheduled = obj["isScheduled"]
        if not isinstance(is_scheduled, bool):
            raise ValueError(f"{repr(is_scheduled)} is not bool")
    else:
        is_scheduled = None
    if "sortBy" in obj:
        sort_by = obj["sortBy"]
        sort_by = _deserialize_payment_sort_by(sort_by)
    else:
        sort_by = None
    if "sortOrder" in obj:
        sort_order = obj["sortOrder"]
        sort_order = _deserialize_sort_order(sort_order)
    else:
        sort_order = None
    if "version" in obj:
        version = obj["version"]
        version = _deserialize_port_one_version(version)
    else:
        version = None
    if "webhookStatus" in obj:
        webhook_status = obj["webhookStatus"]
        webhook_status = _deserialize_payment_webhook_status(webhook_status)
    else:
        webhook_status = None
    if "platformType" in obj:
        platform_type = obj["platformType"]
        platform_type = _deserialize_payment_client_type(platform_type)
    else:
        platform_type = None
    if "currency" in obj:
        currency = obj["currency"]
        currency = _deserialize_currency(currency)
    else:
        currency = None
    if "isEscrow" in obj:
        is_escrow = obj["isEscrow"]
        if not isinstance(is_escrow, bool):
            raise ValueError(f"{repr(is_escrow)} is not bool")
    else:
        is_escrow = None
    if "escrowStatus" in obj:
        escrow_status = obj["escrowStatus"]
        escrow_status = _deserialize_payment_filter_input_escrow_status(escrow_status)
    else:
        escrow_status = None
    if "cardBrand" in obj:
        card_brand = obj["cardBrand"]
        card_brand = _deserialize_card_brand(card_brand)
    else:
        card_brand = None
    if "cardType" in obj:
        card_type = obj["cardType"]
        card_type = _deserialize_card_type(card_type)
    else:
        card_type = None
    if "cardOwnerType" in obj:
        card_owner_type = obj["cardOwnerType"]
        card_owner_type = _deserialize_card_owner_type(card_owner_type)
    else:
        card_owner_type = None
    if "giftCertificateType" in obj:
        gift_certificate_type = obj["giftCertificateType"]
        gift_certificate_type = _deserialize_payment_method_gift_certificate_type(gift_certificate_type)
    else:
        gift_certificate_type = None
    if "cashReceiptType" in obj:
        cash_receipt_type = obj["cashReceiptType"]
        cash_receipt_type = _deserialize_cash_receipt_input_type(cash_receipt_type)
    else:
        cash_receipt_type = None
    if "cashReceiptStatus" in obj:
        cash_receipt_status = obj["cashReceiptStatus"]
        cash_receipt_status = _deserialize_payment_cash_receipt_status(cash_receipt_status)
    else:
        cash_receipt_status = None
    if "cashReceiptIssuedAtRange" in obj:
        cash_receipt_issued_at_range = obj["cashReceiptIssuedAtRange"]
        cash_receipt_issued_at_range = _deserialize_date_time_range(cash_receipt_issued_at_range)
    else:
        cash_receipt_issued_at_range = None
    if "cashReceiptCancelledAtRange" in obj:
        cash_receipt_cancelled_at_range = obj["cashReceiptCancelledAtRange"]
        cash_receipt_cancelled_at_range = _deserialize_date_time_range(cash_receipt_cancelled_at_range)
    else:
        cash_receipt_cancelled_at_range = None
    if "textSearch" in obj:
        text_search = obj["textSearch"]
        if not isinstance(text_search, list):
            raise ValueError(f"{repr(text_search)} is not list")
        for i, item in enumerate(text_search):
            item = _deserialize_payment_text_search(item)
            text_search[i] = item
    else:
        text_search = None
    return PaymentFilterInput(merchant_id, store_id, timestamp_type, from_, until, status, methods, pg_provider, is_test, is_scheduled, sort_by, sort_order, version, webhook_status, platform_type, currency, is_escrow, escrow_status, card_brand, card_type, card_owner_type, gift_certificate_type, cash_receipt_type, cash_receipt_status, cash_receipt_issued_at_range, cash_receipt_cancelled_at_range, text_search)
