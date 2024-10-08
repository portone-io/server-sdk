from __future__ import annotations
from typing import Any, Optional, Union
from portone_server_sdk._generated.common.forbidden_error import ForbiddenError, _deserialize_forbidden_error, _serialize_forbidden_error
from portone_server_sdk._generated.common.invalid_request_error import InvalidRequestError, _deserialize_invalid_request_error, _serialize_invalid_request_error
from portone_server_sdk._generated.platform.platform_not_enabled_error import PlatformNotEnabledError, _deserialize_platform_not_enabled_error, _serialize_platform_not_enabled_error
from portone_server_sdk._generated.platform.platform_partner_not_found_error import PlatformPartnerNotFoundError, _deserialize_platform_partner_not_found_error, _serialize_platform_partner_not_found_error
from portone_server_sdk._generated.platform.platform_user_defined_property_not_found_error import PlatformUserDefinedPropertyNotFoundError, _deserialize_platform_user_defined_property_not_found_error, _serialize_platform_user_defined_property_not_found_error
from portone_server_sdk._generated.common.unauthorized_error import UnauthorizedError, _deserialize_unauthorized_error, _serialize_unauthorized_error

CreatePlatformManualTransferError = Union[ForbiddenError, InvalidRequestError, PlatformNotEnabledError, PlatformPartnerNotFoundError, PlatformUserDefinedPropertyNotFoundError, UnauthorizedError]


def _serialize_create_platform_manual_transfer_error(obj: CreatePlatformManualTransferError) -> Any:
    if obj.type == "FORBIDDEN":
        return _serialize_forbidden_error(obj)
    if obj.type == "INVALID_REQUEST":
        return _serialize_invalid_request_error(obj)
    if obj.type == "PLATFORM_NOT_ENABLED":
        return _serialize_platform_not_enabled_error(obj)
    if obj.type == "PLATFORM_PARTNER_NOT_FOUND":
        return _serialize_platform_partner_not_found_error(obj)
    if obj.type == "PLATFORM_USER_DEFINED_PROPERTY_NOT_FOUND":
        return _serialize_platform_user_defined_property_not_found_error(obj)
    if obj.type == "UNAUTHORIZED":
        return _serialize_unauthorized_error(obj)


def _deserialize_create_platform_manual_transfer_error(obj: Any) -> CreatePlatformManualTransferError:
    try:
        return _deserialize_forbidden_error(obj)
    except Exception:
        pass
    try:
        return _deserialize_invalid_request_error(obj)
    except Exception:
        pass
    try:
        return _deserialize_platform_not_enabled_error(obj)
    except Exception:
        pass
    try:
        return _deserialize_platform_partner_not_found_error(obj)
    except Exception:
        pass
    try:
        return _deserialize_platform_user_defined_property_not_found_error(obj)
    except Exception:
        pass
    try:
        return _deserialize_unauthorized_error(obj)
    except Exception:
        pass
    raise ValueError(f"{repr(obj)} is not CreatePlatformManualTransferError")
