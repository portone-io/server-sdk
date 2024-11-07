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
