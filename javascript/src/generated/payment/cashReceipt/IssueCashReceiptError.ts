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
	| { readonly type: unique symbol }
