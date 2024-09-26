import type { CashReceiptAlreadyIssuedError } from "#generated/cashReceipt/CashReceiptAlreadyIssuedError"
import type { ChannelNotFoundError } from "#generated/common/ChannelNotFoundError"
import type { ForbiddenError } from "#generated/common/ForbiddenError"
import type { InvalidRequestError } from "#generated/common/InvalidRequestError"
import type { PgProviderError } from "#generated/common/PgProviderError"
import type { UnauthorizedError } from "#generated/common/UnauthorizedError"

export type IssueCashReceiptError =
	| CashReceiptAlreadyIssuedError
	| ChannelNotFoundError
	| ForbiddenError
	| InvalidRequestError
	| PgProviderError
	| UnauthorizedError
