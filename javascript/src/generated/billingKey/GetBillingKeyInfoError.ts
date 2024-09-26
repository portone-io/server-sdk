import type { BillingKeyNotFoundError } from "#generated/common/BillingKeyNotFoundError"
import type { ForbiddenError } from "#generated/common/ForbiddenError"
import type { InvalidRequestError } from "#generated/common/InvalidRequestError"
import type { UnauthorizedError } from "#generated/common/UnauthorizedError"

export type GetBillingKeyInfoError =
	| BillingKeyNotFoundError
	| ForbiddenError
	| InvalidRequestError
	| UnauthorizedError
