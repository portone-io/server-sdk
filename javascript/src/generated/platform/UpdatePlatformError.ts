import type { ForbiddenError } from "./../common/ForbiddenError"
import type { InvalidRequestError } from "./../common/InvalidRequestError"
import type { PlatformInvalidSettlementFormulaError } from "./../platform/PlatformInvalidSettlementFormulaError"
import type { PlatformNotEnabledError } from "./../platform/PlatformNotEnabledError"
import type { UnauthorizedError } from "./../common/UnauthorizedError"

export type UpdatePlatformError =
	| ForbiddenError
	| InvalidRequestError
	| PlatformInvalidSettlementFormulaError
	| PlatformNotEnabledError
	| UnauthorizedError
	| { readonly type: unique symbol }
