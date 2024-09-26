import type { ForbiddenError } from "#generated/common/ForbiddenError"
import type { InvalidRequestError } from "#generated/common/InvalidRequestError"
import type { PlatformAccountVerificationAlreadyUsedError } from "#generated/platform/PlatformAccountVerificationAlreadyUsedError"
import type { PlatformAccountVerificationFailedError } from "#generated/platform/PlatformAccountVerificationFailedError"
import type { PlatformAccountVerificationNotFoundError } from "#generated/platform/PlatformAccountVerificationNotFoundError"
import type { PlatformArchivedPartnerError } from "#generated/platform/PlatformArchivedPartnerError"
import type { PlatformContractNotFoundError } from "#generated/platform/PlatformContractNotFoundError"
import type { PlatformInsufficientDataToChangePartnerTypeError } from "#generated/platform/PlatformInsufficientDataToChangePartnerTypeError"
import type { PlatformNotEnabledError } from "#generated/platform/PlatformNotEnabledError"
import type { PlatformPartnerNotFoundError } from "#generated/platform/PlatformPartnerNotFoundError"
import type { PlatformUserDefinedPropertyNotFoundError } from "#generated/platform/PlatformUserDefinedPropertyNotFoundError"
import type { UnauthorizedError } from "#generated/common/UnauthorizedError"

export type UpdatePlatformPartnerError =
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
	| PlatformUserDefinedPropertyNotFoundError
	| UnauthorizedError
