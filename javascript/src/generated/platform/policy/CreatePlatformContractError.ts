import type { ForbiddenError } from "#generated/common/ForbiddenError"
import type { InvalidRequestError } from "#generated/common/InvalidRequestError"
import type { PlatformContractAlreadyExistsError } from "#generated/platform/policy/PlatformContractAlreadyExistsError"
import type { PlatformNotEnabledError } from "#generated/platform/PlatformNotEnabledError"
import type { UnauthorizedError } from "#generated/common/UnauthorizedError"

export type CreatePlatformContractError =
	| ForbiddenError
	| InvalidRequestError
	| PlatformContractAlreadyExistsError
	| PlatformNotEnabledError
	| UnauthorizedError
