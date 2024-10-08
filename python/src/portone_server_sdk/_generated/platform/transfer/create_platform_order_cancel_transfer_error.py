from __future__ import annotations
from typing import Any, Optional, Union
from portone_server_sdk._generated.common.forbidden_error import ForbiddenError, _deserialize_forbidden_error, _serialize_forbidden_error
from portone_server_sdk._generated.common.invalid_request_error import InvalidRequestError, _deserialize_invalid_request_error, _serialize_invalid_request_error
from portone_server_sdk._generated.platform.transfer.platform_cancellable_amount_exceeded_error import PlatformCancellableAmountExceededError, _deserialize_platform_cancellable_amount_exceeded_error, _serialize_platform_cancellable_amount_exceeded_error
from portone_server_sdk._generated.platform.transfer.platform_cancellable_discount_amount_exceeded_error import PlatformCancellableDiscountAmountExceededError, _deserialize_platform_cancellable_discount_amount_exceeded_error, _serialize_platform_cancellable_discount_amount_exceeded_error
from portone_server_sdk._generated.platform.transfer.platform_cancellable_discount_tax_free_amount_exceeded_error import PlatformCancellableDiscountTaxFreeAmountExceededError, _deserialize_platform_cancellable_discount_tax_free_amount_exceeded_error, _serialize_platform_cancellable_discount_tax_free_amount_exceeded_error
from portone_server_sdk._generated.platform.transfer.platform_cancellable_product_quantity_exceeded_error import PlatformCancellableProductQuantityExceededError, _deserialize_platform_cancellable_product_quantity_exceeded_error, _serialize_platform_cancellable_product_quantity_exceeded_error
from portone_server_sdk._generated.platform.transfer.platform_cancellation_and_payment_type_mismatched_error import PlatformCancellationAndPaymentTypeMismatchedError, _deserialize_platform_cancellation_and_payment_type_mismatched_error, _serialize_platform_cancellation_and_payment_type_mismatched_error
from portone_server_sdk._generated.platform.transfer.platform_cancellation_not_found_error import PlatformCancellationNotFoundError, _deserialize_platform_cancellation_not_found_error, _serialize_platform_cancellation_not_found_error
from portone_server_sdk._generated.platform.transfer.platform_cannot_specify_transfer_error import PlatformCannotSpecifyTransferError, _deserialize_platform_cannot_specify_transfer_error, _serialize_platform_cannot_specify_transfer_error
from portone_server_sdk._generated.platform.transfer.platform_discount_share_policy_id_duplicated_error import PlatformDiscountSharePolicyIdDuplicatedError, _deserialize_platform_discount_share_policy_id_duplicated_error, _serialize_platform_discount_share_policy_id_duplicated_error
from portone_server_sdk._generated.platform.platform_not_enabled_error import PlatformNotEnabledError, _deserialize_platform_not_enabled_error, _serialize_platform_not_enabled_error
from portone_server_sdk._generated.platform.transfer.platform_order_detail_mismatched_error import PlatformOrderDetailMismatchedError, _deserialize_platform_order_detail_mismatched_error, _serialize_platform_order_detail_mismatched_error
from portone_server_sdk._generated.platform.transfer.platform_order_transfer_already_cancelled_error import PlatformOrderTransferAlreadyCancelledError, _deserialize_platform_order_transfer_already_cancelled_error, _serialize_platform_order_transfer_already_cancelled_error
from portone_server_sdk._generated.platform.transfer.platform_payment_not_found_error import PlatformPaymentNotFoundError, _deserialize_platform_payment_not_found_error, _serialize_platform_payment_not_found_error
from portone_server_sdk._generated.platform.transfer.platform_product_id_duplicated_error import PlatformProductIdDuplicatedError, _deserialize_platform_product_id_duplicated_error, _serialize_platform_product_id_duplicated_error
from portone_server_sdk._generated.platform.transfer.platform_product_id_not_found_error import PlatformProductIdNotFoundError, _deserialize_platform_product_id_not_found_error, _serialize_platform_product_id_not_found_error
from portone_server_sdk._generated.platform.transfer.platform_settlement_amount_exceeded_error import PlatformSettlementAmountExceededError, _deserialize_platform_settlement_amount_exceeded_error, _serialize_platform_settlement_amount_exceeded_error
from portone_server_sdk._generated.platform.transfer.platform_settlement_cancel_amount_exceeded_port_one_cancel_error import PlatformSettlementCancelAmountExceededPortOneCancelError, _deserialize_platform_settlement_cancel_amount_exceeded_port_one_cancel_error, _serialize_platform_settlement_cancel_amount_exceeded_port_one_cancel_error
from portone_server_sdk._generated.platform.transfer.platform_transfer_already_exists_error import PlatformTransferAlreadyExistsError, _deserialize_platform_transfer_already_exists_error, _serialize_platform_transfer_already_exists_error
from portone_server_sdk._generated.platform.transfer.platform_transfer_discount_share_policy_not_found_error import PlatformTransferDiscountSharePolicyNotFoundError, _deserialize_platform_transfer_discount_share_policy_not_found_error, _serialize_platform_transfer_discount_share_policy_not_found_error
from portone_server_sdk._generated.platform.transfer.platform_transfer_not_found_error import PlatformTransferNotFoundError, _deserialize_platform_transfer_not_found_error, _serialize_platform_transfer_not_found_error
from portone_server_sdk._generated.platform.platform_user_defined_property_not_found_error import PlatformUserDefinedPropertyNotFoundError, _deserialize_platform_user_defined_property_not_found_error, _serialize_platform_user_defined_property_not_found_error
from portone_server_sdk._generated.common.unauthorized_error import UnauthorizedError, _deserialize_unauthorized_error, _serialize_unauthorized_error

CreatePlatformOrderCancelTransferError = Union[ForbiddenError, InvalidRequestError, PlatformCancellableAmountExceededError, PlatformCancellableDiscountAmountExceededError, PlatformCancellableDiscountTaxFreeAmountExceededError, PlatformCancellableProductQuantityExceededError, PlatformCancellationAndPaymentTypeMismatchedError, PlatformCancellationNotFoundError, PlatformCannotSpecifyTransferError, PlatformDiscountSharePolicyIdDuplicatedError, PlatformNotEnabledError, PlatformOrderDetailMismatchedError, PlatformOrderTransferAlreadyCancelledError, PlatformPaymentNotFoundError, PlatformProductIdDuplicatedError, PlatformProductIdNotFoundError, PlatformSettlementAmountExceededError, PlatformSettlementCancelAmountExceededPortOneCancelError, PlatformTransferAlreadyExistsError, PlatformTransferDiscountSharePolicyNotFoundError, PlatformTransferNotFoundError, PlatformUserDefinedPropertyNotFoundError, UnauthorizedError]


def _serialize_create_platform_order_cancel_transfer_error(obj: CreatePlatformOrderCancelTransferError) -> Any:
    if obj.type == "FORBIDDEN":
        return _serialize_forbidden_error(obj)
    if obj.type == "INVALID_REQUEST":
        return _serialize_invalid_request_error(obj)
    if obj.type == "PLATFORM_CANCELLABLE_AMOUNT_EXCEEDED":
        return _serialize_platform_cancellable_amount_exceeded_error(obj)
    if obj.type == "PLATFORM_CANCELLABLE_DISCOUNT_AMOUNT_EXCEEDED":
        return _serialize_platform_cancellable_discount_amount_exceeded_error(obj)
    if obj.type == "PLATFORM_CANCELLABLE_DISCOUNT_TAX_FREE_AMOUNT_EXCEEDED":
        return _serialize_platform_cancellable_discount_tax_free_amount_exceeded_error(obj)
    if obj.type == "PLATFORM_CANCELLABLE_PRODUCT_QUANTITY_EXCEEDED":
        return _serialize_platform_cancellable_product_quantity_exceeded_error(obj)
    if obj.type == "PLATFORM_CANCELLATION_AND_PAYMENT_TYPE_MISMATCHED":
        return _serialize_platform_cancellation_and_payment_type_mismatched_error(obj)
    if obj.type == "PLATFORM_CANCELLATION_NOT_FOUND":
        return _serialize_platform_cancellation_not_found_error(obj)
    if obj.type == "PLATFORM_CANNOT_SPECIFY_TRANSFER":
        return _serialize_platform_cannot_specify_transfer_error(obj)
    if obj.type == "PLATFORM_DISCOUNT_SHARE_POLICY_ID_DUPLICATED":
        return _serialize_platform_discount_share_policy_id_duplicated_error(obj)
    if obj.type == "PLATFORM_NOT_ENABLED":
        return _serialize_platform_not_enabled_error(obj)
    if obj.type == "PLATFORM_ORDER_DETAIL_MISMATCHED":
        return _serialize_platform_order_detail_mismatched_error(obj)
    if obj.type == "PLATFORM_ORDER_TRANSFER_ALREADY_CANCELLED":
        return _serialize_platform_order_transfer_already_cancelled_error(obj)
    if obj.type == "PLATFORM_PAYMENT_NOT_FOUND":
        return _serialize_platform_payment_not_found_error(obj)
    if obj.type == "PLATFORM_PRODUCT_ID_DUPLICATED":
        return _serialize_platform_product_id_duplicated_error(obj)
    if obj.type == "PLATFORM_PRODUCT_ID_NOT_FOUND":
        return _serialize_platform_product_id_not_found_error(obj)
    if obj.type == "PLATFORM_SETTLEMENT_AMOUNT_EXCEEDED":
        return _serialize_platform_settlement_amount_exceeded_error(obj)
    if obj.type == "PLATFORM_SETTLEMENT_CANCEL_AMOUNT_EXCEEDED_PORT_ONE_CANCEL":
        return _serialize_platform_settlement_cancel_amount_exceeded_port_one_cancel_error(obj)
    if obj.type == "PLATFORM_TRANSFER_ALREADY_EXISTS":
        return _serialize_platform_transfer_already_exists_error(obj)
    if obj.type == "PLATFORM_TRANSFER_DISCOUNT_SHARE_POLICY_NOT_FOUND":
        return _serialize_platform_transfer_discount_share_policy_not_found_error(obj)
    if obj.type == "PLATFORM_TRANSFER_NOT_FOUND":
        return _serialize_platform_transfer_not_found_error(obj)
    if obj.type == "PLATFORM_USER_DEFINED_PROPERTY_NOT_FOUND":
        return _serialize_platform_user_defined_property_not_found_error(obj)
    if obj.type == "UNAUTHORIZED":
        return _serialize_unauthorized_error(obj)


def _deserialize_create_platform_order_cancel_transfer_error(obj: Any) -> CreatePlatformOrderCancelTransferError:
    try:
        return _deserialize_forbidden_error(obj)
    except Exception:
        pass
    try:
        return _deserialize_invalid_request_error(obj)
    except Exception:
        pass
    try:
        return _deserialize_platform_cancellable_amount_exceeded_error(obj)
    except Exception:
        pass
    try:
        return _deserialize_platform_cancellable_discount_amount_exceeded_error(obj)
    except Exception:
        pass
    try:
        return _deserialize_platform_cancellable_discount_tax_free_amount_exceeded_error(obj)
    except Exception:
        pass
    try:
        return _deserialize_platform_cancellable_product_quantity_exceeded_error(obj)
    except Exception:
        pass
    try:
        return _deserialize_platform_cancellation_and_payment_type_mismatched_error(obj)
    except Exception:
        pass
    try:
        return _deserialize_platform_cancellation_not_found_error(obj)
    except Exception:
        pass
    try:
        return _deserialize_platform_cannot_specify_transfer_error(obj)
    except Exception:
        pass
    try:
        return _deserialize_platform_discount_share_policy_id_duplicated_error(obj)
    except Exception:
        pass
    try:
        return _deserialize_platform_not_enabled_error(obj)
    except Exception:
        pass
    try:
        return _deserialize_platform_order_detail_mismatched_error(obj)
    except Exception:
        pass
    try:
        return _deserialize_platform_order_transfer_already_cancelled_error(obj)
    except Exception:
        pass
    try:
        return _deserialize_platform_payment_not_found_error(obj)
    except Exception:
        pass
    try:
        return _deserialize_platform_product_id_duplicated_error(obj)
    except Exception:
        pass
    try:
        return _deserialize_platform_product_id_not_found_error(obj)
    except Exception:
        pass
    try:
        return _deserialize_platform_settlement_amount_exceeded_error(obj)
    except Exception:
        pass
    try:
        return _deserialize_platform_settlement_cancel_amount_exceeded_port_one_cancel_error(obj)
    except Exception:
        pass
    try:
        return _deserialize_platform_transfer_already_exists_error(obj)
    except Exception:
        pass
    try:
        return _deserialize_platform_transfer_discount_share_policy_not_found_error(obj)
    except Exception:
        pass
    try:
        return _deserialize_platform_transfer_not_found_error(obj)
    except Exception:
        pass
    try:
        return _deserialize_platform_user_defined_property_not_found_error(obj)
    except Exception:
        pass
    try:
        return _deserialize_unauthorized_error(obj)
    except Exception:
        pass
    raise ValueError(f"{repr(obj)} is not CreatePlatformOrderCancelTransferError")
