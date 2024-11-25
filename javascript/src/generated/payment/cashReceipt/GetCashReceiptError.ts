import type { Unrecognized } from "./../../../utils/unrecognized"
import type { CashReceiptNotFoundError } from "./../../payment/cashReceipt/CashReceiptNotFoundError"
import type { ForbiddenError } from "./../../common/ForbiddenError"
import type { InvalidRequestError } from "./../../common/InvalidRequestError"
import type { UnauthorizedError } from "./../../common/UnauthorizedError"
export type GetCashReceiptError =
	| CashReceiptNotFoundError
	| ForbiddenError
	| InvalidRequestError
	| UnauthorizedError
	| { readonly type: Unrecognized }

export function isUnrecognizedGetCashReceiptError(entity: GetCashReceiptError): entity is { readonly type: Unrecognized } {
	return entity.type !== "CASH_RECEIPT_NOT_FOUND"
		&& entity.type !== "FORBIDDEN"
		&& entity.type !== "INVALID_REQUEST"
		&& entity.type !== "UNAUTHORIZED"
}
