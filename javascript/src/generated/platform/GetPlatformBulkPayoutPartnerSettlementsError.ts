import type { ForbiddenError } from "#generated/common/ForbiddenError"
import type { InvalidRequestError } from "#generated/common/InvalidRequestError"
import type { PlatformBulkPayoutNotFoundError } from "#generated/platform/PlatformBulkPayoutNotFoundError"
import type { PlatformNotEnabledError } from "#generated/platform/PlatformNotEnabledError"
import type { UnauthorizedError } from "#generated/common/UnauthorizedError"

export type GetPlatformBulkPayoutPartnerSettlementsError =
	| ForbiddenError
	| InvalidRequestError
	| PlatformBulkPayoutNotFoundError
	| PlatformNotEnabledError
	| UnauthorizedError
