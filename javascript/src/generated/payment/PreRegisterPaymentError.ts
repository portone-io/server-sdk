import type { Unrecognized } from "./../../utils/unrecognized"
import type { AlreadyPaidError } from "./../payment/AlreadyPaidError"
import type { ForbiddenError } from "./../common/ForbiddenError"
import type { InvalidRequestError } from "./../common/InvalidRequestError"
import type { UnauthorizedError } from "./../common/UnauthorizedError"
export type PreRegisterPaymentError =
	| AlreadyPaidError
	| ForbiddenError
	| InvalidRequestError
	| UnauthorizedError
	| { readonly type: Unrecognized }

export function isUnrecognizedPreRegisterPaymentError(entity: PreRegisterPaymentError): entity is { readonly type: Unrecognized } {
	return entity.type !== "ALREADY_PAID"
		&& entity.type !== "FORBIDDEN"
		&& entity.type !== "INVALID_REQUEST"
		&& entity.type !== "UNAUTHORIZED"
}
