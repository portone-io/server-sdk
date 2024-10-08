from __future__ import annotations
from typing import Any, Optional, Union
from portone_server_sdk._generated.common.forbidden_error import ForbiddenError, _deserialize_forbidden_error, _serialize_forbidden_error
from portone_server_sdk._generated.common.invalid_request_error import InvalidRequestError, _deserialize_invalid_request_error, _serialize_invalid_request_error
from portone_server_sdk._generated.platform.platform_account_verification_already_used_error import PlatformAccountVerificationAlreadyUsedError, _deserialize_platform_account_verification_already_used_error, _serialize_platform_account_verification_already_used_error
from portone_server_sdk._generated.platform.platform_account_verification_failed_error import PlatformAccountVerificationFailedError, _deserialize_platform_account_verification_failed_error, _serialize_platform_account_verification_failed_error
from portone_server_sdk._generated.platform.platform_account_verification_not_found_error import PlatformAccountVerificationNotFoundError, _deserialize_platform_account_verification_not_found_error, _serialize_platform_account_verification_not_found_error
from portone_server_sdk._generated.platform.platform_contract_not_found_error import PlatformContractNotFoundError, _deserialize_platform_contract_not_found_error, _serialize_platform_contract_not_found_error
from portone_server_sdk._generated.platform.platform_currency_not_supported_error import PlatformCurrencyNotSupportedError, _deserialize_platform_currency_not_supported_error, _serialize_platform_currency_not_supported_error
from portone_server_sdk._generated.platform.platform_not_enabled_error import PlatformNotEnabledError, _deserialize_platform_not_enabled_error, _serialize_platform_not_enabled_error
from portone_server_sdk._generated.platform.partner.platform_partner_id_already_exists_error import PlatformPartnerIdAlreadyExistsError, _deserialize_platform_partner_id_already_exists_error, _serialize_platform_partner_id_already_exists_error
from portone_server_sdk._generated.platform.platform_user_defined_property_not_found_error import PlatformUserDefinedPropertyNotFoundError, _deserialize_platform_user_defined_property_not_found_error, _serialize_platform_user_defined_property_not_found_error
from portone_server_sdk._generated.common.unauthorized_error import UnauthorizedError, _deserialize_unauthorized_error, _serialize_unauthorized_error

CreatePlatformPartnerError = Union[ForbiddenError, InvalidRequestError, PlatformAccountVerificationAlreadyUsedError, PlatformAccountVerificationFailedError, PlatformAccountVerificationNotFoundError, PlatformContractNotFoundError, PlatformCurrencyNotSupportedError, PlatformNotEnabledError, PlatformPartnerIdAlreadyExistsError, PlatformUserDefinedPropertyNotFoundError, UnauthorizedError]


def _serialize_create_platform_partner_error(obj: CreatePlatformPartnerError) -> Any:
    if obj.type == "FORBIDDEN":
        return _serialize_forbidden_error(obj)
    if obj.type == "INVALID_REQUEST":
        return _serialize_invalid_request_error(obj)
    if obj.type == "PLATFORM_ACCOUNT_VERIFICATION_ALREADY_USED":
        return _serialize_platform_account_verification_already_used_error(obj)
    if obj.type == "PLATFORM_ACCOUNT_VERIFICATION_FAILED":
        return _serialize_platform_account_verification_failed_error(obj)
    if obj.type == "PLATFORM_ACCOUNT_VERIFICATION_NOT_FOUND":
        return _serialize_platform_account_verification_not_found_error(obj)
    if obj.type == "PLATFORM_CONTRACT_NOT_FOUND":
        return _serialize_platform_contract_not_found_error(obj)
    if obj.type == "PLATFORM_CURRENCY_NOT_SUPPORTED":
        return _serialize_platform_currency_not_supported_error(obj)
    if obj.type == "PLATFORM_NOT_ENABLED":
        return _serialize_platform_not_enabled_error(obj)
    if obj.type == "PLATFORM_PARTNER_ID_ALREADY_EXISTS":
        return _serialize_platform_partner_id_already_exists_error(obj)
    if obj.type == "PLATFORM_USER_DEFINED_PROPERTY_NOT_FOUND":
        return _serialize_platform_user_defined_property_not_found_error(obj)
    if obj.type == "UNAUTHORIZED":
        return _serialize_unauthorized_error(obj)


def _deserialize_create_platform_partner_error(obj: Any) -> CreatePlatformPartnerError:
    try:
        return _deserialize_forbidden_error(obj)
    except Exception:
        pass
    try:
        return _deserialize_invalid_request_error(obj)
    except Exception:
        pass
    try:
        return _deserialize_platform_account_verification_already_used_error(obj)
    except Exception:
        pass
    try:
        return _deserialize_platform_account_verification_failed_error(obj)
    except Exception:
        pass
    try:
        return _deserialize_platform_account_verification_not_found_error(obj)
    except Exception:
        pass
    try:
        return _deserialize_platform_contract_not_found_error(obj)
    except Exception:
        pass
    try:
        return _deserialize_platform_currency_not_supported_error(obj)
    except Exception:
        pass
    try:
        return _deserialize_platform_not_enabled_error(obj)
    except Exception:
        pass
    try:
        return _deserialize_platform_partner_id_already_exists_error(obj)
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
    raise ValueError(f"{repr(obj)} is not CreatePlatformPartnerError")
