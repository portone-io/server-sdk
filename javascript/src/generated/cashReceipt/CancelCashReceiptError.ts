import type { CashReceiptNotFoundError } from "#generated/cashReceipt/CashReceiptNotFoundError"
import type { CashReceiptNotIssuedError } from "#generated/cashReceipt/CashReceiptNotIssuedError"
import type { ForbiddenError } from "#generated/common/ForbiddenError"
import type { InvalidRequestError } from "#generated/common/InvalidRequestError"
import type { PgProviderError } from "#generated/common/PgProviderError"
import type { UnauthorizedError } from "#generated/common/UnauthorizedError"

export type CancelCashReceiptError =
	| CashReceiptNotFoundError
	| CashReceiptNotIssuedError
	| ForbiddenError
	| InvalidRequestError
	| PgProviderError
	| UnauthorizedError
