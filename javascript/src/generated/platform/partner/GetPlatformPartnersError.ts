import type { ForbiddenError } from "./../../common/ForbiddenError"
import type { InvalidRequestError } from "./../../common/InvalidRequestError"
import type { PlatformNotEnabledError } from "./../../platform/PlatformNotEnabledError"
import type { UnauthorizedError } from "./../../common/UnauthorizedError"

export type GetPlatformPartnersError =
	| ForbiddenError
	| InvalidRequestError
	| PlatformNotEnabledError
	| UnauthorizedError
	| { readonly type: unique symbol }
