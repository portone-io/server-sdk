from __future__ import annotations
from typing import Any, Optional, Union
from portone_server_sdk._generated.common.forbidden_error import ForbiddenError, _deserialize_forbidden_error, _serialize_forbidden_error
from portone_server_sdk._generated.common.unauthorized_error import UnauthorizedError, _deserialize_unauthorized_error, _serialize_unauthorized_error

GetAnalyticsOverseasPaymentUsageError = Union[ForbiddenError, UnauthorizedError]


def _serialize_get_analytics_overseas_payment_usage_error(obj: GetAnalyticsOverseasPaymentUsageError) -> Any:
    if obj.type == "FORBIDDEN":
        return _serialize_forbidden_error(obj)
    if obj.type == "UNAUTHORIZED":
        return _serialize_unauthorized_error(obj)


def _deserialize_get_analytics_overseas_payment_usage_error(obj: Any) -> GetAnalyticsOverseasPaymentUsageError:
    try:
        return _deserialize_forbidden_error(obj)
    except Exception:
        pass
    try:
        return _deserialize_unauthorized_error(obj)
    except Exception:
        pass
    raise ValueError(f"{repr(obj)} is not GetAnalyticsOverseasPaymentUsageError")
