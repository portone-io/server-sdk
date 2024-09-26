import type { ForbiddenError } from "#generated/common/ForbiddenError"
import type { InvalidRequestError } from "#generated/common/InvalidRequestError"
import type { PlatformDiscountSharePolicyAlreadyExistsError } from "#generated/platform/policy/PlatformDiscountSharePolicyAlreadyExistsError"
import type { PlatformNotEnabledError } from "#generated/platform/PlatformNotEnabledError"
import type { UnauthorizedError } from "#generated/common/UnauthorizedError"

export type CreatePlatformDiscountSharePolicyError =
	| ForbiddenError
	| InvalidRequestError
	| PlatformDiscountSharePolicyAlreadyExistsError
	| PlatformNotEnabledError
	| UnauthorizedError
