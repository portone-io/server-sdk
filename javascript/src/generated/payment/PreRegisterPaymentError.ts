import type { AlreadyPaidError } from "./../payment/AlreadyPaidError"
import type { ForbiddenError } from "./../common/ForbiddenError"
import type { InvalidRequestError } from "./../common/InvalidRequestError"
import type { UnauthorizedError } from "./../common/UnauthorizedError"

export type PreRegisterPaymentError =
	| AlreadyPaidError
	| ForbiddenError
	| InvalidRequestError
	| UnauthorizedError
