from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field
from portone_server_sdk._generated.common.country import Country, _deserialize_country, _serialize_country
from portone_server_sdk._generated.common.currency import Currency, _deserialize_currency, _serialize_currency
from portone_server_sdk._generated.common.customer_input import CustomerInput, _deserialize_customer_input, _serialize_customer_input
from portone_server_sdk._generated.payment.instant_payment_method_input import InstantPaymentMethodInput, _deserialize_instant_payment_method_input, _serialize_instant_payment_method_input
from portone_server_sdk._generated.common.payment_amount_input import PaymentAmountInput, _deserialize_payment_amount_input, _serialize_payment_amount_input
from portone_server_sdk._generated.common.payment_product import PaymentProduct, _deserialize_payment_product, _serialize_payment_product
from portone_server_sdk._generated.common.payment_product_type import PaymentProductType, _deserialize_payment_product_type, _serialize_payment_product_type
from portone_server_sdk._generated.common.separated_address_input import SeparatedAddressInput, _deserialize_separated_address_input, _serialize_separated_address_input

@dataclass
class InstantPaymentInput:
    """수기 결제 요청 정보
    """
    method: InstantPaymentMethodInput
    """결제수단 정보
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
    store_id: Optional[str]
    """상점 아이디

    접근 권한이 있는 상점 아이디만 입력 가능하며, 미입력시 토큰에 담긴 상점 아이디를 사용합니다.
    """
    channel_key: Optional[str]
    """채널 키

    채널 키 또는 채널 그룹 ID 필수
    """
    channel_group_id: Optional[str]
    """채널 그룹 ID

    채널 키 또는 채널 그룹 ID 필수
    """
    is_cultural_expense: Optional[bool]
    """문화비 지출 여부

    기본값은 false 입니다.
    """
    is_escrow: Optional[bool]
    """에스크로 결제 여부

    기본값은 false 입니다.
    """
    customer: Optional[CustomerInput]
    """고객 정보
    """
    custom_data: Optional[str]
    """사용자 지정 데이터
    """
    country: Optional[Country]
    """결제 국가
    """
    notice_urls: Optional[list[str]]
    """웹훅 주소

    결제 승인/실패 시 요청을 받을 웹훅 주소입니다.
    상점에 설정되어 있는 값보다 우선적으로 적용됩니다.
    입력된 값이 없을 경우에는 빈 배열로 해석됩니다.
    """
    products: Optional[list[PaymentProduct]]
    """상품 정보

    입력된 값이 없을 경우에는 빈 배열로 해석됩니다.
    """
    product_count: Optional[int]
    """상품 개수
    (int32)
    """
    product_type: Optional[PaymentProductType]
    """상품 유형
    """
    shipping_address: Optional[SeparatedAddressInput]
    """배송지 주소
    """
    promotion_id: Optional[str]
    """해당 결제에 적용할 프로모션 아이디
    """


def _serialize_instant_payment_input(obj: InstantPaymentInput) -> Any:
    entity = {}
    entity["method"] = _serialize_instant_payment_method_input(obj.method)
    entity["orderName"] = obj.order_name
    entity["amount"] = _serialize_payment_amount_input(obj.amount)
    entity["currency"] = _serialize_currency(obj.currency)
    if obj.store_id is not None:
        entity["storeId"] = obj.store_id
    if obj.channel_key is not None:
        entity["channelKey"] = obj.channel_key
    if obj.channel_group_id is not None:
        entity["channelGroupId"] = obj.channel_group_id
    if obj.is_cultural_expense is not None:
        entity["isCulturalExpense"] = obj.is_cultural_expense
    if obj.is_escrow is not None:
        entity["isEscrow"] = obj.is_escrow
    if obj.customer is not None:
        entity["customer"] = _serialize_customer_input(obj.customer)
    if obj.custom_data is not None:
        entity["customData"] = obj.custom_data
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
    return entity


def _deserialize_instant_payment_input(obj: Any) -> InstantPaymentInput:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "method" not in obj:
        raise KeyError(f"'method' is not in {obj}")
    method = obj["method"]
    method = _deserialize_instant_payment_method_input(method)
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
    if "channelGroupId" in obj:
        channel_group_id = obj["channelGroupId"]
        if not isinstance(channel_group_id, str):
            raise ValueError(f"{repr(channel_group_id)} is not str")
    else:
        channel_group_id = None
    if "isCulturalExpense" in obj:
        is_cultural_expense = obj["isCulturalExpense"]
        if not isinstance(is_cultural_expense, bool):
            raise ValueError(f"{repr(is_cultural_expense)} is not bool")
    else:
        is_cultural_expense = None
    if "isEscrow" in obj:
        is_escrow = obj["isEscrow"]
        if not isinstance(is_escrow, bool):
            raise ValueError(f"{repr(is_escrow)} is not bool")
    else:
        is_escrow = None
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
    return InstantPaymentInput(method, order_name, amount, currency, store_id, channel_key, channel_group_id, is_cultural_expense, is_escrow, customer, custom_data, country, notice_urls, products, product_count, product_type, shipping_address, promotion_id)
