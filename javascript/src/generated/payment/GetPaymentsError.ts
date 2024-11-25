import type { Unrecognized } from "./../../utils/unrecognized"
import type { ForbiddenError } from "./../common/ForbiddenError"
import type { InvalidRequestError } from "./../common/InvalidRequestError"
import type { UnauthorizedError } from "./../common/UnauthorizedError"
export type GetPaymentsError =
	| ForbiddenError
	| InvalidRequestError
	| UnauthorizedError
	| { readonly type: Unrecognized }

export function isUnrecognizedGetPaymentsError(entity: GetPaymentsError): entity is { readonly type: Unrecognized } {
	return entity.type !== "FORBIDDEN"
		&& entity.type !== "INVALID_REQUEST"
		&& entity.type !== "UNAUTHORIZED"
}
