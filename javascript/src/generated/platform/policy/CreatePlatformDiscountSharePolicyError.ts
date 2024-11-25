import type { Unrecognized } from "./../../../utils/unrecognized"
import type { ForbiddenError } from "./../../common/ForbiddenError"
import type { InvalidRequestError } from "./../../common/InvalidRequestError"
import type { PlatformDiscountSharePolicyAlreadyExistsError } from "./../../platform/policy/PlatformDiscountSharePolicyAlreadyExistsError"
import type { PlatformNotEnabledError } from "./../../platform/PlatformNotEnabledError"
import type { UnauthorizedError } from "./../../common/UnauthorizedError"
export type CreatePlatformDiscountSharePolicyError =
	| ForbiddenError
	| InvalidRequestError
	| PlatformDiscountSharePolicyAlreadyExistsError
	| PlatformNotEnabledError
	| UnauthorizedError
	| { readonly type: Unrecognized }

export function isUnrecognizedCreatePlatformDiscountSharePolicyError(entity: CreatePlatformDiscountSharePolicyError): entity is { readonly type: Unrecognized } {
	return entity.type !== "FORBIDDEN"
		&& entity.type !== "INVALID_REQUEST"
		&& entity.type !== "PLATFORM_DISCOUNT_SHARE_POLICY_ALREADY_EXISTS"
		&& entity.type !== "PLATFORM_NOT_ENABLED"
		&& entity.type !== "UNAUTHORIZED"
}
