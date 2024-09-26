import type { ForbiddenError } from "#generated/common/ForbiddenError"
import type { InvalidRequestError } from "#generated/common/InvalidRequestError"
import type { PlatformAdditionalFeePolicyNotFoundError } from "#generated/platform/PlatformAdditionalFeePolicyNotFoundError"
import type { PlatformCannotArchiveScheduledAdditionalFeePolicyError } from "#generated/platform/policy/PlatformCannotArchiveScheduledAdditionalFeePolicyError"
import type { PlatformNotEnabledError } from "#generated/platform/PlatformNotEnabledError"
import type { UnauthorizedError } from "#generated/common/UnauthorizedError"

export type ArchivePlatformAdditionalFeePolicyError =
	| ForbiddenError
	| InvalidRequestError
	| PlatformAdditionalFeePolicyNotFoundError
	| PlatformCannotArchiveScheduledAdditionalFeePolicyError
	| PlatformNotEnabledError
	| UnauthorizedError
