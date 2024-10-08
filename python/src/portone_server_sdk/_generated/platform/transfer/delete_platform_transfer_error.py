from __future__ import annotations
from typing import Any, Optional, Union
from portone_server_sdk._generated.common.forbidden_error import ForbiddenError, _deserialize_forbidden_error, _serialize_forbidden_error
from portone_server_sdk._generated.common.invalid_request_error import InvalidRequestError, _deserialize_invalid_request_error, _serialize_invalid_request_error
from portone_server_sdk._generated.platform.transfer.platform_cancel_order_transfers_exists_error import PlatformCancelOrderTransfersExistsError, _deserialize_platform_cancel_order_transfers_exists_error, _serialize_platform_cancel_order_transfers_exists_error
from portone_server_sdk._generated.platform.platform_not_enabled_error import PlatformNotEnabledError, _deserialize_platform_not_enabled_error, _serialize_platform_not_enabled_error
from portone_server_sdk._generated.platform.transfer.platform_transfer_non_deletable_status_error import PlatformTransferNonDeletableStatusError, _deserialize_platform_transfer_non_deletable_status_error, _serialize_platform_transfer_non_deletable_status_error
from portone_server_sdk._generated.platform.transfer.platform_transfer_not_found_error import PlatformTransferNotFoundError, _deserialize_platform_transfer_not_found_error, _serialize_platform_transfer_not_found_error
from portone_server_sdk._generated.common.unauthorized_error import UnauthorizedError, _deserialize_unauthorized_error, _serialize_unauthorized_error

DeletePlatformTransferError = Union[ForbiddenError, InvalidRequestError, PlatformCancelOrderTransfersExistsError, PlatformNotEnabledError, PlatformTransferNonDeletableStatusError, PlatformTransferNotFoundError, UnauthorizedError]


def _serialize_delete_platform_transfer_error(obj: DeletePlatformTransferError) -> Any:
    if obj.type == "FORBIDDEN":
        return _serialize_forbidden_error(obj)
    if obj.type == "INVALID_REQUEST":
        return _serialize_invalid_request_error(obj)
    if obj.type == "PLATFORM_CANCEL_ORDER_TRANSFERS_EXISTS":
        return _serialize_platform_cancel_order_transfers_exists_error(obj)
    if obj.type == "PLATFORM_NOT_ENABLED":
        return _serialize_platform_not_enabled_error(obj)
    if obj.type == "PLATFORM_TRANSFER_NON_DELETABLE_STATUS":
        return _serialize_platform_transfer_non_deletable_status_error(obj)
    if obj.type == "PLATFORM_TRANSFER_NOT_FOUND":
        return _serialize_platform_transfer_not_found_error(obj)
    if obj.type == "UNAUTHORIZED":
        return _serialize_unauthorized_error(obj)


def _deserialize_delete_platform_transfer_error(obj: Any) -> DeletePlatformTransferError:
    try:
        return _deserialize_forbidden_error(obj)
    except Exception:
        pass
    try:
        return _deserialize_invalid_request_error(obj)
    except Exception:
        pass
    try:
        return _deserialize_platform_cancel_order_transfers_exists_error(obj)
    except Exception:
        pass
    try:
        return _deserialize_platform_not_enabled_error(obj)
    except Exception:
        pass
    try:
        return _deserialize_platform_transfer_non_deletable_status_error(obj)
    except Exception:
        pass
    try:
        return _deserialize_platform_transfer_not_found_error(obj)
    except Exception:
        pass
    try:
        return _deserialize_unauthorized_error(obj)
    except Exception:
        pass
    raise ValueError(f"{repr(obj)} is not DeletePlatformTransferError")
