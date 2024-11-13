import type { ForbiddenError } from "./../common/ForbiddenError"
import type { InvalidRequestError } from "./../common/InvalidRequestError"
import type { PlatformContractNotFoundError } from "./../platform/PlatformContractNotFoundError"
import type { PlatformNotEnabledError } from "./../platform/PlatformNotEnabledError"
import type { UnauthorizedError } from "./../common/UnauthorizedError"

export type CancelPlatformContractScheduleError =
	| ForbiddenError
	| InvalidRequestError
	| PlatformContractNotFoundError
	| PlatformNotEnabledError
	| UnauthorizedError
	| { readonly type: unique symbol }
