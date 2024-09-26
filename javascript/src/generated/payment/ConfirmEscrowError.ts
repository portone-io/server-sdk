import type { ForbiddenError } from "#generated/common/ForbiddenError"
import type { InvalidRequestError } from "#generated/common/InvalidRequestError"
import type { PaymentNotFoundError } from "#generated/payment/PaymentNotFoundError"
import type { PaymentNotPaidError } from "#generated/payment/PaymentNotPaidError"
import type { PgProviderError } from "#generated/common/PgProviderError"
import type { UnauthorizedError } from "#generated/common/UnauthorizedError"

export type ConfirmEscrowError =
	| ForbiddenError
	| InvalidRequestError
	| PaymentNotFoundError
	| PaymentNotPaidError
	| PgProviderError
	| UnauthorizedError
