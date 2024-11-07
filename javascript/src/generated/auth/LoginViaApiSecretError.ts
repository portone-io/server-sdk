import type { InvalidRequestError } from "./../common/InvalidRequestError"
import type { UnauthorizedError } from "./../common/UnauthorizedError"

export type LoginViaApiSecretError =
	| InvalidRequestError
	| UnauthorizedError
