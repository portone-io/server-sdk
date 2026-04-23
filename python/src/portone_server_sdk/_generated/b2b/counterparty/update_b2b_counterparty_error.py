from __future__ import annotations
from typing import Any, Optional, Union
from ...b2b.counterparty.b2b_counterparty_brn_modification_not_allowed_error import B2bCounterpartyBrnModificationNotAllowedError, _deserialize_b2b_counterparty_brn_modification_not_allowed_error, _serialize_b2b_counterparty_brn_modification_not_allowed_error
from ...b2b.counterparty.b2b_counterparty_missing_required_fields_error import B2bCounterpartyMissingRequiredFieldsError, _deserialize_b2b_counterparty_missing_required_fields_error, _serialize_b2b_counterparty_missing_required_fields_error
from ...common.b2b_counterparty_not_found_error import B2bCounterpartyNotFoundError, _deserialize_b2b_counterparty_not_found_error, _serialize_b2b_counterparty_not_found_error
from ...b2b.counterparty.b2b_counterparty_partner_not_updatable_error import B2bCounterpartyPartnerNotUpdatableError, _deserialize_b2b_counterparty_partner_not_updatable_error, _serialize_b2b_counterparty_partner_not_updatable_error
from ...b2b.counterparty.b2b_counterparty_too_many_additional_contacts_error import B2bCounterpartyTooManyAdditionalContactsError, _deserialize_b2b_counterparty_too_many_additional_contacts_error, _serialize_b2b_counterparty_too_many_additional_contacts_error
from ...b2b.counterparty.b2b_counterparty_verification_brn_mismatch_error import B2bCounterpartyVerificationBrnMismatchError, _deserialize_b2b_counterparty_verification_brn_mismatch_error, _serialize_b2b_counterparty_verification_brn_mismatch_error
from ...b2b.counterparty.b2b_counterparty_verification_invalid_error import B2bCounterpartyVerificationInvalidError, _deserialize_b2b_counterparty_verification_invalid_error, _serialize_b2b_counterparty_verification_invalid_error
from ...b2b.counterparty.b2b_counterparty_verification_not_found_error import B2bCounterpartyVerificationNotFoundError, _deserialize_b2b_counterparty_verification_not_found_error, _serialize_b2b_counterparty_verification_not_found_error
from ...b2b.counterparty.b2b_counterparty_verification_type_mismatch_error import B2bCounterpartyVerificationTypeMismatchError, _deserialize_b2b_counterparty_verification_type_mismatch_error, _serialize_b2b_counterparty_verification_type_mismatch_error
from ...common.b2b_external_service_error import B2bExternalServiceError, _deserialize_b2b_external_service_error, _serialize_b2b_external_service_error
from ...common.b2b_not_enabled_error import B2bNotEnabledError, _deserialize_b2b_not_enabled_error, _serialize_b2b_not_enabled_error
from ...common.forbidden_error import ForbiddenError, _deserialize_forbidden_error, _serialize_forbidden_error
from ...common.invalid_request_error import InvalidRequestError, _deserialize_invalid_request_error, _serialize_invalid_request_error
from ...common.unauthorized_error import UnauthorizedError, _deserialize_unauthorized_error, _serialize_unauthorized_error

UpdateB2bCounterpartyError = Union[B2bCounterpartyBrnModificationNotAllowedError, B2bCounterpartyMissingRequiredFieldsError, B2bCounterpartyNotFoundError, B2bCounterpartyPartnerNotUpdatableError, B2bCounterpartyTooManyAdditionalContactsError, B2bCounterpartyVerificationBrnMismatchError, B2bCounterpartyVerificationInvalidError, B2bCounterpartyVerificationNotFoundError, B2bCounterpartyVerificationTypeMismatchError, B2bExternalServiceError, B2bNotEnabledError, ForbiddenError, InvalidRequestError, UnauthorizedError, dict]


def _serialize_update_b2b_counterparty_error(obj: UpdateB2bCounterpartyError) -> Any:
    if isinstance(obj, dict):
        return obj
    if isinstance(obj, B2bCounterpartyBrnModificationNotAllowedError):
        return _serialize_b2b_counterparty_brn_modification_not_allowed_error(obj)
    if isinstance(obj, B2bCounterpartyMissingRequiredFieldsError):
        return _serialize_b2b_counterparty_missing_required_fields_error(obj)
    if isinstance(obj, B2bCounterpartyNotFoundError):
        return _serialize_b2b_counterparty_not_found_error(obj)
    if isinstance(obj, B2bCounterpartyPartnerNotUpdatableError):
        return _serialize_b2b_counterparty_partner_not_updatable_error(obj)
    if isinstance(obj, B2bCounterpartyTooManyAdditionalContactsError):
        return _serialize_b2b_counterparty_too_many_additional_contacts_error(obj)
    if isinstance(obj, B2bCounterpartyVerificationBrnMismatchError):
        return _serialize_b2b_counterparty_verification_brn_mismatch_error(obj)
    if isinstance(obj, B2bCounterpartyVerificationInvalidError):
        return _serialize_b2b_counterparty_verification_invalid_error(obj)
    if isinstance(obj, B2bCounterpartyVerificationNotFoundError):
        return _serialize_b2b_counterparty_verification_not_found_error(obj)
    if isinstance(obj, B2bCounterpartyVerificationTypeMismatchError):
        return _serialize_b2b_counterparty_verification_type_mismatch_error(obj)
    if isinstance(obj, B2bExternalServiceError):
        return _serialize_b2b_external_service_error(obj)
    if isinstance(obj, B2bNotEnabledError):
        return _serialize_b2b_not_enabled_error(obj)
    if isinstance(obj, ForbiddenError):
        return _serialize_forbidden_error(obj)
    if isinstance(obj, InvalidRequestError):
        return _serialize_invalid_request_error(obj)
    if isinstance(obj, UnauthorizedError):
        return _serialize_unauthorized_error(obj)


def _deserialize_update_b2b_counterparty_error(obj: Any) -> UpdateB2bCounterpartyError:
    try:
        return _deserialize_b2b_counterparty_brn_modification_not_allowed_error(obj)
    except Exception:
        pass
    try:
        return _deserialize_b2b_counterparty_missing_required_fields_error(obj)
    except Exception:
        pass
    try:
        return _deserialize_b2b_counterparty_not_found_error(obj)
    except Exception:
        pass
    try:
        return _deserialize_b2b_counterparty_partner_not_updatable_error(obj)
    except Exception:
        pass
    try:
        return _deserialize_b2b_counterparty_too_many_additional_contacts_error(obj)
    except Exception:
        pass
    try:
        return _deserialize_b2b_counterparty_verification_brn_mismatch_error(obj)
    except Exception:
        pass
    try:
        return _deserialize_b2b_counterparty_verification_invalid_error(obj)
    except Exception:
        pass
    try:
        return _deserialize_b2b_counterparty_verification_not_found_error(obj)
    except Exception:
        pass
    try:
        return _deserialize_b2b_counterparty_verification_type_mismatch_error(obj)
    except Exception:
        pass
    try:
        return _deserialize_b2b_external_service_error(obj)
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
    raise ValueError(f"{repr(obj)} is not UpdateB2bCounterpartyError")
