import type { Unrecognized } from "./../../utils/unrecognized"
import type { ForbiddenError } from "./../common/ForbiddenError"
import type { InvalidRequestError } from "./../common/InvalidRequestError"
import type { PlatformArchivedPartnersCannotBeScheduledError } from "./../platform/PlatformArchivedPartnersCannotBeScheduledError"
import type { PlatformContractNotFoundError } from "./../platform/PlatformContractNotFoundError"
import type { PlatformNotEnabledError } from "./../platform/PlatformNotEnabledError"
import type { PlatformPartnerSchedulesAlreadyExistError } from "./../platform/PlatformPartnerSchedulesAlreadyExistError"
import type { PlatformUserDefinedPropertyNotFoundError } from "./../platform/PlatformUserDefinedPropertyNotFoundError"
import type { UnauthorizedError } from "./../common/UnauthorizedError"
export type SchedulePlatformPartnersError =
	| ForbiddenError
	| InvalidRequestError
	| PlatformArchivedPartnersCannotBeScheduledError
	| PlatformContractNotFoundError
	| PlatformNotEnabledError
	| PlatformPartnerSchedulesAlreadyExistError
	| PlatformUserDefinedPropertyNotFoundError
	| UnauthorizedError
	| { readonly type: Unrecognized }

export function isUnrecognizedSchedulePlatformPartnersError(entity: SchedulePlatformPartnersError): entity is { readonly type: Unrecognized } {
	return entity.type !== "FORBIDDEN"
		&& entity.type !== "INVALID_REQUEST"
		&& entity.type !== "PLATFORM_ARCHIVED_PARTNERS_CANNOT_BE_SCHEDULED"
		&& entity.type !== "PLATFORM_CONTRACT_NOT_FOUND"
		&& entity.type !== "PLATFORM_NOT_ENABLED"
		&& entity.type !== "PLATFORM_PARTNER_SCHEDULES_ALREADY_EXIST"
		&& entity.type !== "PLATFORM_USER_DEFINED_PROPERTY_NOT_FOUND"
		&& entity.type !== "UNAUTHORIZED"
}
