import type { Unrecognized } from "./../../utils/unrecognized"
import type { InvalidRequestError } from "./../common/InvalidRequestError"
import type { PlatformNotEnabledError } from "./../platform/PlatformNotEnabledError"
import type { UnauthorizedError } from "./../common/UnauthorizedError"
export type GetPlatformError =
	| InvalidRequestError
	| PlatformNotEnabledError
	| UnauthorizedError
	| { readonly type: Unrecognized }

export function isUnrecognizedGetPlatformError(entity: GetPlatformError): entity is { readonly type: Unrecognized } {
	return entity.type !== "INVALID_REQUEST"
		&& entity.type !== "PLATFORM_NOT_ENABLED"
		&& entity.type !== "UNAUTHORIZED"
}
