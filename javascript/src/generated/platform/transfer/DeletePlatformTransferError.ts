import type { ForbiddenError } from "#generated/common/ForbiddenError"
import type { InvalidRequestError } from "#generated/common/InvalidRequestError"
import type { PlatformCancelOrderTransfersExistsError } from "#generated/platform/transfer/PlatformCancelOrderTransfersExistsError"
import type { PlatformNotEnabledError } from "#generated/platform/PlatformNotEnabledError"
import type { PlatformTransferNonDeletableStatusError } from "#generated/platform/transfer/PlatformTransferNonDeletableStatusError"
import type { PlatformTransferNotFoundError } from "#generated/platform/transfer/PlatformTransferNotFoundError"
import type { UnauthorizedError } from "#generated/common/UnauthorizedError"

export type DeletePlatformTransferError =
	| ForbiddenError
	| InvalidRequestError
	| PlatformCancelOrderTransfersExistsError
	| PlatformNotEnabledError
	| PlatformTransferNonDeletableStatusError
	| PlatformTransferNotFoundError
	| UnauthorizedError
