from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field
from ..identity_verification.identity_verification_method import IdentityVerificationMethod, _deserialize_identity_verification_method, _serialize_identity_verification_method
from ..identity_verification.identity_verification_operator import IdentityVerificationOperator, _deserialize_identity_verification_operator, _serialize_identity_verification_operator
from ..identity_verification.send_identity_verification_body_customer import SendIdentityVerificationBodyCustomer, _deserialize_send_identity_verification_body_customer, _serialize_send_identity_verification_body_customer

@dataclass
class SendIdentityVerificationBody:
    """본인인증 요청을 위한 입력 정보
    """
    channel_key: str
    """채널 키
    """
    customer: SendIdentityVerificationBodyCustomer
    """고객 정보
    """
    operator: IdentityVerificationOperator
    """통신사
    """
    method: IdentityVerificationMethod
    """본인인증 방식
    """
    store_id: Optional[str] = field(default=None)
    """상점 아이디

    접근 권한이 있는 상점 아이디만 입력 가능하며, 미입력시 토큰에 담긴 상점 아이디를 사용합니다.
    """
    custom_data: Optional[str] = field(default=None)
    """사용자 지정 데이터
    """
    bypass: Optional[dict] = field(default=None)
    """PG사별 추가 파라미터 ("PG사별 연동 가이드" 참고)
    """


def _serialize_send_identity_verification_body(obj: SendIdentityVerificationBody) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["channelKey"] = obj.channel_key
    entity["customer"] = _serialize_send_identity_verification_body_customer(obj.customer)
    entity["operator"] = _serialize_identity_verification_operator(obj.operator)
    entity["method"] = _serialize_identity_verification_method(obj.method)
    if obj.store_id is not None:
        entity["storeId"] = obj.store_id
    if obj.custom_data is not None:
        entity["customData"] = obj.custom_data
    if obj.bypass is not None:
        entity["bypass"] = obj.bypass
    return entity


def _deserialize_send_identity_verification_body(obj: Any) -> SendIdentityVerificationBody:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "channelKey" not in obj:
        raise KeyError(f"'channelKey' is not in {obj}")
    channel_key = obj["channelKey"]
    if not isinstance(channel_key, str):
        raise ValueError(f"{repr(channel_key)} is not str")
    if "customer" not in obj:
        raise KeyError(f"'customer' is not in {obj}")
    customer = obj["customer"]
    customer = _deserialize_send_identity_verification_body_customer(customer)
    if "operator" not in obj:
        raise KeyError(f"'operator' is not in {obj}")
    operator = obj["operator"]
    operator = _deserialize_identity_verification_operator(operator)
    if "method" not in obj:
        raise KeyError(f"'method' is not in {obj}")
    method = obj["method"]
    method = _deserialize_identity_verification_method(method)
    if "storeId" in obj:
        store_id = obj["storeId"]
        if not isinstance(store_id, str):
            raise ValueError(f"{repr(store_id)} is not str")
    else:
        store_id = None
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
    return SendIdentityVerificationBody(channel_key, customer, operator, method, store_id, custom_data, bypass)
