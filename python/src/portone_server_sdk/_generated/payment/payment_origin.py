from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field
from ..payment.payment_origin_platform_type import PaymentOriginPlatformType, _deserialize_payment_origin_platform_type, _serialize_payment_origin_platform_type

@dataclass
class PaymentOrigin:
    """결제 출처 정보
    """
    platform_type: PaymentOriginPlatformType
    """결제를 요청한 플랫폼 타입
    """
    ip_address: str
    """결제를 요청한 IP 주소
    """
    user_agent: Optional[str] = field(default=None)
    """결제를 요청한 user agent 문자열
    """
    url: Optional[str] = field(default=None)
    """결제를 요청한 페이지 URL
    """


def _serialize_payment_origin(obj: PaymentOrigin) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["platformType"] = _serialize_payment_origin_platform_type(obj.platform_type)
    entity["ipAddress"] = obj.ip_address
    if obj.user_agent is not None:
        entity["userAgent"] = obj.user_agent
    if obj.url is not None:
        entity["url"] = obj.url
    return entity


def _deserialize_payment_origin(obj: Any) -> PaymentOrigin:
    if not isinstance(obj, dict):
        raise ValueError("Expected dict for obj")
    if "platformType" not in obj:
        raise KeyError("Missing required field 'platformType'")
    platform_type = obj["platformType"]
    platform_type = _deserialize_payment_origin_platform_type(platform_type)
    if "ipAddress" not in obj:
        raise KeyError("Missing required field 'ipAddress'")
    ip_address = obj["ipAddress"]
    if not isinstance(ip_address, str):
        raise ValueError("Expected str for ip_address")
    if "userAgent" in obj:
        user_agent = obj["userAgent"]
        if not isinstance(user_agent, str):
            raise ValueError("Expected str for user_agent")
    else:
        user_agent = None
    if "url" in obj:
        url = obj["url"]
        if not isinstance(url, str):
            raise ValueError("Expected str for url")
    else:
        url = None
    return PaymentOrigin(platform_type, ip_address, user_agent, url)
