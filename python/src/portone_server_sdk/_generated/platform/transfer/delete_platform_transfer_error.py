from __future__ import annotations
from typing import Any, Optional, Union
from ...common.forbidden_error import ForbiddenError, _deserialize_forbidden_error, _serialize_forbidden_error
from ...common.invalid_request_error import InvalidRequestError, _deserialize_invalid_request_error, _serialize_invalid_request_error
from ...platform.transfer.platform_cancel_order_transfers_exists_error import PlatformCancelOrderTransfersExistsError, _deserialize_platform_cancel_order_transfers_exists_error, _serialize_platform_cancel_order_transfers_exists_error
from ...platform.platform_not_enabled_error import PlatformNotEnabledError, _deserialize_platform_not_enabled_error, _serialize_platform_not_enabled_error
from ...platform.transfer.platform_transfer_non_deletable_status_error import PlatformTransferNonDeletableStatusError, _deserialize_platform_transfer_non_deletable_status_error, _serialize_platform_transfer_non_deletable_status_error
from ...platform.transfer.platform_transfer_not_found_error import PlatformTransferNotFoundError, _deserialize_platform_transfer_not_found_error, _serialize_platform_transfer_not_found_error
from ...common.unauthorized_error import UnauthorizedError, _deserialize_unauthorized_error, _serialize_unauthorized_error

DeletePlatformTransferError = Union[ForbiddenError, InvalidRequestError, PlatformCancelOrderTransfersExistsError, PlatformNotEnabledError, PlatformTransferNonDeletableStatusError, PlatformTransferNotFoundError, UnauthorizedError, dict]


def _serialize_delete_platform_transfer_error(obj: DeletePlatformTransferError) -> Any:
    if isinstance(obj, dict):
        return obj
    if isinstance(obj, ForbiddenError):
        return _serialize_forbidden_error(obj)
    if isinstance(obj, InvalidRequestError):
        return _serialize_invalid_request_error(obj)
    if isinstance(obj, PlatformCancelOrderTransfersExistsError):
        return _serialize_platform_cancel_order_transfers_exists_error(obj)
    if isinstance(obj, PlatformNotEnabledError):
        return _serialize_platform_not_enabled_error(obj)
    if isinstance(obj, PlatformTransferNonDeletableStatusError):
        return _serialize_platform_transfer_non_deletable_status_error(obj)
    if isinstance(obj, PlatformTransferNotFoundError):
        return _serialize_platform_transfer_not_found_error(obj)
    if isinstance(obj, UnauthorizedError):
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
