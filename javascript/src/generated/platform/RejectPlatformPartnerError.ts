import type { ForbiddenError } from "#generated/common/ForbiddenError"
import type { InvalidRequestError } from "#generated/common/InvalidRequestError"
import type { PlatformArchivedPartnerError } from "#generated/platform/PlatformArchivedPartnerError"
import type { PlatformNotEnabledError } from "#generated/platform/PlatformNotEnabledError"
import type { PlatformPartnerNotFoundError } from "#generated/platform/PlatformPartnerNotFoundError"
import type { UnauthorizedError } from "#generated/common/UnauthorizedError"

export type RejectPlatformPartnerError =
	| ForbiddenError
	| InvalidRequestError
	| PlatformArchivedPartnerError
	| PlatformNotEnabledError
	| PlatformPartnerNotFoundError
	| UnauthorizedError
