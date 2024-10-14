import type { ChannelNotFoundError } from "#generated/common/ChannelNotFoundError"
import type { ChannelSpecificError } from "#generated/payment/billingKey/ChannelSpecificError"
import type { ForbiddenError } from "#generated/common/ForbiddenError"
import type { InvalidRequestError } from "#generated/common/InvalidRequestError"
import type { PgProviderError } from "#generated/common/PgProviderError"
import type { UnauthorizedError } from "#generated/common/UnauthorizedError"

export type IssueBillingKeyError =
	| ChannelNotFoundError
	| ChannelSpecificError
	| ForbiddenError
	| InvalidRequestError
	| PgProviderError
	| UnauthorizedError
