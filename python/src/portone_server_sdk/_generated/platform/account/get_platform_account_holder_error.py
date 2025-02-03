from __future__ import annotations
from typing import Any, Optional, Union
from ...common.forbidden_error import ForbiddenError, _deserialize_forbidden_error, _serialize_forbidden_error
from ...common.invalid_request_error import InvalidRequestError, _deserialize_invalid_request_error, _serialize_invalid_request_error
from ...platform.platform_external_api_failed_error import PlatformExternalApiFailedError, _deserialize_platform_external_api_failed_error, _serialize_platform_external_api_failed_error
from ...platform.account.platform_external_api_temporarily_failed_error import PlatformExternalApiTemporarilyFailedError, _deserialize_platform_external_api_temporarily_failed_error, _serialize_platform_external_api_temporarily_failed_error
from ...platform.platform_not_enabled_error import PlatformNotEnabledError, _deserialize_platform_not_enabled_error, _serialize_platform_not_enabled_error
from ...platform.account.platform_not_supported_bank_error import PlatformNotSupportedBankError, _deserialize_platform_not_supported_bank_error, _serialize_platform_not_supported_bank_error
from ...common.unauthorized_error import UnauthorizedError, _deserialize_unauthorized_error, _serialize_unauthorized_error

GetPlatformAccountHolderError = Union[ForbiddenError, InvalidRequestError, PlatformExternalApiFailedError, PlatformExternalApiTemporarilyFailedError, PlatformNotEnabledError, PlatformNotSupportedBankError, UnauthorizedError, dict]


def _serialize_get_platform_account_holder_error(obj: GetPlatformAccountHolderError) -> Any:
    if isinstance(obj, dict):
        return obj
    if isinstance(obj, ForbiddenError):
        return _serialize_forbidden_error(obj)
    if isinstance(obj, InvalidRequestError):
        return _serialize_invalid_request_error(obj)
    if isinstance(obj, PlatformExternalApiFailedError):
        return _serialize_platform_external_api_failed_error(obj)
    if isinstance(obj, PlatformExternalApiTemporarilyFailedError):
        return _serialize_platform_external_api_temporarily_failed_error(obj)
    if isinstance(obj, PlatformNotEnabledError):
        return _serialize_platform_not_enabled_error(obj)
    if isinstance(obj, PlatformNotSupportedBankError):
        return _serialize_platform_not_supported_bank_error(obj)
    if isinstance(obj, UnauthorizedError):
        return _serialize_unauthorized_error(obj)


def _deserialize_get_platform_account_holder_error(obj: Any) -> GetPlatformAccountHolderError:
    try:
        return _deserialize_forbidden_error(obj)
    except Exception:
        pass
    try:
        return _deserialize_invalid_request_error(obj)
    except Exception:
        pass
    try:
        return _deserialize_platform_external_api_failed_error(obj)
    except Exception:
        pass
    try:
        return _deserialize_platform_external_api_temporarily_failed_error(obj)
    except Exception:
        pass
    try:
        return _deserialize_platform_not_enabled_error(obj)
    except Exception:
        pass
    try:
        return _deserialize_platform_not_supported_bank_error(obj)
    except Exception:
        pass
    try:
        return _deserialize_unauthorized_error(obj)
    except Exception:
        pass
    raise ValueError(f"{repr(obj)} is not GetPlatformAccountHolderError")
