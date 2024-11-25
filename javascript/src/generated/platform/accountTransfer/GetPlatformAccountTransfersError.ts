import type { Unrecognized } from "./../../../utils/unrecognized"
import type { ForbiddenError } from "./../../common/ForbiddenError"
import type { InvalidRequestError } from "./../../common/InvalidRequestError"
import type { PlatformNotEnabledError } from "./../../platform/PlatformNotEnabledError"
import type { UnauthorizedError } from "./../../common/UnauthorizedError"
export type GetPlatformAccountTransfersError =
	| ForbiddenError
	| InvalidRequestError
	| PlatformNotEnabledError
	| UnauthorizedError
	| { readonly type: Unrecognized }

export function isUnrecognizedGetPlatformAccountTransfersError(entity: GetPlatformAccountTransfersError): entity is { readonly type: Unrecognized } {
	return entity.type !== "FORBIDDEN"
		&& entity.type !== "INVALID_REQUEST"
		&& entity.type !== "PLATFORM_NOT_ENABLED"
		&& entity.type !== "UNAUTHORIZED"
}
