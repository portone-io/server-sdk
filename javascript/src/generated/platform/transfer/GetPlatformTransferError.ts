import type { ForbiddenError } from "#generated/common/ForbiddenError"
import type { InvalidRequestError } from "#generated/common/InvalidRequestError"
import type { PlatformNotEnabledError } from "#generated/platform/PlatformNotEnabledError"
import type { PlatformTransferNotFoundError } from "#generated/platform/transfer/PlatformTransferNotFoundError"
import type { UnauthorizedError } from "#generated/common/UnauthorizedError"

export type GetPlatformTransferError =
	| ForbiddenError
	| InvalidRequestError
	| PlatformNotEnabledError
	| PlatformTransferNotFoundError
	| UnauthorizedError
