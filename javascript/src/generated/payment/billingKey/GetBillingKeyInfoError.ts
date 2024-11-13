import type { BillingKeyNotFoundError } from "./../../common/BillingKeyNotFoundError"
import type { ForbiddenError } from "./../../common/ForbiddenError"
import type { InvalidRequestError } from "./../../common/InvalidRequestError"
import type { UnauthorizedError } from "./../../common/UnauthorizedError"

export type GetBillingKeyInfoError =
	| BillingKeyNotFoundError
	| ForbiddenError
	| InvalidRequestError
	| UnauthorizedError
	| { readonly type: unique symbol }
