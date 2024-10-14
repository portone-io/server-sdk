import type { ForbiddenError } from "#generated/common/ForbiddenError"
import type { InvalidRequestError } from "#generated/common/InvalidRequestError"
import type { PlatformContractNotFoundError } from "#generated/platform/PlatformContractNotFoundError"
import type { PlatformNotEnabledError } from "#generated/platform/PlatformNotEnabledError"
import type { PlatformPartnerNotFoundError } from "#generated/platform/PlatformPartnerNotFoundError"
import type { UnauthorizedError } from "#generated/common/UnauthorizedError"

export type ReschedulePartnerError =
	| ForbiddenError
	| InvalidRequestError
	| PlatformContractNotFoundError
	| PlatformNotEnabledError
	| PlatformPartnerNotFoundError
	| UnauthorizedError