import type { CashReceiptNotFoundError } from "#generated/payment/cashReceipt/CashReceiptNotFoundError"
import type { ForbiddenError } from "#generated/common/ForbiddenError"
import type { InvalidRequestError } from "#generated/common/InvalidRequestError"
import type { UnauthorizedError } from "#generated/common/UnauthorizedError"

export type GetCashReceiptError =
	| CashReceiptNotFoundError
	| ForbiddenError
	| InvalidRequestError
	| UnauthorizedError
