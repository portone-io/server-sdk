import type { ForbiddenError } from "./../../common/ForbiddenError"
import type { InvalidRequestError } from "./../../common/InvalidRequestError"
import type { PlatformArchivedContractError } from "./../../platform/PlatformArchivedContractError"
import type { PlatformContractNotFoundError } from "./../../platform/PlatformContractNotFoundError"
import type { PlatformNotEnabledError } from "./../../platform/PlatformNotEnabledError"
import type { UnauthorizedError } from "./../../common/UnauthorizedError"

export type UpdatePlatformContractError =
	| ForbiddenError
	| InvalidRequestError
	| PlatformArchivedContractError
	| PlatformContractNotFoundError
	| PlatformNotEnabledError
	| UnauthorizedError
