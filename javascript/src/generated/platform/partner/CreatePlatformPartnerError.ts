import type { ForbiddenError } from "./../../common/ForbiddenError"
import type { InvalidRequestError } from "./../../common/InvalidRequestError"
import type { PlatformAccountVerificationAlreadyUsedError } from "./../../platform/PlatformAccountVerificationAlreadyUsedError"
import type { PlatformAccountVerificationFailedError } from "./../../platform/PlatformAccountVerificationFailedError"
import type { PlatformAccountVerificationNotFoundError } from "./../../platform/PlatformAccountVerificationNotFoundError"
import type { PlatformContractNotFoundError } from "./../../platform/PlatformContractNotFoundError"
import type { PlatformCurrencyNotSupportedError } from "./../../platform/PlatformCurrencyNotSupportedError"
import type { PlatformNotEnabledError } from "./../../platform/PlatformNotEnabledError"
import type { PlatformPartnerIdAlreadyExistsError } from "./../../platform/partner/PlatformPartnerIdAlreadyExistsError"
import type { PlatformUserDefinedPropertyNotFoundError } from "./../../platform/PlatformUserDefinedPropertyNotFoundError"
import type { UnauthorizedError } from "./../../common/UnauthorizedError"

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
	| { readonly type: unique symbol }
