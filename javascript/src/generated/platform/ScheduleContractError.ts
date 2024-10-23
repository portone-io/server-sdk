import type { ForbiddenError } from "#generated/common/ForbiddenError"
import type { InvalidRequestError } from "#generated/common/InvalidRequestError"
import type { PlatformArchivedContractError } from "#generated/platform/PlatformArchivedContractError"
import type { PlatformContractNotFoundError } from "#generated/platform/PlatformContractNotFoundError"
import type { PlatformContractScheduleAlreadyExistsError } from "#generated/platform/PlatformContractScheduleAlreadyExistsError"
import type { PlatformNotEnabledError } from "#generated/platform/PlatformNotEnabledError"
import type { UnauthorizedError } from "#generated/common/UnauthorizedError"

export type ScheduleContractError =
	| ForbiddenError
	| InvalidRequestError
	| PlatformArchivedContractError
	| PlatformContractNotFoundError
	| PlatformContractScheduleAlreadyExistsError
	| PlatformNotEnabledError
	| UnauthorizedError
