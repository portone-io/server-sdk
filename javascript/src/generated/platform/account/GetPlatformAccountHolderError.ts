import type { Unrecognized } from "./../../../utils/unrecognized"
import type { ForbiddenError } from "./../../common/ForbiddenError"
import type { InvalidRequestError } from "./../../common/InvalidRequestError"
import type { PlatformExternalApiFailedError } from "./../../platform/account/PlatformExternalApiFailedError"
import type { PlatformExternalApiTemporarilyFailedError } from "./../../platform/account/PlatformExternalApiTemporarilyFailedError"
import type { PlatformNotEnabledError } from "./../../platform/PlatformNotEnabledError"
import type { PlatformNotSupportedBankError } from "./../../platform/account/PlatformNotSupportedBankError"
import type { UnauthorizedError } from "./../../common/UnauthorizedError"
export type GetPlatformAccountHolderError =
	| ForbiddenError
	| InvalidRequestError
	| PlatformExternalApiFailedError
	| PlatformExternalApiTemporarilyFailedError
	| PlatformNotEnabledError
	| PlatformNotSupportedBankError
	| UnauthorizedError
	| { readonly type: Unrecognized }

export function isUnrecognizedGetPlatformAccountHolderError(entity: GetPlatformAccountHolderError): entity is { readonly type: Unrecognized } {
	return entity.type !== "FORBIDDEN"
		&& entity.type !== "INVALID_REQUEST"
		&& entity.type !== "PLATFORM_EXTERNAL_API_FAILED"
		&& entity.type !== "PLATFORM_EXTERNAL_API_TEMPORARILY_FAILED"
		&& entity.type !== "PLATFORM_NOT_ENABLED"
		&& entity.type !== "PLATFORM_NOT_SUPPORTED_BANK"
		&& entity.type !== "UNAUTHORIZED"
}
