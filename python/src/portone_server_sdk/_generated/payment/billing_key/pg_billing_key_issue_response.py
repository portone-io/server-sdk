from __future__ import annotations
from typing import Any, Optional, Union
from ...payment.billing_key.failed_pg_billing_key_issue_response import FailedPgBillingKeyIssueResponse, _deserialize_failed_pg_billing_key_issue_response, _serialize_failed_pg_billing_key_issue_response
from ...payment.billing_key.issued_pg_billing_key_issue_response import IssuedPgBillingKeyIssueResponse, _deserialize_issued_pg_billing_key_issue_response, _serialize_issued_pg_billing_key_issue_response

PgBillingKeyIssueResponse = Union[FailedPgBillingKeyIssueResponse, IssuedPgBillingKeyIssueResponse, dict]
"""채널 별 빌링키 발급 응답
"""


def _serialize_pg_billing_key_issue_response(obj: PgBillingKeyIssueResponse) -> Any:
    if isinstance(obj, dict):
        return obj
    if isinstance(obj, FailedPgBillingKeyIssueResponse):
        return _serialize_failed_pg_billing_key_issue_response(obj)
    if isinstance(obj, IssuedPgBillingKeyIssueResponse):
        return _serialize_issued_pg_billing_key_issue_response(obj)


def _deserialize_pg_billing_key_issue_response(obj: Any) -> PgBillingKeyIssueResponse:
    try:
        return _deserialize_failed_pg_billing_key_issue_response(obj)
    except Exception:
        pass
    try:
        return _deserialize_issued_pg_billing_key_issue_response(obj)
    except Exception:
        pass
    raise ValueError(f"{repr(obj)} is not PgBillingKeyIssueResponse")
