import type { InvalidRequestError } from "./../common/InvalidRequestError"
import type { PlatformNotEnabledError } from "./../platform/PlatformNotEnabledError"
import type { UnauthorizedError } from "./../common/UnauthorizedError"

export type GetPlatformError =
	| InvalidRequestError
	| PlatformNotEnabledError
	| UnauthorizedError
	| { readonly type: unique symbol }
