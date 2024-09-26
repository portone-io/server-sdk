import type { ForbiddenError } from "#generated/common/ForbiddenError"
import type { InvalidRequestError } from "#generated/common/InvalidRequestError"
import type { PlatformCannotArchiveScheduledContractError } from "#generated/platform/policy/PlatformCannotArchiveScheduledContractError"
import type { PlatformContractNotFoundError } from "#generated/platform/PlatformContractNotFoundError"
import type { PlatformNotEnabledError } from "#generated/platform/PlatformNotEnabledError"
import type { UnauthorizedError } from "#generated/common/UnauthorizedError"

export type ArchivePlatformContractError =
	| ForbiddenError
	| InvalidRequestError
	| PlatformCannotArchiveScheduledContractError
	| PlatformContractNotFoundError
	| PlatformNotEnabledError
	| UnauthorizedError
