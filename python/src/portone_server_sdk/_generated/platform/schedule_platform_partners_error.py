from __future__ import annotations
from typing import Any, Optional, Union
from portone_server_sdk._generated.common.forbidden_error import ForbiddenError, _deserialize_forbidden_error, _serialize_forbidden_error
from portone_server_sdk._generated.common.invalid_request_error import InvalidRequestError, _deserialize_invalid_request_error, _serialize_invalid_request_error
from portone_server_sdk._generated.platform.platform_archived_partners_cannot_be_scheduled_error import PlatformArchivedPartnersCannotBeScheduledError, _deserialize_platform_archived_partners_cannot_be_scheduled_error, _serialize_platform_archived_partners_cannot_be_scheduled_error
from portone_server_sdk._generated.platform.platform_contract_not_found_error import PlatformContractNotFoundError, _deserialize_platform_contract_not_found_error, _serialize_platform_contract_not_found_error
from portone_server_sdk._generated.platform.platform_not_enabled_error import PlatformNotEnabledError, _deserialize_platform_not_enabled_error, _serialize_platform_not_enabled_error
from portone_server_sdk._generated.platform.platform_partner_schedules_already_exist_error import PlatformPartnerSchedulesAlreadyExistError, _deserialize_platform_partner_schedules_already_exist_error, _serialize_platform_partner_schedules_already_exist_error
from portone_server_sdk._generated.platform.platform_user_defined_property_not_found_error import PlatformUserDefinedPropertyNotFoundError, _deserialize_platform_user_defined_property_not_found_error, _serialize_platform_user_defined_property_not_found_error
from portone_server_sdk._generated.common.unauthorized_error import UnauthorizedError, _deserialize_unauthorized_error, _serialize_unauthorized_error

SchedulePlatformPartnersError = Union[ForbiddenError, InvalidRequestError, PlatformArchivedPartnersCannotBeScheduledError, PlatformContractNotFoundError, PlatformNotEnabledError, PlatformPartnerSchedulesAlreadyExistError, PlatformUserDefinedPropertyNotFoundError, UnauthorizedError]


def _serialize_schedule_platform_partners_error(obj: SchedulePlatformPartnersError) -> Any:
    if obj.type == "FORBIDDEN":
        return _serialize_forbidden_error(obj)
    if obj.type == "INVALID_REQUEST":
        return _serialize_invalid_request_error(obj)
    if obj.type == "PLATFORM_ARCHIVED_PARTNERS_CANNOT_BE_SCHEDULED":
        return _serialize_platform_archived_partners_cannot_be_scheduled_error(obj)
    if obj.type == "PLATFORM_CONTRACT_NOT_FOUND":
        return _serialize_platform_contract_not_found_error(obj)
    if obj.type == "PLATFORM_NOT_ENABLED":
        return _serialize_platform_not_enabled_error(obj)
    if obj.type == "PLATFORM_PARTNER_SCHEDULES_ALREADY_EXIST":
        return _serialize_platform_partner_schedules_already_exist_error(obj)
    if obj.type == "PLATFORM_USER_DEFINED_PROPERTY_NOT_FOUND":
        return _serialize_platform_user_defined_property_not_found_error(obj)
    if obj.type == "UNAUTHORIZED":
        return _serialize_unauthorized_error(obj)


def _deserialize_schedule_platform_partners_error(obj: Any) -> SchedulePlatformPartnersError:
    try:
        return _deserialize_forbidden_error(obj)
    except Exception:
        pass
    try:
        return _deserialize_invalid_request_error(obj)
    except Exception:
        pass
    try:
        return _deserialize_platform_archived_partners_cannot_be_scheduled_error(obj)
    except Exception:
        pass
    try:
        return _deserialize_platform_contract_not_found_error(obj)
    except Exception:
        pass
    try:
        return _deserialize_platform_not_enabled_error(obj)
    except Exception:
        pass
    try:
        return _deserialize_platform_partner_schedules_already_exist_error(obj)
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
    raise ValueError(f"{repr(obj)} is not SchedulePlatformPartnersError")
