import type { ForbiddenError } from "#generated/common/ForbiddenError"
import type { InvalidRequestError } from "#generated/common/InvalidRequestError"
import type { PromotionNotFoundError } from "#generated/payment/promotion/PromotionNotFoundError"
import type { UnauthorizedError } from "#generated/common/UnauthorizedError"

export type GetPromotionError =
	| ForbiddenError
	| InvalidRequestError
	| PromotionNotFoundError
	| UnauthorizedError
