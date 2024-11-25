import type { Unrecognized } from "./../../utils/unrecognized"
import type { CancelAmountExceedsCancellableAmountError } from "./../payment/CancelAmountExceedsCancellableAmountError"
import type { CancelTaxAmountExceedsCancellableTaxAmountError } from "./../payment/CancelTaxAmountExceedsCancellableTaxAmountError"
import type { CancelTaxFreeAmountExceedsCancellableTaxFreeAmountError } from "./../payment/CancelTaxFreeAmountExceedsCancellableTaxFreeAmountError"
import type { CancellableAmountConsistencyBrokenError } from "./../payment/CancellableAmountConsistencyBrokenError"
import type { ForbiddenError } from "./../common/ForbiddenError"
import type { InvalidRequestError } from "./../common/InvalidRequestError"
import type { NegativePromotionAdjustedCancelAmountError } from "./../payment/NegativePromotionAdjustedCancelAmountError"
import type { PaymentAlreadyCancelledError } from "./../payment/PaymentAlreadyCancelledError"
import type { PaymentNotFoundError } from "./../payment/PaymentNotFoundError"
import type { PaymentNotPaidError } from "./../payment/PaymentNotPaidError"
import type { PgProviderError } from "./../common/PgProviderError"
import type { PromotionDiscountRetainOptionShouldNotBeChangedError } from "./../payment/PromotionDiscountRetainOptionShouldNotBeChangedError"
import type { SumOfPartsExceedsCancelAmountError } from "./../payment/SumOfPartsExceedsCancelAmountError"
import type { UnauthorizedError } from "./../common/UnauthorizedError"
export type CancelPaymentError =
	| CancellableAmountConsistencyBrokenError
	| CancelAmountExceedsCancellableAmountError
	| CancelTaxAmountExceedsCancellableTaxAmountError
	| CancelTaxFreeAmountExceedsCancellableTaxFreeAmountError
	| ForbiddenError
	| InvalidRequestError
	| NegativePromotionAdjustedCancelAmountError
	| PaymentAlreadyCancelledError
	| PaymentNotFoundError
	| PaymentNotPaidError
	| PgProviderError
	| PromotionDiscountRetainOptionShouldNotBeChangedError
	| SumOfPartsExceedsCancelAmountError
	| UnauthorizedError
	| { readonly type: Unrecognized }

export function isUnrecognizedCancelPaymentError(entity: CancelPaymentError): entity is { readonly type: Unrecognized } {
	return entity.type !== "CANCELLABLE_AMOUNT_CONSISTENCY_BROKEN"
		&& entity.type !== "CANCEL_AMOUNT_EXCEEDS_CANCELLABLE_AMOUNT"
		&& entity.type !== "CANCEL_TAX_AMOUNT_EXCEEDS_CANCELLABLE_TAX_AMOUNT"
		&& entity.type !== "CANCEL_TAX_FREE_AMOUNT_EXCEEDS_CANCELLABLE_TAX_FREE_AMOUNT"
		&& entity.type !== "FORBIDDEN"
		&& entity.type !== "INVALID_REQUEST"
		&& entity.type !== "NEGATIVE_PROMOTION_ADJUSTED_CANCEL_AMOUNT"
		&& entity.type !== "PAYMENT_ALREADY_CANCELLED"
		&& entity.type !== "PAYMENT_NOT_FOUND"
		&& entity.type !== "PAYMENT_NOT_PAID"
		&& entity.type !== "PG_PROVIDER"
		&& entity.type !== "PROMOTION_DISCOUNT_RETAIN_OPTION_SHOULD_NOT_BE_CHANGED"
		&& entity.type !== "SUM_OF_PARTS_EXCEEDS_CANCEL_AMOUNT"
		&& entity.type !== "UNAUTHORIZED"
}
