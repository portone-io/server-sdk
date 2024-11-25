import type { Unrecognized } from "./../../utils/unrecognized"
import type { ForbiddenError } from "./../common/ForbiddenError"
import type { InvalidRequestError } from "./../common/InvalidRequestError"
import type { PlatformArchivedContractError } from "./../platform/PlatformArchivedContractError"
import type { PlatformContractNotFoundError } from "./../platform/PlatformContractNotFoundError"
import type { PlatformContractScheduleAlreadyExistsError } from "./../platform/PlatformContractScheduleAlreadyExistsError"
import type { PlatformNotEnabledError } from "./../platform/PlatformNotEnabledError"
import type { UnauthorizedError } from "./../common/UnauthorizedError"
export type ScheduleContractError =
	| ForbiddenError
	| InvalidRequestError
	| PlatformArchivedContractError
	| PlatformContractNotFoundError
	| PlatformContractScheduleAlreadyExistsError
	| PlatformNotEnabledError
	| UnauthorizedError
	| { readonly type: Unrecognized }

export function isUnrecognizedScheduleContractError(entity: ScheduleContractError): entity is { readonly type: Unrecognized } {
	return entity.type !== "FORBIDDEN"
		&& entity.type !== "INVALID_REQUEST"
		&& entity.type !== "PLATFORM_ARCHIVED_CONTRACT"
		&& entity.type !== "PLATFORM_CONTRACT_NOT_FOUND"
		&& entity.type !== "PLATFORM_CONTRACT_SCHEDULE_ALREADY_EXISTS"
		&& entity.type !== "PLATFORM_NOT_ENABLED"
		&& entity.type !== "UNAUTHORIZED"
}
