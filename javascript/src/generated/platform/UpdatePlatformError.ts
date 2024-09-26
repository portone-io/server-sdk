import type { ForbiddenError } from "#generated/common/ForbiddenError"
import type { InvalidRequestError } from "#generated/common/InvalidRequestError"
import type { PlatformInvalidSettlementFormulaError } from "#generated/platform/PlatformInvalidSettlementFormulaError"
import type { PlatformNotEnabledError } from "#generated/platform/PlatformNotEnabledError"
import type { UnauthorizedError } from "#generated/common/UnauthorizedError"

export type UpdatePlatformError =
	| ForbiddenError
	| InvalidRequestError
	| PlatformInvalidSettlementFormulaError
	| PlatformNotEnabledError
	| UnauthorizedError
