import type { Unrecognized } from "./../../../utils/unrecognized"
import type { ForbiddenError } from "./../../common/ForbiddenError"
import type { InvalidRequestError } from "./../../common/InvalidRequestError"
import type { PlatformCannotArchiveScheduledDiscountSharePolicyError } from "./../../platform/policy/PlatformCannotArchiveScheduledDiscountSharePolicyError"
import type { PlatformDiscountSharePolicyNotFoundError } from "./../../platform/PlatformDiscountSharePolicyNotFoundError"
import type { PlatformNotEnabledError } from "./../../platform/PlatformNotEnabledError"
import type { UnauthorizedError } from "./../../common/UnauthorizedError"
export type ArchivePlatformDiscountSharePolicyError =
	| ForbiddenError
	| InvalidRequestError
	| PlatformCannotArchiveScheduledDiscountSharePolicyError
	| PlatformDiscountSharePolicyNotFoundError
	| PlatformNotEnabledError
	| UnauthorizedError
	| { readonly type: Unrecognized }

export function isUnrecognizedArchivePlatformDiscountSharePolicyError(entity: ArchivePlatformDiscountSharePolicyError): entity is { readonly type: Unrecognized } {
	return entity.type !== "FORBIDDEN"
		&& entity.type !== "INVALID_REQUEST"
		&& entity.type !== "PLATFORM_CANNOT_ARCHIVE_SCHEDULED_DISCOUNT_SHARE_POLICY"
		&& entity.type !== "PLATFORM_DISCOUNT_SHARE_POLICY_NOT_FOUND"
		&& entity.type !== "PLATFORM_NOT_ENABLED"
		&& entity.type !== "UNAUTHORIZED"
}
