from __future__ import annotations
from typing import Any, Optional, Union
from ...common.forbidden_error import ForbiddenError, _deserialize_forbidden_error, _serialize_forbidden_error
from ...common.invalid_request_error import InvalidRequestError, _deserialize_invalid_request_error, _serialize_invalid_request_error
from ...platform.partner_settlement.platform_non_deletable_partner_settlements_error import PlatformNonDeletablePartnerSettlementsError, _deserialize_platform_non_deletable_partner_settlements_error, _serialize_platform_non_deletable_partner_settlements_error
from ...platform.platform_not_enabled_error import PlatformNotEnabledError, _deserialize_platform_not_enabled_error, _serialize_platform_not_enabled_error
from ...platform.platform_partner_settlements_not_found_error import PlatformPartnerSettlementsNotFoundError, _deserialize_platform_partner_settlements_not_found_error, _serialize_platform_partner_settlements_not_found_error
from ...platform.partner_settlement.platform_referenced_cancel_order_transfers_exist_error import PlatformReferencedCancelOrderTransfersExistError, _deserialize_platform_referenced_cancel_order_transfers_exist_error, _serialize_platform_referenced_cancel_order_transfers_exist_error
from ...common.unauthorized_error import UnauthorizedError, _deserialize_unauthorized_error, _serialize_unauthorized_error

DeletePlatformPartnerSettlementsError = Union[ForbiddenError, InvalidRequestError, PlatformNonDeletablePartnerSettlementsError, PlatformNotEnabledError, PlatformPartnerSettlementsNotFoundError, PlatformReferencedCancelOrderTransfersExistError, UnauthorizedError, dict]


def _serialize_delete_platform_partner_settlements_error(obj: DeletePlatformPartnerSettlementsError) -> Any:
    if isinstance(obj, dict):
        return obj
    if isinstance(obj, ForbiddenError):
        return _serialize_forbidden_error(obj)
    if isinstance(obj, InvalidRequestError):
        return _serialize_invalid_request_error(obj)
    if isinstance(obj, PlatformNonDeletablePartnerSettlementsError):
        return _serialize_platform_non_deletable_partner_settlements_error(obj)
    if isinstance(obj, PlatformNotEnabledError):
        return _serialize_platform_not_enabled_error(obj)
    if isinstance(obj, PlatformPartnerSettlementsNotFoundError):
        return _serialize_platform_partner_settlements_not_found_error(obj)
    if isinstance(obj, PlatformReferencedCancelOrderTransfersExistError):
        return _serialize_platform_referenced_cancel_order_transfers_exist_error(obj)
    if isinstance(obj, UnauthorizedError):
        return _serialize_unauthorized_error(obj)


def _deserialize_delete_platform_partner_settlements_error(obj: Any) -> DeletePlatformPartnerSettlementsError:
    try:
        return _deserialize_forbidden_error(obj)
    except Exception:
        pass
    try:
        return _deserialize_invalid_request_error(obj)
    except Exception:
        pass
    try:
        return _deserialize_platform_non_deletable_partner_settlements_error(obj)
    except Exception:
        pass
    try:
        return _deserialize_platform_not_enabled_error(obj)
    except Exception:
        pass
    try:
        return _deserialize_platform_partner_settlements_not_found_error(obj)
    except Exception:
        pass
    try:
        return _deserialize_platform_referenced_cancel_order_transfers_exist_error(obj)
    except Exception:
        pass
    try:
        return _deserialize_unauthorized_error(obj)
    except Exception:
        pass
    raise ValueError(f"{repr(obj)} is not DeletePlatformPartnerSettlementsError")
