import type { ChannelNotFoundError } from "./../../common/ChannelNotFoundError"
import type { ChannelSpecificError } from "./../../payment/billingKey/ChannelSpecificError"
import type { ForbiddenError } from "./../../common/ForbiddenError"
import type { InvalidRequestError } from "./../../common/InvalidRequestError"
import type { PgProviderError } from "./../../common/PgProviderError"
import type { UnauthorizedError } from "./../../common/UnauthorizedError"

export type IssueBillingKeyError =
	| ChannelNotFoundError
	| ChannelSpecificError
	| ForbiddenError
	| InvalidRequestError
	| PgProviderError
	| UnauthorizedError
	| { readonly type: unique symbol }
