import type { Unrecognized } from "./../../utils/unrecognized"
import type { ForbiddenError } from "./../common/ForbiddenError"
import type { InvalidRequestError } from "./../common/InvalidRequestError"
import type { PlatformNotEnabledError } from "./../platform/PlatformNotEnabledError"
import type { PlatformPartnerNotFoundError } from "./../platform/PlatformPartnerNotFoundError"
import type { UnauthorizedError } from "./../common/UnauthorizedError"
export type CancelPlatformPartnerScheduleError =
	| ForbiddenError
	| InvalidRequestError
	| PlatformNotEnabledError
	| PlatformPartnerNotFoundError
	| UnauthorizedError
	| { readonly type: Unrecognized }

export function isUnrecognizedCancelPlatformPartnerScheduleError(entity: CancelPlatformPartnerScheduleError): entity is { readonly type: Unrecognized } {
	return entity.type !== "FORBIDDEN"
		&& entity.type !== "INVALID_REQUEST"
		&& entity.type !== "PLATFORM_NOT_ENABLED"
		&& entity.type !== "PLATFORM_PARTNER_NOT_FOUND"
		&& entity.type !== "UNAUTHORIZED"
}
