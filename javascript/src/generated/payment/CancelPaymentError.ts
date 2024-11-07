import type { CancelAmountExceedsCancellableAmountError } from "./../payment/CancelAmountExceedsCancellableAmountError"
import type { CancelTaxAmountExceedsCancellableTaxAmountError } from "./../payment/CancelTaxAmountExceedsCancellableTaxAmountError"
import type { CancelTaxFreeAmountExceedsCancellableTaxFreeAmountError } from "./../payment/CancelTaxFreeAmountExceedsCancellableTaxFreeAmountError"
import type { CancellableAmountConsistencyBrokenError } from "./../payment/CancellableAmountConsistencyBrokenError"
import type { ForbiddenError } from "./../common/ForbiddenError"
import type { InvalidRequestError } from "./../common/InvalidRequestError"
import type { PaymentAlreadyCancelledError } from "./../payment/PaymentAlreadyCancelledError"
import type { PaymentNotFoundError } from "./../payment/PaymentNotFoundError"
import type { PaymentNotPaidError } from "./../payment/PaymentNotPaidError"
import type { PgProviderError } from "./../common/PgProviderError"
import type { RemainedAmountLessThanPromotionMinPaymentAmountError } from "./../payment/RemainedAmountLessThanPromotionMinPaymentAmountError"
import type { SumOfPartsExceedsCancelAmountError } from "./../payment/SumOfPartsExceedsCancelAmountError"
import type { UnauthorizedError } from "./../common/UnauthorizedError"

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
