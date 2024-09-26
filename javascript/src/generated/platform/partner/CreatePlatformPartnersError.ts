import type { ForbiddenError } from "#generated/common/ForbiddenError"
import type { InvalidRequestError } from "#generated/common/InvalidRequestError"
import type { PlatformContractsNotFoundError } from "#generated/platform/partner/PlatformContractsNotFoundError"
import type { PlatformCurrencyNotSupportedError } from "#generated/platform/PlatformCurrencyNotSupportedError"
import type { PlatformNotEnabledError } from "#generated/platform/PlatformNotEnabledError"
import type { PlatformPartnerIdsAlreadyExistError } from "#generated/platform/partner/PlatformPartnerIdsAlreadyExistError"
import type { PlatformPartnerIdsDuplicatedError } from "#generated/platform/partner/PlatformPartnerIdsDuplicatedError"
import type { PlatformUserDefinedPropertyNotFoundError } from "#generated/platform/PlatformUserDefinedPropertyNotFoundError"
import type { UnauthorizedError } from "#generated/common/UnauthorizedError"

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
