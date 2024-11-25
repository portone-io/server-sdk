import type { Unrecognized } from "./../../utils/unrecognized"
import type { AlreadyPaidError } from "./../payment/AlreadyPaidError"
import type { BillingKeyAlreadyDeletedError } from "./../common/BillingKeyAlreadyDeletedError"
import type { BillingKeyNotFoundError } from "./../common/BillingKeyNotFoundError"
import type { ChannelNotFoundError } from "./../common/ChannelNotFoundError"
import type { DiscountAmountExceedsTotalAmountError } from "./../payment/DiscountAmountExceedsTotalAmountError"
import type { ForbiddenError } from "./../common/ForbiddenError"
import type { InvalidRequestError } from "./../common/InvalidRequestError"
import type { MaxTransactionCountReachedError } from "./../common/MaxTransactionCountReachedError"
import type { PaymentScheduleAlreadyExistsError } from "./../common/PaymentScheduleAlreadyExistsError"
import type { PgProviderError } from "./../common/PgProviderError"
import type { PromotionPayMethodDoesNotMatchError } from "./../payment/PromotionPayMethodDoesNotMatchError"
import type { SumOfPartsExceedsTotalAmountError } from "./../common/SumOfPartsExceedsTotalAmountError"
import type { UnauthorizedError } from "./../common/UnauthorizedError"
export type PayWithBillingKeyError =
	| AlreadyPaidError
	| BillingKeyAlreadyDeletedError
	| BillingKeyNotFoundError
	| ChannelNotFoundError
	| DiscountAmountExceedsTotalAmountError
	| ForbiddenError
	| InvalidRequestError
	| MaxTransactionCountReachedError
	| PaymentScheduleAlreadyExistsError
	| PgProviderError
	| PromotionPayMethodDoesNotMatchError
	| SumOfPartsExceedsTotalAmountError
	| UnauthorizedError
	| { readonly type: Unrecognized }

export function isUnrecognizedPayWithBillingKeyError(entity: PayWithBillingKeyError): entity is { readonly type: Unrecognized } {
	return entity.type !== "ALREADY_PAID"
		&& entity.type !== "BILLING_KEY_ALREADY_DELETED"
		&& entity.type !== "BILLING_KEY_NOT_FOUND"
		&& entity.type !== "CHANNEL_NOT_FOUND"
		&& entity.type !== "DISCOUNT_AMOUNT_EXCEEDS_TOTAL_AMOUNT"
		&& entity.type !== "FORBIDDEN"
		&& entity.type !== "INVALID_REQUEST"
		&& entity.type !== "MAX_TRANSACTION_COUNT_REACHED"
		&& entity.type !== "PAYMENT_SCHEDULE_ALREADY_EXISTS"
		&& entity.type !== "PG_PROVIDER"
		&& entity.type !== "PROMOTION_PAY_METHOD_DOES_NOT_MATCH"
		&& entity.type !== "SUM_OF_PARTS_EXCEEDS_TOTAL_AMOUNT"
		&& entity.type !== "UNAUTHORIZED"
}
