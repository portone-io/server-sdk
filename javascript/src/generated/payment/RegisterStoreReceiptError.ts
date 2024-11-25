import type { Unrecognized } from "./../../utils/unrecognized"
import type { ForbiddenError } from "./../common/ForbiddenError"
import type { InvalidRequestError } from "./../common/InvalidRequestError"
import type { PaymentNotFoundError } from "./../payment/PaymentNotFoundError"
import type { PaymentNotPaidError } from "./../payment/PaymentNotPaidError"
import type { PgProviderError } from "./../common/PgProviderError"
import type { UnauthorizedError } from "./../common/UnauthorizedError"
export type RegisterStoreReceiptError =
	| ForbiddenError
	| InvalidRequestError
	| PaymentNotFoundError
	| PaymentNotPaidError
	| PgProviderError
	| UnauthorizedError
	| { readonly type: Unrecognized }

export function isUnrecognizedRegisterStoreReceiptError(entity: RegisterStoreReceiptError): entity is { readonly type: Unrecognized } {
	return entity.type !== "FORBIDDEN"
		&& entity.type !== "INVALID_REQUEST"
		&& entity.type !== "PAYMENT_NOT_FOUND"
		&& entity.type !== "PAYMENT_NOT_PAID"
		&& entity.type !== "PG_PROVIDER"
		&& entity.type !== "UNAUTHORIZED"
}
