from __future__ import annotations
from typing import Any, Optional, Union
from portone_server_sdk._generated.common.forbidden_error import ForbiddenError, _deserialize_forbidden_error, _serialize_forbidden_error
from portone_server_sdk._generated.common.invalid_request_error import InvalidRequestError, _deserialize_invalid_request_error, _serialize_invalid_request_error
from portone_server_sdk._generated.platform.platform_archived_contract_error import PlatformArchivedContractError, _deserialize_platform_archived_contract_error, _serialize_platform_archived_contract_error
from portone_server_sdk._generated.platform.platform_contract_not_found_error import PlatformContractNotFoundError, _deserialize_platform_contract_not_found_error, _serialize_platform_contract_not_found_error
from portone_server_sdk._generated.platform.platform_contract_schedule_already_exists_error import PlatformContractScheduleAlreadyExistsError, _deserialize_platform_contract_schedule_already_exists_error, _serialize_platform_contract_schedule_already_exists_error
from portone_server_sdk._generated.platform.platform_not_enabled_error import PlatformNotEnabledError, _deserialize_platform_not_enabled_error, _serialize_platform_not_enabled_error
from portone_server_sdk._generated.common.unauthorized_error import UnauthorizedError, _deserialize_unauthorized_error, _serialize_unauthorized_error

ScheduleContractError = Union[ForbiddenError, InvalidRequestError, PlatformArchivedContractError, PlatformContractNotFoundError, PlatformContractScheduleAlreadyExistsError, PlatformNotEnabledError, UnauthorizedError]


def _serialize_schedule_contract_error(obj: ScheduleContractError) -> Any:
    if obj.type == "FORBIDDEN":
        return _serialize_forbidden_error(obj)
    if obj.type == "INVALID_REQUEST":
        return _serialize_invalid_request_error(obj)
    if obj.type == "PLATFORM_ARCHIVED_CONTRACT":
        return _serialize_platform_archived_contract_error(obj)
    if obj.type == "PLATFORM_CONTRACT_NOT_FOUND":
        return _serialize_platform_contract_not_found_error(obj)
    if obj.type == "PLATFORM_CONTRACT_SCHEDULE_ALREADY_EXISTS":
        return _serialize_platform_contract_schedule_already_exists_error(obj)
    if obj.type == "PLATFORM_NOT_ENABLED":
        return _serialize_platform_not_enabled_error(obj)
    if obj.type == "UNAUTHORIZED":
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
    raise ValueError(f"{repr(obj)} is not ScheduleContractError")
