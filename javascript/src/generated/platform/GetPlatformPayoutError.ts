import type { ForbiddenError } from "#generated/common/ForbiddenError"
import type { InvalidRequestError } from "#generated/common/InvalidRequestError"
import type { PlatformNotEnabledError } from "#generated/platform/PlatformNotEnabledError"
import type { PlatformPayoutNotFoundError } from "#generated/platform/PlatformPayoutNotFoundError"
import type { UnauthorizedError } from "#generated/common/UnauthorizedError"

export type GetPlatformPayoutError =
	| ForbiddenError
	| InvalidRequestError
	| PlatformNotEnabledError
	| PlatformPayoutNotFoundError
	| UnauthorizedError
