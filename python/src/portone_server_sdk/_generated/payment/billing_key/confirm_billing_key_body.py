from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class ConfirmBillingKeyBody:
    """빌링키 발급 승인 입력 정보
    """
    billing_issue_token: str
    """빌링키 발급 토큰

    빌링키 발급 요청 완료 시 발급된 토큰입니다.
    """
    store_id: Optional[str] = field(default=None)
    """상점 아이디

    접근 권한이 있는 상점 아이디만 입력 가능하며, 미입력시 인증 정보의 상점 아이디를 사용합니다.
    """
    is_test: Optional[bool] = field(default=None)
    """테스트 결제 여부

    검증용 파라미터로, 결제 건 테스트 여부와 일치하지 않을 경우 오류가 반환됩니다.
    """


def _serialize_confirm_billing_key_body(obj: ConfirmBillingKeyBody) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["billingIssueToken"] = obj.billing_issue_token
    if obj.store_id is not None:
        entity["storeId"] = obj.store_id
    if obj.is_test is not None:
        entity["isTest"] = obj.is_test
    return entity


def _deserialize_confirm_billing_key_body(obj: Any) -> ConfirmBillingKeyBody:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "billingIssueToken" not in obj:
        raise KeyError(f"'billingIssueToken' is not in {obj}")
    billing_issue_token = obj["billingIssueToken"]
    if not isinstance(billing_issue_token, str):
        raise ValueError(f"{repr(billing_issue_token)} is not str")
    if "storeId" in obj:
        store_id = obj["storeId"]
        if not isinstance(store_id, str):
            raise ValueError(f"{repr(store_id)} is not str")
    else:
        store_id = None
    if "isTest" in obj:
        is_test = obj["isTest"]
        if not isinstance(is_test, bool):
            raise ValueError(f"{repr(is_test)} is not bool")
    else:
        is_test = None
    return ConfirmBillingKeyBody(billing_issue_token, store_id, is_test)
