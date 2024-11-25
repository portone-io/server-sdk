import type { Unrecognized } from "./../../../utils/unrecognized"
import type { ForbiddenError } from "./../../common/ForbiddenError"
import type { InvalidRequestError } from "./../../common/InvalidRequestError"
import type { PlatformAdditionalFeePolicyNotFoundError } from "./../../platform/PlatformAdditionalFeePolicyNotFoundError"
import type { PlatformCannotArchiveScheduledAdditionalFeePolicyError } from "./../../platform/policy/PlatformCannotArchiveScheduledAdditionalFeePolicyError"
import type { PlatformNotEnabledError } from "./../../platform/PlatformNotEnabledError"
import type { UnauthorizedError } from "./../../common/UnauthorizedError"
export type ArchivePlatformAdditionalFeePolicyError =
	| ForbiddenError
	| InvalidRequestError
	| PlatformAdditionalFeePolicyNotFoundError
	| PlatformCannotArchiveScheduledAdditionalFeePolicyError
	| PlatformNotEnabledError
	| UnauthorizedError
	| { readonly type: Unrecognized }

export function isUnrecognizedArchivePlatformAdditionalFeePolicyError(entity: ArchivePlatformAdditionalFeePolicyError): entity is { readonly type: Unrecognized } {
	return entity.type !== "FORBIDDEN"
		&& entity.type !== "INVALID_REQUEST"
		&& entity.type !== "PLATFORM_ADDITIONAL_FEE_POLICY_NOT_FOUND"
		&& entity.type !== "PLATFORM_CANNOT_ARCHIVE_SCHEDULED_ADDITIONAL_FEE_POLICY"
		&& entity.type !== "PLATFORM_NOT_ENABLED"
		&& entity.type !== "UNAUTHORIZED"
}
