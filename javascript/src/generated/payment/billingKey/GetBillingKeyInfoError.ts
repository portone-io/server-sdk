import type { Unrecognized } from "./../../../utils/unrecognized"
import type { BillingKeyNotFoundError } from "./../../common/BillingKeyNotFoundError"
import type { ForbiddenError } from "./../../common/ForbiddenError"
import type { InvalidRequestError } from "./../../common/InvalidRequestError"
import type { UnauthorizedError } from "./../../common/UnauthorizedError"
export type GetBillingKeyInfoError =
	| BillingKeyNotFoundError
	| ForbiddenError
	| InvalidRequestError
	| UnauthorizedError
	| { readonly type: Unrecognized }

export function isUnrecognizedGetBillingKeyInfoError(entity: GetBillingKeyInfoError): entity is { readonly type: Unrecognized } {
	return entity.type !== "BILLING_KEY_NOT_FOUND"
		&& entity.type !== "FORBIDDEN"
		&& entity.type !== "INVALID_REQUEST"
		&& entity.type !== "UNAUTHORIZED"
}
