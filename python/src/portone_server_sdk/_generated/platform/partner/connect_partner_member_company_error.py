from __future__ import annotations
from typing import Any, Optional, Union
from ...common.forbidden_error import ForbiddenError, _deserialize_forbidden_error, _serialize_forbidden_error
from ...common.invalid_request_error import InvalidRequestError, _deserialize_invalid_request_error, _serialize_invalid_request_error
from ...platform.partner.platform_btx_not_enabled_error import PlatformBtxNotEnabledError, _deserialize_platform_btx_not_enabled_error, _serialize_platform_btx_not_enabled_error
from ...platform.platform_external_api_failed_error import PlatformExternalApiFailedError, _deserialize_platform_external_api_failed_error, _serialize_platform_external_api_failed_error
from ...platform.partner.platform_member_company_not_connectable_status_error import PlatformMemberCompanyNotConnectableStatusError, _deserialize_platform_member_company_not_connectable_status_error, _serialize_platform_member_company_not_connectable_status_error
from ...platform.platform_not_enabled_error import PlatformNotEnabledError, _deserialize_platform_not_enabled_error, _serialize_platform_not_enabled_error
from ...platform.platform_partner_not_found_error import PlatformPartnerNotFoundError, _deserialize_platform_partner_not_found_error, _serialize_platform_partner_not_found_error
from ...platform.partner.platform_partner_schedule_exists_error import PlatformPartnerScheduleExistsError, _deserialize_platform_partner_schedule_exists_error, _serialize_platform_partner_schedule_exists_error
from ...platform.partner.platform_partner_taxation_type_is_simple_error import PlatformPartnerTaxationTypeIsSimpleError, _deserialize_platform_partner_taxation_type_is_simple_error, _serialize_platform_partner_taxation_type_is_simple_error
from ...platform.partner.platform_partner_type_is_not_business_error import PlatformPartnerTypeIsNotBusinessError, _deserialize_platform_partner_type_is_not_business_error, _serialize_platform_partner_type_is_not_business_error
from ...common.unauthorized_error import UnauthorizedError, _deserialize_unauthorized_error, _serialize_unauthorized_error

ConnectPartnerMemberCompanyError = Union[ForbiddenError, InvalidRequestError, PlatformBtxNotEnabledError, PlatformExternalApiFailedError, PlatformMemberCompanyNotConnectableStatusError, PlatformNotEnabledError, PlatformPartnerNotFoundError, PlatformPartnerScheduleExistsError, PlatformPartnerTaxationTypeIsSimpleError, PlatformPartnerTypeIsNotBusinessError, UnauthorizedError, dict]


def _serialize_connect_partner_member_company_error(obj: ConnectPartnerMemberCompanyError) -> Any:
    if isinstance(obj, dict):
        return obj
    if isinstance(obj, ForbiddenError):
        return _serialize_forbidden_error(obj)
    if isinstance(obj, InvalidRequestError):
        return _serialize_invalid_request_error(obj)
    if isinstance(obj, PlatformBtxNotEnabledError):
        return _serialize_platform_btx_not_enabled_error(obj)
    if isinstance(obj, PlatformExternalApiFailedError):
        return _serialize_platform_external_api_failed_error(obj)
    if isinstance(obj, PlatformMemberCompanyNotConnectableStatusError):
        return _serialize_platform_member_company_not_connectable_status_error(obj)
    if isinstance(obj, PlatformNotEnabledError):
        return _serialize_platform_not_enabled_error(obj)
    if isinstance(obj, PlatformPartnerNotFoundError):
        return _serialize_platform_partner_not_found_error(obj)
    if isinstance(obj, PlatformPartnerScheduleExistsError):
        return _serialize_platform_partner_schedule_exists_error(obj)
    if isinstance(obj, PlatformPartnerTaxationTypeIsSimpleError):
        return _serialize_platform_partner_taxation_type_is_simple_error(obj)
    if isinstance(obj, PlatformPartnerTypeIsNotBusinessError):
        return _serialize_platform_partner_type_is_not_business_error(obj)
    if isinstance(obj, UnauthorizedError):
        return _serialize_unauthorized_error(obj)


def _deserialize_connect_partner_member_company_error(obj: Any) -> ConnectPartnerMemberCompanyError:
    try:
        return _deserialize_forbidden_error(obj)
    except Exception:
        pass
    try:
        return _deserialize_invalid_request_error(obj)
    except Exception:
        pass
    try:
        return _deserialize_platform_btx_not_enabled_error(obj)
    except Exception:
        pass
    try:
        return _deserialize_platform_external_api_failed_error(obj)
    except Exception:
        pass
    try:
        return _deserialize_platform_member_company_not_connectable_status_error(obj)
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
        return _deserialize_platform_partner_schedule_exists_error(obj)
    except Exception:
        pass
    try:
        return _deserialize_platform_partner_taxation_type_is_simple_error(obj)
    except Exception:
        pass
    try:
        return _deserialize_platform_partner_type_is_not_business_error(obj)
    except Exception:
        pass
    try:
        return _deserialize_unauthorized_error(obj)
    except Exception:
        pass
    raise ValueError(f"{repr(obj)} is not ConnectPartnerMemberCompanyError")
