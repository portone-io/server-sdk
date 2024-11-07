import type { ForbiddenError } from "./../common/ForbiddenError"
import type { InvalidRequestError } from "./../common/InvalidRequestError"
import type { PlatformArchivedContractError } from "./../platform/PlatformArchivedContractError"
import type { PlatformContractNotFoundError } from "./../platform/PlatformContractNotFoundError"
import type { PlatformContractScheduleAlreadyExistsError } from "./../platform/PlatformContractScheduleAlreadyExistsError"
import type { PlatformNotEnabledError } from "./../platform/PlatformNotEnabledError"
import type { UnauthorizedError } from "./../common/UnauthorizedError"

export type ScheduleContractError =
	| ForbiddenError
	| InvalidRequestError
	| PlatformArchivedContractError
	| PlatformContractNotFoundError
	| PlatformContractScheduleAlreadyExistsError
	| PlatformNotEnabledError
	| UnauthorizedError
