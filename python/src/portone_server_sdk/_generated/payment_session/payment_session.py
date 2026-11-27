from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field
from ..common.checkout_payment_method import CheckoutPaymentMethod, _deserialize_checkout_payment_method, _serialize_checkout_payment_method
from ..common.country import Country, _deserialize_country, _serialize_country
from ..common.currency import Currency, _deserialize_currency, _serialize_currency
from ..payment_session.payment_session_agreement import PaymentSessionAgreement, _deserialize_payment_session_agreement, _serialize_payment_session_agreement
from ..payment_session.payment_session_colors import PaymentSessionColors, _deserialize_payment_session_colors, _serialize_payment_session_colors
from ..payment_session.payment_session_product import PaymentSessionProduct, _deserialize_payment_session_product, _serialize_payment_session_product

@dataclass
class PaymentSession:
    """결제 세션
    """
    id: str
    """결제 세션 아이디
    """
    store_id: str
    """상점 아이디
    """
    payment_id: str
    """결제 건 아이디
    """
    profile_key: str
    """프로필 키
    """
    country: Country
    """국가
    """
    currency: Currency
    """통화
    """
    total_amount: int
    """전체 결제 금액
    (int64)
    """
    order_name: str
    """주문명
    """
    created_at: str
    """생성 시각
    (RFC 3339 date-time)
    """
    expires_at: str
    """만료 시각
    (RFC 3339 date-time)
    """
    payment_method: Optional[CheckoutPaymentMethod] = field(default=None)
    """결제 수단 지정

    지정한 경우, 정보 추가 입력이 필요하지 않은 경우에 주문서를 건너뛰고 결제로 바로 이동합니다.
    """
    redirect_url: Optional[str] = field(default=None)
    """결제 완료 후 리다이렉트 URL

    지정하지 않으면 기본 결과 페이지가 표시됩니다.
    """
    products: Optional[list[PaymentSessionProduct]] = field(default=None)
    """주문 항목 목록
    """
    customer_name: Optional[str] = field(default=None)
    """구매자 이름
    """
    customer_email: Optional[str] = field(default=None)
    """구매자 이메일
    """
    store_name: Optional[str] = field(default=None)
    """상점 이름

    페이지 헤더 및 결제사 UI에 표시됩니다.
    """
    agreements: Optional[list[PaymentSessionAgreement]] = field(default=None)
    """사용자 지정 약관 목록

    구매자가 모든 약관에 동의해야 결제 버튼이 활성화됩니다.
    """
    order_image_url: Optional[str] = field(default=None)
    """주문 대표 이미지 URL
    """
    custom_data: Optional[str] = field(default=None)
    """사용자 지정 데이터

    결제 완료 후 결제 건 조회에서도 확인할 수 있습니다.
    """
    colors: Optional[PaymentSessionColors] = field(default=None)
    """체크아웃 페이지 색 설정
    """


def _serialize_payment_session(obj: PaymentSession) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["id"] = obj.id
    entity["storeId"] = obj.store_id
    entity["paymentId"] = obj.payment_id
    entity["profileKey"] = obj.profile_key
    entity["country"] = _serialize_country(obj.country)
    entity["currency"] = _serialize_currency(obj.currency)
    entity["totalAmount"] = obj.total_amount
    entity["orderName"] = obj.order_name
    entity["createdAt"] = obj.created_at
    entity["expiresAt"] = obj.expires_at
    if obj.payment_method is not None:
        entity["paymentMethod"] = _serialize_checkout_payment_method(obj.payment_method)
    if obj.redirect_url is not None:
        entity["redirectUrl"] = obj.redirect_url
    if obj.products is not None:
        entity["products"] = list(map(_serialize_payment_session_product, obj.products))
    if obj.customer_name is not None:
        entity["customerName"] = obj.customer_name
    if obj.customer_email is not None:
        entity["customerEmail"] = obj.customer_email
    if obj.store_name is not None:
        entity["storeName"] = obj.store_name
    if obj.agreements is not None:
        entity["agreements"] = list(map(_serialize_payment_session_agreement, obj.agreements))
    if obj.order_image_url is not None:
        entity["orderImageUrl"] = obj.order_image_url
    if obj.custom_data is not None:
        entity["customData"] = obj.custom_data
    if obj.colors is not None:
        entity["colors"] = _serialize_payment_session_colors(obj.colors)
    return entity


def _deserialize_payment_session(obj: Any) -> PaymentSession:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "id" not in obj:
        raise KeyError(f"'id' is not in {obj}")
    id = obj["id"]
    if not isinstance(id, str):
        raise ValueError(f"{repr(id)} is not str")
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
    if "profileKey" not in obj:
        raise KeyError(f"'profileKey' is not in {obj}")
    profile_key = obj["profileKey"]
    if not isinstance(profile_key, str):
        raise ValueError(f"{repr(profile_key)} is not str")
    if "country" not in obj:
        raise KeyError(f"'country' is not in {obj}")
    country = obj["country"]
    country = _deserialize_country(country)
    if "currency" not in obj:
        raise KeyError(f"'currency' is not in {obj}")
    currency = obj["currency"]
    currency = _deserialize_currency(currency)
    if "totalAmount" not in obj:
        raise KeyError(f"'totalAmount' is not in {obj}")
    total_amount = obj["totalAmount"]
    if not isinstance(total_amount, int):
        raise ValueError(f"{repr(total_amount)} is not int")
    if "orderName" not in obj:
        raise KeyError(f"'orderName' is not in {obj}")
    order_name = obj["orderName"]
    if not isinstance(order_name, str):
        raise ValueError(f"{repr(order_name)} is not str")
    if "createdAt" not in obj:
        raise KeyError(f"'createdAt' is not in {obj}")
    created_at = obj["createdAt"]
    if not isinstance(created_at, str):
        raise ValueError(f"{repr(created_at)} is not str")
    if "expiresAt" not in obj:
        raise KeyError(f"'expiresAt' is not in {obj}")
    expires_at = obj["expiresAt"]
    if not isinstance(expires_at, str):
        raise ValueError(f"{repr(expires_at)} is not str")
    if "paymentMethod" in obj:
        payment_method = obj["paymentMethod"]
        payment_method = _deserialize_checkout_payment_method(payment_method)
    else:
        payment_method = None
    if "redirectUrl" in obj:
        redirect_url = obj["redirectUrl"]
        if not isinstance(redirect_url, str):
            raise ValueError(f"{repr(redirect_url)} is not str")
    else:
        redirect_url = None
    if "products" in obj:
        products = obj["products"]
        if not isinstance(products, list):
            raise ValueError(f"{repr(products)} is not list")
        for i, item in enumerate(products):
            item = _deserialize_payment_session_product(item)
            products[i] = item
    else:
        products = None
    if "customerName" in obj:
        customer_name = obj["customerName"]
        if not isinstance(customer_name, str):
            raise ValueError(f"{repr(customer_name)} is not str")
    else:
        customer_name = None
    if "customerEmail" in obj:
        customer_email = obj["customerEmail"]
        if not isinstance(customer_email, str):
            raise ValueError(f"{repr(customer_email)} is not str")
    else:
        customer_email = None
    if "storeName" in obj:
        store_name = obj["storeName"]
        if not isinstance(store_name, str):
            raise ValueError(f"{repr(store_name)} is not str")
    else:
        store_name = None
    if "agreements" in obj:
        agreements = obj["agreements"]
        if not isinstance(agreements, list):
            raise ValueError(f"{repr(agreements)} is not list")
        for i, item in enumerate(agreements):
            item = _deserialize_payment_session_agreement(item)
            agreements[i] = item
    else:
        agreements = None
    if "orderImageUrl" in obj:
        order_image_url = obj["orderImageUrl"]
        if not isinstance(order_image_url, str):
            raise ValueError(f"{repr(order_image_url)} is not str")
    else:
        order_image_url = None
    if "customData" in obj:
        custom_data = obj["customData"]
        if not isinstance(custom_data, str):
            raise ValueError(f"{repr(custom_data)} is not str")
    else:
        custom_data = None
    if "colors" in obj:
        colors = obj["colors"]
        colors = _deserialize_payment_session_colors(colors)
    else:
        colors = None
    return PaymentSession(id, store_id, payment_id, profile_key, country, currency, total_amount, order_name, created_at, expires_at, payment_method, redirect_url, products, customer_name, customer_email, store_name, agreements, order_image_url, custom_data, colors)
