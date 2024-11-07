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
