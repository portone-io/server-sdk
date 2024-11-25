import type { Unrecognized } from "./../../../utils/unrecognized"
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
	| { readonly type: Unrecognized }

export function isUnrecognizedCreatePlatformPartnerError(entity: CreatePlatformPartnerError): entity is { readonly type: Unrecognized } {
	return entity.type !== "FORBIDDEN"
		&& entity.type !== "INVALID_REQUEST"
		&& entity.type !== "PLATFORM_ACCOUNT_VERIFICATION_ALREADY_USED"
		&& entity.type !== "PLATFORM_ACCOUNT_VERIFICATION_FAILED"
		&& entity.type !== "PLATFORM_ACCOUNT_VERIFICATION_NOT_FOUND"
		&& entity.type !== "PLATFORM_CONTRACT_NOT_FOUND"
		&& entity.type !== "PLATFORM_CURRENCY_NOT_SUPPORTED"
		&& entity.type !== "PLATFORM_NOT_ENABLED"
		&& entity.type !== "PLATFORM_PARTNER_ID_ALREADY_EXISTS"
		&& entity.type !== "PLATFORM_USER_DEFINED_PROPERTY_NOT_FOUND"
		&& entity.type !== "UNAUTHORIZED"
}
