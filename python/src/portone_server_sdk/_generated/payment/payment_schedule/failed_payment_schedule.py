from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field
from ...common.currency import Currency, _deserialize_currency, _serialize_currency
from ...common.customer import Customer, _deserialize_customer, _serialize_customer
from ...common.payment_product import PaymentProduct, _deserialize_payment_product, _serialize_payment_product

@dataclass
class FailedPaymentSchedule:
    """결제 실패 상태
    """
    """결제 예약 건 상태
    """
    id: str
    """결제 예약 건 아이디
    """
    merchant_id: str
    """고객사 아이디
    """
    store_id: str
    """상점 아이디
    """
    payment_id: str
    """결제 건 아이디
    """
    billing_key: str
    """빌링키
    """
    order_name: str
    """주문명
    """
    is_cultural_expense: bool
    """문화비 지출 여부
    """
    is_escrow: bool
    """에스크로 결제 여부
    """
    customer: Customer
    """고객 정보
    """
    custom_data: str
    """사용자 지정 데이터
    """
    total_amount: int
    """결제 총 금액
    (int64)
    """
    currency: Currency
    """통화
    """
    created_at: str
    """결제 예약 등록 시점
    (RFC 3339 date-time)
    """
    time_to_pay: str
    """결제 예정 시점
    (RFC 3339 date-time)
    """
    started_at: str
    """결제 시작 시점
    (RFC 3339 date-time)
    """
    completed_at: str
    """결제 완료 시점
    (RFC 3339 date-time)
    """
    tax_free_amount: Optional[int] = field(default=None)
    """면세액
    (int64)
    """
    vat_amount: Optional[int] = field(default=None)
    """부가세
    (int64)
    """
    installment_month: Optional[int] = field(default=None)
    """할부 개월 수
    (int32)
    """
    notice_urls: Optional[list[str]] = field(default=None)
    """웹훅 주소
    """
    products: Optional[list[PaymentProduct]] = field(default=None)
    """상품 정보
    """


def _serialize_failed_payment_schedule(obj: FailedPaymentSchedule) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["status"] = "FAILED"
    entity["id"] = obj.id
    entity["merchantId"] = obj.merchant_id
    entity["storeId"] = obj.store_id
    entity["paymentId"] = obj.payment_id
    entity["billingKey"] = obj.billing_key
    entity["orderName"] = obj.order_name
    entity["isCulturalExpense"] = obj.is_cultural_expense
    entity["isEscrow"] = obj.is_escrow
    entity["customer"] = _serialize_customer(obj.customer)
    entity["customData"] = obj.custom_data
    entity["totalAmount"] = obj.total_amount
    entity["currency"] = _serialize_currency(obj.currency)
    entity["createdAt"] = obj.created_at
    entity["timeToPay"] = obj.time_to_pay
    entity["startedAt"] = obj.started_at
    entity["completedAt"] = obj.completed_at
    if obj.tax_free_amount is not None:
        entity["taxFreeAmount"] = obj.tax_free_amount
    if obj.vat_amount is not None:
        entity["vatAmount"] = obj.vat_amount
    if obj.installment_month is not None:
        entity["installmentMonth"] = obj.installment_month
    if obj.notice_urls is not None:
        entity["noticeUrls"] = obj.notice_urls
    if obj.products is not None:
        entity["products"] = list(map(_serialize_payment_product, obj.products))
    return entity


def _deserialize_failed_payment_schedule(obj: Any) -> FailedPaymentSchedule:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "status" not in obj:
        raise KeyError(f"'status' is not in {obj}")
    status = obj["status"]
    if status != "FAILED":
        raise ValueError(f"{repr(status)} is not 'FAILED'")
    if "id" not in obj:
        raise KeyError(f"'id' is not in {obj}")
    id = obj["id"]
    if not isinstance(id, str):
        raise ValueError(f"{repr(id)} is not str")
    if "merchantId" not in obj:
        raise KeyError(f"'merchantId' is not in {obj}")
    merchant_id = obj["merchantId"]
    if not isinstance(merchant_id, str):
        raise ValueError(f"{repr(merchant_id)} is not str")
    if "storeId" not in obj:
        raise KeyError(f"'storeId' is not in {obj}")
    store_id = obj["storeId"]
    if not isinstance(store_id, str):
        raise ValueError(f"{repr(store_id)} is not str")
    if "paymentId" not in obj:
        raise KeyError(f"'paymentId' is not in {obj}")
    payment_id = obj["paymentId"]
    if not isinstance(payment_id, str):
        raise ValueError(f"{repr(payment_id)} is not str")
    if "billingKey" not in obj:
        raise KeyError(f"'billingKey' is not in {obj}")
    billing_key = obj["billingKey"]
    if not isinstance(billing_key, str):
        raise ValueError(f"{repr(billing_key)} is not str")
    if "orderName" not in obj:
        raise KeyError(f"'orderName' is not in {obj}")
    order_name = obj["orderName"]
    if not isinstance(order_name, str):
        raise ValueError(f"{repr(order_name)} is not str")
    if "isCulturalExpense" not in obj:
        raise KeyError(f"'isCulturalExpense' is not in {obj}")
    is_cultural_expense = obj["isCulturalExpense"]
    if not isinstance(is_cultural_expense, bool):
        raise ValueError(f"{repr(is_cultural_expense)} is not bool")
    if "isEscrow" not in obj:
        raise KeyError(f"'isEscrow' is not in {obj}")
    is_escrow = obj["isEscrow"]
    if not isinstance(is_escrow, bool):
        raise ValueError(f"{repr(is_escrow)} is not bool")
    if "customer" not in obj:
        raise KeyError(f"'customer' is not in {obj}")
    customer = obj["customer"]
    customer = _deserialize_customer(customer)
    if "customData" not in obj:
        raise KeyError(f"'customData' is not in {obj}")
    custom_data = obj["customData"]
    if not isinstance(custom_data, str):
        raise ValueError(f"{repr(custom_data)} is not str")
    if "totalAmount" not in obj:
        raise KeyError(f"'totalAmount' is not in {obj}")
    total_amount = obj["totalAmount"]
    if not isinstance(total_amount, int):
        raise ValueError(f"{repr(total_amount)} is not int")
    if "currency" not in obj:
        raise KeyError(f"'currency' is not in {obj}")
    currency = obj["currency"]
    currency = _deserialize_currency(currency)
    if "createdAt" not in obj:
        raise KeyError(f"'createdAt' is not in {obj}")
    created_at = obj["createdAt"]
    if not isinstance(created_at, str):
        raise ValueError(f"{repr(created_at)} is not str")
    if "timeToPay" not in obj:
        raise KeyError(f"'timeToPay' is not in {obj}")
    time_to_pay = obj["timeToPay"]
    if not isinstance(time_to_pay, str):
        raise ValueError(f"{repr(time_to_pay)} is not str")
    if "startedAt" not in obj:
        raise KeyError(f"'startedAt' is not in {obj}")
    started_at = obj["startedAt"]
    if not isinstance(started_at, str):
        raise ValueError(f"{repr(started_at)} is not str")
    if "completedAt" not in obj:
        raise KeyError(f"'completedAt' is not in {obj}")
    completed_at = obj["completedAt"]
    if not isinstance(completed_at, str):
        raise ValueError(f"{repr(completed_at)} is not str")
    if "taxFreeAmount" in obj:
        tax_free_amount = obj["taxFreeAmount"]
        if not isinstance(tax_free_amount, int):
            raise ValueError(f"{repr(tax_free_amount)} is not int")
    else:
        tax_free_amount = None
    if "vatAmount" in obj:
        vat_amount = obj["vatAmount"]
        if not isinstance(vat_amount, int):
            raise ValueError(f"{repr(vat_amount)} is not int")
    else:
        vat_amount = None
    if "installmentMonth" in obj:
        installment_month = obj["installmentMonth"]
        if not isinstance(installment_month, int):
            raise ValueError(f"{repr(installment_month)} is not int")
    else:
        installment_month = None
    if "noticeUrls" in obj:
        notice_urls = obj["noticeUrls"]
        if not isinstance(notice_urls, list):
            raise ValueError(f"{repr(notice_urls)} is not list")
        for i, item in enumerate(notice_urls):
            if not isinstance(item, str):
                raise ValueError(f"{repr(item)} is not str")
    else:
        notice_urls = None
    if "products" in obj:
        products = obj["products"]
        if not isinstance(products, list):
            raise ValueError(f"{repr(products)} is not list")
        for i, item in enumerate(products):
            item = _deserialize_payment_product(item)
            products[i] = item
    else:
        products = None
    return FailedPaymentSchedule(id, merchant_id, store_id, payment_id, billing_key, order_name, is_cultural_expense, is_escrow, customer, custom_data, total_amount, currency, created_at, time_to_pay, started_at, completed_at, tax_free_amount, vat_amount, installment_month, notice_urls, products)
