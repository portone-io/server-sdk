import type { Unrecognized } from "./../../../utils/unrecognized"
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
	| { readonly type: Unrecognized }

export function isUnrecognizedCancelCashReceiptError(entity: CancelCashReceiptError): entity is { readonly type: Unrecognized } {
	return entity.type !== "CASH_RECEIPT_NOT_FOUND"
		&& entity.type !== "CASH_RECEIPT_NOT_ISSUED"
		&& entity.type !== "FORBIDDEN"
		&& entity.type !== "INVALID_REQUEST"
		&& entity.type !== "PG_PROVIDER"
		&& entity.type !== "UNAUTHORIZED"
}
