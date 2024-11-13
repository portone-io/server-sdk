import type { CashReceiptNotFoundError } from "./../../payment/cashReceipt/CashReceiptNotFoundError"
import type { ForbiddenError } from "./../../common/ForbiddenError"
import type { InvalidRequestError } from "./../../common/InvalidRequestError"
import type { UnauthorizedError } from "./../../common/UnauthorizedError"

export type GetCashReceiptError =
	| CashReceiptNotFoundError
	| ForbiddenError
	| InvalidRequestError
	| UnauthorizedError
	| { readonly type: unique symbol }
