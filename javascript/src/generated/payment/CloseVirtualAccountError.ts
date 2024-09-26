import type { ForbiddenError } from "#generated/common/ForbiddenError"
import type { InvalidRequestError } from "#generated/common/InvalidRequestError"
import type { PaymentNotFoundError } from "#generated/payment/PaymentNotFoundError"
import type { PaymentNotWaitingForDepositError } from "#generated/payment/PaymentNotWaitingForDepositError"
import type { PgProviderError } from "#generated/common/PgProviderError"
import type { UnauthorizedError } from "#generated/common/UnauthorizedError"

export type CloseVirtualAccountError =
	| ForbiddenError
	| InvalidRequestError
	| PaymentNotFoundError
	| PaymentNotWaitingForDepositError
	| PgProviderError
	| UnauthorizedError
