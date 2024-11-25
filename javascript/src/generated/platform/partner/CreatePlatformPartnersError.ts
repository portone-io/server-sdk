import type { Unrecognized } from "./../../../utils/unrecognized"
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
	| { readonly type: Unrecognized }

export function isUnrecognizedCreatePlatformPartnersError(entity: CreatePlatformPartnersError): entity is { readonly type: Unrecognized } {
	return entity.type !== "FORBIDDEN"
		&& entity.type !== "INVALID_REQUEST"
		&& entity.type !== "PLATFORM_CONTRACTS_NOT_FOUND"
		&& entity.type !== "PLATFORM_CURRENCY_NOT_SUPPORTED"
		&& entity.type !== "PLATFORM_NOT_ENABLED"
		&& entity.type !== "PLATFORM_PARTNER_IDS_ALREADY_EXISTS"
		&& entity.type !== "PLATFORM_PARTNER_IDS_DUPLICATED"
		&& entity.type !== "PLATFORM_USER_DEFINED_PROPERTY_NOT_FOUND"
		&& entity.type !== "UNAUTHORIZED"
}
