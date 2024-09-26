import type { ForbiddenError } from "#generated/common/ForbiddenError"
import type { InvalidRequestError } from "#generated/common/InvalidRequestError"
import type { PlatformCannotArchiveScheduledPartnerError } from "#generated/platform/partner/PlatformCannotArchiveScheduledPartnerError"
import type { PlatformNotEnabledError } from "#generated/platform/PlatformNotEnabledError"
import type { PlatformPartnerNotFoundError } from "#generated/platform/PlatformPartnerNotFoundError"
import type { UnauthorizedError } from "#generated/common/UnauthorizedError"

export type ArchivePlatformPartnerError =
	| ForbiddenError
	| InvalidRequestError
	| PlatformCannotArchiveScheduledPartnerError
	| PlatformNotEnabledError
	| PlatformPartnerNotFoundError
	| UnauthorizedError
