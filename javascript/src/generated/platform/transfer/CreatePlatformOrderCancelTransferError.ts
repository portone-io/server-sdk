import type { ForbiddenError } from "#generated/common/ForbiddenError"
import type { InvalidRequestError } from "#generated/common/InvalidRequestError"
import type { PlatformCancellableAmountExceededError } from "#generated/platform/transfer/PlatformCancellableAmountExceededError"
import type { PlatformCancellableDiscountAmountExceededError } from "#generated/platform/transfer/PlatformCancellableDiscountAmountExceededError"
import type { PlatformCancellableDiscountTaxFreeAmountExceededError } from "#generated/platform/transfer/PlatformCancellableDiscountTaxFreeAmountExceededError"
import type { PlatformCancellableProductQuantityExceededError } from "#generated/platform/transfer/PlatformCancellableProductQuantityExceededError"
import type { PlatformCancellationAndPaymentTypeMismatchedError } from "#generated/platform/transfer/PlatformCancellationAndPaymentTypeMismatchedError"
import type { PlatformCancellationNotFoundError } from "#generated/platform/transfer/PlatformCancellationNotFoundError"
import type { PlatformCannotSpecifyTransferError } from "#generated/platform/transfer/PlatformCannotSpecifyTransferError"
import type { PlatformDiscountSharePolicyIdDuplicatedError } from "#generated/platform/transfer/PlatformDiscountSharePolicyIdDuplicatedError"
import type { PlatformNotEnabledError } from "#generated/platform/PlatformNotEnabledError"
import type { PlatformOrderDetailMismatchedError } from "#generated/platform/transfer/PlatformOrderDetailMismatchedError"
import type { PlatformOrderTransferAlreadyCancelledError } from "#generated/platform/transfer/PlatformOrderTransferAlreadyCancelledError"
import type { PlatformPaymentNotFoundError } from "#generated/platform/transfer/PlatformPaymentNotFoundError"
import type { PlatformProductIdDuplicatedError } from "#generated/platform/transfer/PlatformProductIdDuplicatedError"
import type { PlatformProductIdNotFoundError } from "#generated/platform/transfer/PlatformProductIdNotFoundError"
import type { PlatformSettlementAmountExceededError } from "#generated/platform/transfer/PlatformSettlementAmountExceededError"
import type { PlatformSettlementCancelAmountExceededPortOneCancelError } from "#generated/platform/transfer/PlatformSettlementCancelAmountExceededPortOneCancelError"
import type { PlatformTransferAlreadyExistsError } from "#generated/platform/transfer/PlatformTransferAlreadyExistsError"
import type { PlatformTransferDiscountSharePolicyNotFoundError } from "#generated/platform/transfer/PlatformTransferDiscountSharePolicyNotFoundError"
import type { PlatformTransferNotFoundError } from "#generated/platform/transfer/PlatformTransferNotFoundError"
import type { PlatformUserDefinedPropertyNotFoundError } from "#generated/platform/PlatformUserDefinedPropertyNotFoundError"
import type { UnauthorizedError } from "#generated/common/UnauthorizedError"

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
