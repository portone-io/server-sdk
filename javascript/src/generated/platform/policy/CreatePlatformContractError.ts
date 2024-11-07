import type { ForbiddenError } from "./../../common/ForbiddenError"
import type { InvalidRequestError } from "./../../common/InvalidRequestError"
import type { PlatformContractAlreadyExistsError } from "./../../platform/policy/PlatformContractAlreadyExistsError"
import type { PlatformNotEnabledError } from "./../../platform/PlatformNotEnabledError"
import type { UnauthorizedError } from "./../../common/UnauthorizedError"

export type CreatePlatformContractError =
	| ForbiddenError
	| InvalidRequestError
	| PlatformContractAlreadyExistsError
	| PlatformNotEnabledError
	| UnauthorizedError
