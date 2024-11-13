import type { ForbiddenError } from "./../../common/ForbiddenError"
import type { InvalidRequestError } from "./../../common/InvalidRequestError"
import type { PlatformCancelOrderTransfersExistsError } from "./../../platform/transfer/PlatformCancelOrderTransfersExistsError"
import type { PlatformNotEnabledError } from "./../../platform/PlatformNotEnabledError"
import type { PlatformTransferNonDeletableStatusError } from "./../../platform/transfer/PlatformTransferNonDeletableStatusError"
import type { PlatformTransferNotFoundError } from "./../../platform/transfer/PlatformTransferNotFoundError"
import type { UnauthorizedError } from "./../../common/UnauthorizedError"

export type DeletePlatformTransferError =
	| ForbiddenError
	| InvalidRequestError
	| PlatformCancelOrderTransfersExistsError
	| PlatformNotEnabledError
	| PlatformTransferNonDeletableStatusError
	| PlatformTransferNotFoundError
	| UnauthorizedError
	| { readonly type: unique symbol }
