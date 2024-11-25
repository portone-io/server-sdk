import type { Unrecognized } from "./../../../utils/unrecognized"
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
	| { readonly type: Unrecognized }

export function isUnrecognizedDeletePlatformTransferError(entity: DeletePlatformTransferError): entity is { readonly type: Unrecognized } {
	return entity.type !== "FORBIDDEN"
		&& entity.type !== "INVALID_REQUEST"
		&& entity.type !== "PLATFORM_CANCEL_ORDER_TRANSFERS_EXISTS"
		&& entity.type !== "PLATFORM_NOT_ENABLED"
		&& entity.type !== "PLATFORM_TRANSFER_NON_DELETABLE_STATUS"
		&& entity.type !== "PLATFORM_TRANSFER_NOT_FOUND"
		&& entity.type !== "UNAUTHORIZED"
}
