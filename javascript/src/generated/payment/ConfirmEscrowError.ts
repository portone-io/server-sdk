import type { ForbiddenError } from "./../common/ForbiddenError"
import type { InvalidRequestError } from "./../common/InvalidRequestError"
import type { PaymentNotFoundError } from "./../payment/PaymentNotFoundError"
import type { PaymentNotPaidError } from "./../payment/PaymentNotPaidError"
import type { PgProviderError } from "./../common/PgProviderError"
import type { UnauthorizedError } from "./../common/UnauthorizedError"

export type ConfirmEscrowError =
	| ForbiddenError
	| InvalidRequestError
	| PaymentNotFoundError
	| PaymentNotPaidError
	| PgProviderError
	| UnauthorizedError
	| { readonly type: unique symbol }
