import type { ForbiddenError } from "#generated/common/ForbiddenError"
import type { InvalidRequestError } from "#generated/common/InvalidRequestError"
import type { PlatformAdditionalFeePolicyNotFoundError } from "#generated/platform/PlatformAdditionalFeePolicyNotFoundError"
import type { PlatformArchivedAdditionalFeePolicyError } from "#generated/platform/PlatformArchivedAdditionalFeePolicyError"
import type { PlatformNotEnabledError } from "#generated/platform/PlatformNotEnabledError"
import type { UnauthorizedError } from "#generated/common/UnauthorizedError"

export type UpdatePlatformAdditionalFeePolicyError =
	| ForbiddenError
	| InvalidRequestError
	| PlatformAdditionalFeePolicyNotFoundError
	| PlatformArchivedAdditionalFeePolicyError
	| PlatformNotEnabledError
	| UnauthorizedError
