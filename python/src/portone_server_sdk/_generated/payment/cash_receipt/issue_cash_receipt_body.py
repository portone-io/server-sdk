from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field
from ...common.cash_receipt_type import CashReceiptType, _deserialize_cash_receipt_type, _serialize_cash_receipt_type
from ...common.currency import Currency, _deserialize_currency, _serialize_currency
from ...payment.cash_receipt.issue_cash_receipt_customer_input import IssueCashReceiptCustomerInput, _deserialize_issue_cash_receipt_customer_input, _serialize_issue_cash_receipt_customer_input
from ...payment.cash_receipt.issue_cash_receipt_payment_method_type import IssueCashReceiptPaymentMethodType, _deserialize_issue_cash_receipt_payment_method_type, _serialize_issue_cash_receipt_payment_method_type
from ...common.payment_amount_input import PaymentAmountInput, _deserialize_payment_amount_input, _serialize_payment_amount_input
from ...common.payment_product_type import PaymentProductType, _deserialize_payment_product_type, _serialize_payment_product_type

@dataclass
class IssueCashReceiptBody:
    """현금영수증 발급 요청 양식
    """
    payment_id: str
    """결제 건 아이디

    외부 결제 건에 대한 수동 발급의 경우, 아이디를 직접 채번하여 입력합니다.
    """
    channel_key: str
    """채널 키
    """
    type: CashReceiptType
    """현금 영수증 유형
    """
    order_name: str
    """주문명
    """
    currency: Currency
    """화폐
    """
    amount: PaymentAmountInput
    """금액 세부 입력 정보
    """
    customer: IssueCashReceiptCustomerInput
    """고객 정보
    """
    store_id: Optional[str] = field(default=None)
    """상점 아이디

    접근 권한이 있는 상점 아이디만 입력 가능하며, 미입력시 토큰에 담긴 상점 아이디를 사용합니다.
    """
    product_type: Optional[PaymentProductType] = field(default=None)
    """상품 유형
    """
    paid_at: Optional[str] = field(default=None)
    """결제 일자
    (RFC 3339 date-time)
    """
    business_registration_number: Optional[str] = field(default=None)
    """사업자등록번호

    웰컴페이먼츠의 경우에만 입력합니다.
    """
    payment_method: Optional[IssueCashReceiptPaymentMethodType] = field(default=None)
    """결제 수단

    웰컴페이먼츠의 경우에만 입력합니다.
    """


def _serialize_issue_cash_receipt_body(obj: IssueCashReceiptBody) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["paymentId"] = obj.payment_id
    entity["channelKey"] = obj.channel_key
    entity["type"] = _serialize_cash_receipt_type(obj.type)
    entity["orderName"] = obj.order_name
    entity["currency"] = _serialize_currency(obj.currency)
    entity["amount"] = _serialize_payment_amount_input(obj.amount)
    entity["customer"] = _serialize_issue_cash_receipt_customer_input(obj.customer)
    if obj.store_id is not None:
        entity["storeId"] = obj.store_id
    if obj.product_type is not None:
        entity["productType"] = _serialize_payment_product_type(obj.product_type)
    if obj.paid_at is not None:
        entity["paidAt"] = obj.paid_at
    if obj.business_registration_number is not None:
        entity["businessRegistrationNumber"] = obj.business_registration_number
    if obj.payment_method is not None:
        entity["paymentMethod"] = _serialize_issue_cash_receipt_payment_method_type(obj.payment_method)
    return entity


def _deserialize_issue_cash_receipt_body(obj: Any) -> IssueCashReceiptBody:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "paymentId" not in obj:
        raise KeyError(f"'paymentId' is not in {obj}")
    payment_id = obj["paymentId"]
    if not isinstance(payment_id, str):
        raise ValueError(f"{repr(payment_id)} is not str")
    if "channelKey" not in obj:
        raise KeyError(f"'channelKey' is not in {obj}")
    channel_key = obj["channelKey"]
    if not isinstance(channel_key, str):
        raise ValueError(f"{repr(channel_key)} is not str")
    if "type" not in obj:
        raise KeyError(f"'type' is not in {obj}")
    type = obj["type"]
    type = _deserialize_cash_receipt_type(type)
    if "orderName" not in obj:
        raise KeyError(f"'orderName' is not in {obj}")
    order_name = obj["orderName"]
    if not isinstance(order_name, str):
        raise ValueError(f"{repr(order_name)} is not str")
    if "currency" not in obj:
        raise KeyError(f"'currency' is not in {obj}")
    currency = obj["currency"]
    currency = _deserialize_currency(currency)
    if "amount" not in obj:
        raise KeyError(f"'amount' is not in {obj}")
    amount = obj["amount"]
    amount = _deserialize_payment_amount_input(amount)
    if "customer" not in obj:
        raise KeyError(f"'customer' is not in {obj}")
    customer = obj["customer"]
    customer = _deserialize_issue_cash_receipt_customer_input(customer)
    if "storeId" in obj:
        store_id = obj["storeId"]
        if not isinstance(store_id, str):
            raise ValueError(f"{repr(store_id)} is not str")
    else:
        store_id = None
    if "productType" in obj:
        product_type = obj["productType"]
        product_type = _deserialize_payment_product_type(product_type)
    else:
        product_type = None
    if "paidAt" in obj:
        paid_at = obj["paidAt"]
        if not isinstance(paid_at, str):
            raise ValueError(f"{repr(paid_at)} is not str")
    else:
        paid_at = None
    if "businessRegistrationNumber" in obj:
        business_registration_number = obj["businessRegistrationNumber"]
        if not isinstance(business_registration_number, str):
            raise ValueError(f"{repr(business_registration_number)} is not str")
    else:
        business_registration_number = None
    if "paymentMethod" in obj:
        payment_method = obj["paymentMethod"]
        payment_method = _deserialize_issue_cash_receipt_payment_method_type(payment_method)
    else:
        payment_method = None
    return IssueCashReceiptBody(payment_id, channel_key, type, order_name, currency, amount, customer, store_id, product_type, paid_at, business_registration_number, payment_method)
