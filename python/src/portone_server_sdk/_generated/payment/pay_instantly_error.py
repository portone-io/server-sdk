from __future__ import annotations
from typing import Any, Optional, Union
from portone_server_sdk._generated.payment.already_paid_error import AlreadyPaidError, _deserialize_already_paid_error, _serialize_already_paid_error
from portone_server_sdk._generated.common.channel_not_found_error import ChannelNotFoundError, _deserialize_channel_not_found_error, _serialize_channel_not_found_error
from portone_server_sdk._generated.payment.discount_amount_exceeds_total_amount_error import DiscountAmountExceedsTotalAmountError, _deserialize_discount_amount_exceeds_total_amount_error, _serialize_discount_amount_exceeds_total_amount_error
from portone_server_sdk._generated.common.forbidden_error import ForbiddenError, _deserialize_forbidden_error, _serialize_forbidden_error
from portone_server_sdk._generated.common.invalid_request_error import InvalidRequestError, _deserialize_invalid_request_error, _serialize_invalid_request_error
from portone_server_sdk._generated.common.max_transaction_count_reached_error import MaxTransactionCountReachedError, _deserialize_max_transaction_count_reached_error, _serialize_max_transaction_count_reached_error
from portone_server_sdk._generated.common.pg_provider_error import PgProviderError, _deserialize_pg_provider_error, _serialize_pg_provider_error
from portone_server_sdk._generated.payment.promotion_pay_method_does_not_match_error import PromotionPayMethodDoesNotMatchError, _deserialize_promotion_pay_method_does_not_match_error, _serialize_promotion_pay_method_does_not_match_error
from portone_server_sdk._generated.common.sum_of_parts_exceeds_total_amount_error import SumOfPartsExceedsTotalAmountError, _deserialize_sum_of_parts_exceeds_total_amount_error, _serialize_sum_of_parts_exceeds_total_amount_error
from portone_server_sdk._generated.common.unauthorized_error import UnauthorizedError, _deserialize_unauthorized_error, _serialize_unauthorized_error

PayInstantlyError = Union[AlreadyPaidError, ChannelNotFoundError, DiscountAmountExceedsTotalAmountError, ForbiddenError, InvalidRequestError, MaxTransactionCountReachedError, PgProviderError, PromotionPayMethodDoesNotMatchError, SumOfPartsExceedsTotalAmountError, UnauthorizedError]


def _serialize_pay_instantly_error(obj: PayInstantlyError) -> Any:
    if obj.type == "ALREADY_PAID":
        return _serialize_already_paid_error(obj)
    if obj.type == "CHANNEL_NOT_FOUND":
        return _serialize_channel_not_found_error(obj)
    if obj.type == "DISCOUNT_AMOUNT_EXCEEDS_TOTAL_AMOUNT":
        return _serialize_discount_amount_exceeds_total_amount_error(obj)
    if obj.type == "FORBIDDEN":
        return _serialize_forbidden_error(obj)
    if obj.type == "INVALID_REQUEST":
        return _serialize_invalid_request_error(obj)
    if obj.type == "MAX_TRANSACTION_COUNT_REACHED":
        return _serialize_max_transaction_count_reached_error(obj)
    if obj.type == "PG_PROVIDER":
        return _serialize_pg_provider_error(obj)
    if obj.type == "PROMOTION_PAY_METHOD_DOES_NOT_MATCH":
        return _serialize_promotion_pay_method_does_not_match_error(obj)
    if obj.type == "SUM_OF_PARTS_EXCEEDS_TOTAL_AMOUNT":
        return _serialize_sum_of_parts_exceeds_total_amount_error(obj)
    if obj.type == "UNAUTHORIZED":
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