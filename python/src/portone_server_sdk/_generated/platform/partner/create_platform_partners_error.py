from __future__ import annotations
from typing import Any, Optional, Union
from ...common.forbidden_error import ForbiddenError, _deserialize_forbidden_error, _serialize_forbidden_error
from ...common.invalid_request_error import InvalidRequestError, _deserialize_invalid_request_error, _serialize_invalid_request_error
from ...platform.partner.platform_contracts_not_found_error import PlatformContractsNotFoundError, _deserialize_platform_contracts_not_found_error, _serialize_platform_contracts_not_found_error
from ...platform.platform_currency_not_supported_error import PlatformCurrencyNotSupportedError, _deserialize_platform_currency_not_supported_error, _serialize_platform_currency_not_supported_error
from ...platform.platform_not_enabled_error import PlatformNotEnabledError, _deserialize_platform_not_enabled_error, _serialize_platform_not_enabled_error
from ...platform.partner.platform_partner_ids_already_exist_error import PlatformPartnerIdsAlreadyExistError, _deserialize_platform_partner_ids_already_exist_error, _serialize_platform_partner_ids_already_exist_error
from ...platform.partner.platform_partner_ids_duplicated_error import PlatformPartnerIdsDuplicatedError, _deserialize_platform_partner_ids_duplicated_error, _serialize_platform_partner_ids_duplicated_error
from ...platform.platform_user_defined_property_not_found_error import PlatformUserDefinedPropertyNotFoundError, _deserialize_platform_user_defined_property_not_found_error, _serialize_platform_user_defined_property_not_found_error
from ...common.unauthorized_error import UnauthorizedError, _deserialize_unauthorized_error, _serialize_unauthorized_error

CreatePlatformPartnersError = Union[ForbiddenError, InvalidRequestError, PlatformContractsNotFoundError, PlatformCurrencyNotSupportedError, PlatformNotEnabledError, PlatformPartnerIdsAlreadyExistError, PlatformPartnerIdsDuplicatedError, PlatformUserDefinedPropertyNotFoundError, UnauthorizedError, dict]


def _serialize_create_platform_partners_error(obj: CreatePlatformPartnersError) -> Any:
    if isinstance(obj, dict):
        return obj
    if isinstance(obj, ForbiddenError):
        return _serialize_forbidden_error(obj)
    if isinstance(obj, InvalidRequestError):
        return _serialize_invalid_request_error(obj)
    if isinstance(obj, PlatformContractsNotFoundError):
        return _serialize_platform_contracts_not_found_error(obj)
    if isinstance(obj, PlatformCurrencyNotSupportedError):
        return _serialize_platform_currency_not_supported_error(obj)
    if isinstance(obj, PlatformNotEnabledError):
        return _serialize_platform_not_enabled_error(obj)
    if isinstance(obj, PlatformPartnerIdsAlreadyExistError):
        return _serialize_platform_partner_ids_already_exist_error(obj)
    if isinstance(obj, PlatformPartnerIdsDuplicatedError):
        return _serialize_platform_partner_ids_duplicated_error(obj)
    if isinstance(obj, PlatformUserDefinedPropertyNotFoundError):
        return _serialize_platform_user_defined_property_not_found_error(obj)
    if isinstance(obj, UnauthorizedError):
        return _serialize_unauthorized_error(obj)


def _deserialize_create_platform_partners_error(obj: Any) -> CreatePlatformPartnersError:
    try:
        return _deserialize_forbidden_error(obj)
    except Exception:
        pass
    try:
        return _deserialize_invalid_request_error(obj)
    except Exception:
        pass
    try:
        return _deserialize_platform_contracts_not_found_error(obj)
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
        return _deserialize_platform_partner_ids_already_exist_error(obj)
    except Exception:
        pass
    try:
        return _deserialize_platform_partner_ids_duplicated_error(obj)
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
    raise ValueError(f"{repr(obj)} is not CreatePlatformPartnersError")
