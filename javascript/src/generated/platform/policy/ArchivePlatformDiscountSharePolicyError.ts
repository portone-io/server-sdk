import type { ForbiddenError } from "#generated/common/ForbiddenError"
import type { InvalidRequestError } from "#generated/common/InvalidRequestError"
import type { PlatformCannotArchiveScheduledDiscountSharePolicyError } from "#generated/platform/policy/PlatformCannotArchiveScheduledDiscountSharePolicyError"
import type { PlatformDiscountSharePolicyNotFoundError } from "#generated/platform/PlatformDiscountSharePolicyNotFoundError"
import type { PlatformNotEnabledError } from "#generated/platform/PlatformNotEnabledError"
import type { UnauthorizedError } from "#generated/common/UnauthorizedError"

export type ArchivePlatformDiscountSharePolicyError =
	| ForbiddenError
	| InvalidRequestError
	| PlatformCannotArchiveScheduledDiscountSharePolicyError
	| PlatformDiscountSharePolicyNotFoundError
	| PlatformNotEnabledError
	| UnauthorizedError
