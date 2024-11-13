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
	| { readonly type: unique symbol }
