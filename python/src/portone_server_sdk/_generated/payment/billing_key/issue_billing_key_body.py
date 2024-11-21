from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field
from ...common.customer_input import CustomerInput, _deserialize_customer_input, _serialize_customer_input
from ...payment.billing_key.instant_billing_key_payment_method_input import InstantBillingKeyPaymentMethodInput, _deserialize_instant_billing_key_payment_method_input, _serialize_instant_billing_key_payment_method_input

@dataclass
class IssueBillingKeyBody:
    """빌링키 발급 요청 양식
    """
    method: InstantBillingKeyPaymentMethodInput
    """빌링키 결제 수단 정보
    """
    store_id: Optional[str] = field(default=None)
    """상점 아이디

    접근 권한이 있는 상점 아이디만 입력 가능하며, 미입력시 토큰에 담긴 상점 아이디를 사용합니다.
    """
    channel_key: Optional[str] = field(default=None)
    """채널 키

    채널 키 또는 채널 그룹 ID 필수
    """
    channel_group_id: Optional[str] = field(default=None)
    """채널 그룹 ID

    채널 키 또는 채널 그룹 ID 필수
    """
    customer: Optional[CustomerInput] = field(default=None)
    """고객 정보
    """
    custom_data: Optional[str] = field(default=None)
    """사용자 지정 데이터
    """
    bypass: Optional[dict] = field(default=None)
    """PG사별 추가 파라미터 ("PG사별 연동 가이드" 참고)
    """
    notice_urls: Optional[list[str]] = field(default=None)
    """웹훅 주소

    빌링키 발급 시 요청을 받을 웹훅 주소입니다.
    상점에 설정되어 있는 값보다 우선적으로 적용됩니다.
    입력된 값이 없을 경우에는 빈 배열로 해석됩니다.
    """


def _serialize_issue_billing_key_body(obj: IssueBillingKeyBody) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["method"] = _serialize_instant_billing_key_payment_method_input(obj.method)
    if obj.store_id is not None:
        entity["storeId"] = obj.store_id
    if obj.channel_key is not None:
        entity["channelKey"] = obj.channel_key
    if obj.channel_group_id is not None:
        entity["channelGroupId"] = obj.channel_group_id
    if obj.customer is not None:
        entity["customer"] = _serialize_customer_input(obj.customer)
    if obj.custom_data is not None:
        entity["customData"] = obj.custom_data
    if obj.bypass is not None:
        entity["bypass"] = obj.bypass
    if obj.notice_urls is not None:
        entity["noticeUrls"] = obj.notice_urls
    return entity


def _deserialize_issue_billing_key_body(obj: Any) -> IssueBillingKeyBody:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "method" not in obj:
        raise KeyError(f"'method' is not in {obj}")
    method = obj["method"]
    method = _deserialize_instant_billing_key_payment_method_input(method)
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
    if "bypass" in obj:
        bypass = obj["bypass"]
        if not isinstance(bypass, dict):
            raise ValueError(f"{repr(bypass)} is not dict")
    else:
        bypass = None
    if "noticeUrls" in obj:
        notice_urls = obj["noticeUrls"]
        if not isinstance(notice_urls, list):
            raise ValueError(f"{repr(notice_urls)} is not list")
        for i, item in enumerate(notice_urls):
            if not isinstance(item, str):
                raise ValueError(f"{repr(item)} is not str")
    else:
        notice_urls = None
    return IssueBillingKeyBody(method, store_id, channel_key, channel_group_id, customer, custom_data, bypass, notice_urls)
