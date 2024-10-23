import type { AlreadyPaidError } from "#generated/payment/AlreadyPaidError"
import type { BillingKeyAlreadyDeletedError } from "#generated/common/BillingKeyAlreadyDeletedError"
import type { BillingKeyNotFoundError } from "#generated/common/BillingKeyNotFoundError"
import type { ChannelNotFoundError } from "#generated/common/ChannelNotFoundError"
import type { DiscountAmountExceedsTotalAmountError } from "#generated/payment/DiscountAmountExceedsTotalAmountError"
import type { ForbiddenError } from "#generated/common/ForbiddenError"
import type { InvalidRequestError } from "#generated/common/InvalidRequestError"
import type { MaxTransactionCountReachedError } from "#generated/common/MaxTransactionCountReachedError"
import type { PaymentScheduleAlreadyExistsError } from "#generated/common/PaymentScheduleAlreadyExistsError"
import type { PgProviderError } from "#generated/common/PgProviderError"
import type { PromotionPayMethodDoesNotMatchError } from "#generated/payment/PromotionPayMethodDoesNotMatchError"
import type { SumOfPartsExceedsTotalAmountError } from "#generated/common/SumOfPartsExceedsTotalAmountError"
import type { UnauthorizedError } from "#generated/common/UnauthorizedError"

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
