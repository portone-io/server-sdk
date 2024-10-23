from __future__ import annotations
from typing import Any, Optional, Union
from portone_server_sdk._generated.b2b.member_company.b2b_bank_account_not_found_error import B2bBankAccountNotFoundError, _deserialize_b2b_bank_account_not_found_error, _serialize_b2b_bank_account_not_found_error
from portone_server_sdk._generated.common.b2b_external_service_error import B2bExternalServiceError, _deserialize_b2b_external_service_error, _serialize_b2b_external_service_error
from portone_server_sdk._generated.b2b.member_company.b2b_financial_system_communication_error import B2bFinancialSystemCommunicationError, _deserialize_b2b_financial_system_communication_error, _serialize_b2b_financial_system_communication_error
from portone_server_sdk._generated.b2b.member_company.b2b_financial_system_failure_error import B2bFinancialSystemFailureError, _deserialize_b2b_financial_system_failure_error, _serialize_b2b_financial_system_failure_error
from portone_server_sdk._generated.b2b.member_company.b2b_financial_system_under_maintenance_error import B2bFinancialSystemUnderMaintenanceError, _deserialize_b2b_financial_system_under_maintenance_error, _serialize_b2b_financial_system_under_maintenance_error
from portone_server_sdk._generated.b2b.member_company.b2b_foreign_exchange_account_error import B2bForeignExchangeAccountError, _deserialize_b2b_foreign_exchange_account_error, _serialize_b2b_foreign_exchange_account_error
from portone_server_sdk._generated.common.b2b_not_enabled_error import B2bNotEnabledError, _deserialize_b2b_not_enabled_error, _serialize_b2b_not_enabled_error
from portone_server_sdk._generated.b2b.member_company.b2b_regular_maintenance_time_error import B2bRegularMaintenanceTimeError, _deserialize_b2b_regular_maintenance_time_error, _serialize_b2b_regular_maintenance_time_error
from portone_server_sdk._generated.b2b.member_company.b2b_suspended_account_error import B2bSuspendedAccountError, _deserialize_b2b_suspended_account_error, _serialize_b2b_suspended_account_error
from portone_server_sdk._generated.common.forbidden_error import ForbiddenError, _deserialize_forbidden_error, _serialize_forbidden_error
from portone_server_sdk._generated.common.invalid_request_error import InvalidRequestError, _deserialize_invalid_request_error, _serialize_invalid_request_error
from portone_server_sdk._generated.common.unauthorized_error import UnauthorizedError, _deserialize_unauthorized_error, _serialize_unauthorized_error

GetB2bAccountHolderError = Union[B2bBankAccountNotFoundError, B2bExternalServiceError, B2bFinancialSystemCommunicationError, B2bFinancialSystemFailureError, B2bFinancialSystemUnderMaintenanceError, B2bForeignExchangeAccountError, B2bNotEnabledError, B2bRegularMaintenanceTimeError, B2bSuspendedAccountError, ForbiddenError, InvalidRequestError, UnauthorizedError]


def _serialize_get_b2b_account_holder_error(obj: GetB2bAccountHolderError) -> Any:
    if obj.type == "B2B_BANK_ACCOUNT_NOT_FOUND":
        return _serialize_b2b_bank_account_not_found_error(obj)
    if obj.type == "B2B_EXTERNAL_SERVICE":
        return _serialize_b2b_external_service_error(obj)
    if obj.type == "B2B_FINANCIAL_SYSTEM_COMMUNICATION":
        return _serialize_b2b_financial_system_communication_error(obj)
    if obj.type == "B2B_FINANCIAL_SYSTEM_FAILURE":
        return _serialize_b2b_financial_system_failure_error(obj)
    if obj.type == "B2B_FINANCIAL_SYSTEM_UNDER_MAINTENANCE":
        return _serialize_b2b_financial_system_under_maintenance_error(obj)
    if obj.type == "B2B_FOREIGN_EXCHANGE_ACCOUNT":
        return _serialize_b2b_foreign_exchange_account_error(obj)
    if obj.type == "B2B_NOT_ENABLED":
        return _serialize_b2b_not_enabled_error(obj)
    if obj.type == "B2B_REGULAR_MAINTENANCE_TIME":
        return _serialize_b2b_regular_maintenance_time_error(obj)
    if obj.type == "B2B_SUSPENDED_ACCOUNT":
        return _serialize_b2b_suspended_account_error(obj)
    if obj.type == "FORBIDDEN":
        return _serialize_forbidden_error(obj)
    if obj.type == "INVALID_REQUEST":
        return _serialize_invalid_request_error(obj)
    if obj.type == "UNAUTHORIZED":
        return _serialize_unauthorized_error(obj)


def _deserialize_get_b2b_account_holder_error(obj: Any) -> GetB2bAccountHolderError:
    try:
        return _deserialize_b2b_bank_account_not_found_error(obj)
    except Exception:
        pass
    try:
        return _deserialize_b2b_external_service_error(obj)
    except Exception:
        pass
    try:
        return _deserialize_b2b_financial_system_communication_error(obj)
    except Exception:
        pass
    try:
        return _deserialize_b2b_financial_system_failure_error(obj)
    except Exception:
        pass
    try:
        return _deserialize_b2b_financial_system_under_maintenance_error(obj)
    except Exception:
        pass
    try:
        return _deserialize_b2b_foreign_exchange_account_error(obj)
    except Exception:
        pass
    try:
        return _deserialize_b2b_not_enabled_error(obj)
    except Exception:
        pass
    try:
        return _deserialize_b2b_regular_maintenance_time_error(obj)
    except Exception:
        pass
    try:
        return _deserialize_b2b_suspended_account_error(obj)
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
    raise ValueError(f"{repr(obj)} is not GetB2bAccountHolderError")
