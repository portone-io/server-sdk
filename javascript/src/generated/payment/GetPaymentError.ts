import type { Unrecognized } from "./../../utils/unrecognized"
import type { ForbiddenError } from "./../common/ForbiddenError"
import type { InvalidRequestError } from "./../common/InvalidRequestError"
import type { PaymentNotFoundError } from "./../payment/PaymentNotFoundError"
import type { UnauthorizedError } from "./../common/UnauthorizedError"
export type GetPaymentError =
	| ForbiddenError
	| InvalidRequestError
	| PaymentNotFoundError
	| UnauthorizedError
	| { readonly type: Unrecognized }

export function isUnrecognizedGetPaymentError(entity: GetPaymentError): entity is { readonly type: Unrecognized } {
	return entity.type !== "FORBIDDEN"
		&& entity.type !== "INVALID_REQUEST"
		&& entity.type !== "PAYMENT_NOT_FOUND"
		&& entity.type !== "UNAUTHORIZED"
}
