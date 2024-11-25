import type { Unrecognized } from "./../../../utils/unrecognized"
import type { ForbiddenError } from "./../../common/ForbiddenError"
import type { InvalidRequestError } from "./../../common/InvalidRequestError"
import type { PlatformCancellableAmountExceededError } from "./../../platform/transfer/PlatformCancellableAmountExceededError"
import type { PlatformCancellableDiscountAmountExceededError } from "./../../platform/transfer/PlatformCancellableDiscountAmountExceededError"
import type { PlatformCancellableDiscountTaxFreeAmountExceededError } from "./../../platform/transfer/PlatformCancellableDiscountTaxFreeAmountExceededError"
import type { PlatformCancellableProductQuantityExceededError } from "./../../platform/transfer/PlatformCancellableProductQuantityExceededError"
import type { PlatformCancellationAndPaymentTypeMismatchedError } from "./../../platform/transfer/PlatformCancellationAndPaymentTypeMismatchedError"
import type { PlatformCancellationNotFoundError } from "./../../platform/transfer/PlatformCancellationNotFoundError"
import type { PlatformCannotSpecifyTransferError } from "./../../platform/transfer/PlatformCannotSpecifyTransferError"
import type { PlatformDiscountSharePolicyIdDuplicatedError } from "./../../platform/transfer/PlatformDiscountSharePolicyIdDuplicatedError"
import type { PlatformNotEnabledError } from "./../../platform/PlatformNotEnabledError"
import type { PlatformOrderDetailMismatchedError } from "./../../platform/transfer/PlatformOrderDetailMismatchedError"
import type { PlatformOrderTransferAlreadyCancelledError } from "./../../platform/transfer/PlatformOrderTransferAlreadyCancelledError"
import type { PlatformPaymentNotFoundError } from "./../../platform/transfer/PlatformPaymentNotFoundError"
import type { PlatformProductIdDuplicatedError } from "./../../platform/transfer/PlatformProductIdDuplicatedError"
import type { PlatformProductIdNotFoundError } from "./../../platform/transfer/PlatformProductIdNotFoundError"
import type { PlatformSettlementAmountExceededError } from "./../../platform/transfer/PlatformSettlementAmountExceededError"
import type { PlatformSettlementCancelAmountExceededPortOneCancelError } from "./../../platform/transfer/PlatformSettlementCancelAmountExceededPortOneCancelError"
import type { PlatformTransferAlreadyExistsError } from "./../../platform/transfer/PlatformTransferAlreadyExistsError"
import type { PlatformTransferDiscountSharePolicyNotFoundError } from "./../../platform/transfer/PlatformTransferDiscountSharePolicyNotFoundError"
import type { PlatformTransferNotFoundError } from "./../../platform/transfer/PlatformTransferNotFoundError"
import type { PlatformUserDefinedPropertyNotFoundError } from "./../../platform/PlatformUserDefinedPropertyNotFoundError"
import type { UnauthorizedError } from "./../../common/UnauthorizedError"
export type CreatePlatformOrderCancelTransferError =
	| ForbiddenError
	| InvalidRequestError
	| PlatformCancellableAmountExceededError
	| PlatformCancellableDiscountAmountExceededError
	| PlatformCancellableDiscountTaxFreeAmountExceededError
	| PlatformCancellableProductQuantityExceededError
	| PlatformCancellationAndPaymentTypeMismatchedError
	| PlatformCancellationNotFoundError
	| PlatformCannotSpecifyTransferError
	| PlatformDiscountSharePolicyIdDuplicatedError
	| PlatformNotEnabledError
	| PlatformOrderDetailMismatchedError
	| PlatformOrderTransferAlreadyCancelledError
	| PlatformPaymentNotFoundError
	| PlatformProductIdDuplicatedError
	| PlatformProductIdNotFoundError
	| PlatformSettlementAmountExceededError
	| PlatformSettlementCancelAmountExceededPortOneCancelError
	| PlatformTransferAlreadyExistsError
	| PlatformTransferDiscountSharePolicyNotFoundError
	| PlatformTransferNotFoundError
	| PlatformUserDefinedPropertyNotFoundError
	| UnauthorizedError
	| { readonly type: Unrecognized }

export function isUnrecognizedCreatePlatformOrderCancelTransferError(entity: CreatePlatformOrderCancelTransferError): entity is { readonly type: Unrecognized } {
	return entity.type !== "FORBIDDEN"
		&& entity.type !== "INVALID_REQUEST"
		&& entity.type !== "PLATFORM_CANCELLABLE_AMOUNT_EXCEEDED"
		&& entity.type !== "PLATFORM_CANCELLABLE_DISCOUNT_AMOUNT_EXCEEDED"
		&& entity.type !== "PLATFORM_CANCELLABLE_DISCOUNT_TAX_FREE_AMOUNT_EXCEEDED"
		&& entity.type !== "PLATFORM_CANCELLABLE_PRODUCT_QUANTITY_EXCEEDED"
		&& entity.type !== "PLATFORM_CANCELLATION_AND_PAYMENT_TYPE_MISMATCHED"
		&& entity.type !== "PLATFORM_CANCELLATION_NOT_FOUND"
		&& entity.type !== "PLATFORM_CANNOT_SPECIFY_TRANSFER"
		&& entity.type !== "PLATFORM_DISCOUNT_SHARE_POLICY_ID_DUPLICATED"
		&& entity.type !== "PLATFORM_NOT_ENABLED"
		&& entity.type !== "PLATFORM_ORDER_DETAIL_MISMATCHED"
		&& entity.type !== "PLATFORM_ORDER_TRANSFER_ALREADY_CANCELLED"
		&& entity.type !== "PLATFORM_PAYMENT_NOT_FOUND"
		&& entity.type !== "PLATFORM_PRODUCT_ID_DUPLICATED"
		&& entity.type !== "PLATFORM_PRODUCT_ID_NOT_FOUND"
		&& entity.type !== "PLATFORM_SETTLEMENT_AMOUNT_EXCEEDED"
		&& entity.type !== "PLATFORM_SETTLEMENT_CANCEL_AMOUNT_EXCEEDED_PORT_ONE_CANCEL"
		&& entity.type !== "PLATFORM_TRANSFER_ALREADY_EXISTS"
		&& entity.type !== "PLATFORM_TRANSFER_DISCOUNT_SHARE_POLICY_NOT_FOUND"
		&& entity.type !== "PLATFORM_TRANSFER_NOT_FOUND"
		&& entity.type !== "PLATFORM_USER_DEFINED_PROPERTY_NOT_FOUND"
		&& entity.type !== "UNAUTHORIZED"
}
