import type { Unrecognized } from "./../../../utils/unrecognized"
import type { ForbiddenError } from "./../../common/ForbiddenError"
import type { InvalidRequestError } from "./../../common/InvalidRequestError"
import type { PromotionNotFoundError } from "./../../payment/promotion/PromotionNotFoundError"
import type { UnauthorizedError } from "./../../common/UnauthorizedError"
export type GetPromotionError =
	| ForbiddenError
	| InvalidRequestError
	| PromotionNotFoundError
	| UnauthorizedError
	| { readonly type: Unrecognized }

export function isUnrecognizedGetPromotionError(entity: GetPromotionError): entity is { readonly type: Unrecognized } {
	return entity.type !== "FORBIDDEN"
		&& entity.type !== "INVALID_REQUEST"
		&& entity.type !== "PROMOTION_NOT_FOUND"
		&& entity.type !== "UNAUTHORIZED"
}
