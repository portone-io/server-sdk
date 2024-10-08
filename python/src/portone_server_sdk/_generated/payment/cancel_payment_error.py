from __future__ import annotations
from typing import Any, Optional, Union
from portone_server_sdk._generated.payment.cancel_amount_exceeds_cancellable_amount_error import CancelAmountExceedsCancellableAmountError, _deserialize_cancel_amount_exceeds_cancellable_amount_error, _serialize_cancel_amount_exceeds_cancellable_amount_error
from portone_server_sdk._generated.payment.cancel_tax_amount_exceeds_cancellable_tax_amount_error import CancelTaxAmountExceedsCancellableTaxAmountError, _deserialize_cancel_tax_amount_exceeds_cancellable_tax_amount_error, _serialize_cancel_tax_amount_exceeds_cancellable_tax_amount_error
from portone_server_sdk._generated.payment.cancel_tax_free_amount_exceeds_cancellable_tax_free_amount_error import CancelTaxFreeAmountExceedsCancellableTaxFreeAmountError, _deserialize_cancel_tax_free_amount_exceeds_cancellable_tax_free_amount_error, _serialize_cancel_tax_free_amount_exceeds_cancellable_tax_free_amount_error
from portone_server_sdk._generated.payment.cancellable_amount_consistency_broken_error import CancellableAmountConsistencyBrokenError, _deserialize_cancellable_amount_consistency_broken_error, _serialize_cancellable_amount_consistency_broken_error
from portone_server_sdk._generated.common.forbidden_error import ForbiddenError, _deserialize_forbidden_error, _serialize_forbidden_error
from portone_server_sdk._generated.common.invalid_request_error import InvalidRequestError, _deserialize_invalid_request_error, _serialize_invalid_request_error
from portone_server_sdk._generated.payment.payment_already_cancelled_error import PaymentAlreadyCancelledError, _deserialize_payment_already_cancelled_error, _serialize_payment_already_cancelled_error
from portone_server_sdk._generated.payment.payment_not_found_error import PaymentNotFoundError, _deserialize_payment_not_found_error, _serialize_payment_not_found_error
from portone_server_sdk._generated.payment.payment_not_paid_error import PaymentNotPaidError, _deserialize_payment_not_paid_error, _serialize_payment_not_paid_error
from portone_server_sdk._generated.common.pg_provider_error import PgProviderError, _deserialize_pg_provider_error, _serialize_pg_provider_error
from portone_server_sdk._generated.payment.remained_amount_less_than_promotion_min_payment_amount_error import RemainedAmountLessThanPromotionMinPaymentAmountError, _deserialize_remained_amount_less_than_promotion_min_payment_amount_error, _serialize_remained_amount_less_than_promotion_min_payment_amount_error
from portone_server_sdk._generated.payment.sum_of_parts_exceeds_cancel_amount_error import SumOfPartsExceedsCancelAmountError, _deserialize_sum_of_parts_exceeds_cancel_amount_error, _serialize_sum_of_parts_exceeds_cancel_amount_error
from portone_server_sdk._generated.common.unauthorized_error import UnauthorizedError, _deserialize_unauthorized_error, _serialize_unauthorized_error

CancelPaymentError = Union[CancellableAmountConsistencyBrokenError, CancelAmountExceedsCancellableAmountError, CancelTaxAmountExceedsCancellableTaxAmountError, CancelTaxFreeAmountExceedsCancellableTaxFreeAmountError, ForbiddenError, InvalidRequestError, PaymentAlreadyCancelledError, PaymentNotFoundError, PaymentNotPaidError, PgProviderError, RemainedAmountLessThanPromotionMinPaymentAmountError, SumOfPartsExceedsCancelAmountError, UnauthorizedError]


def _serialize_cancel_payment_error(obj: CancelPaymentError) -> Any:
    if obj.type == "CANCELLABLE_AMOUNT_CONSISTENCY_BROKEN":
        return _serialize_cancellable_amount_consistency_broken_error(obj)
    if obj.type == "CANCEL_AMOUNT_EXCEEDS_CANCELLABLE_AMOUNT":
        return _serialize_cancel_amount_exceeds_cancellable_amount_error(obj)
    if obj.type == "CANCEL_TAX_AMOUNT_EXCEEDS_CANCELLABLE_TAX_AMOUNT":
        return _serialize_cancel_tax_amount_exceeds_cancellable_tax_amount_error(obj)
    if obj.type == "CANCEL_TAX_FREE_AMOUNT_EXCEEDS_CANCELLABLE_TAX_FREE_AMOUNT":
        return _serialize_cancel_tax_free_amount_exceeds_cancellable_tax_free_amount_error(obj)
    if obj.type == "FORBIDDEN":
        return _serialize_forbidden_error(obj)
    if obj.type == "INVALID_REQUEST":
        return _serialize_invalid_request_error(obj)
    if obj.type == "PAYMENT_ALREADY_CANCELLED":
        return _serialize_payment_already_cancelled_error(obj)
    if obj.type == "PAYMENT_NOT_FOUND":
        return _serialize_payment_not_found_error(obj)
    if obj.type == "PAYMENT_NOT_PAID":
        return _serialize_payment_not_paid_error(obj)
    if obj.type == "PG_PROVIDER":
        return _serialize_pg_provider_error(obj)
    if obj.type == "REMAINED_AMOUNT_LESS_THAN_PROMOTION_MIN_PAYMENT_AMOUNT":
        return _serialize_remained_amount_less_than_promotion_min_payment_amount_error(obj)
    if obj.type == "SUM_OF_PARTS_EXCEEDS_CANCEL_AMOUNT":
        return _serialize_sum_of_parts_exceeds_cancel_amount_error(obj)
    if obj.type == "UNAUTHORIZED":
        return _serialize_unauthorized_error(obj)


def _deserialize_cancel_payment_error(obj: Any) -> CancelPaymentError:
    try:
        return _deserialize_cancellable_amount_consistency_broken_error(obj)
    except Exception:
        pass
    try:
        return _deserialize_cancel_amount_exceeds_cancellable_amount_error(obj)
    except Exception:
        pass
    try:
        return _deserialize_cancel_tax_amount_exceeds_cancellable_tax_amount_error(obj)
    except Exception:
        pass
    try:
        return _deserialize_cancel_tax_free_amount_exceeds_cancellable_tax_free_amount_error(obj)
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
        return _deserialize_payment_already_cancelled_error(obj)
    except Exception:
        pass
    try:
        return _deserialize_payment_not_found_error(obj)
    except Exception:
        pass
    try:
        return _deserialize_payment_not_paid_error(obj)
    except Exception:
        pass
    try:
        return _deserialize_pg_provider_error(obj)
    except Exception:
        pass
    try:
        return _deserialize_remained_amount_less_than_promotion_min_payment_amount_error(obj)
    except Exception:
        pass
    try:
        return _deserialize_sum_of_parts_exceeds_cancel_amount_error(obj)
    except Exception:
        pass
    try:
        return _deserialize_unauthorized_error(obj)
    except Exception:
        pass
    raise ValueError(f"{repr(obj)} is not CancelPaymentError")
