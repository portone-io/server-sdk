import type { ForbiddenError } from "#generated/common/ForbiddenError"
import type { InvalidRequestError } from "#generated/common/InvalidRequestError"
import type { PlatformAccountVerificationAlreadyUsedError } from "#generated/platform/PlatformAccountVerificationAlreadyUsedError"
import type { PlatformAccountVerificationFailedError } from "#generated/platform/PlatformAccountVerificationFailedError"
import type { PlatformAccountVerificationNotFoundError } from "#generated/platform/PlatformAccountVerificationNotFoundError"
import type { PlatformContractNotFoundError } from "#generated/platform/PlatformContractNotFoundError"
import type { PlatformCurrencyNotSupportedError } from "#generated/platform/PlatformCurrencyNotSupportedError"
import type { PlatformNotEnabledError } from "#generated/platform/PlatformNotEnabledError"
import type { PlatformPartnerIdAlreadyExistsError } from "#generated/platform/partner/PlatformPartnerIdAlreadyExistsError"
import type { PlatformUserDefinedPropertyNotFoundError } from "#generated/platform/PlatformUserDefinedPropertyNotFoundError"
import type { UnauthorizedError } from "#generated/common/UnauthorizedError"

export type CreatePlatformPartnerError =
	| ForbiddenError
	| InvalidRequestError
	| PlatformAccountVerificationAlreadyUsedError
	| PlatformAccountVerificationFailedError
	| PlatformAccountVerificationNotFoundError
	| PlatformContractNotFoundError
	| PlatformCurrencyNotSupportedError
	| PlatformNotEnabledError
	| PlatformPartnerIdAlreadyExistsError
	| PlatformUserDefinedPropertyNotFoundError
	| UnauthorizedError
