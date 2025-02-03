from __future__ import annotations
from typing import Any, Optional, Union
from ...common.forbidden_error import ForbiddenError, _deserialize_forbidden_error, _serialize_forbidden_error
from ...common.invalid_request_error import InvalidRequestError, _deserialize_invalid_request_error, _serialize_invalid_request_error
from ...platform.partner.platform_cannot_archive_scheduled_partner_error import PlatformCannotArchiveScheduledPartnerError, _deserialize_platform_cannot_archive_scheduled_partner_error, _serialize_platform_cannot_archive_scheduled_partner_error
from ...platform.platform_not_enabled_error import PlatformNotEnabledError, _deserialize_platform_not_enabled_error, _serialize_platform_not_enabled_error
from ...platform.platform_partner_not_found_error import PlatformPartnerNotFoundError, _deserialize_platform_partner_not_found_error, _serialize_platform_partner_not_found_error
from ...common.unauthorized_error import UnauthorizedError, _deserialize_unauthorized_error, _serialize_unauthorized_error

ArchivePlatformPartnerError = Union[ForbiddenError, InvalidRequestError, PlatformCannotArchiveScheduledPartnerError, PlatformNotEnabledError, PlatformPartnerNotFoundError, UnauthorizedError, dict]


def _serialize_archive_platform_partner_error(obj: ArchivePlatformPartnerError) -> Any:
    if isinstance(obj, dict):
        return obj
    if isinstance(obj, ForbiddenError):
        return _serialize_forbidden_error(obj)
    if isinstance(obj, InvalidRequestError):
        return _serialize_invalid_request_error(obj)
    if isinstance(obj, PlatformCannotArchiveScheduledPartnerError):
        return _serialize_platform_cannot_archive_scheduled_partner_error(obj)
    if isinstance(obj, PlatformNotEnabledError):
        return _serialize_platform_not_enabled_error(obj)
    if isinstance(obj, PlatformPartnerNotFoundError):
        return _serialize_platform_partner_not_found_error(obj)
    if isinstance(obj, UnauthorizedError):
        return _serialize_unauthorized_error(obj)


def _deserialize_archive_platform_partner_error(obj: Any) -> ArchivePlatformPartnerError:
    try:
        return _deserialize_forbidden_error(obj)
    except Exception:
        pass
    try:
        return _deserialize_invalid_request_error(obj)
    except Exception:
        pass
    try:
        return _deserialize_platform_cannot_archive_scheduled_partner_error(obj)
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
        return _deserialize_unauthorized_error(obj)
    except Exception:
        pass
    raise ValueError(f"{repr(obj)} is not ArchivePlatformPartnerError")
