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
