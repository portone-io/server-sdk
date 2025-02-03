from __future__ import annotations
from typing import Any, Optional, Union
from ...common.forbidden_error import ForbiddenError, _deserialize_forbidden_error, _serialize_forbidden_error
from ...common.invalid_request_error import InvalidRequestError, _deserialize_invalid_request_error, _serialize_invalid_request_error
from ...platform.platform_account_verification_already_used_error import PlatformAccountVerificationAlreadyUsedError, _deserialize_platform_account_verification_already_used_error, _serialize_platform_account_verification_already_used_error
from ...platform.platform_account_verification_failed_error import PlatformAccountVerificationFailedError, _deserialize_platform_account_verification_failed_error, _serialize_platform_account_verification_failed_error
from ...platform.platform_account_verification_not_found_error import PlatformAccountVerificationNotFoundError, _deserialize_platform_account_verification_not_found_error, _serialize_platform_account_verification_not_found_error
from ...platform.platform_company_verification_already_used_error import PlatformCompanyVerificationAlreadyUsedError, _deserialize_platform_company_verification_already_used_error, _serialize_platform_company_verification_already_used_error
from ...platform.platform_contract_not_found_error import PlatformContractNotFoundError, _deserialize_platform_contract_not_found_error, _serialize_platform_contract_not_found_error
from ...platform.platform_currency_not_supported_error import PlatformCurrencyNotSupportedError, _deserialize_platform_currency_not_supported_error, _serialize_platform_currency_not_supported_error
from ...platform.platform_not_enabled_error import PlatformNotEnabledError, _deserialize_platform_not_enabled_error, _serialize_platform_not_enabled_error
from ...platform.partner.platform_partner_id_already_exists_error import PlatformPartnerIdAlreadyExistsError, _deserialize_platform_partner_id_already_exists_error, _serialize_platform_partner_id_already_exists_error
from ...platform.platform_user_defined_property_not_found_error import PlatformUserDefinedPropertyNotFoundError, _deserialize_platform_user_defined_property_not_found_error, _serialize_platform_user_defined_property_not_found_error
from ...common.unauthorized_error import UnauthorizedError, _deserialize_unauthorized_error, _serialize_unauthorized_error

CreatePlatformPartnerError = Union[ForbiddenError, InvalidRequestError, PlatformAccountVerificationAlreadyUsedError, PlatformAccountVerificationFailedError, PlatformAccountVerificationNotFoundError, PlatformCompanyVerificationAlreadyUsedError, PlatformContractNotFoundError, PlatformCurrencyNotSupportedError, PlatformNotEnabledError, PlatformPartnerIdAlreadyExistsError, PlatformUserDefinedPropertyNotFoundError, UnauthorizedError, dict]


def _serialize_create_platform_partner_error(obj: CreatePlatformPartnerError) -> Any:
    if isinstance(obj, dict):
        return obj
    if isinstance(obj, ForbiddenError):
        return _serialize_forbidden_error(obj)
    if isinstance(obj, InvalidRequestError):
        return _serialize_invalid_request_error(obj)
    if isinstance(obj, PlatformAccountVerificationAlreadyUsedError):
        return _serialize_platform_account_verification_already_used_error(obj)
    if isinstance(obj, PlatformAccountVerificationFailedError):
        return _serialize_platform_account_verification_failed_error(obj)
    if isinstance(obj, PlatformAccountVerificationNotFoundError):
        return _serialize_platform_account_verification_not_found_error(obj)
    if isinstance(obj, PlatformCompanyVerificationAlreadyUsedError):
        return _serialize_platform_company_verification_already_used_error(obj)
    if isinstance(obj, PlatformContractNotFoundError):
        return _serialize_platform_contract_not_found_error(obj)
    if isinstance(obj, PlatformCurrencyNotSupportedError):
        return _serialize_platform_currency_not_supported_error(obj)
    if isinstance(obj, PlatformNotEnabledError):
        return _serialize_platform_not_enabled_error(obj)
    if isinstance(obj, PlatformPartnerIdAlreadyExistsError):
        return _serialize_platform_partner_id_already_exists_error(obj)
    if isinstance(obj, PlatformUserDefinedPropertyNotFoundError):
        return _serialize_platform_user_defined_property_not_found_error(obj)
    if isinstance(obj, UnauthorizedError):
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
        return _deserialize_platform_company_verification_already_used_error(obj)
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
