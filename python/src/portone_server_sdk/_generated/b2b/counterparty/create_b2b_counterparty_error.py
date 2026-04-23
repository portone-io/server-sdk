from __future__ import annotations
from typing import Any, Optional, Union
from ...b2b.counterparty.b2b_counterparty_brn_invalid_error import B2bCounterpartyBrnInvalidError, _deserialize_b2b_counterparty_brn_invalid_error, _serialize_b2b_counterparty_brn_invalid_error
from ...b2b.counterparty.b2b_counterparty_id_already_exists_by_partner_error import B2bCounterpartyIdAlreadyExistsByPartnerError, _deserialize_b2b_counterparty_id_already_exists_by_partner_error, _serialize_b2b_counterparty_id_already_exists_by_partner_error
from ...b2b.counterparty.b2b_counterparty_id_already_exists_error import B2bCounterpartyIdAlreadyExistsError, _deserialize_b2b_counterparty_id_already_exists_error, _serialize_b2b_counterparty_id_already_exists_error
from ...b2b.counterparty.b2b_counterparty_missing_required_fields_error import B2bCounterpartyMissingRequiredFieldsError, _deserialize_b2b_counterparty_missing_required_fields_error, _serialize_b2b_counterparty_missing_required_fields_error
from ...b2b.counterparty.b2b_counterparty_nts_connection_failed_error import B2bCounterpartyNtsConnectionFailedError, _deserialize_b2b_counterparty_nts_connection_failed_error, _serialize_b2b_counterparty_nts_connection_failed_error
from ...b2b.counterparty.b2b_counterparty_partner_not_connectable_error import B2bCounterpartyPartnerNotConnectableError, _deserialize_b2b_counterparty_partner_not_connectable_error, _serialize_b2b_counterparty_partner_not_connectable_error
from ...b2b.counterparty.b2b_counterparty_self_origin_brn_mismatch_error import B2bCounterpartySelfOriginBrnMismatchError, _deserialize_b2b_counterparty_self_origin_brn_mismatch_error, _serialize_b2b_counterparty_self_origin_brn_mismatch_error
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

CreateB2bCounterpartyError = Union[B2bCounterpartyBrnInvalidError, B2bCounterpartyIdAlreadyExistsError, B2bCounterpartyIdAlreadyExistsByPartnerError, B2bCounterpartyMissingRequiredFieldsError, B2bCounterpartyNtsConnectionFailedError, B2bCounterpartyPartnerNotConnectableError, B2bCounterpartySelfOriginBrnMismatchError, B2bCounterpartyTooManyAdditionalContactsError, B2bCounterpartyVerificationBrnMismatchError, B2bCounterpartyVerificationInvalidError, B2bCounterpartyVerificationNotFoundError, B2bCounterpartyVerificationTypeMismatchError, B2bExternalServiceError, B2bNotEnabledError, ForbiddenError, InvalidRequestError, UnauthorizedError, dict]


def _serialize_create_b2b_counterparty_error(obj: CreateB2bCounterpartyError) -> Any:
    if isinstance(obj, dict):
        return obj
    if isinstance(obj, B2bCounterpartyBrnInvalidError):
        return _serialize_b2b_counterparty_brn_invalid_error(obj)
    if isinstance(obj, B2bCounterpartyIdAlreadyExistsError):
        return _serialize_b2b_counterparty_id_already_exists_error(obj)
    if isinstance(obj, B2bCounterpartyIdAlreadyExistsByPartnerError):
        return _serialize_b2b_counterparty_id_already_exists_by_partner_error(obj)
    if isinstance(obj, B2bCounterpartyMissingRequiredFieldsError):
        return _serialize_b2b_counterparty_missing_required_fields_error(obj)
    if isinstance(obj, B2bCounterpartyNtsConnectionFailedError):
        return _serialize_b2b_counterparty_nts_connection_failed_error(obj)
    if isinstance(obj, B2bCounterpartyPartnerNotConnectableError):
        return _serialize_b2b_counterparty_partner_not_connectable_error(obj)
    if isinstance(obj, B2bCounterpartySelfOriginBrnMismatchError):
        return _serialize_b2b_counterparty_self_origin_brn_mismatch_error(obj)
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


def _deserialize_create_b2b_counterparty_error(obj: Any) -> CreateB2bCounterpartyError:
    try:
        return _deserialize_b2b_counterparty_brn_invalid_error(obj)
    except Exception:
        pass
    try:
        return _deserialize_b2b_counterparty_id_already_exists_error(obj)
    except Exception:
        pass
    try:
        return _deserialize_b2b_counterparty_id_already_exists_by_partner_error(obj)
    except Exception:
        pass
    try:
        return _deserialize_b2b_counterparty_missing_required_fields_error(obj)
    except Exception:
        pass
    try:
        return _deserialize_b2b_counterparty_nts_connection_failed_error(obj)
    except Exception:
        pass
    try:
        return _deserialize_b2b_counterparty_partner_not_connectable_error(obj)
    except Exception:
        pass
    try:
        return _deserialize_b2b_counterparty_self_origin_brn_mismatch_error(obj)
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
    raise ValueError(f"{repr(obj)} is not CreateB2bCounterpartyError")
