import type { Unrecognized } from "./../../../utils/unrecognized"
import type { ForbiddenError } from "./../../common/ForbiddenError"
import type { InvalidRequestError } from "./../../common/InvalidRequestError"
import type { PlatformCannotArchiveScheduledPartnerError } from "./../../platform/partner/PlatformCannotArchiveScheduledPartnerError"
import type { PlatformNotEnabledError } from "./../../platform/PlatformNotEnabledError"
import type { PlatformPartnerNotFoundError } from "./../../platform/PlatformPartnerNotFoundError"
import type { UnauthorizedError } from "./../../common/UnauthorizedError"
export type ArchivePlatformPartnerError =
	| ForbiddenError
	| InvalidRequestError
	| PlatformCannotArchiveScheduledPartnerError
	| PlatformNotEnabledError
	| PlatformPartnerNotFoundError
	| UnauthorizedError
	| { readonly type: Unrecognized }

export function isUnrecognizedArchivePlatformPartnerError(entity: ArchivePlatformPartnerError): entity is { readonly type: Unrecognized } {
	return entity.type !== "FORBIDDEN"
		&& entity.type !== "INVALID_REQUEST"
		&& entity.type !== "PLATFORM_CANNOT_ARCHIVE_SCHEDULED_PARTNER"
		&& entity.type !== "PLATFORM_NOT_ENABLED"
		&& entity.type !== "PLATFORM_PARTNER_NOT_FOUND"
		&& entity.type !== "UNAUTHORIZED"
}
