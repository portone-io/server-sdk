import type { Unrecognized } from "./../../../utils/unrecognized"
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
	| { readonly type: Unrecognized }

export function isUnrecognizedIssueBillingKeyError(entity: IssueBillingKeyError): entity is { readonly type: Unrecognized } {
	return entity.type !== "CHANNEL_NOT_FOUND"
		&& entity.type !== "CHANNEL_SPECIFIC"
		&& entity.type !== "FORBIDDEN"
		&& entity.type !== "INVALID_REQUEST"
		&& entity.type !== "PG_PROVIDER"
		&& entity.type !== "UNAUTHORIZED"
}
