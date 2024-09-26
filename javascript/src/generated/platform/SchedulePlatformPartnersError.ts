import type { ForbiddenError } from "#generated/common/ForbiddenError"
import type { InvalidRequestError } from "#generated/common/InvalidRequestError"
import type { PlatformArchivedPartnersCannotBeScheduledError } from "#generated/platform/PlatformArchivedPartnersCannotBeScheduledError"
import type { PlatformContractNotFoundError } from "#generated/platform/PlatformContractNotFoundError"
import type { PlatformNotEnabledError } from "#generated/platform/PlatformNotEnabledError"
import type { PlatformPartnerSchedulesAlreadyExistError } from "#generated/platform/PlatformPartnerSchedulesAlreadyExistError"
import type { PlatformUserDefinedPropertyNotFoundError } from "#generated/platform/PlatformUserDefinedPropertyNotFoundError"
import type { UnauthorizedError } from "#generated/common/UnauthorizedError"

export type SchedulePlatformPartnersError =
	| ForbiddenError
	| InvalidRequestError
	| PlatformArchivedPartnersCannotBeScheduledError
	| PlatformContractNotFoundError
	| PlatformNotEnabledError
	| PlatformPartnerSchedulesAlreadyExistError
	| PlatformUserDefinedPropertyNotFoundError
	| UnauthorizedError
