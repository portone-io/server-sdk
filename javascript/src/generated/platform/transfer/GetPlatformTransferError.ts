import type { Unrecognized } from "./../../../utils/unrecognized"
import type { ForbiddenError } from "./../../common/ForbiddenError"
import type { InvalidRequestError } from "./../../common/InvalidRequestError"
import type { PlatformNotEnabledError } from "./../../platform/PlatformNotEnabledError"
import type { PlatformTransferNotFoundError } from "./../../platform/transfer/PlatformTransferNotFoundError"
import type { UnauthorizedError } from "./../../common/UnauthorizedError"
export type GetPlatformTransferError =
	| ForbiddenError
	| InvalidRequestError
	| PlatformNotEnabledError
	| PlatformTransferNotFoundError
	| UnauthorizedError
	| { readonly type: Unrecognized }

export function isUnrecognizedGetPlatformTransferError(entity: GetPlatformTransferError): entity is { readonly type: Unrecognized } {
	return entity.type !== "FORBIDDEN"
		&& entity.type !== "INVALID_REQUEST"
		&& entity.type !== "PLATFORM_NOT_ENABLED"
		&& entity.type !== "PLATFORM_TRANSFER_NOT_FOUND"
		&& entity.type !== "UNAUTHORIZED"
}
