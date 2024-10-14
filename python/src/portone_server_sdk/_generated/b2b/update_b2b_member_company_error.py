from __future__ import annotations
from typing import Any, Optional, Union
from portone_server_sdk._generated.b2b.b2b_member_company_not_found_error import B2bMemberCompanyNotFoundError, _deserialize_b2b_member_company_not_found_error, _serialize_b2b_member_company_not_found_error
from portone_server_sdk._generated.b2b.b2b_not_enabled_error import B2bNotEnabledError, _deserialize_b2b_not_enabled_error, _serialize_b2b_not_enabled_error
from portone_server_sdk._generated.common.invalid_request_error import InvalidRequestError, _deserialize_invalid_request_error, _serialize_invalid_request_error
from portone_server_sdk._generated.common.unauthorized_error import UnauthorizedError, _deserialize_unauthorized_error, _serialize_unauthorized_error

UpdateB2bMemberCompanyError = Union[B2bMemberCompanyNotFoundError, B2bNotEnabledError, InvalidRequestError, UnauthorizedError]


def _serialize_update_b2b_member_company_error(obj: UpdateB2bMemberCompanyError) -> Any:
    if obj.type == "B2B_MEMBER_COMPANY_NOT_FOUND":
        return _serialize_b2b_member_company_not_found_error(obj)
    if obj.type == "B2B_NOT_ENABLED":
        return _serialize_b2b_not_enabled_error(obj)
    if obj.type == "INVALID_REQUEST":
        return _serialize_invalid_request_error(obj)
    if obj.type == "UNAUTHORIZED":
        return _serialize_unauthorized_error(obj)


def _deserialize_update_b2b_member_company_error(obj: Any) -> UpdateB2bMemberCompanyError:
    try:
        return _deserialize_b2b_member_company_not_found_error(obj)
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
    raise ValueError(f"{repr(obj)} is not UpdateB2bMemberCompanyError")