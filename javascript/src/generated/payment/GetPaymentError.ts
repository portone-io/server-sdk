import type { ForbiddenError } from "#generated/common/ForbiddenError"
import type { InvalidRequestError } from "#generated/common/InvalidRequestError"
import type { PaymentNotFoundError } from "#generated/payment/PaymentNotFoundError"
import type { UnauthorizedError } from "#generated/common/UnauthorizedError"

export type GetPaymentError =
	| ForbiddenError
	| InvalidRequestError
	| PaymentNotFoundError
	| UnauthorizedError
