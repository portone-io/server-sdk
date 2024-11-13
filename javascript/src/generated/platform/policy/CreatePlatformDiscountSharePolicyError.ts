import type { ForbiddenError } from "./../../common/ForbiddenError"
import type { InvalidRequestError } from "./../../common/InvalidRequestError"
import type { PlatformDiscountSharePolicyAlreadyExistsError } from "./../../platform/policy/PlatformDiscountSharePolicyAlreadyExistsError"
import type { PlatformNotEnabledError } from "./../../platform/PlatformNotEnabledError"
import type { UnauthorizedError } from "./../../common/UnauthorizedError"

export type CreatePlatformDiscountSharePolicyError =
	| ForbiddenError
	| InvalidRequestError
	| PlatformDiscountSharePolicyAlreadyExistsError
	| PlatformNotEnabledError
	| UnauthorizedError
	| { readonly type: unique symbol }
