import type { ForbiddenError } from "./../../common/ForbiddenError"
import type { InvalidRequestError } from "./../../common/InvalidRequestError"
import type { PlatformContractsNotFoundError } from "./../../platform/partner/PlatformContractsNotFoundError"
import type { PlatformCurrencyNotSupportedError } from "./../../platform/PlatformCurrencyNotSupportedError"
import type { PlatformNotEnabledError } from "./../../platform/PlatformNotEnabledError"
import type { PlatformPartnerIdsAlreadyExistError } from "./../../platform/partner/PlatformPartnerIdsAlreadyExistError"
import type { PlatformPartnerIdsDuplicatedError } from "./../../platform/partner/PlatformPartnerIdsDuplicatedError"
import type { PlatformUserDefinedPropertyNotFoundError } from "./../../platform/PlatformUserDefinedPropertyNotFoundError"
import type { UnauthorizedError } from "./../../common/UnauthorizedError"

export type CreatePlatformPartnersError =
	| ForbiddenError
	| InvalidRequestError
	| PlatformContractsNotFoundError
	| PlatformCurrencyNotSupportedError
	| PlatformNotEnabledError
	| PlatformPartnerIdsAlreadyExistError
	| PlatformPartnerIdsDuplicatedError
	| PlatformUserDefinedPropertyNotFoundError
	| UnauthorizedError
