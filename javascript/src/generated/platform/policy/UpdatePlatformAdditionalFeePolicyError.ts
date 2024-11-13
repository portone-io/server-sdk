import type { ForbiddenError } from "./../../common/ForbiddenError"
import type { InvalidRequestError } from "./../../common/InvalidRequestError"
import type { PlatformAdditionalFeePolicyNotFoundError } from "./../../platform/PlatformAdditionalFeePolicyNotFoundError"
import type { PlatformArchivedAdditionalFeePolicyError } from "./../../platform/PlatformArchivedAdditionalFeePolicyError"
import type { PlatformNotEnabledError } from "./../../platform/PlatformNotEnabledError"
import type { UnauthorizedError } from "./../../common/UnauthorizedError"

export type UpdatePlatformAdditionalFeePolicyError =
	| ForbiddenError
	| InvalidRequestError
	| PlatformAdditionalFeePolicyNotFoundError
	| PlatformArchivedAdditionalFeePolicyError
	| PlatformNotEnabledError
	| UnauthorizedError
	| { readonly type: unique symbol }
