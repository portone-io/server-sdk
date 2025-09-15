from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field
from ...common.currency import Currency, _deserialize_currency, _serialize_currency

@dataclass
class ConfirmBillingKeyIssueAndPayBody:
    """빌링키 발급 및 초회 결제 승인 입력 정보
    """
    billing_issue_token: str
    """빌링키 발급 토큰

    빌링키 발급 및 초회 결제 요청 완료 시 발급된 토큰입니다.
    """
    store_id: Optional[str] = field(default=None)
    """상점 아이디

    접근 권한이 있는 상점 아이디만 입력 가능하며, 미입력시 인증 정보의 상점 아이디를 사용합니다.
    """
    payment_id: Optional[str] = field(default=None)
    """결제 건 아이디

    검증용 파라미터로, 결제 건 아이디와 일치하지 않을 경우 오류가 반환됩니다.
    """
    currency: Optional[Currency] = field(default=None)
    """통화

    검증용 파라미터로, 결제 건 화폐와 일치하지 않을 경우 오류가 반환됩니다.
    """
    total_amount: Optional[int] = field(default=None)
    """결제 금액

    검증용 파라미터로, 결제 건 총 금액과 일치하지 않을 경우 오류가 반환됩니다.
    (int64)
    """
    tax_free_amount: Optional[int] = field(default=None)
    """면세 금액

    검증용 파라미터로, 결제 건 면세 금액과 일치하지 않을 경우 오류가 반환됩니다.
    (int64)
    """
    is_test: Optional[bool] = field(default=None)
    """테스트 결제 여부

    검증용 파라미터로, 결제 건 테스트 여부와 일치하지 않을 경우 오류가 반환됩니다.
    """


def _serialize_confirm_billing_key_issue_and_pay_body(obj: ConfirmBillingKeyIssueAndPayBody) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["billingIssueToken"] = obj.billing_issue_token
    if obj.store_id is not None:
        entity["storeId"] = obj.store_id
    if obj.payment_id is not None:
        entity["paymentId"] = obj.payment_id
    if obj.currency is not None:
        entity["currency"] = _serialize_currency(obj.currency)
    if obj.total_amount is not None:
        entity["totalAmount"] = obj.total_amount
    if obj.tax_free_amount is not None:
        entity["taxFreeAmount"] = obj.tax_free_amount
    if obj.is_test is not None:
        entity["isTest"] = obj.is_test
    return entity


def _deserialize_confirm_billing_key_issue_and_pay_body(obj: Any) -> ConfirmBillingKeyIssueAndPayBody:
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
    if "paymentId" in obj:
        payment_id = obj["paymentId"]
        if not isinstance(payment_id, str):
            raise ValueError(f"{repr(payment_id)} is not str")
    else:
        payment_id = None
    if "currency" in obj:
        currency = obj["currency"]
        currency = _deserialize_currency(currency)
    else:
        currency = None
    if "totalAmount" in obj:
        total_amount = obj["totalAmount"]
        if not isinstance(total_amount, int):
            raise ValueError(f"{repr(total_amount)} is not int")
    else:
        total_amount = None
    if "taxFreeAmount" in obj:
        tax_free_amount = obj["taxFreeAmount"]
        if not isinstance(tax_free_amount, int):
            raise ValueError(f"{repr(tax_free_amount)} is not int")
    else:
        tax_free_amount = None
    if "isTest" in obj:
        is_test = obj["isTest"]
        if not isinstance(is_test, bool):
            raise ValueError(f"{repr(is_test)} is not bool")
    else:
        is_test = None
    return ConfirmBillingKeyIssueAndPayBody(billing_issue_token, store_id, payment_id, currency, total_amount, tax_free_amount, is_test)
