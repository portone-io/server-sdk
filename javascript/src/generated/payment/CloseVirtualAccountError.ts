import type { Unrecognized } from "./../../utils/unrecognized"
import type { ForbiddenError } from "./../common/ForbiddenError"
import type { InvalidRequestError } from "./../common/InvalidRequestError"
import type { PaymentNotFoundError } from "./../payment/PaymentNotFoundError"
import type { PaymentNotWaitingForDepositError } from "./../payment/PaymentNotWaitingForDepositError"
import type { PgProviderError } from "./../common/PgProviderError"
import type { UnauthorizedError } from "./../common/UnauthorizedError"
export type CloseVirtualAccountError =
	| ForbiddenError
	| InvalidRequestError
	| PaymentNotFoundError
	| PaymentNotWaitingForDepositError
	| PgProviderError
	| UnauthorizedError
	| { readonly type: Unrecognized }

export function isUnrecognizedCloseVirtualAccountError(entity: CloseVirtualAccountError): entity is { readonly type: Unrecognized } {
	return entity.type !== "FORBIDDEN"
		&& entity.type !== "INVALID_REQUEST"
		&& entity.type !== "PAYMENT_NOT_FOUND"
		&& entity.type !== "PAYMENT_NOT_WAITING_FOR_DEPOSIT"
		&& entity.type !== "PG_PROVIDER"
		&& entity.type !== "UNAUTHORIZED"
}
