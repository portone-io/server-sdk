import type { Unrecognized } from "./../../../utils/unrecognized"
import type { ForbiddenError } from "./../../common/ForbiddenError"
import type { InvalidRequestError } from "./../../common/InvalidRequestError"
import type { PlatformArchivedContractError } from "./../../platform/PlatformArchivedContractError"
import type { PlatformContractNotFoundError } from "./../../platform/PlatformContractNotFoundError"
import type { PlatformNotEnabledError } from "./../../platform/PlatformNotEnabledError"
import type { UnauthorizedError } from "./../../common/UnauthorizedError"
export type UpdatePlatformContractError =
	| ForbiddenError
	| InvalidRequestError
	| PlatformArchivedContractError
	| PlatformContractNotFoundError
	| PlatformNotEnabledError
	| UnauthorizedError
	| { readonly type: Unrecognized }

export function isUnrecognizedUpdatePlatformContractError(entity: UpdatePlatformContractError): entity is { readonly type: Unrecognized } {
	return entity.type !== "FORBIDDEN"
		&& entity.type !== "INVALID_REQUEST"
		&& entity.type !== "PLATFORM_ARCHIVED_CONTRACT"
		&& entity.type !== "PLATFORM_CONTRACT_NOT_FOUND"
		&& entity.type !== "PLATFORM_NOT_ENABLED"
		&& entity.type !== "UNAUTHORIZED"
}
