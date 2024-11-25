import type { Unrecognized } from "./../../../utils/unrecognized"
import type { ForbiddenError } from "./../../common/ForbiddenError"
import type { InvalidRequestError } from "./../../common/InvalidRequestError"
import type { UnauthorizedError } from "./../../common/UnauthorizedError"
export type GetPaymentSchedulesError =
	| ForbiddenError
	| InvalidRequestError
	| UnauthorizedError
	| { readonly type: Unrecognized }

export function isUnrecognizedGetPaymentSchedulesError(entity: GetPaymentSchedulesError): entity is { readonly type: Unrecognized } {
	return entity.type !== "FORBIDDEN"
		&& entity.type !== "INVALID_REQUEST"
		&& entity.type !== "UNAUTHORIZED"
}
