import type { Unrecognized } from "./../../utils/unrecognized"
import type { ForbiddenError } from "./../common/ForbiddenError"
import type { InvalidRequestError } from "./../common/InvalidRequestError"
import type { PlatformArchivedDiscountSharePolicyError } from "./../platform/PlatformArchivedDiscountSharePolicyError"
import type { PlatformDiscountSharePolicyNotFoundError } from "./../platform/PlatformDiscountSharePolicyNotFoundError"
import type { PlatformDiscountSharePolicyScheduleAlreadyExistsError } from "./../platform/PlatformDiscountSharePolicyScheduleAlreadyExistsError"
import type { PlatformNotEnabledError } from "./../platform/PlatformNotEnabledError"
import type { UnauthorizedError } from "./../common/UnauthorizedError"
export type ScheduleDiscountSharePolicyError =
	| ForbiddenError
	| InvalidRequestError
	| PlatformArchivedDiscountSharePolicyError
	| PlatformDiscountSharePolicyNotFoundError
	| PlatformDiscountSharePolicyScheduleAlreadyExistsError
	| PlatformNotEnabledError
	| UnauthorizedError
	| { readonly type: Unrecognized }

export function isUnrecognizedScheduleDiscountSharePolicyError(entity: ScheduleDiscountSharePolicyError): entity is { readonly type: Unrecognized } {
	return entity.type !== "FORBIDDEN"
		&& entity.type !== "INVALID_REQUEST"
		&& entity.type !== "PLATFORM_ARCHIVED_DISCOUNT_SHARE_POLICY"
		&& entity.type !== "PLATFORM_DISCOUNT_SHARE_POLICY_NOT_FOUND"
		&& entity.type !== "PLATFORM_DISCOUNT_SHARE_POLICY_SCHEDULE_ALREADY_EXISTS"
		&& entity.type !== "PLATFORM_NOT_ENABLED"
		&& entity.type !== "UNAUTHORIZED"
}
