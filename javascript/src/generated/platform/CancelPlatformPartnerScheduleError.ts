import type { ForbiddenError } from "./../common/ForbiddenError"
import type { InvalidRequestError } from "./../common/InvalidRequestError"
import type { PlatformNotEnabledError } from "./../platform/PlatformNotEnabledError"
import type { PlatformPartnerNotFoundError } from "./../platform/PlatformPartnerNotFoundError"
import type { UnauthorizedError } from "./../common/UnauthorizedError"

export type CancelPlatformPartnerScheduleError =
	| ForbiddenError
	| InvalidRequestError
	| PlatformNotEnabledError
	| PlatformPartnerNotFoundError
	| UnauthorizedError
	| { readonly type: unique symbol }
