import type { ForbiddenError } from "./../../common/ForbiddenError"
import type { InvalidRequestError } from "./../../common/InvalidRequestError"
import type { PlatformCannotArchiveScheduledContractError } from "./../../platform/policy/PlatformCannotArchiveScheduledContractError"
import type { PlatformContractNotFoundError } from "./../../platform/PlatformContractNotFoundError"
import type { PlatformNotEnabledError } from "./../../platform/PlatformNotEnabledError"
import type { UnauthorizedError } from "./../../common/UnauthorizedError"

export type ArchivePlatformContractError =
	| ForbiddenError
	| InvalidRequestError
	| PlatformCannotArchiveScheduledContractError
	| PlatformContractNotFoundError
	| PlatformNotEnabledError
	| UnauthorizedError
