from __future__ import annotations
from typing import Any, Optional, Union
from portone_server_sdk._generated.b2b.member_company.b2b_company_already_registered_error import B2bCompanyAlreadyRegisteredError, _deserialize_b2b_company_already_registered_error, _serialize_b2b_company_already_registered_error
from portone_server_sdk._generated.common.b2b_external_service_error import B2bExternalServiceError, _deserialize_b2b_external_service_error, _serialize_b2b_external_service_error
from portone_server_sdk._generated.common.b2b_id_already_exists_error import B2bIdAlreadyExistsError, _deserialize_b2b_id_already_exists_error, _serialize_b2b_id_already_exists_error
from portone_server_sdk._generated.common.b2b_not_enabled_error import B2bNotEnabledError, _deserialize_b2b_not_enabled_error, _serialize_b2b_not_enabled_error
from portone_server_sdk._generated.common.forbidden_error import ForbiddenError, _deserialize_forbidden_error, _serialize_forbidden_error
from portone_server_sdk._generated.common.invalid_request_error import InvalidRequestError, _deserialize_invalid_request_error, _serialize_invalid_request_error
from portone_server_sdk._generated.common.unauthorized_error import UnauthorizedError, _deserialize_unauthorized_error, _serialize_unauthorized_error

RegisterB2bMemberCompanyError = Union[B2bCompanyAlreadyRegisteredError, B2bExternalServiceError, B2bIdAlreadyExistsError, B2bNotEnabledError, ForbiddenError, InvalidRequestError, UnauthorizedError]


def _serialize_register_b2b_member_company_error(obj: RegisterB2bMemberCompanyError) -> Any:
    if obj.type == "B2B_COMPANY_ALREADY_REGISTERED":
        return _serialize_b2b_company_already_registered_error(obj)
    if obj.type == "B2B_EXTERNAL_SERVICE":
        return _serialize_b2b_external_service_error(obj)
    if obj.type == "B2B_ID_ALREADY_EXISTS":
        return _serialize_b2b_id_already_exists_error(obj)
    if obj.type == "B2B_NOT_ENABLED":
        return _serialize_b2b_not_enabled_error(obj)
    if obj.type == "FORBIDDEN":
        return _serialize_forbidden_error(obj)
    if obj.type == "INVALID_REQUEST":
        return _serialize_invalid_request_error(obj)
    if obj.type == "UNAUTHORIZED":
        return _serialize_unauthorized_error(obj)


def _deserialize_register_b2b_member_company_error(obj: Any) -> RegisterB2bMemberCompanyError:
    try:
        return _deserialize_b2b_company_already_registered_error(obj)
    except Exception:
        pass
    try:
        return _deserialize_b2b_external_service_error(obj)
    except Exception:
        pass
    try:
        return _deserialize_b2b_id_already_exists_error(obj)
    except Exception:
        pass
    try:
        return _deserialize_b2b_not_enabled_error(obj)
    except Exception:
        pass
    try:
        return _deserialize_forbidden_error(obj)
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
    raise ValueError(f"{repr(obj)} is not RegisterB2bMemberCompanyError")
