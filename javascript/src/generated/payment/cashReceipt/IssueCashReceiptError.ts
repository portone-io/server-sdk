import type { Unrecognized } from "./../../../utils/unrecognized"
import type { CashReceiptAlreadyIssuedError } from "./../../payment/cashReceipt/CashReceiptAlreadyIssuedError"
import type { ChannelNotFoundError } from "./../../common/ChannelNotFoundError"
import type { ForbiddenError } from "./../../common/ForbiddenError"
import type { InvalidRequestError } from "./../../common/InvalidRequestError"
import type { PgProviderError } from "./../../common/PgProviderError"
import type { UnauthorizedError } from "./../../common/UnauthorizedError"
export type IssueCashReceiptError =
	| CashReceiptAlreadyIssuedError
	| ChannelNotFoundError
	| ForbiddenError
	| InvalidRequestError
	| PgProviderError
	| UnauthorizedError
	| { readonly type: Unrecognized }

export function isUnrecognizedIssueCashReceiptError(entity: IssueCashReceiptError): entity is { readonly type: Unrecognized } {
	return entity.type !== "CASH_RECEIPT_ALREADY_ISSUED"
		&& entity.type !== "CHANNEL_NOT_FOUND"
		&& entity.type !== "FORBIDDEN"
		&& entity.type !== "INVALID_REQUEST"
		&& entity.type !== "PG_PROVIDER"
		&& entity.type !== "UNAUTHORIZED"
}
