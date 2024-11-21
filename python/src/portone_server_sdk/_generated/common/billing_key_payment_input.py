from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field
from ..common.cash_receipt_input import CashReceiptInput, _deserialize_cash_receipt_input, _serialize_cash_receipt_input
from ..common.country import Country, _deserialize_country, _serialize_country
from ..common.currency import Currency, _deserialize_currency, _serialize_currency
from ..common.customer_input import CustomerInput, _deserialize_customer_input, _serialize_customer_input
from ..common.payment_amount_input import PaymentAmountInput, _deserialize_payment_amount_input, _serialize_payment_amount_input
from ..common.payment_product import PaymentProduct, _deserialize_payment_product, _serialize_payment_product
from ..common.payment_product_type import PaymentProductType, _deserialize_payment_product_type, _serialize_payment_product_type
from ..common.separated_address_input import SeparatedAddressInput, _deserialize_separated_address_input, _serialize_separated_address_input

@dataclass
class BillingKeyPaymentInput:
    """빌링키 결제 요청 입력 정보
    """
    billing_key: str
    """빌링키 결제에 사용할 빌링키
    """
    order_name: str
    """주문명
    """
    amount: PaymentAmountInput
    """결제 금액 세부 입력 정보
    """
    currency: Currency
    """통화
    """
    store_id: Optional[str] = field(default=None)
    """상점 아이디

    접근 권한이 있는 상점 아이디만 입력 가능하며, 미입력시 토큰에 담긴 상점 아이디를 사용합니다.
    """
    channel_key: Optional[str] = field(default=None)
    """채널 키

    다수 채널에 대해 발급된 빌링키에 대해, 결제 채널을 특정하고 싶을 때 명시
    """
    customer: Optional[CustomerInput] = field(default=None)
    """고객 정보
    """
    custom_data: Optional[str] = field(default=None)
    """사용자 지정 데이터
    """
    installment_month: Optional[int] = field(default=None)
    """할부 개월 수
    (int32)
    """
    use_free_interest_from_merchant: Optional[bool] = field(default=None)
    """무이자 할부 이자를 고객사가 부담할지 여부
    """
    use_card_point: Optional[bool] = field(default=None)
    """카드 포인트 사용 여부
    """
    cash_receipt: Optional[CashReceiptInput] = field(default=None)
    """현금영수증 정보
    """
    country: Optional[Country] = field(default=None)
    """결제 국가
    """
    notice_urls: Optional[list[str]] = field(default=None)
    """웹훅 주소

    결제 승인/실패 시 요청을 받을 웹훅 주소입니다.
    상점에 설정되어 있는 값보다 우선적으로 적용됩니다.
    입력된 값이 없을 경우에는 빈 배열로 해석됩니다.
    """
    products: Optional[list[PaymentProduct]] = field(default=None)
    """상품 정보

    입력된 값이 없을 경우에는 빈 배열로 해석됩니다.
    """
    product_count: Optional[int] = field(default=None)
    """상품 개수
    (int32)
    """
    product_type: Optional[PaymentProductType] = field(default=None)
    """상품 유형
    """
    shipping_address: Optional[SeparatedAddressInput] = field(default=None)
    """배송지 주소
    """
    promotion_id: Optional[str] = field(default=None)
    """해당 결제에 적용할 프로모션 아이디
    """
    bypass: Optional[dict] = field(default=None)
    """PG사별 추가 파라미터 ("PG사별 연동 가이드" 참고)
    """


def _serialize_billing_key_payment_input(obj: BillingKeyPaymentInput) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["billingKey"] = obj.billing_key
    entity["orderName"] = obj.order_name
    entity["amount"] = _serialize_payment_amount_input(obj.amount)
    entity["currency"] = _serialize_currency(obj.currency)
    if obj.store_id is not None:
        entity["storeId"] = obj.store_id
    if obj.channel_key is not None:
        entity["channelKey"] = obj.channel_key
    if obj.customer is not None:
        entity["customer"] = _serialize_customer_input(obj.customer)
    if obj.custom_data is not None:
        entity["customData"] = obj.custom_data
    if obj.installment_month is not None:
        entity["installmentMonth"] = obj.installment_month
    if obj.use_free_interest_from_merchant is not None:
        entity["useFreeInterestFromMerchant"] = obj.use_free_interest_from_merchant
    if obj.use_card_point is not None:
        entity["useCardPoint"] = obj.use_card_point
    if obj.cash_receipt is not None:
        entity["cashReceipt"] = _serialize_cash_receipt_input(obj.cash_receipt)
    if obj.country is not None:
        entity["country"] = _serialize_country(obj.country)
    if obj.notice_urls is not None:
        entity["noticeUrls"] = obj.notice_urls
    if obj.products is not None:
        entity["products"] = list(map(_serialize_payment_product, obj.products))
    if obj.product_count is not None:
        entity["productCount"] = obj.product_count
    if obj.product_type is not None:
        entity["productType"] = _serialize_payment_product_type(obj.product_type)
    if obj.shipping_address is not None:
        entity["shippingAddress"] = _serialize_separated_address_input(obj.shipping_address)
    if obj.promotion_id is not None:
        entity["promotionId"] = obj.promotion_id
    if obj.bypass is not None:
        entity["bypass"] = obj.bypass
    return entity


def _deserialize_billing_key_payment_input(obj: Any) -> BillingKeyPaymentInput:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
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
    if "amount" not in obj:
        raise KeyError(f"'amount' is not in {obj}")
    amount = obj["amount"]
    amount = _deserialize_payment_amount_input(amount)
    if "currency" not in obj:
        raise KeyError(f"'currency' is not in {obj}")
    currency = obj["currency"]
    currency = _deserialize_currency(currency)
    if "storeId" in obj:
        store_id = obj["storeId"]
        if not isinstance(store_id, str):
            raise ValueError(f"{repr(store_id)} is not str")
    else:
        store_id = None
    if "channelKey" in obj:
        channel_key = obj["channelKey"]
        if not isinstance(channel_key, str):
            raise ValueError(f"{repr(channel_key)} is not str")
    else:
        channel_key = None
    if "customer" in obj:
        customer = obj["customer"]
        customer = _deserialize_customer_input(customer)
    else:
        customer = None
    if "customData" in obj:
        custom_data = obj["customData"]
        if not isinstance(custom_data, str):
            raise ValueError(f"{repr(custom_data)} is not str")
    else:
        custom_data = None
    if "installmentMonth" in obj:
        installment_month = obj["installmentMonth"]
        if not isinstance(installment_month, int):
            raise ValueError(f"{repr(installment_month)} is not int")
    else:
        installment_month = None
    if "useFreeInterestFromMerchant" in obj:
        use_free_interest_from_merchant = obj["useFreeInterestFromMerchant"]
        if not isinstance(use_free_interest_from_merchant, bool):
            raise ValueError(f"{repr(use_free_interest_from_merchant)} is not bool")
    else:
        use_free_interest_from_merchant = None
    if "useCardPoint" in obj:
        use_card_point = obj["useCardPoint"]
        if not isinstance(use_card_point, bool):
            raise ValueError(f"{repr(use_card_point)} is not bool")
    else:
        use_card_point = None
    if "cashReceipt" in obj:
        cash_receipt = obj["cashReceipt"]
        cash_receipt = _deserialize_cash_receipt_input(cash_receipt)
    else:
        cash_receipt = None
    if "country" in obj:
        country = obj["country"]
        country = _deserialize_country(country)
    else:
        country = None
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
    if "productCount" in obj:
        product_count = obj["productCount"]
        if not isinstance(product_count, int):
            raise ValueError(f"{repr(product_count)} is not int")
    else:
        product_count = None
    if "productType" in obj:
        product_type = obj["productType"]
        product_type = _deserialize_payment_product_type(product_type)
    else:
        product_type = None
    if "shippingAddress" in obj:
        shipping_address = obj["shippingAddress"]
        shipping_address = _deserialize_separated_address_input(shipping_address)
    else:
        shipping_address = None
    if "promotionId" in obj:
        promotion_id = obj["promotionId"]
        if not isinstance(promotion_id, str):
            raise ValueError(f"{repr(promotion_id)} is not str")
    else:
        promotion_id = None
    if "bypass" in obj:
        bypass = obj["bypass"]
        if not isinstance(bypass, dict):
            raise ValueError(f"{repr(bypass)} is not dict")
    else:
        bypass = None
    return BillingKeyPaymentInput(billing_key, order_name, amount, currency, store_id, channel_key, customer, custom_data, installment_month, use_free_interest_from_merchant, use_card_point, cash_receipt, country, notice_urls, products, product_count, product_type, shipping_address, promotion_id, bypass)
