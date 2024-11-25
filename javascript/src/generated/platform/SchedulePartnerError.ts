import type { Unrecognized } from "./../../utils/unrecognized"
import type { ForbiddenError } from "./../common/ForbiddenError"
import type { InvalidRequestError } from "./../common/InvalidRequestError"
import type { PlatformAccountVerificationAlreadyUsedError } from "./../platform/PlatformAccountVerificationAlreadyUsedError"
import type { PlatformAccountVerificationFailedError } from "./../platform/PlatformAccountVerificationFailedError"
import type { PlatformAccountVerificationNotFoundError } from "./../platform/PlatformAccountVerificationNotFoundError"
import type { PlatformArchivedPartnerError } from "./../platform/PlatformArchivedPartnerError"
import type { PlatformContractNotFoundError } from "./../platform/PlatformContractNotFoundError"
import type { PlatformInsufficientDataToChangePartnerTypeError } from "./../platform/PlatformInsufficientDataToChangePartnerTypeError"
import type { PlatformNotEnabledError } from "./../platform/PlatformNotEnabledError"
import type { PlatformPartnerNotFoundError } from "./../platform/PlatformPartnerNotFoundError"
import type { PlatformPartnerScheduleAlreadyExistsError } from "./../platform/PlatformPartnerScheduleAlreadyExistsError"
import type { PlatformUserDefinedPropertyNotFoundError } from "./../platform/PlatformUserDefinedPropertyNotFoundError"
import type { UnauthorizedError } from "./../common/UnauthorizedError"
export type SchedulePartnerError =
	| ForbiddenError
	| InvalidRequestError
	| PlatformAccountVerificationAlreadyUsedError
	| PlatformAccountVerificationFailedError
	| PlatformAccountVerificationNotFoundError
	| PlatformArchivedPartnerError
	| PlatformContractNotFoundError
	| PlatformInsufficientDataToChangePartnerTypeError
	| PlatformNotEnabledError
	| PlatformPartnerNotFoundError
	| PlatformPartnerScheduleAlreadyExistsError
	| PlatformUserDefinedPropertyNotFoundError
	| UnauthorizedError
	| { readonly type: Unrecognized }

export function isUnrecognizedSchedulePartnerError(entity: SchedulePartnerError): entity is { readonly type: Unrecognized } {
	return entity.type !== "FORBIDDEN"
		&& entity.type !== "INVALID_REQUEST"
		&& entity.type !== "PLATFORM_ACCOUNT_VERIFICATION_ALREADY_USED"
		&& entity.type !== "PLATFORM_ACCOUNT_VERIFICATION_FAILED"
		&& entity.type !== "PLATFORM_ACCOUNT_VERIFICATION_NOT_FOUND"
		&& entity.type !== "PLATFORM_ARCHIVED_PARTNER"
		&& entity.type !== "PLATFORM_CONTRACT_NOT_FOUND"
		&& entity.type !== "PLATFORM_INSUFFICIENT_DATA_TO_CHANGE_PARTNER_TYPE"
		&& entity.type !== "PLATFORM_NOT_ENABLED"
		&& entity.type !== "PLATFORM_PARTNER_NOT_FOUND"
		&& entity.type !== "PLATFORM_PARTNER_SCHEDULE_ALREADY_EXISTS"
		&& entity.type !== "PLATFORM_USER_DEFINED_PROPERTY_NOT_FOUND"
		&& entity.type !== "UNAUTHORIZED"
}
