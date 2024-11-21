from __future__ import annotations
from typing import Any, Optional, Union
from ..common.forbidden_error import ForbiddenError, _deserialize_forbidden_error, _serialize_forbidden_error
from ..common.invalid_request_error import InvalidRequestError, _deserialize_invalid_request_error, _serialize_invalid_request_error
from ..platform.platform_archived_contract_error import PlatformArchivedContractError, _deserialize_platform_archived_contract_error, _serialize_platform_archived_contract_error
from ..platform.platform_contract_not_found_error import PlatformContractNotFoundError, _deserialize_platform_contract_not_found_error, _serialize_platform_contract_not_found_error
from ..platform.platform_contract_schedule_already_exists_error import PlatformContractScheduleAlreadyExistsError, _deserialize_platform_contract_schedule_already_exists_error, _serialize_platform_contract_schedule_already_exists_error
from ..platform.platform_not_enabled_error import PlatformNotEnabledError, _deserialize_platform_not_enabled_error, _serialize_platform_not_enabled_error
from ..common.unauthorized_error import UnauthorizedError, _deserialize_unauthorized_error, _serialize_unauthorized_error

ScheduleContractError = Union[ForbiddenError, InvalidRequestError, PlatformArchivedContractError, PlatformContractNotFoundError, PlatformContractScheduleAlreadyExistsError, PlatformNotEnabledError, UnauthorizedError, dict]


def _serialize_schedule_contract_error(obj: ScheduleContractError) -> Any:
    if isinstance(obj, dict):
        return obj
    if isinstance(obj, ForbiddenError):
        return _serialize_forbidden_error(obj)
    if isinstance(obj, InvalidRequestError):
        return _serialize_invalid_request_error(obj)
    if isinstance(obj, PlatformArchivedContractError):
        return _serialize_platform_archived_contract_error(obj)
    if isinstance(obj, PlatformContractNotFoundError):
        return _serialize_platform_contract_not_found_error(obj)
    if isinstance(obj, PlatformContractScheduleAlreadyExistsError):
        return _serialize_platform_contract_schedule_already_exists_error(obj)
    if isinstance(obj, PlatformNotEnabledError):
        return _serialize_platform_not_enabled_error(obj)
    if isinstance(obj, UnauthorizedError):
        return _serialize_unauthorized_error(obj)


def _deserialize_schedule_contract_error(obj: Any) -> ScheduleContractError:
    try:
        return _deserialize_forbidden_error(obj)
    except Exception:
        pass
    try:
        return _deserialize_invalid_request_error(obj)
    except Exception:
        pass
    try:
        return _deserialize_platform_archived_contract_error(obj)
    except Exception:
        pass
    try:
        return _deserialize_platform_contract_not_found_error(obj)
    except Exception:
        pass
    try:
        return _deserialize_platform_contract_schedule_already_exists_error(obj)
    except Exception:
        pass
    try:
        return _deserialize_platform_not_enabled_error(obj)
    except Exception:
        pass
    try:
        return _deserialize_unauthorized_error(obj)
    except Exception:
        pass
    return obj
