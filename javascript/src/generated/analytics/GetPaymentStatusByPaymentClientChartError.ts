import type { ForbiddenError } from "#generated/common/ForbiddenError"
import type { InvalidRequestError } from "#generated/common/InvalidRequestError"
import type { UnauthorizedError } from "#generated/common/UnauthorizedError"

export type GetPaymentStatusByPaymentClientChartError =
	| ForbiddenError
	| InvalidRequestError
	| UnauthorizedError
