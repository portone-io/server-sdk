import type { CashReceiptNotFoundError } from "./../../payment/cashReceipt/CashReceiptNotFoundError"
import type { CashReceiptNotIssuedError } from "./../../payment/cashReceipt/CashReceiptNotIssuedError"
import type { ForbiddenError } from "./../../common/ForbiddenError"
import type { InvalidRequestError } from "./../../common/InvalidRequestError"
import type { PgProviderError } from "./../../common/PgProviderError"
import type { UnauthorizedError } from "./../../common/UnauthorizedError"

export type CancelCashReceiptError =
	| CashReceiptNotFoundError
	| CashReceiptNotIssuedError
	| ForbiddenError
	| InvalidRequestError
	| PgProviderError
	| UnauthorizedError
	| { readonly type: unique symbol }
