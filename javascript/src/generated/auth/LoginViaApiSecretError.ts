import type { InvalidRequestError } from "#generated/common/InvalidRequestError"
import type { UnauthorizedError } from "#generated/common/UnauthorizedError"

export type LoginViaApiSecretError =
	| InvalidRequestError
	| UnauthorizedError