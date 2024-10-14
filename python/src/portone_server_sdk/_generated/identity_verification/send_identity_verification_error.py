from __future__ import annotations
from typing import Any, Optional, Union
from portone_server_sdk._generated.common.channel_not_found_error import ChannelNotFoundError, _deserialize_channel_not_found_error, _serialize_channel_not_found_error
from portone_server_sdk._generated.common.forbidden_error import ForbiddenError, _deserialize_forbidden_error, _serialize_forbidden_error
from portone_server_sdk._generated.identity_verification.identity_verification_already_sent_error import IdentityVerificationAlreadySentError, _deserialize_identity_verification_already_sent_error, _serialize_identity_verification_already_sent_error
from portone_server_sdk._generated.identity_verification.identity_verification_already_verified_error import IdentityVerificationAlreadyVerifiedError, _deserialize_identity_verification_already_verified_error, _serialize_identity_verification_already_verified_error
from portone_server_sdk._generated.identity_verification.identity_verification_not_found_error import IdentityVerificationNotFoundError, _deserialize_identity_verification_not_found_error, _serialize_identity_verification_not_found_error
from portone_server_sdk._generated.common.invalid_request_error import InvalidRequestError, _deserialize_invalid_request_error, _serialize_invalid_request_error
from portone_server_sdk._generated.common.max_transaction_count_reached_error import MaxTransactionCountReachedError, _deserialize_max_transaction_count_reached_error, _serialize_max_transaction_count_reached_error
from portone_server_sdk._generated.common.pg_provider_error import PgProviderError, _deserialize_pg_provider_error, _serialize_pg_provider_error
from portone_server_sdk._generated.common.unauthorized_error import UnauthorizedError, _deserialize_unauthorized_error, _serialize_unauthorized_error

SendIdentityVerificationError = Union[ChannelNotFoundError, ForbiddenError, IdentityVerificationAlreadySentError, IdentityVerificationAlreadyVerifiedError, IdentityVerificationNotFoundError, InvalidRequestError, MaxTransactionCountReachedError, PgProviderError, UnauthorizedError]


def _serialize_send_identity_verification_error(obj: SendIdentityVerificationError) -> Any:
    if obj.type == "CHANNEL_NOT_FOUND":
        return _serialize_channel_not_found_error(obj)
    if obj.type == "FORBIDDEN":
        return _serialize_forbidden_error(obj)
    if obj.type == "IDENTITY_VERIFICATION_ALREADY_SENT":
        return _serialize_identity_verification_already_sent_error(obj)
    if obj.type == "IDENTITY_VERIFICATION_ALREADY_VERIFIED":
        return _serialize_identity_verification_already_verified_error(obj)
    if obj.type == "IDENTITY_VERIFICATION_NOT_FOUND":
        return _serialize_identity_verification_not_found_error(obj)
    if obj.type == "INVALID_REQUEST":
        return _serialize_invalid_request_error(obj)
    if obj.type == "MAX_TRANSACTION_COUNT_REACHED":
        return _serialize_max_transaction_count_reached_error(obj)
    if obj.type == "PG_PROVIDER":
        return _serialize_pg_provider_error(obj)
    if obj.type == "UNAUTHORIZED":
        return _serialize_unauthorized_error(obj)


def _deserialize_send_identity_verification_error(obj: Any) -> SendIdentityVerificationError:
    try:
        return _deserialize_channel_not_found_error(obj)
    except Exception:
        pass
    try:
        return _deserialize_forbidden_error(obj)
    except Exception:
        pass
    try:
        return _deserialize_identity_verification_already_sent_error(obj)
    except Exception:
        pass
    try:
        return _deserialize_identity_verification_already_verified_error(obj)
    except Exception:
        pass
    try:
        return _deserialize_identity_verification_not_found_error(obj)
    except Exception:
        pass
    try:
        return _deserialize_invalid_request_error(obj)
    except Exception:
        pass
    try:
        return _deserialize_max_transaction_count_reached_error(obj)
    except Exception:
        pass
    try:
        return _deserialize_pg_provider_error(obj)
    except Exception:
        pass
    try:
        return _deserialize_unauthorized_error(obj)
    except Exception:
        pass
    raise ValueError(f"{repr(obj)} is not SendIdentityVerificationError")
