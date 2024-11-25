import type { Unrecognized } from "./../../utils/unrecognized"
import type { ForbiddenError } from "./../common/ForbiddenError"
import type { InvalidRequestError } from "./../common/InvalidRequestError"
import type { PlatformAdditionalFeePolicyNotFoundError } from "./../platform/PlatformAdditionalFeePolicyNotFoundError"
import type { PlatformAdditionalFeePolicyScheduleAlreadyExistsError } from "./../platform/PlatformAdditionalFeePolicyScheduleAlreadyExistsError"
import type { PlatformArchivedAdditionalFeePolicyError } from "./../platform/PlatformArchivedAdditionalFeePolicyError"
import type { PlatformNotEnabledError } from "./../platform/PlatformNotEnabledError"
import type { UnauthorizedError } from "./../common/UnauthorizedError"
export type ScheduleAdditionalFeePolicyError =
	| ForbiddenError
	| InvalidRequestError
	| PlatformAdditionalFeePolicyNotFoundError
	| PlatformAdditionalFeePolicyScheduleAlreadyExistsError
	| PlatformArchivedAdditionalFeePolicyError
	| PlatformNotEnabledError
	| UnauthorizedError
	| { readonly type: Unrecognized }

export function isUnrecognizedScheduleAdditionalFeePolicyError(entity: ScheduleAdditionalFeePolicyError): entity is { readonly type: Unrecognized } {
	return entity.type !== "FORBIDDEN"
		&& entity.type !== "INVALID_REQUEST"
		&& entity.type !== "PLATFORM_ADDITIONAL_FEE_POLICY_NOT_FOUND"
		&& entity.type !== "PLATFORM_ADDITIONAL_FEE_POLICY_SCHEDULE_ALREADY_EXISTS"
		&& entity.type !== "PLATFORM_ARCHIVED_ADDITIONAL_FEE_POLICY"
		&& entity.type !== "PLATFORM_NOT_ENABLED"
		&& entity.type !== "UNAUTHORIZED"
}
