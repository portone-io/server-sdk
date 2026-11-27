from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field
from ..common.channel_group_summary import ChannelGroupSummary, _deserialize_channel_group_summary, _serialize_channel_group_summary
from ..common.country import Country, _deserialize_country, _serialize_country
from ..common.currency import Currency, _deserialize_currency, _serialize_currency
from ..common.customer import Customer, _deserialize_customer, _serialize_customer
from ..payment.payment_amount import PaymentAmount, _deserialize_payment_amount, _serialize_payment_amount
from ..payment.payment_cancellation import PaymentCancellation, _deserialize_payment_cancellation, _serialize_payment_cancellation
from ..payment.payment_cash_receipt import PaymentCashReceipt, _deserialize_payment_cash_receipt, _serialize_payment_cash_receipt
from ..payment.payment_escrow import PaymentEscrow, _deserialize_payment_escrow, _serialize_payment_escrow
from ..payment.payment_method import PaymentMethod, _deserialize_payment_method, _serialize_payment_method
from ..common.payment_product import PaymentProduct, _deserialize_payment_product, _serialize_payment_product
from ..payment.payment_webhook import PaymentWebhook, _deserialize_payment_webhook, _serialize_payment_webhook
from ..common.port_one_version import PortOneVersion, _deserialize_port_one_version, _serialize_port_one_version
from ..common.selected_channel import SelectedChannel, _deserialize_selected_channel, _serialize_selected_channel

@dataclass
class CancelledPaymentTransaction:
    """결제 취소 상태 건
    """
    """결제 시도 상태
    """
    id: str
    """결제 시도 아이디 (transactionId)

    V1 결제 건의 경우 imp_uid에 해당합니다.
    """
    payment_id: str
    """결제 건 아이디
    """
    merchant_id: str
    """고객사 아이디
    """
    store_id: str
    """상점 아이디
    """
    channel: SelectedChannel
    """결제 채널
    """
    version: PortOneVersion
    """포트원 버전
    """
    requested_at: str
    """결제 요청 시점
    (RFC 3339 date-time)
    """
    updated_at: str
    """업데이트 시점
    (RFC 3339 date-time)
    """
    status_changed_at: str
    """상태 업데이트 시점
    (RFC 3339 date-time)
    """
    order_name: str
    """주문명
    """
    amount: PaymentAmount
    """결제 금액 관련 세부 정보
    """
    currency: Currency
    """통화
    """
    customer: Customer
    """구매자 정보
    """
    cancellations: list[PaymentCancellation]
    """결제 취소 내역
    """
    cancelled_at: str
    """결제 취소 시점
    (RFC 3339 date-time)
    """
    method: Optional[PaymentMethod] = field(default=None)
    """결제수단 정보
    """
    channel_group: Optional[ChannelGroupSummary] = field(default=None)
    """결제 채널 그룹 정보
    """
    schedule_id: Optional[str] = field(default=None)
    """결제 예약 건 아이디

    결제 예약을 이용한 경우에만 존재
    """
    billing_key: Optional[str] = field(default=None)
    """결제 시 사용된 빌링키

    빌링키 결제인 경우에만 존재
    """
    webhooks: Optional[list[PaymentWebhook]] = field(default=None)
    """웹훅 발송 내역
    """
    promotion_id: Optional[str] = field(default=None)
    """프로모션 아이디
    """
    is_cultural_expense: Optional[bool] = field(default=None)
    """문화비 지출 여부
    """
    escrow: Optional[PaymentEscrow] = field(default=None)
    """에스크로 결제 정보

    에스크로 결제인 경우 존재합니다.
    """
    products: Optional[list[PaymentProduct]] = field(default=None)
    """상품 정보
    """
    product_count: Optional[int] = field(default=None)
    """상품 갯수
    (int32)
    """
    custom_data: Optional[str] = field(default=None)
    """사용자 지정 데이터
    """
    country: Optional[Country] = field(default=None)
    """국가 코드
    """
    paid_at: Optional[str] = field(default=None)
    """결제 완료 시점
    (RFC 3339 date-time)
    """
    pg_tx_id: Optional[str] = field(default=None)
    """PG사 거래 아이디
    """
    cash_receipt: Optional[PaymentCashReceipt] = field(default=None)
    """현금영수증
    """
    receipt_url: Optional[str] = field(default=None)
    """거래 영수증 URL
    """


def _serialize_cancelled_payment_transaction(obj: CancelledPaymentTransaction) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["status"] = "CANCELLED"
    entity["id"] = obj.id
    entity["paymentId"] = obj.payment_id
    entity["merchantId"] = obj.merchant_id
    entity["storeId"] = obj.store_id
    entity["channel"] = _serialize_selected_channel(obj.channel)
    entity["version"] = _serialize_port_one_version(obj.version)
    entity["requestedAt"] = obj.requested_at
    entity["updatedAt"] = obj.updated_at
    entity["statusChangedAt"] = obj.status_changed_at
    entity["orderName"] = obj.order_name
    entity["amount"] = _serialize_payment_amount(obj.amount)
    entity["currency"] = _serialize_currency(obj.currency)
    entity["customer"] = _serialize_customer(obj.customer)
    entity["cancellations"] = list(map(_serialize_payment_cancellation, obj.cancellations))
    entity["cancelledAt"] = obj.cancelled_at
    if obj.method is not None:
        entity["method"] = _serialize_payment_method(obj.method)
    if obj.channel_group is not None:
        entity["channelGroup"] = _serialize_channel_group_summary(obj.channel_group)
    if obj.schedule_id is not None:
        entity["scheduleId"] = obj.schedule_id
    if obj.billing_key is not None:
        entity["billingKey"] = obj.billing_key
    if obj.webhooks is not None:
        entity["webhooks"] = list(map(_serialize_payment_webhook, obj.webhooks))
    if obj.promotion_id is not None:
        entity["promotionId"] = obj.promotion_id
    if obj.is_cultural_expense is not None:
        entity["isCulturalExpense"] = obj.is_cultural_expense
    if obj.escrow is not None:
        entity["escrow"] = _serialize_payment_escrow(obj.escrow)
    if obj.products is not None:
        entity["products"] = list(map(_serialize_payment_product, obj.products))
    if obj.product_count is not None:
        entity["productCount"] = obj.product_count
    if obj.custom_data is not None:
        entity["customData"] = obj.custom_data
    if obj.country is not None:
        entity["country"] = _serialize_country(obj.country)
    if obj.paid_at is not None:
        entity["paidAt"] = obj.paid_at
    if obj.pg_tx_id is not None:
        entity["pgTxId"] = obj.pg_tx_id
    if obj.cash_receipt is not None:
        entity["cashReceipt"] = _serialize_payment_cash_receipt(obj.cash_receipt)
    if obj.receipt_url is not None:
        entity["receiptUrl"] = obj.receipt_url
    return entity


def _deserialize_cancelled_payment_transaction(obj: Any) -> CancelledPaymentTransaction:
    if not isinstance(obj, dict):
        raise ValueError("Expected dict for obj")
    if "status" not in obj:
        raise KeyError("Missing required field 'status'")
    status = obj["status"]
    if status != "CANCELLED":
        raise ValueError("Expected 'CANCELLED' for status")
    if "id" not in obj:
        raise KeyError("Missing required field 'id'")
    id = obj["id"]
    if not isinstance(id, str):
        raise ValueError("Expected str for id")
    if "paymentId" not in obj:
        raise KeyError("Missing required field 'paymentId'")
    payment_id = obj["paymentId"]
    if not isinstance(payment_id, str):
        raise ValueError("Expected str for payment_id")
    if "merchantId" not in obj:
        raise KeyError("Missing required field 'merchantId'")
    merchant_id = obj["merchantId"]
    if not isinstance(merchant_id, str):
        raise ValueError("Expected str for merchant_id")
    if "storeId" not in obj:
        raise KeyError("Missing required field 'storeId'")
    store_id = obj["storeId"]
    if not isinstance(store_id, str):
        raise ValueError("Expected str for store_id")
    if "channel" not in obj:
        raise KeyError("Missing required field 'channel'")
    channel = obj["channel"]
    channel = _deserialize_selected_channel(channel)
    if "version" not in obj:
        raise KeyError("Missing required field 'version'")
    version = obj["version"]
    version = _deserialize_port_one_version(version)
    if "requestedAt" not in obj:
        raise KeyError("Missing required field 'requestedAt'")
    requested_at = obj["requestedAt"]
    if not isinstance(requested_at, str):
        raise ValueError("Expected str for requested_at")
    if "updatedAt" not in obj:
        raise KeyError("Missing required field 'updatedAt'")
    updated_at = obj["updatedAt"]
    if not isinstance(updated_at, str):
        raise ValueError("Expected str for updated_at")
    if "statusChangedAt" not in obj:
        raise KeyError("Missing required field 'statusChangedAt'")
    status_changed_at = obj["statusChangedAt"]
    if not isinstance(status_changed_at, str):
        raise ValueError("Expected str for status_changed_at")
    if "orderName" not in obj:
        raise KeyError("Missing required field 'orderName'")
    order_name = obj["orderName"]
    if not isinstance(order_name, str):
        raise ValueError("Expected str for order_name")
    if "amount" not in obj:
        raise KeyError("Missing required field 'amount'")
    amount = obj["amount"]
    amount = _deserialize_payment_amount(amount)
    if "currency" not in obj:
        raise KeyError("Missing required field 'currency'")
    currency = obj["currency"]
    currency = _deserialize_currency(currency)
    if "customer" not in obj:
        raise KeyError("Missing required field 'customer'")
    customer = obj["customer"]
    customer = _deserialize_customer(customer)
    if "cancellations" not in obj:
        raise KeyError("Missing required field 'cancellations'")
    cancellations = obj["cancellations"]
    if not isinstance(cancellations, list):
        raise ValueError("Expected list for cancellations")
    for i, item in enumerate(cancellations):
        item = _deserialize_payment_cancellation(item)
        cancellations[i] = item
    if "cancelledAt" not in obj:
        raise KeyError("Missing required field 'cancelledAt'")
    cancelled_at = obj["cancelledAt"]
    if not isinstance(cancelled_at, str):
        raise ValueError("Expected str for cancelled_at")
    if "method" in obj:
        method = obj["method"]
        method = _deserialize_payment_method(method)
    else:
        method = None
    if "channelGroup" in obj:
        channel_group = obj["channelGroup"]
        channel_group = _deserialize_channel_group_summary(channel_group)
    else:
        channel_group = None
    if "scheduleId" in obj:
        schedule_id = obj["scheduleId"]
        if not isinstance(schedule_id, str):
            raise ValueError("Expected str for schedule_id")
    else:
        schedule_id = None
    if "billingKey" in obj:
        billing_key = obj["billingKey"]
        if not isinstance(billing_key, str):
            raise ValueError("Expected str for billing_key")
    else:
        billing_key = None
    if "webhooks" in obj:
        webhooks = obj["webhooks"]
        if not isinstance(webhooks, list):
            raise ValueError("Expected list for webhooks")
        for i, item in enumerate(webhooks):
            item = _deserialize_payment_webhook(item)
            webhooks[i] = item
    else:
        webhooks = None
    if "promotionId" in obj:
        promotion_id = obj["promotionId"]
        if not isinstance(promotion_id, str):
            raise ValueError("Expected str for promotion_id")
    else:
        promotion_id = None
    if "isCulturalExpense" in obj:
        is_cultural_expense = obj["isCulturalExpense"]
        if not isinstance(is_cultural_expense, bool):
            raise ValueError("Expected bool for is_cultural_expense")
    else:
        is_cultural_expense = None
    if "escrow" in obj:
        escrow = obj["escrow"]
        escrow = _deserialize_payment_escrow(escrow)
    else:
        escrow = None
    if "products" in obj:
        products = obj["products"]
        if not isinstance(products, list):
            raise ValueError("Expected list for products")
        for i, item in enumerate(products):
            item = _deserialize_payment_product(item)
            products[i] = item
    else:
        products = None
    if "productCount" in obj:
        product_count = obj["productCount"]
        if not isinstance(product_count, int):
            raise ValueError("Expected int for product_count")
    else:
        product_count = None
    if "customData" in obj:
        custom_data = obj["customData"]
        if not isinstance(custom_data, str):
            raise ValueError("Expected str for custom_data")
    else:
        custom_data = None
    if "country" in obj:
        country = obj["country"]
        country = _deserialize_country(country)
    else:
        country = None
    if "paidAt" in obj:
        paid_at = obj["paidAt"]
        if not isinstance(paid_at, str):
            raise ValueError("Expected str for paid_at")
    else:
        paid_at = None
    if "pgTxId" in obj:
        pg_tx_id = obj["pgTxId"]
        if not isinstance(pg_tx_id, str):
            raise ValueError("Expected str for pg_tx_id")
    else:
        pg_tx_id = None
    if "cashReceipt" in obj:
        cash_receipt = obj["cashReceipt"]
        cash_receipt = _deserialize_payment_cash_receipt(cash_receipt)
    else:
        cash_receipt = None
    if "receiptUrl" in obj:
        receipt_url = obj["receiptUrl"]
        if not isinstance(receipt_url, str):
            raise ValueError("Expected str for receipt_url")
    else:
        receipt_url = None
    return CancelledPaymentTransaction(id, payment_id, merchant_id, store_id, channel, version, requested_at, updated_at, status_changed_at, order_name, amount, currency, customer, cancellations, cancelled_at, method, channel_group, schedule_id, billing_key, webhooks, promotion_id, is_cultural_expense, escrow, products, product_count, custom_data, country, paid_at, pg_tx_id, cash_receipt, receipt_url)
