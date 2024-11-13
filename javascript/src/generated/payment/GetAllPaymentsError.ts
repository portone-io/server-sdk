import type { ForbiddenError } from "./../common/ForbiddenError"
import type { InvalidRequestError } from "./../common/InvalidRequestError"
import type { UnauthorizedError } from "./../common/UnauthorizedError"

export type GetAllPaymentsError =
	| ForbiddenError
	| InvalidRequestError
	| UnauthorizedError
	| { readonly type: unique symbol }
