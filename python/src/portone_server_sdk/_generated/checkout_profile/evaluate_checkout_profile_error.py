from __future__ import annotations
from typing import Any, Optional, Union
from ..common.invalid_request_error import InvalidRequestError, _deserialize_invalid_request_error, _serialize_invalid_request_error
from ..checkout_profile.profile_settings_not_found_error import ProfileSettingsNotFoundError, _deserialize_profile_settings_not_found_error, _serialize_profile_settings_not_found_error

EvaluateCheckoutProfileError = Union[InvalidRequestError, ProfileSettingsNotFoundError, dict]


def _serialize_evaluate_checkout_profile_error(obj: EvaluateCheckoutProfileError) -> Any:
    if isinstance(obj, dict):
        return obj
    if isinstance(obj, InvalidRequestError):
        return _serialize_invalid_request_error(obj)
    if isinstance(obj, ProfileSettingsNotFoundError):
        return _serialize_profile_settings_not_found_error(obj)


def _deserialize_evaluate_checkout_profile_error(obj: Any) -> EvaluateCheckoutProfileError:
    try:
        return _deserialize_invalid_request_error(obj)
    except Exception:
        pass
    try:
        return _deserialize_profile_settings_not_found_error(obj)
    except Exception:
        pass
    raise ValueError(f"{repr(obj)} is not EvaluateCheckoutProfileError")
