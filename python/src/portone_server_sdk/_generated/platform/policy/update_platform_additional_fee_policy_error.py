from __future__ import annotations
from typing import Any, Optional, Union
from ...common.forbidden_error import ForbiddenError, _deserialize_forbidden_error, _serialize_forbidden_error
from ...common.invalid_request_error import InvalidRequestError, _deserialize_invalid_request_error, _serialize_invalid_request_error
from ...platform.platform_additional_fee_policy_not_found_error import PlatformAdditionalFeePolicyNotFoundError, _deserialize_platform_additional_fee_policy_not_found_error, _serialize_platform_additional_fee_policy_not_found_error
from ...platform.platform_archived_additional_fee_policy_error import PlatformArchivedAdditionalFeePolicyError, _deserialize_platform_archived_additional_fee_policy_error, _serialize_platform_archived_additional_fee_policy_error
from ...platform.platform_not_enabled_error import PlatformNotEnabledError, _deserialize_platform_not_enabled_error, _serialize_platform_not_enabled_error
from ...common.unauthorized_error import UnauthorizedError, _deserialize_unauthorized_error, _serialize_unauthorized_error

UpdatePlatformAdditionalFeePolicyError = Union[ForbiddenError, InvalidRequestError, PlatformAdditionalFeePolicyNotFoundError, PlatformArchivedAdditionalFeePolicyError, PlatformNotEnabledError, UnauthorizedError, dict]


def _serialize_update_platform_additional_fee_policy_error(obj: UpdatePlatformAdditionalFeePolicyError) -> Any:
    if isinstance(obj, dict):
        return obj
    if isinstance(obj, ForbiddenError):
        return _serialize_forbidden_error(obj)
    if isinstance(obj, InvalidRequestError):
        return _serialize_invalid_request_error(obj)
    if isinstance(obj, PlatformAdditionalFeePolicyNotFoundError):
        return _serialize_platform_additional_fee_policy_not_found_error(obj)
    if isinstance(obj, PlatformArchivedAdditionalFeePolicyError):
        return _serialize_platform_archived_additional_fee_policy_error(obj)
    if isinstance(obj, PlatformNotEnabledError):
        return _serialize_platform_not_enabled_error(obj)
    if isinstance(obj, UnauthorizedError):
        return _serialize_unauthorized_error(obj)


def _deserialize_update_platform_additional_fee_policy_error(obj: Any) -> UpdatePlatformAdditionalFeePolicyError:
    try:
        return _deserialize_forbidden_error(obj)
    except Exception:
        pass
    try:
        return _deserialize_invalid_request_error(obj)
    except Exception:
        pass
    try:
        return _deserialize_platform_additional_fee_policy_not_found_error(obj)
    except Exception:
        pass
    try:
        return _deserialize_platform_archived_additional_fee_policy_error(obj)
    except Exception:
        pass
    try:
        return _deserialize_platform_not_enabled_error(obj)
    except Exception:
        pass
    try:
        return _deserialize_unauthorized_error(obj)
    except Exception:
        pass
    raise ValueError(f"{repr(obj)} is not UpdatePlatformAdditionalFeePolicyError")
