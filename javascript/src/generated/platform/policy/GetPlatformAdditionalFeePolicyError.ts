import type { ForbiddenError } from "./../../common/ForbiddenError"
import type { InvalidRequestError } from "./../../common/InvalidRequestError"
import type { PlatformAdditionalFeePolicyNotFoundError } from "./../../platform/PlatformAdditionalFeePolicyNotFoundError"
import type { PlatformNotEnabledError } from "./../../platform/PlatformNotEnabledError"
import type { UnauthorizedError } from "./../../common/UnauthorizedError"

export type GetPlatformAdditionalFeePolicyError =
	| ForbiddenError
	| InvalidRequestError
	| PlatformAdditionalFeePolicyNotFoundError
	| PlatformNotEnabledError
	| UnauthorizedError
