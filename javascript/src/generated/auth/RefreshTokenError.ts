import type { InvalidRequestError } from "./../common/InvalidRequestError"
import type { UnauthorizedError } from "./../common/UnauthorizedError"

export type RefreshTokenError =
	| InvalidRequestError
	| UnauthorizedError
	| { readonly type: unique symbol }
