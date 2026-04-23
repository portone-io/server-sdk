from __future__ import annotations
from typing import Any, Optional, Union
from ...common.forbidden_error import ForbiddenError, _deserialize_forbidden_error, _serialize_forbidden_error
from ...common.invalid_request_error import InvalidRequestError, _deserialize_invalid_request_error, _serialize_invalid_request_error
from ...platform.payout.platform_bulk_payout_id_already_exists_error import PlatformBulkPayoutIdAlreadyExistsError, _deserialize_platform_bulk_payout_id_already_exists_error, _serialize_platform_bulk_payout_id_already_exists_error
from ...platform.payout.platform_duplicated_partner_settlement_ids_error import PlatformDuplicatedPartnerSettlementIdsError, _deserialize_platform_duplicated_partner_settlement_ids_error, _serialize_platform_duplicated_partner_settlement_ids_error
from ...platform.payout.platform_negative_payout_amount_partners_error import PlatformNegativePayoutAmountPartnersError, _deserialize_platform_negative_payout_amount_partners_error, _serialize_platform_negative_payout_amount_partners_error
from ...platform.payout.platform_no_selected_partner_settlements_error import PlatformNoSelectedPartnerSettlementsError, _deserialize_platform_no_selected_partner_settlements_error, _serialize_platform_no_selected_partner_settlements_error
from ...platform.payout.platform_non_payable_partner_settlements_error import PlatformNonPayablePartnerSettlementsError, _deserialize_platform_non_payable_partner_settlements_error, _serialize_platform_non_payable_partner_settlements_error
from ...platform.platform_not_enabled_error import PlatformNotEnabledError, _deserialize_platform_not_enabled_error, _serialize_platform_not_enabled_error
from ...platform.platform_partner_settlements_not_found_error import PlatformPartnerSettlementsNotFoundError, _deserialize_platform_partner_settlements_not_found_error, _serialize_platform_partner_settlements_not_found_error
from ...common.unauthorized_error import UnauthorizedError, _deserialize_unauthorized_error, _serialize_unauthorized_error

CompletePlatformPayoutByPartnerSettlementIdsError = Union[ForbiddenError, InvalidRequestError, PlatformBulkPayoutIdAlreadyExistsError, PlatformNegativePayoutAmountPartnersError, PlatformDuplicatedPartnerSettlementIdsError, PlatformNonPayablePartnerSettlementsError, PlatformNotEnabledError, PlatformNoSelectedPartnerSettlementsError, PlatformPartnerSettlementsNotFoundError, UnauthorizedError, dict]


def _serialize_complete_platform_payout_by_partner_settlement_ids_error(obj: CompletePlatformPayoutByPartnerSettlementIdsError) -> Any:
    if isinstance(obj, dict):
        return obj
    if isinstance(obj, ForbiddenError):
        return _serialize_forbidden_error(obj)
    if isinstance(obj, InvalidRequestError):
        return _serialize_invalid_request_error(obj)
    if isinstance(obj, PlatformBulkPayoutIdAlreadyExistsError):
        return _serialize_platform_bulk_payout_id_already_exists_error(obj)
    if isinstance(obj, PlatformNegativePayoutAmountPartnersError):
        return _serialize_platform_negative_payout_amount_partners_error(obj)
    if isinstance(obj, PlatformDuplicatedPartnerSettlementIdsError):
        return _serialize_platform_duplicated_partner_settlement_ids_error(obj)
    if isinstance(obj, PlatformNonPayablePartnerSettlementsError):
        return _serialize_platform_non_payable_partner_settlements_error(obj)
    if isinstance(obj, PlatformNotEnabledError):
        return _serialize_platform_not_enabled_error(obj)
    if isinstance(obj, PlatformNoSelectedPartnerSettlementsError):
        return _serialize_platform_no_selected_partner_settlements_error(obj)
    if isinstance(obj, PlatformPartnerSettlementsNotFoundError):
        return _serialize_platform_partner_settlements_not_found_error(obj)
    if isinstance(obj, UnauthorizedError):
        return _serialize_unauthorized_error(obj)


def _deserialize_complete_platform_payout_by_partner_settlement_ids_error(obj: Any) -> CompletePlatformPayoutByPartnerSettlementIdsError:
    try:
        return _deserialize_forbidden_error(obj)
    except Exception:
        pass
    try:
        return _deserialize_invalid_request_error(obj)
    except Exception:
        pass
    try:
        return _deserialize_platform_bulk_payout_id_already_exists_error(obj)
    except Exception:
        pass
    try:
        return _deserialize_platform_negative_payout_amount_partners_error(obj)
    except Exception:
        pass
    try:
        return _deserialize_platform_duplicated_partner_settlement_ids_error(obj)
    except Exception:
        pass
    try:
        return _deserialize_platform_non_payable_partner_settlements_error(obj)
    except Exception:
        pass
    try:
        return _deserialize_platform_not_enabled_error(obj)
    except Exception:
        pass
    try:
        return _deserialize_platform_no_selected_partner_settlements_error(obj)
    except Exception:
        pass
    try:
        return _deserialize_platform_partner_settlements_not_found_error(obj)
    except Exception:
        pass
    try:
        return _deserialize_unauthorized_error(obj)
    except Exception:
        pass
    raise ValueError(f"{repr(obj)} is not CompletePlatformPayoutByPartnerSettlementIdsError")
