from __future__ import annotations
from typing import Any, Optional, Union
from ..common.forbidden_error import ForbiddenError, _deserialize_forbidden_error, _serialize_forbidden_error
from ..common.invalid_request_error import InvalidRequestError, _deserialize_invalid_request_error, _serialize_invalid_request_error
from ..platform.platform_archived_partners_cannot_be_scheduled_error import PlatformArchivedPartnersCannotBeScheduledError, _deserialize_platform_archived_partners_cannot_be_scheduled_error, _serialize_platform_archived_partners_cannot_be_scheduled_error
from ..platform.platform_contract_not_found_error import PlatformContractNotFoundError, _deserialize_platform_contract_not_found_error, _serialize_platform_contract_not_found_error
from ..platform.platform_member_company_connected_partners_cannot_be_scheduled_error import PlatformMemberCompanyConnectedPartnersCannotBeScheduledError, _deserialize_platform_member_company_connected_partners_cannot_be_scheduled_error, _serialize_platform_member_company_connected_partners_cannot_be_scheduled_error
from ..platform.platform_not_enabled_error import PlatformNotEnabledError, _deserialize_platform_not_enabled_error, _serialize_platform_not_enabled_error
from ..platform.platform_partner_schedules_already_exist_error import PlatformPartnerSchedulesAlreadyExistError, _deserialize_platform_partner_schedules_already_exist_error, _serialize_platform_partner_schedules_already_exist_error
from ..platform.platform_user_defined_property_not_found_error import PlatformUserDefinedPropertyNotFoundError, _deserialize_platform_user_defined_property_not_found_error, _serialize_platform_user_defined_property_not_found_error
from ..common.unauthorized_error import UnauthorizedError, _deserialize_unauthorized_error, _serialize_unauthorized_error

SchedulePlatformPartnersError = Union[ForbiddenError, InvalidRequestError, PlatformArchivedPartnersCannotBeScheduledError, PlatformContractNotFoundError, PlatformMemberCompanyConnectedPartnersCannotBeScheduledError, PlatformNotEnabledError, PlatformPartnerSchedulesAlreadyExistError, PlatformUserDefinedPropertyNotFoundError, UnauthorizedError, dict]


def _serialize_schedule_platform_partners_error(obj: SchedulePlatformPartnersError) -> Any:
    if isinstance(obj, dict):
        return obj
    if isinstance(obj, ForbiddenError):
        return _serialize_forbidden_error(obj)
    if isinstance(obj, InvalidRequestError):
        return _serialize_invalid_request_error(obj)
    if isinstance(obj, PlatformArchivedPartnersCannotBeScheduledError):
        return _serialize_platform_archived_partners_cannot_be_scheduled_error(obj)
    if isinstance(obj, PlatformContractNotFoundError):
        return _serialize_platform_contract_not_found_error(obj)
    if isinstance(obj, PlatformMemberCompanyConnectedPartnersCannotBeScheduledError):
        return _serialize_platform_member_company_connected_partners_cannot_be_scheduled_error(obj)
    if isinstance(obj, PlatformNotEnabledError):
        return _serialize_platform_not_enabled_error(obj)
    if isinstance(obj, PlatformPartnerSchedulesAlreadyExistError):
        return _serialize_platform_partner_schedules_already_exist_error(obj)
    if isinstance(obj, PlatformUserDefinedPropertyNotFoundError):
        return _serialize_platform_user_defined_property_not_found_error(obj)
    if isinstance(obj, UnauthorizedError):
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
        return _deserialize_platform_member_company_connected_partners_cannot_be_scheduled_error(obj)
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
