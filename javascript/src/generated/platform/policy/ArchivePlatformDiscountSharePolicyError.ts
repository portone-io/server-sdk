import type { ForbiddenError } from "./../../common/ForbiddenError"
import type { InvalidRequestError } from "./../../common/InvalidRequestError"
import type { PlatformCannotArchiveScheduledDiscountSharePolicyError } from "./../../platform/policy/PlatformCannotArchiveScheduledDiscountSharePolicyError"
import type { PlatformDiscountSharePolicyNotFoundError } from "./../../platform/PlatformDiscountSharePolicyNotFoundError"
import type { PlatformNotEnabledError } from "./../../platform/PlatformNotEnabledError"
import type { UnauthorizedError } from "./../../common/UnauthorizedError"

export type ArchivePlatformDiscountSharePolicyError =
	| ForbiddenError
	| InvalidRequestError
	| PlatformCannotArchiveScheduledDiscountSharePolicyError
	| PlatformDiscountSharePolicyNotFoundError
	| PlatformNotEnabledError
	| UnauthorizedError
