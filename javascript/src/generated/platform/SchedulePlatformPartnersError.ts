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
	| { readonly type: unique symbol }
