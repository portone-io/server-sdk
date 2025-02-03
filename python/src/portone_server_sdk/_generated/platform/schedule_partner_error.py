from __future__ import annotations
from typing import Any, Optional, Union
from ..common.forbidden_error import ForbiddenError, _deserialize_forbidden_error, _serialize_forbidden_error
from ..common.invalid_request_error import InvalidRequestError, _deserialize_invalid_request_error, _serialize_invalid_request_error
from ..platform.platform_account_verification_already_used_error import PlatformAccountVerificationAlreadyUsedError, _deserialize_platform_account_verification_already_used_error, _serialize_platform_account_verification_already_used_error
from ..platform.platform_account_verification_failed_error import PlatformAccountVerificationFailedError, _deserialize_platform_account_verification_failed_error, _serialize_platform_account_verification_failed_error
from ..platform.platform_account_verification_not_found_error import PlatformAccountVerificationNotFoundError, _deserialize_platform_account_verification_not_found_error, _serialize_platform_account_verification_not_found_error
from ..platform.platform_archived_partner_error import PlatformArchivedPartnerError, _deserialize_platform_archived_partner_error, _serialize_platform_archived_partner_error
from ..platform.platform_company_verification_already_used_error import PlatformCompanyVerificationAlreadyUsedError, _deserialize_platform_company_verification_already_used_error, _serialize_platform_company_verification_already_used_error
from ..platform.platform_contract_not_found_error import PlatformContractNotFoundError, _deserialize_platform_contract_not_found_error, _serialize_platform_contract_not_found_error
from ..platform.platform_insufficient_data_to_change_partner_type_error import PlatformInsufficientDataToChangePartnerTypeError, _deserialize_platform_insufficient_data_to_change_partner_type_error, _serialize_platform_insufficient_data_to_change_partner_type_error
from ..platform.platform_member_company_connected_partner_brn_unchangeable_error import PlatformMemberCompanyConnectedPartnerBrnUnchangeableError, _deserialize_platform_member_company_connected_partner_brn_unchangeable_error, _serialize_platform_member_company_connected_partner_brn_unchangeable_error
from ..platform.platform_member_company_connected_partner_cannot_be_scheduled_error import PlatformMemberCompanyConnectedPartnerCannotBeScheduledError, _deserialize_platform_member_company_connected_partner_cannot_be_scheduled_error, _serialize_platform_member_company_connected_partner_cannot_be_scheduled_error
from ..platform.platform_member_company_connected_partner_type_unchangeable_error import PlatformMemberCompanyConnectedPartnerTypeUnchangeableError, _deserialize_platform_member_company_connected_partner_type_unchangeable_error, _serialize_platform_member_company_connected_partner_type_unchangeable_error
from ..platform.platform_not_enabled_error import PlatformNotEnabledError, _deserialize_platform_not_enabled_error, _serialize_platform_not_enabled_error
from ..platform.platform_partner_not_found_error import PlatformPartnerNotFoundError, _deserialize_platform_partner_not_found_error, _serialize_platform_partner_not_found_error
from ..platform.platform_partner_schedule_already_exists_error import PlatformPartnerScheduleAlreadyExistsError, _deserialize_platform_partner_schedule_already_exists_error, _serialize_platform_partner_schedule_already_exists_error
from ..platform.platform_user_defined_property_not_found_error import PlatformUserDefinedPropertyNotFoundError, _deserialize_platform_user_defined_property_not_found_error, _serialize_platform_user_defined_property_not_found_error
from ..common.unauthorized_error import UnauthorizedError, _deserialize_unauthorized_error, _serialize_unauthorized_error

SchedulePartnerError = Union[ForbiddenError, InvalidRequestError, PlatformAccountVerificationAlreadyUsedError, PlatformAccountVerificationFailedError, PlatformAccountVerificationNotFoundError, PlatformArchivedPartnerError, PlatformCompanyVerificationAlreadyUsedError, PlatformContractNotFoundError, PlatformInsufficientDataToChangePartnerTypeError, PlatformMemberCompanyConnectedPartnerBrnUnchangeableError, PlatformMemberCompanyConnectedPartnerCannotBeScheduledError, PlatformMemberCompanyConnectedPartnerTypeUnchangeableError, PlatformNotEnabledError, PlatformPartnerNotFoundError, PlatformPartnerScheduleAlreadyExistsError, PlatformUserDefinedPropertyNotFoundError, UnauthorizedError, dict]


def _serialize_schedule_partner_error(obj: SchedulePartnerError) -> Any:
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
    if isinstance(obj, PlatformArchivedPartnerError):
        return _serialize_platform_archived_partner_error(obj)
    if isinstance(obj, PlatformCompanyVerificationAlreadyUsedError):
        return _serialize_platform_company_verification_already_used_error(obj)
    if isinstance(obj, PlatformContractNotFoundError):
        return _serialize_platform_contract_not_found_error(obj)
    if isinstance(obj, PlatformInsufficientDataToChangePartnerTypeError):
        return _serialize_platform_insufficient_data_to_change_partner_type_error(obj)
    if isinstance(obj, PlatformMemberCompanyConnectedPartnerBrnUnchangeableError):
        return _serialize_platform_member_company_connected_partner_brn_unchangeable_error(obj)
    if isinstance(obj, PlatformMemberCompanyConnectedPartnerCannotBeScheduledError):
        return _serialize_platform_member_company_connected_partner_cannot_be_scheduled_error(obj)
    if isinstance(obj, PlatformMemberCompanyConnectedPartnerTypeUnchangeableError):
        return _serialize_platform_member_company_connected_partner_type_unchangeable_error(obj)
    if isinstance(obj, PlatformNotEnabledError):
        return _serialize_platform_not_enabled_error(obj)
    if isinstance(obj, PlatformPartnerNotFoundError):
        return _serialize_platform_partner_not_found_error(obj)
    if isinstance(obj, PlatformPartnerScheduleAlreadyExistsError):
        return _serialize_platform_partner_schedule_already_exists_error(obj)
    if isinstance(obj, PlatformUserDefinedPropertyNotFoundError):
        return _serialize_platform_user_defined_property_not_found_error(obj)
    if isinstance(obj, UnauthorizedError):
        return _serialize_unauthorized_error(obj)


def _deserialize_schedule_partner_error(obj: Any) -> SchedulePartnerError:
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
        return _deserialize_platform_archived_partner_error(obj)
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
        return _deserialize_platform_insufficient_data_to_change_partner_type_error(obj)
    except Exception:
        pass
    try:
        return _deserialize_platform_member_company_connected_partner_brn_unchangeable_error(obj)
    except Exception:
        pass
    try:
        return _deserialize_platform_member_company_connected_partner_cannot_be_scheduled_error(obj)
    except Exception:
        pass
    try:
        return _deserialize_platform_member_company_connected_partner_type_unchangeable_error(obj)
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
        return _deserialize_platform_partner_schedule_already_exists_error(obj)
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
    raise ValueError(f"{repr(obj)} is not SchedulePartnerError")
