import type { ForbiddenError } from "./../../common/ForbiddenError"
import type { InvalidRequestError } from "./../../common/InvalidRequestError"
import type { PromotionNotFoundError } from "./../../payment/promotion/PromotionNotFoundError"
import type { UnauthorizedError } from "./../../common/UnauthorizedError"

export type GetPromotionError =
	| ForbiddenError
	| InvalidRequestError
	| PromotionNotFoundError
	| UnauthorizedError
	| { readonly type: unique symbol }
