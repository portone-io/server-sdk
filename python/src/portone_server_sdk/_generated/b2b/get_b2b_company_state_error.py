from __future__ import annotations
from typing import Any, Optional, Union
from portone_server_sdk._generated.b2b.b2b_company_not_found_error import B2bCompanyNotFoundError, _deserialize_b2b_company_not_found_error, _serialize_b2b_company_not_found_error
from portone_server_sdk._generated.b2b.b2b_external_service_error import B2bExternalServiceError, _deserialize_b2b_external_service_error, _serialize_b2b_external_service_error
from portone_server_sdk._generated.b2b.b2b_hometax_under_maintenance_error import B2bHometaxUnderMaintenanceError, _deserialize_b2b_hometax_under_maintenance_error, _serialize_b2b_hometax_under_maintenance_error
from portone_server_sdk._generated.b2b.b2b_not_enabled_error import B2bNotEnabledError, _deserialize_b2b_not_enabled_error, _serialize_b2b_not_enabled_error
from portone_server_sdk._generated.common.invalid_request_error import InvalidRequestError, _deserialize_invalid_request_error, _serialize_invalid_request_error
from portone_server_sdk._generated.common.unauthorized_error import UnauthorizedError, _deserialize_unauthorized_error, _serialize_unauthorized_error

GetB2bCompanyStateError = Union[B2bCompanyNotFoundError, B2bExternalServiceError, B2bHometaxUnderMaintenanceError, B2bNotEnabledError, InvalidRequestError, UnauthorizedError]


def _serialize_get_b2b_company_state_error(obj: GetB2bCompanyStateError) -> Any:
    if obj.type == "B2B_COMPANY_NOT_FOUND":
        return _serialize_b2b_company_not_found_error(obj)
    if obj.type == "B2B_EXTERNAL_SERVICE":
        return _serialize_b2b_external_service_error(obj)
    if obj.type == "B2B_HOMETAX_UNDER_MAINTENANCE":
        return _serialize_b2b_hometax_under_maintenance_error(obj)
    if obj.type == "B2B_NOT_ENABLED":
        return _serialize_b2b_not_enabled_error(obj)
    if obj.type == "INVALID_REQUEST":
        return _serialize_invalid_request_error(obj)
    if obj.type == "UNAUTHORIZED":
        return _serialize_unauthorized_error(obj)


def _deserialize_get_b2b_company_state_error(obj: Any) -> GetB2bCompanyStateError:
    try:
        return _deserialize_b2b_company_not_found_error(obj)
    except Exception:
        pass
    try:
        return _deserialize_b2b_external_service_error(obj)
    except Exception:
        pass
    try:
        return _deserialize_b2b_hometax_under_maintenance_error(obj)
    except Exception:
        pass
    try:
        return _deserialize_b2b_not_enabled_error(obj)
    except Exception:
        pass
    try:
        return _deserialize_invalid_request_error(obj)
    except Exception:
        pass
    try:
        return _deserialize_unauthorized_error(obj)
    except Exception:
        pass
    raise ValueError(f"{repr(obj)} is not GetB2bCompanyStateError")