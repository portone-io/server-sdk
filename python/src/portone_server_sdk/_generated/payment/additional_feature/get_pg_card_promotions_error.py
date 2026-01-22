from __future__ import annotations
from typing import Any, Optional, Union
from ...common.channel_not_found_error import ChannelNotFoundError, _deserialize_channel_not_found_error, _serialize_channel_not_found_error
from ...common.invalid_request_error import InvalidRequestError, _deserialize_invalid_request_error, _serialize_invalid_request_error
from ...common.pg_provider_error import PgProviderError, _deserialize_pg_provider_error, _serialize_pg_provider_error
from ...common.unauthorized_error import UnauthorizedError, _deserialize_unauthorized_error, _serialize_unauthorized_error

GetPgCardPromotionsError = Union[ChannelNotFoundError, InvalidRequestError, PgProviderError, UnauthorizedError, dict]


def _serialize_get_pg_card_promotions_error(obj: GetPgCardPromotionsError) -> Any:
    if isinstance(obj, dict):
        return obj
    if isinstance(obj, ChannelNotFoundError):
        return _serialize_channel_not_found_error(obj)
    if isinstance(obj, InvalidRequestError):
        return _serialize_invalid_request_error(obj)
    if isinstance(obj, PgProviderError):
        return _serialize_pg_provider_error(obj)
    if isinstance(obj, UnauthorizedError):
        return _serialize_unauthorized_error(obj)


def _deserialize_get_pg_card_promotions_error(obj: Any) -> GetPgCardPromotionsError:
    try:
        return _deserialize_channel_not_found_error(obj)
    except Exception:
        pass
    try:
        return _deserialize_invalid_request_error(obj)
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
    raise ValueError(f"{repr(obj)} is not GetPgCardPromotionsError")
