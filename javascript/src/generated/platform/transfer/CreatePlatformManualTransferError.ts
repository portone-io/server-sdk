import type { Unrecognized } from "./../../../utils/unrecognized"
import type { ForbiddenError } from "./../../common/ForbiddenError"
import type { InvalidRequestError } from "./../../common/InvalidRequestError"
import type { PlatformNotEnabledError } from "./../../platform/PlatformNotEnabledError"
import type { PlatformPartnerNotFoundError } from "./../../platform/PlatformPartnerNotFoundError"
import type { PlatformUserDefinedPropertyNotFoundError } from "./../../platform/PlatformUserDefinedPropertyNotFoundError"
import type { UnauthorizedError } from "./../../common/UnauthorizedError"
export type CreatePlatformManualTransferError =
	| ForbiddenError
	| InvalidRequestError
	| PlatformNotEnabledError
	| PlatformPartnerNotFoundError
	| PlatformUserDefinedPropertyNotFoundError
	| UnauthorizedError
	| { readonly type: Unrecognized }

export function isUnrecognizedCreatePlatformManualTransferError(entity: CreatePlatformManualTransferError): entity is { readonly type: Unrecognized } {
	return entity.type !== "FORBIDDEN"
		&& entity.type !== "INVALID_REQUEST"
		&& entity.type !== "PLATFORM_NOT_ENABLED"
		&& entity.type !== "PLATFORM_PARTNER_NOT_FOUND"
		&& entity.type !== "PLATFORM_USER_DEFINED_PROPERTY_NOT_FOUND"
		&& entity.type !== "UNAUTHORIZED"
}
