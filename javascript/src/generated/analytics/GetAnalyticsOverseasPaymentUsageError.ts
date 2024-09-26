import type { ForbiddenError } from "#generated/common/ForbiddenError"
import type { UnauthorizedError } from "#generated/common/UnauthorizedError"

export type GetAnalyticsOverseasPaymentUsageError =
	| ForbiddenError
	| UnauthorizedError
