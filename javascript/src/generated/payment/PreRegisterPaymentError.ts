import type { AlreadyPaidError } from "#generated/payment/AlreadyPaidError"
import type { ForbiddenError } from "#generated/common/ForbiddenError"
import type { InvalidRequestError } from "#generated/common/InvalidRequestError"
import type { UnauthorizedError } from "#generated/common/UnauthorizedError"

export type PreRegisterPaymentError =
	| AlreadyPaidError
	| ForbiddenError
	| InvalidRequestError
	| UnauthorizedError
