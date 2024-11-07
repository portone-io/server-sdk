import type { ForbiddenError } from "./../common/ForbiddenError"
import type { InvalidRequestError } from "./../common/InvalidRequestError"
import type { PaymentNotFoundError } from "./../payment/PaymentNotFoundError"
import type { UnauthorizedError } from "./../common/UnauthorizedError"

export type GetPaymentError =
	| ForbiddenError
	| InvalidRequestError
	| PaymentNotFoundError
	| UnauthorizedError
