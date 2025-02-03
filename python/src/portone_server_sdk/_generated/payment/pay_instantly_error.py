from __future__ import annotations
from typing import Any, Optional, Union
from ..payment.already_paid_error import AlreadyPaidError, _deserialize_already_paid_error, _serialize_already_paid_error
from ..common.channel_not_found_error import ChannelNotFoundError, _deserialize_channel_not_found_error, _serialize_channel_not_found_error
from ..payment.discount_amount_exceeds_total_amount_error import DiscountAmountExceedsTotalAmountError, _deserialize_discount_amount_exceeds_total_amount_error, _serialize_discount_amount_exceeds_total_amount_error
from ..common.forbidden_error import ForbiddenError, _deserialize_forbidden_error, _serialize_forbidden_error
from ..common.invalid_request_error import InvalidRequestError, _deserialize_invalid_request_error, _serialize_invalid_request_error
from ..common.max_transaction_count_reached_error import MaxTransactionCountReachedError, _deserialize_max_transaction_count_reached_error, _serialize_max_transaction_count_reached_error
from ..common.payment_schedule_already_exists_error import PaymentScheduleAlreadyExistsError, _deserialize_payment_schedule_already_exists_error, _serialize_payment_schedule_already_exists_error
from ..common.pg_provider_error import PgProviderError, _deserialize_pg_provider_error, _serialize_pg_provider_error
from ..payment.promotion_pay_method_does_not_match_error import PromotionPayMethodDoesNotMatchError, _deserialize_promotion_pay_method_does_not_match_error, _serialize_promotion_pay_method_does_not_match_error
from ..common.sum_of_parts_exceeds_total_amount_error import SumOfPartsExceedsTotalAmountError, _deserialize_sum_of_parts_exceeds_total_amount_error, _serialize_sum_of_parts_exceeds_total_amount_error
from ..common.unauthorized_error import UnauthorizedError, _deserialize_unauthorized_error, _serialize_unauthorized_error

PayInstantlyError = Union[AlreadyPaidError, ChannelNotFoundError, DiscountAmountExceedsTotalAmountError, ForbiddenError, InvalidRequestError, MaxTransactionCountReachedError, PaymentScheduleAlreadyExistsError, PgProviderError, PromotionPayMethodDoesNotMatchError, SumOfPartsExceedsTotalAmountError, UnauthorizedError, dict]


def _serialize_pay_instantly_error(obj: PayInstantlyError) -> Any:
    if isinstance(obj, dict):
        return obj
    if isinstance(obj, AlreadyPaidError):
        return _serialize_already_paid_error(obj)
    if isinstance(obj, ChannelNotFoundError):
        return _serialize_channel_not_found_error(obj)
    if isinstance(obj, DiscountAmountExceedsTotalAmountError):
        return _serialize_discount_amount_exceeds_total_amount_error(obj)
    if isinstance(obj, ForbiddenError):
        return _serialize_forbidden_error(obj)
    if isinstance(obj, InvalidRequestError):
        return _serialize_invalid_request_error(obj)
    if isinstance(obj, MaxTransactionCountReachedError):
        return _serialize_max_transaction_count_reached_error(obj)
    if isinstance(obj, PaymentScheduleAlreadyExistsError):
        return _serialize_payment_schedule_already_exists_error(obj)
    if isinstance(obj, PgProviderError):
        return _serialize_pg_provider_error(obj)
    if isinstance(obj, PromotionPayMethodDoesNotMatchError):
        return _serialize_promotion_pay_method_does_not_match_error(obj)
    if isinstance(obj, SumOfPartsExceedsTotalAmountError):
        return _serialize_sum_of_parts_exceeds_total_amount_error(obj)
    if isinstance(obj, UnauthorizedError):
        return _serialize_unauthorized_error(obj)


def _deserialize_pay_instantly_error(obj: Any) -> PayInstantlyError:
    try:
        return _deserialize_already_paid_error(obj)
    except Exception:
        pass
    try:
        return _deserialize_channel_not_found_error(obj)
    except Exception:
        pass
    try:
        return _deserialize_discount_amount_exceeds_total_amount_error(obj)
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
        return _deserialize_max_transaction_count_reached_error(obj)
    except Exception:
        pass
    try:
        return _deserialize_payment_schedule_already_exists_error(obj)
    except Exception:
        pass
    try:
        return _deserialize_pg_provider_error(obj)
    except Exception:
        pass
    try:
        return _deserialize_promotion_pay_method_does_not_match_error(obj)
    except Exception:
        pass
    try:
        return _deserialize_sum_of_parts_exceeds_total_amount_error(obj)
    except Exception:
        pass
    try:
        return _deserialize_unauthorized_error(obj)
    except Exception:
        pass
    raise ValueError(f"{repr(obj)} is not PayInstantlyError")
