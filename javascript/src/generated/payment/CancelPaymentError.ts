import type { CancelAmountExceedsCancellableAmountError } from "#generated/payment/CancelAmountExceedsCancellableAmountError"
import type { CancelTaxAmountExceedsCancellableTaxAmountError } from "#generated/payment/CancelTaxAmountExceedsCancellableTaxAmountError"
import type { CancelTaxFreeAmountExceedsCancellableTaxFreeAmountError } from "#generated/payment/CancelTaxFreeAmountExceedsCancellableTaxFreeAmountError"
import type { CancellableAmountConsistencyBrokenError } from "#generated/payment/CancellableAmountConsistencyBrokenError"
import type { ForbiddenError } from "#generated/common/ForbiddenError"
import type { InvalidRequestError } from "#generated/common/InvalidRequestError"
import type { PaymentAlreadyCancelledError } from "#generated/payment/PaymentAlreadyCancelledError"
import type { PaymentNotFoundError } from "#generated/payment/PaymentNotFoundError"
import type { PaymentNotPaidError } from "#generated/payment/PaymentNotPaidError"
import type { PgProviderError } from "#generated/common/PgProviderError"
import type { RemainedAmountLessThanPromotionMinPaymentAmountError } from "#generated/payment/RemainedAmountLessThanPromotionMinPaymentAmountError"
import type { SumOfPartsExceedsCancelAmountError } from "#generated/payment/SumOfPartsExceedsCancelAmountError"
import type { UnauthorizedError } from "#generated/common/UnauthorizedError"

export type CancelPaymentError =
	| CancellableAmountConsistencyBrokenError
	| CancelAmountExceedsCancellableAmountError
	| CancelTaxAmountExceedsCancellableTaxAmountError
	| CancelTaxFreeAmountExceedsCancellableTaxFreeAmountError
	| ForbiddenError
	| InvalidRequestError
	| PaymentAlreadyCancelledError
	| PaymentNotFoundError
	| PaymentNotPaidError
	| PgProviderError
	| RemainedAmountLessThanPromotionMinPaymentAmountError
	| SumOfPartsExceedsCancelAmountError
	| UnauthorizedError
