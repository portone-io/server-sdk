import type { AlreadyPaidError } from "#generated/payment/AlreadyPaidError"
import type { ChannelNotFoundError } from "#generated/common/ChannelNotFoundError"
import type { DiscountAmountExceedsTotalAmountError } from "#generated/payment/DiscountAmountExceedsTotalAmountError"
import type { ForbiddenError } from "#generated/common/ForbiddenError"
import type { InvalidRequestError } from "#generated/common/InvalidRequestError"
import type { MaxTransactionCountReachedError } from "#generated/common/MaxTransactionCountReachedError"
import type { PgProviderError } from "#generated/common/PgProviderError"
import type { PromotionPayMethodDoesNotMatchError } from "#generated/payment/PromotionPayMethodDoesNotMatchError"
import type { SumOfPartsExceedsTotalAmountError } from "#generated/common/SumOfPartsExceedsTotalAmountError"
import type { UnauthorizedError } from "#generated/common/UnauthorizedError"

export type PayInstantlyError =
	| AlreadyPaidError
	| ChannelNotFoundError
	| DiscountAmountExceedsTotalAmountError
	| ForbiddenError
	| InvalidRequestError
	| MaxTransactionCountReachedError
	| PgProviderError
	| PromotionPayMethodDoesNotMatchError
	| SumOfPartsExceedsTotalAmountError
	| UnauthorizedError
