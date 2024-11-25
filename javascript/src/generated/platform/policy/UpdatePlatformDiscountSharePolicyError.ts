import type { Unrecognized } from "./../../../utils/unrecognized"
import type { ForbiddenError } from "./../../common/ForbiddenError"
import type { InvalidRequestError } from "./../../common/InvalidRequestError"
import type { PlatformArchivedDiscountSharePolicyError } from "./../../platform/PlatformArchivedDiscountSharePolicyError"
import type { PlatformDiscountSharePolicyNotFoundError } from "./../../platform/PlatformDiscountSharePolicyNotFoundError"
import type { PlatformNotEnabledError } from "./../../platform/PlatformNotEnabledError"
import type { UnauthorizedError } from "./../../common/UnauthorizedError"
export type UpdatePlatformDiscountSharePolicyError =
	| ForbiddenError
	| InvalidRequestError
	| PlatformArchivedDiscountSharePolicyError
	| PlatformDiscountSharePolicyNotFoundError
	| PlatformNotEnabledError
	| UnauthorizedError
	| { readonly type: Unrecognized }

export function isUnrecognizedUpdatePlatformDiscountSharePolicyError(entity: UpdatePlatformDiscountSharePolicyError): entity is { readonly type: Unrecognized } {
	return entity.type !== "FORBIDDEN"
		&& entity.type !== "INVALID_REQUEST"
		&& entity.type !== "PLATFORM_ARCHIVED_DISCOUNT_SHARE_POLICY"
		&& entity.type !== "PLATFORM_DISCOUNT_SHARE_POLICY_NOT_FOUND"
		&& entity.type !== "PLATFORM_NOT_ENABLED"
		&& entity.type !== "UNAUTHORIZED"
}
